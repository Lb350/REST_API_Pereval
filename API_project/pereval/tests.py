from django.test import TestCase
from rest_framework import status

from rest_framework.test import APITestCase

from .models import PerevalAdded, User, Coord, Level
from django.urls import reverse

from .serializers import PerevalAddedSerializer


class PerevalTestCase(APITestCase):
    def setUp(self):
        user_1 = User.objects.create(email='test_email_1', phone=89999999999, fam='test_fam_1', name='test_name_1',
                                     otc='test_otc_1')
        coord_1 = Coord.objects.create(latitude=55.38420000, longitude=8.15250000, height=3000)
        level_1 = Level.objects.create(winter='3A', spring='3A', summer='1A', autumn='1A')
        self.pereval_1 = PerevalAdded.objects.create(user=user_1, beauty_title='test_beauty_title_1',
                                                     title="test_title_1", other_title='test_other_title_1',
                                                     coord=coord_1, level=level_1)

        user_2 = User.objects.create(email='test_email_2', phone=87777777777, fam='test_fam_2', name='test_name_2',
                                     otc='test_otc_2')
        coord_2 = Coord.objects.create(latitude=55.38420000, longitude=8.15250000, height=3000)
        level_2 = Level.objects.create(winter='3A', spring='3A', summer='1A', autumn='1A')
        self.pereval_2 = PerevalAdded.objects.create(user=user_2, beauty_title='test_beauty_title_2',
                                                     title="test_title_2", other_title='test_other_title_2',
                                                     coord=coord_2, level=level_2)

    def test_get_list(self):
        url = reverse('PerevalAdded-list')
        response = self.client.get(url)
        serializer_data = PerevalAddedSerializer([self.pereval_1, self.pereval_2], many=True).data
        self.assertEqual(serializer_data, response.data)
        self.assertEqual(len(serializer_data), 2)
        self.assertEqual(status.HTTP_200_OK, response.status_code)

    def test_get_detail(self):
        url = reverse('PerevalAdded-detail', args=(self.pereval_1.id,))
        response = self.client.get(url)
        serializer_data = PerevalAddedSerializer(self.pereval_1).data
        self.assertEqual(serializer_data, response.data)
        self.assertEqual(status.HTTP_200_OK, response.status_code)


class PerevalAddedSerializerTestCase(TestCase):
    def setUp(self):
        user_1 = User.objects.create(email='test_email_1', fam='test_fam_1', name='test_name_1',
                                     otc='test_otc_1', phone=89999999999)
        coord_1 = Coord.objects.create(latitude="55.38420000", longitude="8.15250000", height=3000)
        level_1 = Level.objects.create(winter='3A', spring='3A', summer='1A', autumn='1A')
        self.pereval_1 = PerevalAdded.objects.create(user=user_1, beauty_title='test_beauty_title_1',
                                                     title="test_title_1", other_title='test_other_title_1',
                                                     connect="new", coord=coord_1, level=level_1)

        user_2 = User.objects.create(email='test_email_2', fam='test_fam_2', name='test_name_2',
                                     otc='test_otc_2', phone=87777777777)
        coord_2 = Coord.objects.create(latitude="55.38420000", longitude="8.15250000", height=3000)
        level_2 = Level.objects.create(winter='3A', spring='3A', summer='1A', autumn='1A')
        self.pereval_2 = PerevalAdded.objects.create(user=user_2, beauty_title='test_beauty_title_2',
                                                     title="test_title_2", other_title='test_other_title_2',
                                                     connect="new", coord=coord_2, level=level_2)

    def test_check(self):
        serializer_data = PerevalAddedSerializer([self.pereval_1, self.pereval_2], many=True).data

        expected_data = [
            {
                "id": 1,
                "status": "NW",
                "beauty_title": "test_beauty_title_1",
                "title": "test_title_1",
                "other_title": "test_other_title_1",
                "connect": 'new',
                "add_time": self.pereval_1.add_time.strftime("%Y-%m-%dT%H:%M:%S.%fZ"),
                "user": {
                    "email": "test_email_1",
                    "fam": "test_fam_1",
                    "name": "test_name_1",
                    "otc": "test_otc_1",
                    "phone": "89999999999"
                },
                "coord": {
                    "latitude": "55.38420000",
                    "longitude": "8.15250000",
                    "height": 3000
                },
                "level": {
                    "winter": "3A",
                    "spring": "3A",
                    "summer": "1A",
                    "autumn": "1A"
                },
                "images": [],
            },
            {
                "id": 2,
                "status": "NW",
                "beauty_title": "test_beauty_title_2",
                "title": "test_title_2",
                "other_title": "test_other_title_2",
                "connect": 'new',
                "add_time": self.pereval_2.add_time.strftime("%Y-%m-%dT%H:%M:%S.%fZ"),
                "user": {
                    "email": "test_email_2",
                    "fam": "test_fam_2",
                    "name": "test_name_2",
                    "otc": "test_otc_2",
                    "phone": "87777777777"
                },
                "coord": {
                    "latitude": "55.38420000",
                    "longitude": "8.15250000",
                    "height": 3000
                },
                "level": {
                    "winter": "3A",
                    "spring": "3A",
                    "summer": "1A",
                    "autumn": "1A"
                },
                "images": [],
            },
        ]

        self.assertEqual(serializer_data, expected_data)