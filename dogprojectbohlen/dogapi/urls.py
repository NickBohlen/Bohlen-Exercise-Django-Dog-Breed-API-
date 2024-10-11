from django.urls import path
from .views import DogList, DogDetail, BreedList, BreedDetail

urlpatterns = [
    path('dogs/', DogList.as_view(), name='dog-list'),
    path('dogs/<int:pk>/', DogDetail.as_view(), name='dog-detail'),
    path('breeds/', BreedList.as_view(), name='breed-list'),
    path('breeds/<int:pk>/', BreedDetail.as_view(), name='breed-detail'),
]
