from django.urls import path

from users import views


#python3 manage.py makemigrations
#python3 manage.py migrate

app_name = "users"


urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout")
]