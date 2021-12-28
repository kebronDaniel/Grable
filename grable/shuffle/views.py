from collections import abc
from django import forms
from django.db import router
from django.forms.widgets import RadioSelect
from django.http.response import Http404
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from .forms import RoundForm
from .models import Round
import random


def index(request):
    users = User.objects.all()
    return render(request, "shuffle/index.html", context={"users": users})


def shuffler(request):
    users = User.objects.all()
    members = []
    # Later get all active users with thier full name
    for user in users:
        members.append(user.username)

    chunks = [members[x : x + 3] for x in range(0, len(members), 3)]
    form = RoundForm()
    if request.method == "POST":
        random.shuffle(members)
        allMembers = ",".join(members)
        name = request.POST["name"]
        round = Round(name=name, members=allMembers)
        round.save()
        return redirect("/allRounds")

    return render(
        request, "shuffle/shuffler.html", context={"chunks": chunks, "form": form}
    )


def allRounds(request):
    allRounds = Round.objects.all()
    return render(request, "shuffle/allRounds.html", context={"allRounds": allRounds})


def roundDetail(request, round_id):
    round = Round.objects.get(id=round_id)
    allMembers = round.members
    members = allMembers.split(",")
    chunks = [members[x : x + 3] for x in range(0, len(members), 3)]
    return render(
        request, "shuffle/round.html", context={"round": round, "chunks": chunks}
    )
