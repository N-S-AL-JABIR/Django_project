from django.shortcuts import render, redirect
from . forms import TestForm

# Create your views here.
def form_test(request):
    if request.method == 'POST':
        form = TestForm(request.POST)
        if form.is_valid():
            return redirect("form_test")
    else:
        form = TestForm()
    return render(request, 'form_test.html', {'form': form})
