from django.test import TestCase
from .models import TodoGroup, TodoItem

class ItemTestCase(TestCase):
    def setUp(self):
        group = TodoGroup.objects.create()
        TodoItem.objects.create(name="a", ticked_off=False, group=group)
        TodoItem.objects.create(name="b", ticked_off=False, group=group)
        TodoItem.objects.create(name="c", ticked_off=False, group=group)
        TodoItem.objects.create(name="d", ticked_off=True, group=group)

    def test_is_ticked(self):
        self.assertEqual(TodoItem.objects.get(name="a").ticked_off, False)
        self.assertEqual(TodoItem.objects.get(name="d").ticked_off, False)

    def test_can_be_ticked(self):
        group: TodoItem = TodoGroup.objects.get()
        itemG = TodoItem.objects.create(name="g", ticked_off=False, group=group)
        self.assertEqual(itemG.ticked_off, False)

        itemG2: TodoItem = TodoItem.objects.get(name="g")
        itemG2.ticked_off = True
        itemG2.save()

        itemG3: TodoItem = TodoItem.objects.get(name="g")
        self.assertEqual(itemG3.ticked_off, True)
