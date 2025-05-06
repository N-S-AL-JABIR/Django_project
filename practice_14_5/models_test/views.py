from django.shortcuts import render, redirect
from .forms import ModelTestForm


def models_test(request):
    if request.method == "POST":
        form = ModelTestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("models_test")
    else:
        form = ModelTestForm()
    return render(request, "models_test.html", {"form": form})


# Create your views here.
