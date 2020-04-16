from django.urls import reverse
from rest_framework.test import APITestCase
from test_app.models import MyUser
from rest_framework import status
'''
FROM: USER APP
'''
# Yet to consider possible user registration errors
class MyUserTest(APITestCase):
    def setUp(self):
        # Create a user
        self.test_user = MyUser.objects.create_atrisk('tiagomartinsperes@gmail.com', 'tiagoperes', 'EWFdfew45te!sadf32', 'Tiago', 'Peres')

        # URL for creating user
        self.create_url = reverse('user-create')

    def test_create_user(self):
        """
        Ensure we can create a new user and a valid token is created with it.
        """
        data = {
            'email': 'cnf32344@zzrgg.com',
            'username': 'andresantos',
            'password': 'test',
            'first_name': 'André',
            'last_name': 'Santos'
        }

        response = self.client.post(self.create_url , data, format='json')

        # Make sure we have two users in the database
        self.assertEqual(MyUser.objects.count(), 2)
        # Return 201
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        # Return the username and email upon successful creation
        self.assertEqual(response.data['email'], data['email'])
        self.assertEqual(response.data['username'], data['username'])
        self.assertFalse('password' in response.data)
        self.assertEqual(response.data['first_name'], data['first_name'])
        self.assertEqual(response.data['last_name'], data['last_name'])

    #TODO test creating user with short password; with too long username; with preexisting email; ...