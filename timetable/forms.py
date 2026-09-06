from django import forms
from .models import Timetable


class TimetableForm(forms.ModelForm):

    class Meta:
        model = Timetable

        fields = [
            'day',
            'subject',
            'faculty',
            'start_time',
            'end_time',
            'room_number',
            'department',
            'semester',
        ]

        widgets = {

            'start_time': forms.TimeInput(
                attrs={'type': 'time'}
            ),

            'end_time': forms.TimeInput(
                attrs={'type': 'time'}
            ),

        }

    def clean(self):

        cleaned_data = super().clean()

        start_time = cleaned_data.get('start_time')
        end_time = cleaned_data.get('end_time')

        if start_time and end_time:

            if end_time <= start_time:

                raise forms.ValidationError(
                    'End time must be after start time.'
                )

        return cleaned_data