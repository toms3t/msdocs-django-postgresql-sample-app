from django.shortcuts import render, redirect


def index(request):
    lst = ["a", "b"]
    context = {
        "a": lst,
    }
    return render(request, "penapp/index.html", context)
