from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from rest_framework.routers import DefaultRouter

from app.people.views import PersonModelView, PersonCalcAPIView

admin.site.site_header = "People Register"
admin.site.site_title = "People Register"

router = DefaultRouter()
router.register(r'people', PersonModelView)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/person-calc/<str:user_id>/', PersonCalcAPIView.as_view(), name="person-calc-imc",)
]

if settings.DEBUG:
    schema_view = get_schema_view(
        openapi.Info(
            title="Person Register API",
            default_version='v1',
            description="Api for Person Crud",
        ),
        public=True,
        permission_classes=(permissions.AllowAny,),
    )
    urlpatterns += [
        path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
        path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    ]
