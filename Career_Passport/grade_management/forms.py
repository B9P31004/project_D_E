from django import forms
from .models import grades

class grade_inputForm(forms.ModelForm):
    class Meta:
        model=grades
        fields=('school_year','semester','regular_test','national_language','math','english','social_studies','science','music','art','technical_arts_and_home_economics','health_and_physical_education')
        def __init__(self,*args,**kwargs):
            super().__init__(*args,**kwargs)
            for field in self.fields.values():
                field.widget.attrs['class']='form-control'