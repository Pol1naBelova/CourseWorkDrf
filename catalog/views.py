from django.shortcuts import render, redirect
from .models import Film, Ticket, ProfileTickets, Profile, FilmComment
from django.core.exceptions import ValidationError, ObjectDoesNotExist
from django.http import JsonResponse
from django.db.models import Q

from rest_framework.viewsets import ViewSet
from rest_framework.generics import ListAPIView, GenericAPIView
from rest_framework.decorators import action

from .serializers import FilmSerializer, FilmCommentSerializer, TicketSerializer
from .paginators import LargeResultsSetPagination

class FilmListView(ListAPIView):
    queryset = Film.objects.all()
    serializer_class = FilmSerializer
    pagination_class = LargeResultsSetPagination

    def get_queryset(self):
        queryset = Film.objects.all()
        film_id = self.request.query_params.get('film_id')
        if film_id is not None:
            return queryset.filter(pk=film_id)
        return queryset

class CatalogViewSet(ViewSet):


    @action(detail=False, methods=["GET"])
    def catalog(self, request):
        films = Film.objects.all()
        serializer = FilmSerializer(list(films), many=True)
        return JsonResponse({
            "films": serializer.data
        })

class CommentsViewSet(ViewSet):

    @action(detail=False, methods=["GET"])
    def comments(self, request):
        comment = FilmComment.objects.all()
        search = request.query_params.get("comment_start")
        if search is not None:
            comment = comment.filter(
                Q(film__title__startswith=search)
            )
        serializer = FilmCommentSerializer(list(comment), many=True)
        return JsonResponse({
            "comments": serializer.data
        })

class TicketListView(ListAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer

    def get_queryset(self):
        queryset = Ticket.objects.all()
        search = self.request.query_params.get("ticket_start")
        if search is not None:
            queryset = queryset.filter(
                Q(film__title__startswith=search)
            )
        return queryset
class TicketViewSet(ViewSet):
    @action(detail=True, methods=["POST"])
    def add(self, request):
        film_id = request.POST["film_id"]
        if not film_id:
            return ValidationError("Field film_id is required")

        film_id = int(film_id)
        profileTickets = ProfileTickets.objects.all().values("ticket")
        tickets = Ticket.objects.filter(
            ~Q(id__in=profileTickets)
        )

        try:
            tickets_aviable = list(tickets.filter(
                Q(film_id=film_id)
            ))
        except ObjectDoesNotExist:
            return JsonResponse({
                "tickets": []
            })

        ticket = tickets_aviable[0]
        ProfileTickets.objects.create(ticket=ticket, profile=Profile.objects.all().first(), date_purchased=datetime.now())

        return redirect('film', film_id=film_id)

    @action(detail=True, methods=["POST"])
    def remove(self, request):
        if not request.POST["ticket_id"]:
            return ValidationError("Field ticket_id is required")
        try:
            ticket = Ticket.objects.get(pk=int(request.POST["ticket_id"]))
            profile_ticket = ProfileTickets.objects.get(ticket=ticket.id)
            profile_ticket.delete()
        except ObjectDoesNotExist:
            pass
        finally:
            return redirect("film", film_id=request.POST["film_id"])


from datetime import datetime



def catalog_view(request):
    films = Film.objects.all()

    return render(request, 'catalog/catalog.html', {"films" : films})


def film_view(request, film_id):

    film = Film.objects.get(pk=film_id)
    profileTickets = ProfileTickets.objects.all().values("ticket")
    tickets = list(Ticket.objects.filter(film=film.id).exclude(id__in=profileTickets))
    tickets_puchased = [ticket.ticket for ticket in list(ProfileTickets.objects.filter(profile=request.user.id)) if ticket.ticket.film.id == film_id]

    return render(request, 'catalog/film.html', {"film" : film, "tickets": list(tickets), "tickets_purchased" : tickets_puchased})

