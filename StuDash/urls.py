from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static
from main.views import IndexPageView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("accounts.urls")),
    path("courses/", include("grades.urls"), name="courses"),
    path("", IndexPageView.as_view(), name="home"),
    path("bookmarks/", include("bookmarks.urls"), name="bookmarks"),
    path("grades/", include("grades.urls"), name="grades"),
    path("messages/", include("messages.urls"), name="messages"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
