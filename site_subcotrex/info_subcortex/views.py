from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def portfolio(request):
    return render(request, 'portfolio.html')

def kontakt(request):
    return render(request, 'kontakt.html')

def oferta(request):
    return render(request, 'oferta.html')
    
# def admias_view(request):
    # return render(request, 'admias.html')  