from django.urls import include, path

from blog.views import all_blogs, create_blog

urlpatterns = [
    path("create/", create_blog),
    path("", all_blogs),
]
