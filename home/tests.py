from django.test import TestCase
from django.core.files import File
from .models import LandingPage, Experience
import mock

# Create your tests here.
class LandingPageTestCase(TestCase):

    mock_resume = mock.MagicMock(spec=File)
    mock_resume.name = "Beme.pdf"

    mock_avatar = mock.MagicMock(spec=File)
    mock_avatar.name="broken_sunglasses.png"


    def setUp(self):
        LandingPage.objects.create(
            name="Casey Neistat",
            bio="New York's favorite film maker",
            resume=self.mock_resume,
            avatar=self.mock_avatar
        )

    def test_text_matches(self):
        casey = LandingPage.objects.get(name="Casey Neistat")
        self.assertEqual(casey.name, "Casey Neistat")
        self.assertEqual(casey.bio, "New York's favorite film maker")

    def test_files_uploaded_properly(self):
        casey = LandingPage.objects.get(name="Casey Neistat")
        self.assertEqual(casey.resume, self.mock_resume)
        self.assertEqual(casey.avatar, self.mock_avatar)