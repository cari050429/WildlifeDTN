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
from django.views.decorators.csrf import csrf_exempt
 

@csrf_exempt
def login_view(request):
    permission_classes=permissions.AllowAny
    authentication_classes=SessionAuthentication
    print(request.body)
    if request.method =='POST':
        data = json.loads(request.body)
        username = data.get('username')
        password = data.get('password')
        print(username)


        user=authenticate(request=request, username=username, password=password)#might need to pass in request, 

        if user is not None:
            print('Username:')
            login(request, user)
            if user.is_authenticated and user.is_superuser: 
                return JsonResponse({'message': 'User is autenticated'})
            else:
                return JsonResponse({'message':'User is authenticated, but not a superuser'})
    return JsonResponse({'message':'Either password or username is invalid, try again'},status=400)





        


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
 

