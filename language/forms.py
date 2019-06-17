from django import forms

class TextForm(forms.Form):
    translation = forms.CharField(label='Translation', max_length=300)
    translation.widget.attrs.update({'id' : 'your_id', 'value' : "", 'class' : 'form-control', 'placeholder' : "Write Translation", 'rows' :"4"})