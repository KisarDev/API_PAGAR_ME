from django.contrib import admin
from django.urls import include, path

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="API de Transação bancária.",
      default_version='v1',
      description="Essa API simula transações de débito e crédito e efetua calculos para os diferentes modos.",
      terms_of_service="https://www.suaapi.com/terms/",
      contact=openapi.Contact(email="cesarmartins.pro@gmail.com"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
     path('swagger/', schema_view.with_ui('swagger', cache_timeout=0),
         name='schema-swagger-ui'),
]