from django.contrib import admin
from django.urls import path
from youtube.views import HomeView, NewVideo, CommentView, LoginView, RegisterView, VideoView, VideoFileView,LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(),name='index'),
    path('login', LoginView.as_view(),name='login'),
    path('register', RegisterView.as_view(),name='register'),
    path('new_video', NewVideo.as_view(),name='new_video'),
    path('video/<int:id>', VideoView.as_view()),
    path('comment', CommentView.as_view()),
    path('get_video/<file_name>', VideoFileView.as_view()),
    path('logout', LogoutView.as_view(),name='logout')
]

from django.conf import settings
from django.conf.urls import include, url  # For django versions before 2.0
from django.urls import include, path  # For django versions from 2.0 and up

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),

        # For django versions before 2.0:
        # url(r'^__debug__/', include(debug_toolbar.urls)),

    ] + urlpatterns
