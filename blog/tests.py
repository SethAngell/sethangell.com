from django.test import TestCase
from .models import BlogPost, PostImage

# Create your tests here.
class BlogPostTestCase(TestCase):


    file_test_post = open("./test_content/SampleHeaderPost.txt")
    file_test_image = "./test_content/test_avatar.jpg"
    test_post = ""
    test_title = "Sample Header post"
    for line in file_test_post:
        test_post += line

    def setUp(self) -> None:
        BlogPost.objects.create(
            md_body=self.test_post
        )

        self.test_post = self.test_post.split("\n")
        self.test_post.pop(0)
        self.test_post = "\n".join(self.test_post)
        self.penultimate_post = BlogPost.objects.get(slug="sample-header-post")

    def test_body_saved_properly(self):
        self.assertEqual(self.penultimate_post.md_body, self.test_post)

    def test_title_saved_properly(self):
        self.assertEqual(self.penultimate_post.title, self.test_title)

    def test_preview_stripped_properly(self):
        self.assertEqual(self.penultimate_post.preview, "This should be a standard sentence, except this word should be bold. Along with that, here are a few")

    def test_slugify_success(self):
        penultimate_post = BlogPost.objects.get(slug="sample-header-post")
        self.assertEqual(penultimate_post.slug, self.test_title.lower().replace(" ", "-"))


