from django import forms
from basicapp.models import MyModel

class MyForm(forms.Form):
    name = forms.CharField(max_length=264)
    father_name = forms.CharField(max_length=264)
    roll_no = forms.CharField(max_length=264)


class MyModelForm(forms.ModelForm):
    class Meta():
        model = MyModel
        fields = '__all__'
