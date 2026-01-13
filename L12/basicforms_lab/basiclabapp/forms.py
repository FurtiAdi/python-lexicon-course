from django import forms

class SupportTicketForm(forms.Form):
    full_name = forms.CharField()
    email = forms.EmailField()
    text = forms.CharField(widget=forms.Textarea, min_length=20)

    def clean(self):
        name = self.cleaned_data['full_name']
        if len(name.split()) < 2:
            raise forms.ValidationError("Full name must contain at least two words.")
        return name