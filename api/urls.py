from django.urls import path
from api.views import api_endpoint

app_name = 'api'
urlpatterns = [
    path('', api_endpoint, name='endpoint')    
]