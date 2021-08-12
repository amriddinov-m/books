from django.contrib.auth.models import User
from django.db import models

from store.choices import RATE_CHOICES


class Book(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    author_name = models.CharField(max_length=255)
    owner = models.ForeignKey(User,
                              on_delete=models.SET_NULL,
                              null=True, related_name='my_books')
    readers = models.ManyToManyField(User, through='UserBookRelation', related_name='books')

    def __str__(self):
        return 'id:{}: {}'.format(self.id, self.name)


class UserBookRelation(models.Model):
    user = models.ForeignKey(User,
                             on_delete=models.CASCADE)
    book = models.ForeignKey(Book,
                             on_delete=models.CASCADE)
    like = models.BooleanField(default=False)
    in_bookmarks = models.BooleanField(default=False)
    rate = models.PositiveIntegerField(choices=RATE_CHOICES)

    def __str__(self):
        return '{}: {}, RATE {}'.format(self.user.username, self.book.name, self.rate)
