from django.forms import ModelForm
from .models import Round


class RoundForm(ModelForm):
    class Meta:
        model = Round
        fields = [
            "name",
        ]
