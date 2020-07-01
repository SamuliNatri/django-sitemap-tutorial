from django.urls import path
from .views import PostDetailView

app_name = 'blog'

urlpatterns = [
    path('<slug:slug>/', PostDetailView.as_view(), name='detail')
]