from django.db import models


class User(models.Model):

    name = models.CharField(max_length=50, null=False, blank=False)
    username = models.CharField(unique=True, max_length=50, null=False, blank=False)
    mobile =  models.IntegerField(max_length=13, null=False, blank=False)
    email = models.EmailField(unique=True, null=False, blank=False)
    password = models.CharField(max_length=50, null=False, blank=False)

    def __str__(self):
        return self.name

# Create your models here.
class Board(models.Model):
    name = models.CharField(max_length=150, null=False, blank=False)
    title = models.CharField(max_length=150, null=True, blank=True)
    description = models.CharField(max_length=500, null=True, blank=True)
    order_of_display = models.IntegerField(null=True, blank=True)

    #foreign keys

    members = models.ManyToManyField(User, related_name='boards', blank=True)

    created_by = models.ForeignKey(User, related_name='boards_created', on_delete=models.CASCADE, null=True,
                                   blank=True)
    updated_by = models.ForeignKey(User, related_name='boards_updated', on_delete=models.CASCADE,
                                   null=True, blank=True)
    # common fields

    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    is_archive = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_public = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class List(models.Model):
    name = models.CharField(max_length=150, null=False, blank=False)
    title = models.CharField(max_length=150, null=True, blank=True)
    description = models.CharField(max_length=500, null=True, blank=True)
    order_of_display = models.IntegerField(null=True, blank=True)

    # foreign keys
    board = models.ForeignKey(Board, related_name='lists', on_delete=models.CASCADE,
                              null=True, blank=True)
    created_by = models.ForeignKey(User, related_name='lists_created', on_delete=models.CASCADE,
                                   null=True, blank=True)
    updated_by = models.ForeignKey(User, related_name='lists_updated', on_delete=models.CASCADE,
                                   null=True, blank=True)
    # common fields
                                
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)
    is_archive = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Card(models.Model):
    name = models.CharField(max_length=150, null=False, blank=False)
    title = models.CharField(max_length=150, null=True, blank=True)
    description = models.CharField(max_length=500, null=True, blank=True)
    order_of_display = models.IntegerField(null=True, blank=True)

    # foreign keys
    lists = models.ForeignKey(List, related_name='cards', on_delete=models.CASCADE,
                              null=True, blank=True)
    created_by = models.ForeignKey(User, related_name='cards_created', on_delete=models.CASCADE,
                                   null=True, blank=True)
    updated_by = models.ForeignKey(User, related_name='cards_updated', on_delete=models.CASCADE,
                                   null=True, blank=True)
                    
    # common fields
                                
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)
    is_archive = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class CheckList(models.Model):
    name = models.CharField(max_length=150, null=False, blank=False)
    title = models.CharField(max_length=150, null=True, blank=True)
    description = models.CharField(max_length=500, null=True, blank=True)
    order_of_display = models.IntegerField(null=True, blank=True)

    # foreign keys
    card = models.ForeignKey(Card, related_name='checklists', on_delete=models.CASCADE,
                              null=True, blank=True)
    created_by = models.ForeignKey(User, related_name='checklists_created', on_delete=models.CASCADE,
                                   null=True, blank=True)
    updated_by = models.ForeignKey(User, related_name='checklists_updated', on_delete=models.CASCADE,
                                   null=True, blank=True)
                    
    # common fields
                                
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)
    is_archive = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class SubTask(models.Model):
    name = models.CharField(max_length=150, null=False, blank=False)
    title = models.CharField(max_length=150, null=True, blank=True)
    description = models.CharField(max_length=500, null=True, blank=True)
    order_of_display = models.IntegerField(null=True, blank=True)

    # foreign keys
    checklist = models.ForeignKey(CheckList, related_name='subtasks', on_delete=models.CASCADE,
                              null=True, blank=True)
    created_by = models.ForeignKey(User, related_name='subtasks_created', on_delete=models.CASCADE,
                                   null=True, blank=True)
    updated_by = models.ForeignKey(User, related_name='subtasks_updated', on_delete=models.CASCADE,
                                   null=True, blank=True)
                    
    # common fields
                                
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)
    is_archive = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_complete = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Comment(models.Model):
    title = models.CharField(max_length=150, null=True, blank=True)
    description = models.CharField(max_length=500, null=True, blank=True)
    order_of_display = models.IntegerField(null=True, blank=True)

    # foreign keys
    card = models.ForeignKey(Card, related_name='comments', on_delete=models.CASCADE,
                              null=True, blank=True)
    created_by = models.ForeignKey(User, related_name='comments_created', on_delete=models.CASCADE,
                                   null=True, blank=True)
    updated_by = models.ForeignKey(User, related_name='comments_updated', on_delete=models.CASCADE,
                                   null=True, blank=True)
                    
    # common fields
                                
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)
    is_archive = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title
