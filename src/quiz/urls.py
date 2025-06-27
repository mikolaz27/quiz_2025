from django.urls import include, path

from blog.views import all_blogs, create_blog
from quiz.views import bitcoin, normalize_email

urlpatterns = [
    path("bitcoin/", bitcoin, name="bitcoin"),
    path("email/", normalize_email, name="normalize_email"),
]
