from django import forms
from .models import WaitTimes
from datetime import date
from django.urls import reverse_lazy
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit



class Attraction_select_form(forms.Form):

    theme_park = forms.ChoiceField(choices=[], # Initialize with empty choices, will be populated in __init__
        widget=forms.Select(attrs={"hx-get": "/Magic_app/load_attraction/", "hx-target": "#id_attraction"}))
    
    attraction = forms.ChoiceField(
        choices=[], # Initialize with empty choices, will be populated in __init__
        widget=forms.Select()) # You might want to add hx-trigger etc. if you chain further
    
    start_date = forms.DateTimeField(widget=forms.DateInput(attrs={
        'type':'date',
        'min':'2025-06-04',
        'max': '2025-06-24'}))
    end_date = forms.DateTimeField(widget=forms.DateInput(attrs={
        'type':'date',
        'min':'2025-06-04',
        'max': '2025-06-24'}))


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.helper = FormHelper(self)
        self.helper.from_action = reverse_lazy('index')
        self.helper.add_input(Submit('submit','Submit'))

        theme_park_options = WaitTimes.objects.values_list('theme_park', flat=True).distinct().order_by('theme_park')
        self.fields['theme_park'].choices = [('', '---Select Theme Park---')] + \
                                            [(tp, tp) for tp in theme_park_options if tp is not None]

        if "theme_park" in self.data and self.data.get('theme_park'): # Check if theme_park has a value
            theme_park_name = self.data.get('theme_park')

            # Filter attractions based on the selected theme_park
            attraction_options = WaitTimes.objects.filter(
                theme_park=theme_park_name
            ).values_list('attraction', flat=True).distinct().order_by('attraction')

            self.fields["attraction"].choices = [(a, a) for a in attraction_options if a is not None] # Ensure no None values
            self.fields["attraction"].choices.insert(0, ('', '---Select Attraction---')) # Add a default "Select" option
            
        else:
            # If no theme_park is selected yet, or it's an initial GET request,
            # attraction should be empty or have a default "Select" option.
            self.fields["attraction"].choices = [('', '---Select Attraction---')]

    """ def clean_start(self):
        start_date = self.cleaned_data['start'] # Access cleaned_data here
        today = date.today()
        if start_date > today:
            raise forms.ValidationError("Start date cannot be in the future.")
        return start_date

    def clean_end(self):
        end_date = self.cleaned_data['end'] # Access cleaned_data here
        today = date.today()
        if end_date > today:
            raise forms.ValidationError("End date cannot be in the future.")
        return end_date
          """
        