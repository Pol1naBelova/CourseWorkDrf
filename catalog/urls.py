from django.urls import path, include

from . import views

urlpatterns = [
    path("catalog", views.catalog_view, name="catalog"),
    path("film/<int:film_id>", views.film_view, name="film"),

    path("film/buy_ticket", views.TicketViewSet.as_view({"post": "add"})),
    path("film/remove_ticket", views.TicketViewSet.as_view({"post": "remove"})),

    path("film/catalog", views.CatalogViewSet.as_view({"get": "catalog"})),
    path("film/comments", views.CommentsViewSet.as_view({"get": "comments"})),
    path("films", views.FilmListView.as_view()),


    path("tickets", views.TicketListView.as_view())

]

