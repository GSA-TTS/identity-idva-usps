""" USPS Project URL definitions """
from django.urls import include, path, re_path
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
    openapi.Info(
        title="USPS Microservice",
        default_version="v0.1",
    ),
    public=True,
)

urlpatterns = [
    path("", include("api.urls")),
    # path to download json or yaml open api spec file
    re_path(
        r"^doc(?P<format>\.json|\.yaml)$",
        schema_view.without_ui(cache_timeout=0),
        name="schema-json",
    ),
    # path to swagger documentation
    path(
        "doc/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    # path to swagger with redoc
    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
]
