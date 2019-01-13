from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views import (
    BlogListView,
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
    path('', BlogListView.as_view(), name='home'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
