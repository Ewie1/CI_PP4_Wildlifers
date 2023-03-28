# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.test import TestCase
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


class TestProgramViews(TestCase):
    """
    Class for testing program views
    """

    def test_get_programs_page(self):
        """
        Function to confirm program page
        display without error
        """
        response = self.client.get('/programs/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'programs/programs_list.html')
