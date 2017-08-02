from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import RequestTable
from .serializer import RequestTableSerializer


def index(request):
	return HttpResponse("<h1> Green Taxi homepage </h1>")

# GET all the fields in JSON format
class RequestList(APIView):

	def get(self, request):
		req = RequestTable.objects.all()
		serializer = RequestTableSerializer(req, many=True)
		return Response(serializer.data)



