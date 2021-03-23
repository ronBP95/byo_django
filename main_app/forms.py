from django import forms
from .models import Feeding

class FeedingForm(forms.ModelForm):
    # meta class beacuse that's how django can do it
    class Meta:
        # which model
        model = Feeding
        fields = ['date', 'meal']