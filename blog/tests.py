from django.test import TestCase
from .models import BlogPost

# Create your tests here.
class BlogPostTestCase(TestCase):


    file_test_post = open("./test_content/SampleHeaderPost.txt")
    test_post = ""
    test_title = "Sample Header post"
    for line in file_test_post:
        test_post += line

    def setUp(self) -> None:
        BlogPost.objects.create(
            body=self.test_post
        )
        self.penultimate_post = BlogPost.objects.get(slug="sample-header-post")

    def test_body_saved_properly(self):
        self.assertEqual(self.penultimate_post.body, self.test_post)

    def test_title_saved_properly(self):
        self.assertEqual(self.penultimate_post.title, self.test_title)

    def test_preview_stripped_properly(self):
        self.assertEqual(self.penultimate_post.preview, "This should be a standard sentence, except this word should be bold. Along with that, here are a few")

    def test_slugify_success(self):
        penultimate_post = BlogPost.objects.get(slug="sample-header-post")
        self.assertEqual(penultimate_post.slug, self.test_title.lower().replace(" ", "-"))

