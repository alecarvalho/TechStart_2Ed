"""TechStart URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from sellersApp.views import index, form, create, view, edit, update, delete
from ProductApp.views import formProduct, formCategory, indexCategory, indexProduct, viewCategory, viewProduct, createProduct, createCategory, editCategory, deleteCategory,updateCategory, editProduct, updateProduct, deleteProduct
from marketplaceApp.views import indexMarketplace, formMarketplace, createMarketplace, viewMarketplace, editMarketplace, updateMarketplace, deleteMarketplace

urlpatterns = [

    path('admin/', admin.site.urls),
    path('', index, name= 'index'),
    path('form/', form, name= 'form'), 
    path('create/', create, name= 'create'),
    path('view/<int:pk>/', view, name= 'view'),
    path('edit/<int:pk>/', edit, name= 'edit'),
    path('update/<int:pk>/', update, name= 'update'),
    path('delete/<int:pk>/', delete, name= 'delete'),

#Produtos e categorias

    path('admin/', admin.site.urls),
    path('', indexProduct, name= 'indexProduct'),
    path('formProduct/', formProduct, name= 'formProduct'), 
    path('createProduct/', createProduct, name= 'createProduct'),
    path('viewProduct/<int:pk>/', viewProduct, name= 'viewProduct'),
    path('editProduct/<int:pk>/', editProduct, name= 'editProduct'),
    path('updateProduct/<int:pk>/', updateProduct, name= 'updateProduct'),
    path('deleteProduct/<int:pk>/', deleteProduct, name= 'deleteProduct'),



    path('admin/', admin.site.urls),
    path('', indexCategory, name= 'indexCategory'),
    path('formCategory/', formCategory, name= 'formCategory'), 
    path('createCategory/', createCategory, name= 'createCategory'),
    path('viewCategory/<int:pk>/', viewCategory, name= 'viewCategory'),
    path('editCategory/<int:pk>/', editCategory, name= 'editCategory'),
    path('updateCategory/<int:pk>/', updateCategory, name= 'updateCategory'),
    path('deleteCategory/<int:pk>/', deleteCategory, name= 'deleteCategory'),


    # Marketplaces
    path('admin/', admin.site.urls),
    path('', indexMarketplace, name= 'indexMarketplace'),
    path('formMarketplace/', formMarketplace, name= 'formMarketplace'), 
    path('createMarketplace/', createMarketplace, name= 'createMarketplace'),
    path('viewMarketplace/<int:pk>/', viewMarketplace, name= 'viewMarketplace'),
    path('editMarketplace/<int:pk>/', editMarketplace, name= 'editMarketplace'),
    path('updateMarketplace/<int:pk>/', updateMarketplace, name= 'updateMarketplace'),
    path('deleteMarketplace/<int:pk>/', deleteMarketplace, name= 'deleteMarketplace'),

    

]
