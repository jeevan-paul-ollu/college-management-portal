from django import forms
from .models import Student


class StudentForm(forms.ModelForm):

    class Meta:
        model = Student

        fields = [
            'student_id',
            'first_name',
            'last_name',
            'email',
            'phone',
            'date_of_birth',
            'gender',
            'department',
            'course',
            'year',
            'address',
        ]

        widgets = {
            'date_of_birth': forms.DateInput(
                attrs={'type': 'date'}
            ),

            'address': forms.Textarea(
                attrs={'rows': 4}
            ),
        }