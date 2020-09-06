from django import forms
from .models import Group

class GrForm(forms.ModelForm):

    class Meta:
        model = Group # 어떤 모델과 대응
        fields = ('name','image','members')

