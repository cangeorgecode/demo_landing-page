from django.shortcuts import render, redirect
from core.forms import LeadForm
from core.models import FAQ
from django.contrib import messages

def index(request):
    form = LeadForm(request.POST or None)
    faqs = FAQ.objects.all()
    if form.is_valid():
        form.save()
        messages.success(request, 'Your form has been submitted, thank you!')
        return redirect('success')
    return render(request, 'core/index.html', {'faqs': faqs})

def success(request):
    return render(request, 'core/success.html')
