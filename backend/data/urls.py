from django.urls import path
from .views import ListData, DetailData, CreateData, DeleteData, login_view

urlpatterns=[
    path('<int:pk>/',DetailData.as_view()),
    path('', ListData.as_view()),
    path('post/', CreateData.as_view()),
    path('delete/<int:pk>/',DeleteData.as_view()),
    path('login/',login_view),
]
