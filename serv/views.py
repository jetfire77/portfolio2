from django.shortcuts import render

# Create your views here.
def services(request):
     # passing context to make link active
    context = {'services': 'active'}
    return render(request, 'serv/services.html', context)
