from django.db.models import CharField, PositiveIntegerField, Model

class Product(Model):
    title = CharField(max_length=200)
    image = CharField(max_length=200)
    likes = PositiveIntegerField(default=0)

class User(Model):
    pass 