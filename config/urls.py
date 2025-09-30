from django.contrib import admin
from django.urls import include, path
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView
from django.views.generic import RedirectView
from django.http import JsonResponse

def healthz(_request):  # простой health-check
    return JsonResponse({"status": "ok"})

urlpatterns = [
    path("", RedirectView.as_view(url="/api/docs/",
                                  permanent=False),
         name="root"),

    path("healthz/", healthz, name="healthz"),
    path("admin/",
         admin.site.urls),
    path("",
         include("habits.urls",
                 namespace="habits")),
    path("users/",
         include("users.urls",
                 namespace="users")),
    path("api/docs/", RedirectView.as_view(
        url="/api/schema/swagger-ui/",
        permanent=False),
         name="docs"),
    path("api/schema/",
         SpectacularAPIView.as_view(),
         name="schema"),
    path("api/docs/",
         SpectacularRedocView.as_view(url_name="schema"),
         name="docs"),
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path("api/schema/swagger-ui/", SpectacularSwaggerView.as_view(
        url_name="schema"),
         name="swagger-ui"),
]
