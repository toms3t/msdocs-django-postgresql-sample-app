from django.shortcuts import render, redirect


def index(request):
    print("Request for index page received")
    lst = ["a", "b"]
    context = {
        "a": lst,
    }
    return render(request, "penapp/index.html", context)
