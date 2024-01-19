from django.urls import path

from flights import views


#python3 manage.py makemigrations
#python3 manage.py migrate

app_name = "flights"


urlpatterns = [
    path("", views.index, name="index"),
    path("<int:flight_id>/", views.flight, name="flight")
]