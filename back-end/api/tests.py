from django.urls import reverse
from geodata.models import Shape
from rest_framework import status
from rest_framework.test import APITestCase

class ShapeViewTests(APITestCase):

    def test_create_shape(self):
        url = reverse('create_shape')  # Ensure your URL names are set correctly
        data = {
            "type": "Star",
            "coordinates": [
                [
                    [-10941774.093703765, 5849726.30320556],
                    [-11110422.173675667, 5695935.26857105],
                ]
            ]
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['type'], 'Star')

    def test_list_shapes(self):
        Shape.objects.create(
            type='Star',
            coordinates=[
                [
                    [-10941774.093703765, 5849726.30320556],
                    [-11110422.173675667, 5695935.26857105],
                ]
            ]
        )
        url = reverse('get_data')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['type'], 'Star')
