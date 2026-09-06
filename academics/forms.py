from django import forms
from .models import Subject


class SubjectForm(forms.ModelForm):

    class Meta:

        model = Subject

        fields = [
            'subject_code',
            'subject_name',
            'department',
            'course',
            'semester',
            'credits',
            'description',
        ]

        widgets = {
            'description': forms.Textarea(
                attrs={
                    'rows': 4
                }
            ),
        }