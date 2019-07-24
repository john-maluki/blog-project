from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model
from rest_framework.reverse import reverse as api_reverse
from rest_framework import status
from blog.models import Post

User = get_user_model()


class BlogApiTestCase(APITestCase):
    def setUp(self):
        user_obj = User(username='test', email='test@gmail.com')
        user_obj.set_password('123456789')
        user_obj.save()
        Post.objects.create(
            author=user_obj,
            title='some title',
            body='some body'
        )

    def test_single_user(self):
        user_count = User.objects.count()
        self.assertEqual(user_count, 1)

    def test_single_post(self):
        post_count = Post.objects.count()
        self.assertEqual(post_count, 1)

    def test_get_list(self):
        data = {}
        url = api_reverse('post_list')
        response = self.client.get(url, data, formart='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post_create_item(self):
        data = {
            'author': 'test',
            'title': 'test1',
            'body': 'test creating item'
        }

        url = api_reverse('post_list')
        response = self.client.post(url, data, formart='json')
        self.assertEqual(
            response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED
        )
    # test if you can get an item post

    def test_get_item(self):
        blog_post = Post.objects.first()
        data = {}
        url = blog_post.get_api_url()
        response = self.client.get(url, data, formart='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
