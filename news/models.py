from django.db import models
from django.contrib.auth.models import User

class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    rating = models.IntegerField()

    def update_rating(self):
        total_post_rating = sum(post.rating for post in self.post_set.all()) * 3
        total_comment_rating = sum(comment.rating for comment in self.comment_set.all())
        total_post_comment_rating = sum(comment.rating for comment in self.postcomment_set.all())
        self.rating = total_post_rating + total_comment_rating + total_post_comment_rating

    def __str__(self):
        return self.user.username

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Post(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    post_type = models.CharField(max_length=10, choices=[('article', 'Article'), ('news', 'News')])
    created_at = models.DateTimeField(auto_now_add=True)
    categories = models.ManyToManyField(Category, through='PostCategory')
    title = models.CharField(max_length=200)
    text = models.TextField()
    rating = models.IntegerField()

    def like(self):
        self.rating += 1

    def dislike(self):
        self.rating -= 1

        def preview(self):
            preview_text = self.text[:124]
            if len(self.text) > 124:
                preview_text += "..."
            return preview_text

    def __str__(self):
        return self.title

class PostCategory(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField()

    def like(self):
        self.rating += 1

    def dislike(self):
        self.rating -= 1

    def __str__(self):
        return self.text[:50]