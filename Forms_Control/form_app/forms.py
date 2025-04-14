from django import forms
from django.core import validators


class ContactForm(forms.Form):
    name = forms.CharField( label='Your Name', max_length=100,help_text='length should be less than 100')
    file = forms.FileField()
    # email = forms.EmailField()
    # select = forms.ChoiceField(choices=[("1", "Option 1"), ("2", "Option 2")])
    # age = forms.IntegerField()
    # weight = forms.FloatField()
    # balance = forms.DecimalField()
    # check = forms.BooleanField()
    # birth_date = forms.DateField()
    # appointment = forms.DateTimeField()
    # CHOISES=[('s', 'Small'), ('m', 'Medium'), ('l', 'Large')]
    # size =forms.ChoiceField(choices = CHOISES)
    # MEAL = [('b', 'Breakfast'), ('l', 'Lunch'), ('d', 'Dinner')]
    # pizza = forms.MultipleChoiceField(choices = MEAL)

# class StudentForm(forms.Form):
#     name = forms.CharField(widget=forms.TextInput())
#     email = forms.EmailField(widget=forms.EmailInput())
#     password = forms.CharField(widget=forms.PasswordInput())
#     # def clean_name(self):
#     #     name = self.cleaned_data['name']
#     #     if len(name) < 10:
#     #         raise forms.ValidationError("Enter a name at least 10 characters long")
#     #     return name
#     # def clean_email(self):
#     #     email = self.cleaned_data['email']
#     #     if '.com' not in email:
#     #         raise forms.ValidationError("Your email should contain '.com'")
#     #     return email
#     def clean(self):
#         cleaned_data = super().clean()
#         name = cleaned_data.get('name')
#         email = cleaned_data.get('email')
#         password = cleaned_data.get('password')
#         if len(name) < 10:
#             raise forms.ValidationError("Enter a name at least 10 characters long")
#         if '.com' not in email:
#             raise forms.ValidationError("Your email should contain '.com'")
#         if len(password) < 8:
#             raise forms.ValidationError("Password should be at least 8 characters long")
#         return cleaned_data

class StudentForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(),validators=[validators.MaxLengthValidator(10,message='Name should be less than 10 characters')])
    email = forms.EmailField(widget=forms.EmailInput(),validators=[validators.EmailValidator(message='Enter a valid email')])
    password = forms.CharField(widget=forms.PasswordInput())
    confirm_password = forms.CharField(widget=forms.PasswordInput())
    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get('name')
        email = cleaned_data.get('email')
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')
        if len(name) < 6:
            raise forms.ValidationError("Enter a name at least 10 characters long")
        if '.com' not in email:
            raise forms.ValidationError("Your email should contain '.com'")
        if len(password) < 8:
            raise forms.ValidationError("Password should be at least 8 characters long")
        if password != confirm_password:
            raise forms.ValidationError("Password and Confirm Password should be same")
        return cleaned_data