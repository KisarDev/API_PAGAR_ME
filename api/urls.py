from django.urls import path
from .import views
urlpatterns = [
    path('register_transaction/', views.register_transaction, name='register_transaction')
]
