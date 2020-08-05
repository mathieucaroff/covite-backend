from django.db import models

class Ressource(models.Model):
    class Meta:
        abstract = True
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

class TodoGroup(Ressource):
    pass
    # (todoItem_set)

class SuccessorRelationship(models.Model):
    pass

class TodoItem(Ressource):
    name = models.CharField()
    ticked_off = models.BooleanField()
    group = models.ForeignKey(to=TodoGroup, on_delete=models.CASCADE)
    successorList = models.ManyToManyField(to='self', related_name='antecedentList', through=SuccessorRelationship)
    # (antecedentList)
