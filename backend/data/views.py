from rest_framework import generics 
from rest_framework import permissions
from .models import Data
from.serializers import DataSerializer
from .permissions import IsSuperuserOrReadOnly
from rest_framework.authentication import SessionAuthentication
from django.contrib.auth import logout, authenticate, login
from django.shortcuts import redirect
from django.http import JsonResponse
import json 

def login_view(request):
    if request.method =='POST':
        data=json.loads(request.body)
        username=data.get('username')
        password=data.get('password')

        user=authenticate(request, username=username, password=password)#might need to pass in request, 

        if user is not None:
            login(request, user)
            if user.is_authenticated and user.is_superuser: 
                return JsonResponse({'message': 'User is autenticated'})
            elif user.is_authenticated:
                return JsonResponse({'message':'User is authenticated, but not a superuser'})
            else: 
                return JsonResponse({'message':'User is not valid'}, status=401)
    return JsonResponse({'message':'invalid request'},status=400)





        


class ListData(generics.ListAPIView): #to view all the data, will be used with the search 
    queryset=Data.objects.all()
    serializer_class=DataSerializer

class CreateData(generics.ListCreateAPIView): #to post, will be used by the raspberry pi 
    queryset=Data.objects.all()
    serializer_class=DataSerializer#query set is used in read onlys so it is not included here 

class DeleteData(generics.DestroyAPIView):
    queryset=Data.objects.all()
    serializer_class=DataSerializer
    lookup_field='pk'

class DetailData(generics.RetrieveAPIView): #to view the detailed data, will be used after searching to see all the information of a certain picture 
    queryset=Data.objects.all()
    serializer_class=DataSerializer
 

