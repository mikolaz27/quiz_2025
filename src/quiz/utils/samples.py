from quiz.models import Question, Quiz


def sample_quiz(title: str, **params) -> Quiz:
    default = {
        "description": "Some description",
        #
    }
    default.update(params)
    return Quiz.objects.create(title=title, **default)


def sample_question(quiz: Quiz, order_number: int, **params) -> Question:
    default = {"text": "Text for testing"}
    default.update(params)
    return Question.objects.create(quiz=quiz, order_number=order_number, **default)
