from django.contrib import admin
from django.urls import path, re_path, include
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter
from user import views as u_views

router = DefaultRouter()

router.register(r"groups", u_views.GroupAPIViewset)

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r"^api/v1/rest-auth/", include("rest_auth.urls")),
    re_path(r"^api/v1/logged-in-user/", u_views.LoggedInUserAPIView.as_view()),
    path("api/v1/permissions/", u_views.PermissionListAPIView.as_view()),
    re_path(r"^api/v1/", include(router.urls)),
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
