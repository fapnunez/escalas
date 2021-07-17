from django.forms import ModelForm
from .models import (
    Medico,
    Posto,
    Folga,
    Escala
)


class MedicoForm(ModelForm):
    class Meta:
        model = Medico
        fields = '__all__'


class PostoForm(ModelForm):
    class Meta:
        model = Posto
        fields = '__all__'


class FolgaForm(ModelForm):
    class Meta:
        model = Folga
        fields = '__all__'
    

class EscalaForm(ModelForm):
    class Meta:
        model = Escala
        fields = '__all__'