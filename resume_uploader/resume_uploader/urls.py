from django.contrib import admin
from django.urls import path
from myapp import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.AllList.as_view(), name="AllCandidates"),
    path("form/", views.homeview, name="home"),
    path("candidate/<int:pk>", views.CandidateView.as_view(), name="candidate"),
    path("update_resume/<int:id>/", views.update_resume, name="update_resume"),
    # path("update/<int:pk>/", views.UpdateView.as_view(), name="update_view"),
    path("send/<int:pk>/", views.SendEmail.as_view(), name="send_email"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
