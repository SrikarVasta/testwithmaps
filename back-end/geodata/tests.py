from django.test import TestCase
from django.utils import timezone
from .models import Shape

class ShapeModelTests(TestCase):

    def test_create_shape(self):
        shape = Shape.objects.create(
            type='Star',
            coordinates=[
                [
                    [-10941774.093703765, 5849726.30320556],
                    [-11110422.173675667, 5695935.26857105],
                ]
            ]
        )
        self.assertEqual(shape.type, 'Star')
        self.assertTrue(isinstance(shape.coordinates, list))
        self.assertTrue(isinstance(shape.date_created, timezone.datetime))

    def test_to_json(self):
        shape = Shape.objects.create(
            type='Circle',
            coordinates=[
                [
                    [100, 100],
                    [200, 200]
                ]
            ]
        )
        expected_json = {
            "type": "Circle",
            "coordinates": [
                [
                    [100, 100],
                    [200, 200]
                ]
            ]
        }
        self.assertEqual(shape.to_json(), expected_json)
