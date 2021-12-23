from collections import abc
from django import forms
from django.db import router
from django.http.response import Http404
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from .forms import RoundForm
from .models import Round
import random


def index(request):
    users = User.objects.all()
    num = 0
    return render(request, "shuffle/index.html", context={"users": users, "num": num})


def shuffler(request):
    users = User.objects.all()
    members = []
    for user in users:
        members.append(user.username)

    # random.shuffle(members)
    print(members)
    chunks = [members[x : x + 3] for x in range(0, len(members), 3)]

    form = RoundForm()
    if request.method == "POST":
        name = request.POST["name"]
        mem = ",".join(members)
        print(mem)
        sys = request.POST.get("test")
        print(sys)
        # round = Round(name=name, members=members)
        # round.save()
        return redirect("/")

    return render(
        request,
        "shuffle/shuffler.html",
        context={"members": members, "chunks": chunks, "form": form},
    )


def previousRounds(request):
    # use get object or 404 for all
    return render(request, "shuffle/previousRounds.html")


def test(request):
    print("All")
    return redirect("/")
