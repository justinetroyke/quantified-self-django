# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.test import TestCase
from tracker.models import Food

# Create your tests here.
class Test_FoodTestCase(TestCase):

    def setUp(self):
        """Define the test client and other test variables."""
        self.client = APIClient()

    def test_get_all_foods(self):
        """All foods are indexed for GET /api/v1/foods"""
        Food.objects.create(name="kiwi", calories=55)
        Food.objects.create(name="banana", calories=98)
        Food.objects.create(name="tacos", calories=325)
        Food.objects.create(name="rice", calories=120)

        # foods = Food.objects.all()
        # food = foods[0].calories
        response = self.client.get('/api/v1/foods/')

        # print(food)
        # print(type(food))
        self.assertEqual(len(response), 4)
