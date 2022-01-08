from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns=[
    url(r'^$',views.moviesite,name='moviesite'),
    url(r'^search/', views.search_results, name='search_results'),
    url(r'^language/(?P<movie_language>\d+)', views.language_filter, name='language_filter'),
    url(r'^category/(?P<movie_category>\d+)', views.category_filter, name='category_filter'),
    url(r'^status/(?P<movie_status>\d+)', views.status_filter, name='status_filter'),
    url(r'^movie/(\d+)', views.movie_filter, name='movie'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)