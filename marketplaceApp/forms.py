from django.forms import ModelForm
from ProductApp.models import Product, Category

# Create the form class.
class MarketplaceForm(ModelForm):
     class Meta:
        model = Product
        fields = ['name', 'description', 'site', 'phone', 'email', 'technical_manager']
