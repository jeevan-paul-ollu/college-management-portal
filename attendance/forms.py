from django import forms
from .models import Attendance


class AttendanceForm(forms.ModelForm):

    class Meta:

        model = Attendance

        fields = [
            'student',
            'subject',
            'date',
            'status',
        ]

        widgets = {
            'date': forms.DateInput(
                attrs={
                    'type': 'date'
                }
            ),
        }