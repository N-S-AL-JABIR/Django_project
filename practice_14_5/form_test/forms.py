from django import forms
from django.forms.widgets import NumberInput
import datetime


birth_year_choices = [(year) for year in range(1900, 2024)]
# birth_year_choices = ['1900', '1901', '1902', '1903', '1904', '1905', '1906', '1907', '1908', '1909',]
fav_color_choices = [
    ('red', 'Red'),
    ('green', 'Green'),
    ('blue', 'Blue'),
    ('yellow', 'Yellow'),
    ('black', 'Black'),
    ('white', 'White'),
]

class TestForm(forms.Form):
    name = forms.CharField(label='Your name', max_length=100)
    comment = forms.CharField(label="Comment", widget=forms.Textarea(attrs={'rows': 4, 'cols': 40}))
    email= forms.EmailField(label='Email address')
    agree = forms.BooleanField(label='Agree to terms and conditions')
    date = forms.DateField()
    birth_date = forms.DateField(widget=NumberInput(attrs={"type": "date"}))
    birth_year = forms.DateField(
        widget=forms.SelectDateWidget(years=birth_year_choices)
    )

    value = forms.DecimalField()
    email2 = forms.EmailField(required=False)
    massage = forms.CharField(max_length=100)
    first_name = forms.CharField(initial='jabir')

    agree2 = forms.BooleanField(initial=True)
    day =forms.DateField(initial=datetime.date.today())

    fav_color = forms.ChoiceField( choices=fav_color_choices)
    fav_RadioSelect = forms.ChoiceField(
        widget=forms.RadioSelect, choices=fav_color_choices
    )

    fav_Multiple_ChoiceField = forms.MultipleChoiceField(
        widget=forms.CheckboxSelectMultiple, choices=fav_color_choices
    )
