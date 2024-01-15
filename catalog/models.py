from django.db import models
from django.contrib.auth.models import User
from django_history.mixins import HistoryMixin


class Genre(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Жанр"
        verbose_name_plural = "Жанры"


class Film(models.Model):
    title = models.TextField(verbose_name="Название")
    genres = models.ManyToManyField(Genre, related_name="genres")
    short_description = models.CharField(max_length=50, verbose_name="Страна выпуска")
    description = models.TextField(verbose_name="Описание")
    duration = models.DurationField(verbose_name="Длительность")
    ageRestriction = models.PositiveIntegerField(verbose_name="Возрастное ограничение")
    image = models.ImageField(upload_to="media/films", verbose_name="постер")
    rating = models.PositiveIntegerField(verbose_name="рейтинг")

    date_start_sales = models.DateTimeField()
    date_end_sales = models.DateTimeField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Фильм"
        verbose_name_plural = "Фильмы"


class FilmComment(models.Model):
    text = models.CharField(max_length=400)
    timestamp = models.DateTimeField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    film = models.ForeignKey(Film, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.user.id) + " - " + self.film.title

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    name = models.CharField(max_length=70)
    last_name = models.CharField(max_length=100)
    balance = models.PositiveIntegerField()
    watched_films = models.ManyToManyField(Film)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Профиль"
        verbose_name_plural = "Профили"


class ProfileTickets(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.PROTECT)
    ticket = models.ForeignKey("Ticket", on_delete=models.PROTECT)
    date_purchased = models.DateTimeField()

    def __str__(self):
        return self.profile.name + " - " + self.ticket.film.title

    class Meta:
        verbose_name = "Билеты в профиле"
        verbose_name_plural = "Билеты в профилях"


class Ticket(models.Model):
    film = models.ForeignKey(Film, on_delete=models.DO_NOTHING)
    timestamp = models.DateTimeField()
    price = models.PositiveIntegerField()
    validity_period = models.DateTimeField()

    def __str__(self):
        return self.film.title + " - " + str(self.timestamp)

    class Meta:
        verbose_name = "Билет"
        verbose_name_plural = "Билеты"
