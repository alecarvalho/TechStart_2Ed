from django.forms import ModelForm
from sellersApp.models import Sellers

# Create the form class.
class sellersForm(ModelForm):
     class Meta:
        model = Sellers
        fields = ['trade_name', 'company_name', 'cnpj', 'email', 'phone', 'address']