from django.shortcuts import render
from django.core.paginator import Paginator

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
    data['formMarketPlace'] = MarketplacesForm()
    return render(request, 'formMarketPlace.html', data)

def createMarketplace(request):
    form = MarketplacesForm(request.POST or None)
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
    data['formMarketPlaces'] = MarketplacesForm(instance=data['db'])
    return render(request, 'marketplacesForm.html', data)

def updateMarketplace(request, pk):
    data = {}
    data['db'] = Marketplaces.objects.get(pk=pk)
    form = MarketplacesForm(request.POST or None, instance=data['db'])
    if form.is_valid():
        form.save()
        return redirect('indexMarketplace')

def deleteMarketplace(request, pk):
    db = Marketplaces.objects.get(pk=pk)
    db.delete()
    return redirect('indexMarketplace')