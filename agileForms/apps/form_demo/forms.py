from django.forms import ModelForm

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

from .models  import FormDemo

class SimpleFormDemoForm(ModelForm):
    class Meta:
        model = FormDemo
        exclude = ()

class CrispyFormDemoModelForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(CrispyFormDemoModelForm, self).__init__(*args, **kwargs)

        # If you pass FormHelper constructor a form instance
        # It builds a default layout with all its fields
        self.helper = FormHelper(self)

        # You can dynamically adjust your layout
        self.helper.layout.append(Submit('submit', 'Submit'))

    class Meta:
        model = FormDemo
        exclude = ()

