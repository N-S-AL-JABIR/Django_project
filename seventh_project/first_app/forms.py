from django import forms
from first_app.models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
        lebels = {'roll':'Roll No','name':'Name','age':'Age','father_name':'Father Name','address':'Address'}
        widgets = {'address':forms.Textarea(attrs={'rows':3,'cols':30})}
        help_texts = {'name':'Enter your full name','age':'Enter your age','father_name':'Enter your father name','address':'Enter your address'}
        error_messages = {'name':{'required':'Name is required'},'age':{'required':'Age is required'},'father_name':{'required':'Father name is required'},'address':{'required':'Address is required'}}