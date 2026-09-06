from django import forms
from .models import Faculty


class FacultyForm(forms.ModelForm):

    class Meta:
        model = Faculty

        fields = [
            'faculty_id',
            'first_name',
            'last_name',
            'email',
            'phone',
            'gender',
            'department',
            'designation',
            'qualification',
            'joining_date',
            'address',
        ]

        widgets = {
            'joining_date': forms.DateInput(
                attrs={'type': 'date'}
            ),

            'address': forms.Textarea(
                attrs={'rows': 4}
            ),
        }