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


class EmailForm(forms.Form):
    recipient = forms.EmailField(label='Recipient Email')
    subject = forms.CharField(max_length=100, label='Subject')
    message = forms.CharField(widget=forms.Textarea, label='Message')





