from django.test import TestCase
from .models import BlogPost, PostImage
from PIL import Image as img
from io import BytesIO

# Create your tests here.
class BlogPostTestCase(TestCase):

    def generate_test_photos(self, file_type):
        u_conv_image = BytesIO()
        t_u_img = img.new('RGB', size=(100, 100), color=(155, 0, 0))
        t_u_img.save(u_conv_image, file_type)
        u_conv_image.name = f'test_image.{file_type}'
        u_conv_image.seek(0)
        return u_conv_image

    file_test_post = open("./test_content/SampleHeaderPost.txt")
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

        PostImage.objects.create(
            post=self.penultimate_post,
            reference="TestImage",
            alt_text="Developer",
            image=self.generate_test_photos("JPEG")
        )

        self.test_image = PostImage.objects.get(post=self.penultimate_post)

    def test_body_saved_properly(self):
        self.assertEqual(self.penultimate_post.md_body, self.test_post)

    def test_title_saved_properly(self):
        self.assertEqual(self.penultimate_post.title, self.test_title)

    def test_preview_stripped_properly(self):
        self.assertEqual(self.penultimate_post.preview, "This should be a standard sentence, except this word should be bold. Along with that, here are a few")

    def test_slugify_success(self):
        penultimate_post = BlogPost.objects.get(slug="sample-header-post")
        self.assertEqual(penultimate_post.slug, self.test_title.lower().replace(" ", "-"))

    def test_path_looks_correct(self):
        self.assertTrue(str(self.test_image.image.name).__contains__(".png"))

    def test_image_src_properly_translated(self):
        self.assertTrue(str(self.penultimate_post.html_body).__contains__("/media/blog_images/ProfilePicture.png"))


