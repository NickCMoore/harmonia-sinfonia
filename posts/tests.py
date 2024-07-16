from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Post, Comment, Flag
from .forms import PostForm, CommentForm, FlagForm

class PostTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.post = Post.objects.create(title='Test Post', content='Test content', user=self.user)
        self.comment = Comment.objects.create(content='Test comment', post=self.post, user=self.user)

    def test_post_list_view(self):
        response = self.client.get(reverse('posts:post_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'posts/post_list.html')
        self.assertContains(response, self.post.title)

    def test_post_detail_view(self):
        response = self.client.get(reverse('posts:post_detail', args=[self.post.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'posts/post_detail.html')
        self.assertContains(response, self.post.title)

    def test_create_post_view(self):
        self.client.login(username='testuser', password='12345')
        response = self.client.post(reverse('posts:create_post'), {
            'title': 'New Post',
            'content': 'New content',
            'user': self.user.id
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Post.objects.count(), 2)

    def test_delete_post_view(self):
        self.client.login(username='testuser', password='12345')
        response = self.client.post(reverse('posts:delete_post', args=[self.post.pk]))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Post.objects.count(), 0)

    def test_toggle_like_view(self):
        self.client.login(username='testuser', password='12345')
        response = self.client.post(reverse('posts:toggle_like', args=[self.post.pk]))
        self.assertEqual(response.status_code, 302)
        self.assertTrue(self.user in self.post.likes.all())

    def test_delete_comment_view(self):
        self.client.login(username='testuser', password='12345')
        response = self.client.post(reverse('posts:delete_comment', args=[self.comment.pk]))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Comment.objects.count(), 0)

    def test_toggle_upvote_comment(self):
        self.client.login(username='testuser', password='12345')
        response = self.client.post(reverse('posts:toggle_upvote_comment', args=[self.comment.pk]))
        self.assertEqual(response.status_code, 302)
        self.assertTrue(self.user in self.comment.upvotes.all())

    def test_edit_post_view(self):
        self.client.login(username='testuser', password='12345')
        response = self.client.post(reverse('posts:edit_post', args=[self.post.pk]), {
            'title': 'Updated Post',
            'content': 'Updated content'
        })
        self.assertEqual(response.status_code, 302)
        self.post.refresh_from_db()
        self.assertEqual(self.post.title, 'Updated Post')

    