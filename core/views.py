from django.shortcuts import render

# Create your views here.

def home(request):
    # passing context to make link active
    context = {'home': 'active'}
    return render(request, 'core/home.html', context)

def contact(request):
    # passing context to make link active
    context = {'contact': 'active'}
    return render(request, 'core/contact.html', context)

