from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from marketplaceApp.models import Marketplaces
from marketplaceApp.forms import MarketplaceForm

# Create your views here.

def indexMarketplace(request):
    data={}
    search = request.GET.get('search')
    if search:
        data['db'] = Marketplaces.objects.filter(name__icontains=search) or Marketplaces.objects.filter(description__icontains=search) \
                     or Marketplaces.objects.filter(value__icontains=search) or Marketplaces.objects.filter(categories__icontains=search)
    else:
        data['db'] = Marketplaces.objects.all()
        all =  Marketplaces.objects.all()
        paginator = Paginator(all, 5)
        pages = request.GET.get('page')
        data['db']= paginator.get_page(pages)
    return render(request, 'indexMarketplace.html', data)

def formMarketplace(request):
    data = {}
    data['formMarketplace'] = MarketplaceForm()
    return render(request, 'formMarketplace.html', data)

def createMarketplace(request):
    form = MarketplaceForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('indexMarketplace')

def viewMarketplace(request, pk):
    data = {}
    data['db'] = Marketplaces.objects.get(pk=pk)
    return render(request, 'viewMarketplace.html', data)

def editMarketplace(request, pk):
    data = {}
    data['db'] = Marketplaces.objects.get(pk=pk)
    data['formMarketplace'] = MarketplaceForm(instance=data['db'])
    return render(request, 'marketplacesForm.html', data)

def updateMarketplace(request, pk):
    data = {}
    data['db'] = Marketplaces.objects.get(pk=pk)
    form = MarketplaceForm(request.POST or None, instance=data['db'])
    if form.is_valid():
        form.save()
        return redirect('indexMarketplace')

def deleteMarketplace(request, pk):
    db = Marketplaces.objects.get(pk=pk)
    db.delete()
    return redirect('indexMarketplace')