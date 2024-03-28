from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from .models import CallRecord

class CallRecordTests(APITestCase):
    def setUp(self):
        self.call_record = CallRecord.objects.create(
            caller_name='Hari',
            duration='00:10:00',
            recording_url='https://example.com/call_recordings/8885588889.wav'
        )

    def test_get_call_records(self):
        url = reverse('call-record-list-create')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_get_call_record_detail(self):
        url = reverse('call-record-detail', kwargs={'pk': self.call_record.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['caller_name'], 'Hari')

    def test_call_record_aggregation(self):
        url = reverse('call-record-aggregation')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
