from django.urls import path

from quiz.views import bitcoin, normalize_email

urlpatterns = [
    path("bitcoin/", bitcoin, name="bitcoin"),
    path("email/", normalize_email, name="normalize_email"),
]
