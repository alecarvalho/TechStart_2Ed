from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from ProductApp.forms import ProductForm, CategoryForm
from ProductApp.models import Product, Category

# Create your views here.
def indexProduct(request):
    data={}
    search = request.GET.get('search')
    if search:
        data['db'] = Product.objects.filter(name__icontains=search) or Product.objects.filter(description__icontains=search) \
                     or Product.objects.filter(value__icontains=search) or Product.objects.filter(categories__icontains=search)
    else:
        data['db'] = Product.objects.all()
        all =  Product.objects.all()
        paginator = Paginator(all, 5)
        pages = request.GET.get('page')
        data['db']= paginator.get_page(pages)
    data['indexProduct'] = ProductForm
    return render(request, 'indexProduct.html', data)

def formProduct(request):
    data = {}
    data['formProduct'] = ProductForm
    return render(request, 'formProduct.html', data)

def createProduct(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save() 
        return redirect('indexProduct')

def viewProduct(request, pk):
    data = {}
    data['db']= Product.objects.get(pk=pk)
    return render(request, 'viewProduct.html', data) 

def editProduct(request, pk):
    data = {}
    data['db']= Product.objects.get(pk=pk)
    data['formProduct'] = ProductForm(instance= data['db'])
    return render(request, 'formProduct.html',data)

def updateProduct(request, pk):
    data={}
    data['db'] = Product.objects.get(pk=pk)
    form = ProductForm(request.POST or None, instance=data['db'])
    if form.is_valid():
        form.save()
    return redirect('indexProduct')


def deleteProduct(request, pk):
        db = Product.objects.get(pk=pk)
        db.delete()
        return redirect('indexProduct')

# Categoria

def indexCategory(request):
    data={}
    search = request.GET.get('search')
    if search:
        data['db'] = Category.objects.filter(name__icontains=search) or Category.objects.filter(description__icontains=search)
    else:
        data['db'] = Category.objects.all()
        all =  Category.objects.all()
        paginator = Paginator(all, 5)
        pages = request.GET.get('page')
        data['db']= paginator.get_page(pages)
    data['indexCategory'] = CategoryForm
    return render(request, 'indexCategory.html', data)

def formCategory(request):
    data = {}
    data['formCategory'] = CategoryForm
    return render(request, 'formCategory.html', data)

def createCategory(request):
    form = CategoryForm(request.POST or None)
    if form.is_valid():
        form.save() 
        return redirect('indexCategory')

def viewCategory(request, pk):
    data = {}
    data['db']= Category.objects.get(pk=pk)
    return render(request, 'viewCategory.html', data) 

def editCategory(request, pk):
    data = {}
    data['db']= Category.objects.get(pk=pk)
    data['form'] = CategoryForm(instance= data['db'])
    return render(request, 'formCategory.html',data)

def updateCategory(request, pk):
    data={}
    data['db'] = Category.objects.get(pk=pk)
    form = CategoryForm(request.POST or None, instance=data['db'])
    if form.is_valid():
        form.save()
    return redirect('indexCategory')


def deleteCategory(request, pk):
        db = Category.objects.get(pk=pk)
        db.delete()
        return redirect('indexCategory')
