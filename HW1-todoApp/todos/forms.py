from django import forms
from .models import Todo


class TodoForm(forms.ModelForm):
    """
    Form for creating and updating Todo items.
    """
    class Meta:
        model = Todo
        fields = ['title', 'due_date']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'Enter todo title...',
            }),
            'due_date': forms.DateInput(attrs={
                'class': 'form-input',
                'type': 'date',
            }),
        }
        labels = {
            'title': 'Todo Title',
            'due_date': 'Due Date (Optional)',
        }
