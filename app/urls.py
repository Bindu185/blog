from django.contrib import admin
from django.urls import path
from .import views
urlpatterns = [
    path('',views.index,name="index"),
    path('search',views.search),
    path('search-action',views.search_action,name="search_action"),
    path('signup',views.signup,name="signup"),
    path('signup-action',views.signup_action,name="signup_action"),
    path('signin',views.signin,name="signin"),
    path('signin-action',views.signin_action,name="signin_action")
    
]

from django.conf import settings
from django.conf.urls.static import static
if settings.DEBUG:
    urlpatterns +=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)