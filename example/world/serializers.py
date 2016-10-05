from rest_framework import serializers

from . import models


class CitySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.City


class CountrySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Country


class CountrylanguageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Countrylanguage


class DjangoMigrationsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.DjangoMigrations
