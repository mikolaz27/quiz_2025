from django.urls import include, path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions, routers

from api.views import GamerViewSet, QuestionDetailView, QuizListView

app_name = "api"
user_router = routers.DefaultRouter()
user_router.register("gamers", GamerViewSet)

schema_view = get_schema_view(
    openapi.Info(
        title="Quiz API",
        default_version="v1",
        description="Test description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path("docs/", schema_view.with_ui("redoc", cache_timeout=0), name="swagger_docs"),
    path("", include(user_router.urls)),
    path("auth/", include("djoser.urls.jwt")),
    path("quiz/<int:pk>/question/<int:order>/", QuestionDetailView.as_view(), name="question_details"),
    path("quiz/", QuizListView.as_view(), name="quiz_list"),
]

# GET /users/ - all
# GET /users/id/ - one
# POST /users/   -
# PUT /users/id/    -
# PATCH /users/id/  -
# DELETE /users/id/ -
