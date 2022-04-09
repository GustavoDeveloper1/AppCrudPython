from django.forms import ModelForm
from app.models import Atleta

# Create the form class.
class AtletasForm(ModelForm):
     class Meta:
        model = Atleta
        fields = ['Nome', 'Idade', 'Selecao']
