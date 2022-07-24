from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
   openapi.Info(
      title="PROJECT BITLAB API",
      default_version='V1',
      description="Some text of description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="kampottto@gmail.vom"),
      license=openapi.License(name="Project Bitlab License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api-auth/', include('rest_framework.urls')),
    path('v1/', include('questionnaire.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


