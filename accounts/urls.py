from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('', views.TestSimpleJwt.as_view(), name='simple_jwt'),
]