# from django.urls import path

# from . import views


# urlpatterns = [
#     path('', views.index, name='index'),
# ]
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LogoutView
urlpatterns = [
    path('', views.index, name='index'),
    path('video_feed/', views.video_feed, name='video_feed'),
    path('monitoring/', views.monitoring, name='monitoring'),
    path('Database/', views.Database, name='Database'),
    path('Admin_page/', views.Admin_page, name='Admin_page'),
    path('start_recording/', views.start_recording, name='start_recording'),
    path('stop_recording/', views.stop_recording, name='stop_recording'),
    path('upload/', views.upload_video, name='upload_video'),
    path('videos/', views.list_videos, name='list_videos'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_view, name='login'),
    path('protected/', views.some_protected_view, name='protected'),
    path('logout/', LogoutView.as_view(next_page='index'), name='logout'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
