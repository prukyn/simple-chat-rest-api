from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework.views import status
from .models import ChatUser, Message
from .serializer import ChatUserSerializer
# Create your tests here.

class BaseViewTest(APITestCase):
    client = APIClient()

    @staticmethod
    def create_user(email=None):
        if email is not None:
            ChatUser.objects.create(email=email)
    
    def setUp(self):
        self.create_user('jopa.konya@gmail.com')
        self.create_user('jopa!konya@gmail.com')
        self.create_user('m.jopa_konya@gmail.com')
        self.create_user('n..jopa_konya@gmail.ua')


class GetAllUsersTest(BaseViewTest):

    def test_get_all_messages(self):
        response = self.client.get(reverse())


        
