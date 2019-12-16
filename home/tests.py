from django.test import TestCase
from django.core.files import File
from .models import LandingPage, Experience

# Create your tests here.
class LandingPageTestCase(TestCase):

    mock_resume = "./test_content/test_resume.pdf"
    mock_avatar = "./test_content/test_avatar.png"


    def setUp(self):
        LandingPage.objects.create(
            name="Seth Angell",
            bio="code fast and break quickly, but don't forget your unit test parachute",
            resume=self.mock_resume,
            avatar=self.mock_avatar
        )

    def test_text_matches(self):
        casey = LandingPage.objects.get(name="Seth Angell")
        self.assertEqual(casey.name, "Seth Angell")
        self.assertEqual(casey.bio, "code fast and break quickly, but don't forget your unit test parachute")

    def test_files_uploaded_properly(self):
        casey = LandingPage.objects.get(name="Seth Angell")
        self.assertEqual(casey.resume, self.mock_resume)
        self.assertEqual(casey.avatar, self.mock_avatar)