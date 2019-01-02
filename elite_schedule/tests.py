from django.test import TestCase

# Create your tests here.
from .models import Match
import requests
from django.urls  import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.test import APIClient
from django.contrib.auth import  get_user_model

# class RegisterUserTest(APITestCase):
#     @classmethod
#     def setUp(cls):
#         login_cred = {
#             "username": "pandora",
#             "email":"pandora@example.com",
#             "password": "pandora#2010",
#         }
#         url = "http://localhost:9000/rest-auth/login/"
#         response = requests.post(url,login_cred)
#         tk = "JWT " + response.json()["token"]
#         print(tk)
#         cls.token = "JWT " + response.json()["token"]


#     def test_can_get_matches(self):
#         self.client.credentials(HTTP_AUTHORIZATION=self.token)
#         url = reverse("elite_schedule:match")
#         res = self.client.get(url, format='json')
#         self.assertEqual(res.json(), [])
#         self.assertEqual(res.status_code, 200)




       

    # def test_can_register_user(self):



# class ReadUserTest(APITestCase):
#     def setUp(self):
#         self.superuser = User.objects.create_superuser('john', 'john@snow.com', 'johnpassword')
#         self.client.login(username='john', password='johnpassword')
#         self.user = User.objects.create(username="mike")

#     def test_can_read_user_list(self):
#         response = self.client.get(reverse('user-list'))
#         self.assertEqual(response.status_code, status.HTTP_200_OK)

#     def test_can_read_user_detail(self):
#         response = self.client.get(reverse('user-detail', args=[self.user.id]))
#         self.assertEqual(response.status_code, status.HTTP_200_OK)


# class UpdateUserTest(APITestCase):
#     def setUp(self):
#         self.superuser = User.objects.create_superuser('john', 'john@snow.com', 'johnpassword')
#         self.client.login(username='john', password='johnpassword')
#         self.user = User.objects.create(username="mike", first_name="Tyson")
#         self.data = UserSerializer(self.user).data
#         self.data.update({'first_name': 'Changed'})

#     def test_can_update_user(self):
#         response = self.client.put(reverse('user-detail', args=[self.user.id]), self.data)
#         self.assertEqual(response.status_code, status.HTTP_200_OK)


# class DeleteUserTest(APITestCase):
#     def setUp(self):
#         self.superuser = User.objects.create_superuser('john', 'john@snow.com', 'johnpassword')
#         self.client.login(username='john', password='johnpassword')
#         self.user = User.objects.create(username="mikey")

#     def test_can_delete_user(self):
#         response = self.client.delete(reverse('user-detail', args=[self.user.id]))
#         self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)



from rest_framework.test import APITestCase
from rest_framework.test import APIRequestFactory
from elite_schedule import views


class TestMatch(APITestCase):

    def setUp(self):
        self.user = self.setup_user()
        self.factory = APIRequestFactory()
        self.view = views.MatchList.as_view()
        self.uri = '/matches/'

    @staticmethod
    def setup_user():
        User = get_user_model()
        return User.objects.create_user('test',email='testuser@test.com',password='test')
    
    def test_match_list(self):
        request = self.factory.get(self.uri)
        request.user = self.user
        response = self.view(request)
        self.assertEqual(response.status_code, 200, 'Expected Response Code 200, received {0} instead.'.format(response.status_code))