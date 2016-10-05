#!/bin/bash

# Dependency.
# echo must interpret newline backslashes (/n).
ECHO="/usr/local/bin/gecho -e"

app_path=$(dirname "${1}")
app_name=$(basename "${app_path}")
project_path=$(dirname "${app_path}")


models="${1}"
serializers="${app_path}/serializers.py"
views="${app_path}/views.py"
urls="${project_path}/urls.py"

# Generate models.

python manage.py inspectdb > $models

# Generate serializers.

$ECHO "from rest_framework import serializers\n" >> $serializers
$ECHO "from . import models\n\n" >> $serializers

egrep "^class " $models \
  | cut -d '(' -f 1 \
  | awk '{print $1, $2 "Serializer(serializers.HyperlinkedModelSerializer):" RS "    class Meta:" RS "        model = models." $2 RS RS}' \
  >> $serializers

# Generate views.

$ECHO "from rest_framework import viewsets\n" >> $views
$ECHO "from . import models" >> $views
$ECHO "from . import serializers\n\n" >> $views

egrep "^class " $models \
  | cut -d '(' -f 1 \
  | awk '{print $1, $2 "ViewSet(viewsets.ModelViewSet):" RS "    queryset = models." $2 ".objects.all()" RS "    serializer_class = serializers." $2 "Serializer" RS RS}' \
  >> $views

# Generate URLs.

$ECHO "from django.conf.urls import include\n" >> $urls
$ECHO "from rest_framework import routers\n" >> $urls
$ECHO "from .${app_name} import views\n" >> $urls
$ECHO "router = routers.DefaultRouter()\n" >> $urls

egrep "^class " $models \
  | cut -d '(' -f 1 \
  | awk '{print "router.register(r'\''legacy_" tolower($2) "'\'', views." $2 "ViewSet)"}' \
  >> $urls

$ECHO "\nurlpatterns = [url(r'^', include(router.urls))]" >> $urls

$ECHO "Done."
