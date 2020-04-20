from django import forms


class ReviewForm(forms.Form):
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        "class": "form-control",
        "placeholder": "Your name"
    }))
    reviewText = forms.CharField(widget=forms.Textarea(attrs={
        "class": "form-control",
        "placeholder": "Leave a review"
    }))
