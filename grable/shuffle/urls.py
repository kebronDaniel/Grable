from django.urls import path
from . import views

app_name = "shuffle"

urlpatterns = [
    path("", views.index, name="index"),
    path("shuffle/", views.shuffler, name="shuffle"),
    path("allRounds/", views.allRounds, name="allRounds"),
    path("round/<round_id>", views.roundDetail, name="round"),
    path("round/<round_id>/view", views.printView, name="printView"),
    path("showStaff/", views.showAllStaff, name="allStaff"),
    path("deleteRound/<round_id>", views.deleteRound, name="deleteRound"),
]
