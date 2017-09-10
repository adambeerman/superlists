from django.test import TestCase

# Create your tests here.

class SmokeTest(TestCase):

	# Add a purposely failing test to confirm that we trust this Django test driver
	def test_bad_maths(self):
		self.assertEqual(1+1,3)
