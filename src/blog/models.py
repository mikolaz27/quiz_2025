from datetime import datetime

from django.db import models  # NOQA: F401
from mongoengine import (DateTimeField, Document, EmbeddedDocument,
                         EmbeddedDocumentField, IntField, ListField,
                         StringField)

# key1 = {1:1}
# key2 = {1:{2:2}}
# key3 = "21312dfsalkfdslkfnalskcndslakcnsdlk"
# key4 = 123


class Blog(EmbeddedDocument):
    name = StringField(max_length=255)
    text = StringField()
    author = StringField(max_length=255)
    rating = IntField(default=10)

    def __str__(self):
        return f"{self.name}"


class Entity(Document):
    blog = ListField(EmbeddedDocumentField(Blog))
    timestamp = DateTimeField(default=datetime.now())
    last_update = DateTimeField(default=datetime.now())
    headline = StringField(max_length=255)
    payment = IntField(default=1000)

    def __str__(self):
        return f"{self.headline}"
