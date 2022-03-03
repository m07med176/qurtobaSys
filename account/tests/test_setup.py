# Imports
from rest_framework.test import APITestCase
from django.urls import reverse
from faker import Faker
from account.models import Account
import random


# "password","email","username","phone","account_no",
# "is_open","is_superuser","is_admin","is_staff","is_active","type"
        
class TestSetUp(APITestCase):
    def setUp(self):
        # links of Manager
        # self.getManager      = reverse('getManager')
        self.registerManager = reverse('registerManager')
        # self.deleteManager   = reverse('deleteManager')
        # self.updateManager   = reverse('updateManager')

        self.fake = Faker()
        
        self.user_data = {
            'email': self.fake.email(),
            'username': self.fake.name(),
            'password': self.fake.email(),
            "phone":"010"+str(random.randrange(10000000,90000000,8)),
            "account_no":str(random.randrange(1000,9000,4)),

            "is_open":False,
            "is_superuser":False,
            "is_admin":False,
            "is_staff":False,
            "is_active":False,
            "type":0,
        }

        return super().setUp()

    def tearDown(self):
        return super().tearDown()
