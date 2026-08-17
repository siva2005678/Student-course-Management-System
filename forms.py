from django import forms
from .models import Student


class StudentForm(forms.ModelForm):

    class Meta:
        model = Student

        fields = [
            'student_id',
            'name',
            'email',
            'phone',
            'course',
            'fees',
            'joining_date',
            'city',
            'status',
        ]

        widgets = {
            'joining_date': forms.DateInput(
                attrs={'type': 'date'}
            ),
        }