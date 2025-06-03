from django.contrib.auth import get_user_model
from django.db import models
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel

from common.models import BaseModel


class Category2(MPTTModel):
    name = models.CharField(max_length=200, unique=True)
    parent = TreeForeignKey("self", on_delete=models.CASCADE, null=True, blank=True, related_name="children")

    class MPTTMeta:
        order_insertion_by = ["name"]

    class Meta:
        verbose_name_plural = "Categories 2"
        verbose_name = "Category 2"

    def __str__(self):
        return f"{' > '.join([ancestor.name for ancestor in self.get_ancestors()] + [self.name])}"


class Category(BaseModel):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to="media/category/covers", null=True, blank=True)
    parent = models.ForeignKey("self", on_delete=models.CASCADE, null=True, blank=True, related_name="children")

    class Meta:
        verbose_name_plural = "Categories"
        verbose_name = "Category"

    def __str__(self):
        return f"{self.name} ({self.id})"

    def get_ancestors(self):
        ancestors = []
        node = self
        while node.parent:
            node = node.parent
            ancestors.insert(0, node)
        return ancestors

    def get_descendants(self):

        descendants = []

        def _recurse(node):
            for child in node.children.all():
                descendants.append(child)
                _recurse(child)

        _recurse(self)
        return descendants


class LEVEL_CHOICES(models.IntegerChoices):
    BASIC = 0, "Basic"
    MEDIUM = 1, "Medium"
    ADVANCED = 2, "Advanced"


class Result(BaseModel):
    quiz = models.ForeignKey(to="quiz.Quiz", related_name="results", on_delete=models.CASCADE)
    user = models.ForeignKey(to=get_user_model(), related_name="results", on_delete=models.CASCADE)
    count_of_correct_answers = models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        return f"{self.user.email} ({self.quiz.title})"


class Quiz(BaseModel):
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=1025, blank=True, null=True)
    image = models.ImageField(default="default.png", upload_to="media/quiz/covers")
    level = models.PositiveSmallIntegerField(choices=LEVEL_CHOICES.choices, default=LEVEL_CHOICES.BASIC)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name="quizzes", null=True)
    category2 = models.ForeignKey(Category2, on_delete=models.PROTECT, related_name="quizzes2", null=True)

    # category
    def __str__(self):
        return f"{self.title} ({self.id})"

    def questions_count(self):
        return self.questions.count()


class Question(BaseModel):
    quiz = models.ForeignKey(to="quiz.Quiz", related_name="questions", on_delete=models.CASCADE)
    text = models.CharField(max_length=512)
    order_number = models.PositiveSmallIntegerField(default=1)

    def __str__(self):
        return f"{self.text} ({self.order_number})"


class Choice(BaseModel):
    question = models.ForeignKey(to="quiz.Question", related_name="choices", on_delete=models.CASCADE)
    text = models.CharField(max_length=256)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.text} ({self.question.order_number})"
