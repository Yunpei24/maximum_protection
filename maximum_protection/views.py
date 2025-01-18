from django.shortcuts import render

def home(request):
    clients = "Oryx Burkina,SONABHY,SONABEL,ARCEP,BUMIGEB,Ecobank,Microaid,ACEFIME".split(',')
    return render(request, 'home.html', {'clients': clients})
