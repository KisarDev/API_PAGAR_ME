from django.urls import path
from .import views
urlpatterns = [
    path('register_transaction/', views.register_transaction, name='register_transaction'),
    path('list_transaction/', views.list_transaction, name='list_transaction'),
    path('funds/', views.funds, name='funds')
]
