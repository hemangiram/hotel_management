from django import forms
from .models import Booking
from datetime import date

class BookingForm(forms.ModelForm):

    class Meta:
        model = Booking
        fields = ['room', 'check_in', 'check_out']

    def clean(self):
        cleaned_data = super().clean()
        check_in = cleaned_data.get("check_in")
        check_out = cleaned_data.get("check_out")

       
        if check_in and check_out:

            if check_in < date.today():
                raise forms.ValidationError("Check-in date cannot be in the past.")

            if check_out <= check_in:
                raise forms.ValidationError("Check-out must be after check-in.")

        return cleaned_data