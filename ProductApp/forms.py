from django.forms import ModelForm
from ProductApp.models import Product, Category

# Create the form class.
class ProductForm(ModelForm):
     class Meta:
        model = Product
        fields = ['name', 'description', 'price']

class CategoryForm(ModelForm):
     class Meta:
        model = Category
        fields = ['name', 'description']