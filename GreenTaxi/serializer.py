from rest_framework import serializers
from .models import RequestTable


class RequestTableSerializer(serializers.ModelSerializer):

	class Meta:
		model = RequestTable
		fields = '__all__'
