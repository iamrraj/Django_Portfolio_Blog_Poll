from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views


from . import views

from .views import (
    # BlogListView,
    BlogUpdateView,
    BlogDetailView,
    BlogCreateView,
    BlogDeleteView,
    
)

urlpatterns = [
    path('rahul/<int:pk>/delete/', BlogDeleteView.as_view(), name='post_delete'),
    path('rahul/<int:pk>/edit/', BlogUpdateView.as_view(), name='post_edit'),
    path('rahul/new/', BlogCreateView.as_view(), name='post_new'),
    path('rahul/<int:pk>/', BlogDetailView.as_view(), name='post_detail'),
    path('home', views.BlogListView, name='home'),
    path('', views.index, name='index'),
    path('contact', views.contact, name='contact'),

    path('login', auth_views.login, {'template_name': 'login.html'}, name='login'),
    path('signup', views.signup, name='signup'),
    path('logout', auth_views.logout, {'next_page': 'login'}, name='logout'),
    path('detail', views.detail, name='detail'),

    
    path('settings', views.settings, name='settings'),
    path('settings/password', views.password, name='password'),

    path('oauth/', include('social_django.urls', namespace='social')),

    
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
