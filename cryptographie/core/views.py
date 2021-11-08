from django.shortcuts import render
from .models import Resultat
from django.core.paginator import Paginator


def home(request):
    r = [1,5,7,11,13,17]
    if request.POST.get('selected_r', None) :
        resultats = Resultat.objects.filter(solution=True, r=int(request.POST['selected_r']))
    else:
        resultats = Resultat.objects.filter(solution=True)
    paginator = Paginator(resultats, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'index.html', context={"solutions" : page_obj, "restes":r})
