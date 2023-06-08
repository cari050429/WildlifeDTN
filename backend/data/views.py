from rest_framework import generics 

from .models import Data
from.serializers import DataSerializer

class ListData(generics.ListAPIView): #to view all the data, will be used with the search 
    queryset=Data.objects.all()
    serializer_class=DataSerializer

class CreateData(generics.ListCreateAPIView): #to post, will be used by the raspberry pi 
    serializer_class=DataSerializer#query set is used in read onlys so it is not included here 

class DeleteData(generics.DestroyAPIView):
    queryset=Data.objects.all()
    serializer_class=DataSerializer
    identifier='pk'

class DetailData(generics.RetrieveAPIView): #to view the detailed data, will be used after searching to see all the information of a certain picture 
    queryset=Data.objects.all()
    serializer_class=DataSerializer
