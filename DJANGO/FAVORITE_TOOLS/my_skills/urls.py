from django.urls import path
from my_skills import views


app_name = "my_skills"

urlpatterns = [
    path("", views.index, name="index")
]