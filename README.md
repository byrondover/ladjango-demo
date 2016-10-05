# Yet Another Example DRF JSON API + Swagger App (featuring `db2api`)

This is the repo for Django meet-up group demo at Wiredrive 2016.

Requires local MySQL instance running with a `world` example database installed.

* <http://dev.mysql.com/doc/index-other.html>
* <http://downloads.mysql.com/docs/world.sql.zip>

Install requirements.

```shell
pip install -r requirements.txt
```

Launch app.

```shell
python manage.py runserver
```

View DRF Browsable API.

<http://localhost:8080>

View Swagger UI.

<http://localhost:8080/api-docs>

View Swagger Schema Document.

<http://localhost:8080/api-docs?format=openapi>
