from django.shortcuts import render
from rest_framework.decorators import api_view
from app.models import MyModel
from app.serializers import ModelSerializer
from rest_framework.response import Response
from rest_framework import status
# Create your views here.

@api_view(['GET','POST'])
def model_list(request):
    if request.method == 'GET':
        all_rec = MyModel.objects.all()
        serializer = ModelSerializer(all_rec, many = True)
        return Response({"data": serializer.data},
                        status=status.HTTP_200_OK)
    
    elif request.method == 'POST':
        serializer = ModelSerializer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"data": serializer.data},
                        status=status.HTTP_201_CREATED)
        return Response({"data": serializer.errors},
                        status=status.HTTP_400_BAD_REQUEST)    