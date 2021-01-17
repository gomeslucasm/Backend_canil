from rest_framework.test import APIClient, APITestCase
from rest_framework import status

class RegiterUsersTest(APITestCase):

    def setUp(self):
        self.client = APIClient()

    def test_user_volunteer_register(self):
        user = {'username': 'teste4',
                'first_name':'teste',
                'last_name':'teste',
                'email':'teste4@teste.com',
                'cellphone':'99999999',
                'password':'teste'}

        response = self.client.post('/api/register/staff/', user, format='json')
        print('lalala')
        print(response)

        self.assertEqual(response.status, status.HTTP_201_CREATED)
        self.assertEqual(created_user.is_volunteer, True)