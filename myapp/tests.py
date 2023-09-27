from django.test import TestCase

# Create your tests here.
from myapp.models import Reporter

class ReporterTest(TestCase):
    def setUp(self) -> None:
        Reporter.objects.create(first_name = 'nishank',last_name = 'shrma',email = 'ns@gmail.com')
        Reporter.objects.create(first_name = 'santosh',last_name = 'prdhaan',email = 'sp@gmail.com')
    def test_reporter_object_create(self):
        r1 = Reporter.objects.get(email='ns@gmail.com')
        r2 = Reporter.objects.get(email='sp@gmail.com')

        self.assertEqual(r1.first_name, 'nishank')
        self.assertEqual(r1.last_name, 'shrma')
        self.assertEqual(r2.first_name, 'santosh')
        self.assertEqual(r2.last_name, 'prdhaan')