from collections import abc
from django import forms
from django.db import router
from django.forms.widgets import RadioSelect
from django.http.response import Http404
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from .forms import RoundForm
from .models import Round, StaffProfile, Location
import random


def index(request):
    users = User.objects.all()
    return render(request, "shuffle/index.html", context={"users": users})


def shuffler(request):
    users = StaffProfile.objects.filter(isAvailable=True)
    locations = Location.objects.filter(isAvailable=True)
    members = []
    locationList = []
    # Later get all active users with thier full name
    for user in users:
        members.append(user.user.username)

    for location in locations:
        locationList.append(location.name)

    chunks = [members[x : x + 3] for x in range(0, len(members), 3)]
    locationsChunks = [locationList[x : x + 3] for x in range(0, len(locationList), 3)]

    form = RoundForm()
    if request.method == "POST":
        random.shuffle(members)
        random.shuffle(locationList)
        allMembers = ",".join(members)
        locationSet = ",".join(locationList)
        name = request.POST["name"]
        round = Round(name=name, members=allMembers, location=locationSet)
        round.save()
        return redirect("/allRounds")

    return render(
        request,
        "shuffle/shuffler.html",
        context={"chunks": chunks, "form": form, "locationChunks": locationsChunks},
    )


def allRounds(request):
    allRounds = Round.objects.all()
    return render(request, "shuffle/allRounds.html", context={"allRounds": allRounds})


def roundDetail(request, round_id):
    round = Round.objects.get(id=round_id)
    allMembers = round.members
    locations = round.location
    members = allMembers.split(",")
    allLocations = locations.split(",")
    j = 0
    # Number of Locations
    i = 3
    # Number of Members assigned per location
    while i < len(members):
        members.insert(i, allLocations[j])
        i += 4
        j += 1

    chunks = [members[x : x + 4] for x in range(0, len(members), 4)]

    return render(
        request,
        "shuffle/round.html",
        context={
            "round": round,
            "chunks": chunks,
            "allLocations": allLocations,
        },
    )


def deleteRound(request, round_id):
    round = Round.objects.get(id=round_id)
    round.delete()
    return redirect("/allRounds")


def printView(request, round_id):
    round = Round.objects.get(id=round_id)
    allMembers = round.members
    locations = round.location
    members = allMembers.split(",")
    allLocations = locations.split(",")
    j = 0
    # Number of Locations
    i = 3
    # Number of Members assigned per location
    while i < len(members):
        members.insert(i, allLocations[j])
        i += 4
        j += 1

    chunks = [members[x : x + 4] for x in range(0, len(members), 4)]
    return render(
        request,
        "shuffle/roundPrintView.html",
        context={
            "round": round,
            "chunks": chunks,
            "allLocations": allLocations,
        },
    )


def showAllStaff(request):
    staffMembers = StaffProfile.objects.all()
    return render(
        request, "shuffle/showStaff.html", context={"staffMembers": staffMembers}
    )

    # Show the date created for every round
