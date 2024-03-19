from django import forms

from .models import Item

classInput = "w-full py-2 px-6 rounded-xl border"

class NewItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ("category", "name", "description", "price", "image")
        widgets = {
        'category': forms.Select(attrs={
            'class': classInput
        }),
        'name': forms.TextInput(attrs={
            'class': classInput
        }),
        'description': forms.Textarea(attrs={
            'class': classInput
        }),
        'price': forms.TextInput(attrs={
            'class': classInput
        }),
        'image': forms.FileInput(attrs={
            'class': classInput
        })
    }
        
class EditItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ("name", "description", "price", "image", "is_sold")
        widgets = {
        'name': forms.TextInput(attrs={
            'class': classInput
        }),
        'description': forms.Textarea(attrs={
            'class': classInput
        }),
        'price': forms.TextInput(attrs={
            'class': classInput
        }),
        'image': forms.FileInput(attrs={
            'class': classInput
        })
    }
