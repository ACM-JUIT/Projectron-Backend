from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

docs = get_schema_view(
    openapi.Info(
        title="Projectron API",
        default_version="v1",
        description="Welcome to Projectron's API documentation. This API provides all the necessary endpoints required to build a fully functional project application, as well as the best authentication and authorization system for your website.",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)