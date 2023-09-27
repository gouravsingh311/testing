from django import forms
from myapp.models import *

# class UploadFileForm(forms.Form):
#     class Meta:
#         model = FileUplodeModel
#         fields = '__all__'

class ReporterForm(forms.ModelForm):
    
    class Meta:
        model = Reporter
        fields = '__all__'
