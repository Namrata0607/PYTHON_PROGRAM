from django.shortcuts import render

def hobbies_view(request):
    return render(request, 'myhobbies/hobbies.html')
