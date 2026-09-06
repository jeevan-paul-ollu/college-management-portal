from django import forms

from .models import Result


class ResultForm(forms.ModelForm):

    class Meta:

        model = Result

        fields = [
            'student',
            'subject',
            'internal_marks',
            'assignment_marks',
            'mid_marks',
            'semester_marks',
        ]

        widgets = {

            'internal_marks': forms.NumberInput(
                attrs={
                    'min': 0,
                    'max': 20,
                    'step': '0.01'
                }
            ),

            'assignment_marks': forms.NumberInput(
                attrs={
                    'min': 0,
                    'max': 10,
                    'step': '0.01'
                }
            ),

            'mid_marks': forms.NumberInput(
                attrs={
                    'min': 0,
                    'max': 20,
                    'step': '0.01'
                }
            ),

            'semester_marks': forms.NumberInput(
                attrs={
                    'min': 0,
                    'max': 50,
                    'step': '0.01'
                }
            ),
        }