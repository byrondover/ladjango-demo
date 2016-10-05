from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from . import models
from . import serializers


from rest_framework import exceptions, response, schemas, viewsets
from rest_framework.decorators import api_view, renderer_classes
import rest_framework.parsers
import rest_framework.renderers
import rest_framework_json_api.metadata
import rest_framework_json_api.parsers
import rest_framework_json_api.renderers
from rest_framework_swagger.renderers import OpenAPIRenderer, SwaggerUIRenderer
from rest_framework_json_api.utils import format_drf_errors
from rest_framework_json_api.views import RelationshipView

from example.world.negotiation import JsonApiContentNegotiation

HTTP_422_UNPROCESSABLE_ENTITY = 422


@api_view()
@renderer_classes([SwaggerUIRenderer, OpenAPIRenderer, rest_framework_json_api.renderers.JSONRenderer])
def schema_view(request):
    generator = schemas.SchemaGenerator(title='Example API')
    return response.Response(generator.get_schema(request=request))


class JsonApiViewSet(viewsets.ModelViewSet):
    """
    This is an example on how to configure DRF-jsonapi from
    within a class. It allows using DRF-jsonapi alongside
    vanilla DRF API views.
    """
    parser_classes = [
        rest_framework_json_api.parsers.JSONParser,
        rest_framework.parsers.FormParser,
        rest_framework.parsers.MultiPartParser,
    ]
    renderer_classes = [
        rest_framework_json_api.renderers.JSONRenderer,
        rest_framework.renderers.BrowsableAPIRenderer,
    ]
    metadata_class = rest_framework_json_api.metadata.JSONAPIMetadata

    def handle_exception(self, exc):
        if isinstance(exc, exceptions.ValidationError):
            # some require that validation errors return 422 status
            # for example ember-data (isInvalid method on adapter)
            exc.status_code = HTTP_422_UNPROCESSABLE_ENTITY
        # exception handler can't be set on class so you have to
        # override the error response in this method
        response = super(JsonApiViewSet, self).handle_exception(exc)
        context = self.get_exception_handler_context()
        return format_drf_errors(response, context, exc)


class CityViewSet(viewsets.ModelViewSet):
    queryset = models.City.objects.all()
    serializer_class = serializers.CitySerializer


class CountryViewSet(viewsets.ModelViewSet):
    queryset = models.Country.objects.all()
    serializer_class = serializers.CountrySerializer


class CountrylanguageViewSet(viewsets.ModelViewSet):
    queryset = models.Countrylanguage.objects.all()
    serializer_class = serializers.CountrylanguageSerializer


class DjangoMigrationsViewSet(viewsets.ModelViewSet):
    queryset = models.DjangoMigrations.objects.all()
    serializer_class = serializers.DjangoMigrationsSerializer
