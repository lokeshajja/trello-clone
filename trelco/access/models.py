from django.db import models
from django.contrib.auth.models import User

# common fields
class CommonInfo(models.Model):

    created_by = models.ForeignKey(User, related_name='%(class)ss_created', on_delete=models.CASCADE,
                                   null=True, blank=True)
    updated_by = models.ForeignKey(User, related_name='%(class)ss_updated', on_delete=models.CASCADE,
                                   null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    is_archive = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    class Meta:
        abstract = True

# Create your models here.
class Board(CommonInfo):
    name = models.CharField(max_length=150, null=False, blank=False)
    title = models.CharField(max_length=150, null=True, blank=True)
    description = models.CharField(max_length=500, null=True, blank=True)
    order_of_display = models.IntegerField(null=True, blank=True)

    #foreign keys
    members = models.ManyToManyField(User, related_name='boards', blank=True)

    is_public = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class List(CommonInfo):
    name = models.CharField(max_length=150, null=False, blank=False)
    title = models.CharField(max_length=150, null=True, blank=True)
    description = models.CharField(max_length=500, null=True, blank=True)
    order_of_display = models.IntegerField(null=True, blank=True)

    # foreign keys
    board = models.ForeignKey(Board, related_name='lists', on_delete=models.CASCADE,
                              null=True, blank=True)

    def __str__(self):
        return self.name


class Card(CommonInfo):
    name = models.CharField(max_length=150, null=False, blank=False)
    title = models.CharField(max_length=150, null=True, blank=True)
    description = models.CharField(max_length=500, null=True, blank=True)
    order_of_display = models.IntegerField(null=True, blank=True)

    # foreign keys
    list = models.ForeignKey(List, related_name='cards', on_delete=models.CASCADE,
                              null=True, blank=True)

    def __str__(self):
        return self.name

class CheckList(CommonInfo):
    name = models.CharField(max_length=150, null=False, blank=False)
    title = models.CharField(max_length=150, null=True, blank=True)
    description = models.CharField(max_length=500, null=True, blank=True)
    order_of_display = models.IntegerField(null=True, blank=True)

    # foreign keys
    card = models.ForeignKey(Card, related_name='checklists', on_delete=models.CASCADE,
                              null=True, blank=True)

    def __str__(self):
        return self.name

class SubTask(CommonInfo):
    name = models.CharField(max_length=150, null=False, blank=False)
    title = models.CharField(max_length=150, null=True, blank=True)
    description = models.CharField(max_length=500, null=True, blank=True)
    order_of_display = models.IntegerField(null=True, blank=True)

    # foreign keys
    checklist = models.ForeignKey(CheckList, related_name='subtasks', on_delete=models.CASCADE,
                              null=True, blank=True)
                        
    is_complete = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Comment(CommonInfo):
    title = models.CharField(max_length=150, null=True, blank=True)
    description = models.CharField(max_length=500, null=True, blank=True)
    order_of_display = models.IntegerField(null=True, blank=True)

    # foreign keys
    card = models.ForeignKey(Card, related_name='comments', on_delete=models.CASCADE,
                              null=True, blank=True)

    def __str__(self):
        return self.title
