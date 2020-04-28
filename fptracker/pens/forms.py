from django.forms import ModelForm
from pens.models import Pen, Ink
from django.forms.widgets import TextInput

class PenForm(ModelForm):
    class Meta:
        model = Pen
        fields = "__all__"
        widgets = {
            "color": TextInput(attrs={
                'type':'color'
            })
        }

class InkForm(ModelForm):
    class Meta:
        model = Ink
        fields = "__all__"
        widgets = {
            "color": TextInput(attrs={
                'type':'color'
            })
        }