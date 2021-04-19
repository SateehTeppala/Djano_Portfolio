from django import forms
from .models import *

class EmpForm(forms.ModelForm):
    class Meta:
        model = Emp
        fields = ('fullname','mobile','emp_code','position')
        labels ={
            'fullname': 'Full Name',
            'mobile': 'Mobile',
            'emp_code': 'EMP. Code',
            'Position': 'Position'
        }

    def __init__(self,*args,**kwargs):
        super(EmpForm,self).__init__(*args,**kwargs)
        self.fields['position'].empty_label = "Select"