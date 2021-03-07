from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from sellersApp.forms import sellersForm
from sellersApp.models import Sellers


# Create your views here.
def index(request):
    data={}
    search = request.GET.get('search')
    if search:
        data['db'] = Sellers.objects.filter(trade_name__icontains=search) or Sellers.objects.filter(company_name__icontains=search) \
                     or Sellers.objects.filter(cnpj__icontains=search) or Sellers.objects.filter(email__icontains=search)
    else:
        data['db'] = Sellers.objects.all()
        all =  Sellers.objects.all()
        paginator = Paginator(all, 5)
        pages = request.GET.get('page')
        data['db']= paginator.get_page(pages)
    data['index'] = sellersForm
    return render(request, 'index.html', data)
    
def form(request):
    data = {}
    data['form'] = sellersForm
    return render(request, 'form.html', data)

def create(request):
    form = sellersForm(request.POST or None)
    if form.is_valid():
        form.save() 
        return redirect('index')

def view(request, pk):
    data = {}
    data['db']= Sellers.objects.get(pk=pk)
    return render(request, 'view.html', data) 

def edit(request, pk):
    data = {}
    data['db']= Sellers.objects.get(pk=pk)
    data['form'] = sellersForm(instance= data['db'])
    return render(request, 'form.html',data)

def update(request, pk):
    data={}
    data['db'] = Sellers.objects.get(pk=pk)
    form = sellersForm(request.POST or None, instance=data['db'])
    if form.is_valid():
        form.save()
    return redirect('index')


def delete(request, pk):
        db = Sellers.objects.get(pk=pk)
        db.delete()
        return redirect('index')


