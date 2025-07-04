from django.apps import AppConfig


class QuizConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "quiz"

    def ready(self):
        from redis_admin.models import RedisList, RedisSet

        def _set_value(self):
            # call the original property correctly and turn the list into a set
            return set(RedisList.value.fget(self))  # fget = original getter

        # replace the broken implementation with the fixed one
        RedisSet.value = property(_set_value)
