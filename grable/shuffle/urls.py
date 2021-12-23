from django.urls import path
from . import views

app_name = "shuffle"

urlpatterns = [
    path("", views.index, name="index"),
    path("shuffle/", views.shuffler, name="shuffle"),
    path("previousRounds/", views.previousRounds, name="previous"),
    path("test/", views.test, name="test"),
]
