from django.http import HttpRequest, HttpResponse
from faker import Faker

from blog.models import Blog, Entity


def create_blog(request: HttpRequest) -> HttpResponse:
    faker = Faker("UK")

    saved_date = Entity(
        blog=[
            Blog(name=faker.word(), text=faker.paragraph(nb_sentences=5), author=faker.first_name()) for _ in range(3)
        ],
        headline=faker.paragraph(nb_sentences=1),
    ).save()

    return HttpResponse(f"Done: {saved_date}")


def all_blogs(request: HttpRequest) -> HttpResponse:
    blogs = Entity.objects.all()

    print(blogs)

    return HttpResponse(f"all_blogs {[blog.headline for blog in blogs]}")
