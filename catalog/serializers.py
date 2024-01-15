from rest_framework import serializers

class GenresSerializers(serializers.Serializer):
    name = serializers.CharField(max_length=150)

class FilmSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=150)
    genres = GenresSerializers(required=True, many=True)
    short_description = serializers.CharField(max_length=300)
    description = serializers.CharField(max_length=1000)
    duration = serializers.DurationField()
    ageRestriction = serializers.IntegerField()
    image = serializers.ImageField()
    rating = serializers.IntegerField()

    date_start_sales = serializers.DateTimeField()
    date_end_sales = serializers.DateTimeField()


class BaseUserSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=100)
    first_name = serializers.CharField(max_length=100)
    last_name = serializers.CharField(max_length=100)

class FilmCommentSerializer(serializers.Serializer):
    text = serializers.CharField(max_length=400)
    timestamp = serializers.DateTimeField()
    film = FilmSerializer(required=True)
    user = BaseUserSerializer(required=True)

class TicketSerializer(serializers.Serializer):
    film = FilmSerializer(required=True)
    timestamp = serializers.DateTimeField()
    price = serializers.IntegerField()
    validity_period = serializers.DateTimeField()