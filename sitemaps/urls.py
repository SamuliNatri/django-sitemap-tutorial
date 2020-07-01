from django.contrib import admin
from django.urls import include, path
from blog.models import Post
from django.contrib.sitemaps.views import sitemap
from django.contrib.sitemaps import GenericSitemap
from sitemaps.sitemaps import StaticViewSitemap
from pages.views import PostListView
from django.views.generic import TemplateView

sitemaps = {
    'blog': GenericSitemap({
        'queryset': Post.objects.all(),
        'date_field': 'modified',
    }, priority=0.9),
    'static': StaticViewSitemap,
}

urlpatterns = [
    path('', PostListView.as_view(), name='home'),
    path('blog/', include('blog.urls')),
    path('about/', TemplateView.as_view(template_name='about.html'), name='about'),
    path('sitemap.xml', sitemap,
         {'sitemaps': sitemaps},
         name='django.contrib.sitemaps.views.sitemap'),
    path('admin/', admin.site.urls),
]
