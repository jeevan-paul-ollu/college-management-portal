from django import forms
from .models import Notice


class NoticeForm(forms.ModelForm):

    class Meta:
        model = Notice

        fields = [
            'title',
            'description',
            'category',
            'notice_date',
            'is_active',
        ]

        widgets = {
            'description': forms.Textarea(
                attrs={'rows': 6}
            ),

            'notice_date': forms.DateInput(
                attrs={'type': 'date'}
            ),
        }