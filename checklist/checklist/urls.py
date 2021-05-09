from django.contrib import admin
from django.urls import path,include
from django.views.generic import TemplateView
from rest_framework.schemas import get_schema_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('', include('accounts.urls')),

    path('openapi', get_schema_view(
        title="Checklist",
        description="API for all things …",
        version="1.0.0"
    ), name='openapi-schema'),
    
    path('', TemplateView.as_view(
        template_name='doc.html',
        extra_context={'schema_url':'openapi-schema'}
    ), name='api_doc'),
]
