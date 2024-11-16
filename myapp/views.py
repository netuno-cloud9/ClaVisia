from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def sample_data(request):
    return Response({"message": "Hello from Django"})

# Create your views here.
