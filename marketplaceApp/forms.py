from django.forms import ModelForm
from marketplaceApp.models import Marketplaces

# Create the form class.
class MarketplaceForm(ModelForm):
     class Meta:
        model = Marketplaces
        fields = ['name', 'description', 'site', 'phone', 'email', 'technical_manager']
