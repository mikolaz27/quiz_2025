from quiz.models import Category, Category2, Question, Quiz


def sample_quiz(title: str, **params) -> Quiz:
    default = {
        "description": "Some description",
        "category": Category.objects.get_or_create(name="Test category")[0],
        "category2": Category2.objects.get_or_create(name="Test category2")[0],
    }
    default.update(params)
    return Quiz.objects.create(title=title, **default)


def sample_question(quiz: Quiz, order_number: int, **params) -> Question:
    default = {"text": "Text for testing"}
    default.update(params)
    return Question.objects.create(quiz=quiz, order_number=order_number, **default)
