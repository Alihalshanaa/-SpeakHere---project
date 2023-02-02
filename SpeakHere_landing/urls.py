from django.urls import path
from SpeakHere_landing.views import Index

urlpatterns = [
    path( '' ,Index.as_view() ,name='index'),
    
]
