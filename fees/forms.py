from django import forms

from .models import Fee


class FeeForm(forms.ModelForm):

    class Meta:

        model = Fee

        fields = [
            'student',
            'academic_year',
            'total_fees',
            'paid_amount',
            'payment_date',
            'remarks',
        ]

        widgets = {

            'total_fees': forms.NumberInput(
                attrs={
                    'min': 0,
                    'step': '0.01'
                }
            ),

            'paid_amount': forms.NumberInput(
                attrs={
                    'min': 0,
                    'step': '0.01'
                }
            ),

            'payment_date': forms.DateInput(
                attrs={
                    'type': 'date'
                }
            ),

            'remarks': forms.Textarea(
                attrs={
                    'rows': 4
                }
            ),
        }

    def clean(self):

        cleaned_data = super().clean()

        total_fees = cleaned_data.get(
            'total_fees'
        )

        paid_amount = cleaned_data.get(
            'paid_amount'
        )

        if (
            total_fees is not None
            and paid_amount is not None
        ):

            if paid_amount > total_fees:

                raise forms.ValidationError(
                    'Paid amount cannot be greater than total fees.'
                )

        return cleaned_data