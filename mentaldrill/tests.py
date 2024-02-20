
from unittest import TestCase
from .views import add_two_numbers



# Disable all but critical errors during normal test run
# uncomment for debugging failing tests
# logging.disable(logging.CRITICAL)
class TestMentalDrill(TestCase):
    """this test the mental drill app"""

    def test_add_two_numbers(self):
        """It should return the index page"""
        self.assertEqual(add_two_numbers(10,5), 15)




    def test_index(self):
        """It should return the index page
        response = self.client.get("/")
        self.assertEqual(response.status_code, "HTTP_200_OK")
        #self.assertIn(b"Product Catalog Administration", response.data)
        """


