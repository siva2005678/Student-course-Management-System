from rest_framework import serializers
from StudentApp.models import Student


class StudentSerializer(
    serializers.ModelSerializer
):

    class Meta:

        model = Student

        fields = [
            'id',
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

    def validate_name(self, value):

        if not value.strip():
            raise serializers.ValidationError(
                'Name cannot be empty.'
            )

        return value

    def validate_fees(self, value):

        if value < 0:
            raise serializers.ValidationError(
                'Fees cannot be negative.'
            )

        return value