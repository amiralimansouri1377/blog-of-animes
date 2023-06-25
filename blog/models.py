from django.db import models
from django.urls import reverse

# Create your models here.


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Tag(models.Model):
    caption = models.CharField(max_length=100)

    def __str__(self):
        return self.caption


class Post(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True)
    tag = models.ManyToManyField(Tag)

    title = models.CharField(max_length=150)
    image = models.ImageField(upload_to="images")
    content = models.TextField()
    summery = models.CharField(max_length=300)
    pub_date = models.DateField(auto_now=True)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return f"{self.title}"

    def get_absolute_url(self):
        return reverse("detail-post", args=[self.slug])


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True)
    comment_text = models.TextField()
    user_email = models.EmailField()

    def __str__(self):
        return self.comment_text
