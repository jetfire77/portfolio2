from django.shortcuts import render

# Create your views here.

def skill(request):
     # passing context to make link active
    context = {'skill': 'active'}
    return render(request, 'edu/skill.html', context)
