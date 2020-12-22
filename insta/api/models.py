import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser, AnonymousUser
from typing import Union
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFit

# Create your models here.

class BaseModel(models.Model):
    """Base model for the application. Uses UUID for pk."""
    id = models.UUIDField(
        primary_key=True,
        editable=False,
        default=uuid.uuid4,
    )
    class Meta:
        abstract = True

class User(BaseModel, AbstractUser):
    profile_picture = models.ImageField(('profile_picture'),upload_to="photos",blank=True)
    bio = models.CharField(blank=True, null=True, max_length=250)

    def __str__(self):
        return self.username

RequestUser = Union[AnonymousUser, User]       


class Like(BaseModel):
    likes=models.ManyToManyField(User,blank=True, related_name='likes')
     
    @property
    def total_likes(self):
        return self.likes


class Comment(BaseModel):
    content = models.TextField(max_length=2000)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content

    class Meta:
        ordering = ["-created_at"]


class Post(BaseModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    photo = ProcessedImageField(
        upload_to="photos",
        format="JPEG",
        options={"quality": 90},
        processors=[ResizeToFit(width=1200, height=1200)],
    )

    caption = models.TextField()
    comments = models.ForeignKey(Comment, editable=True, on_delete=models.CASCADE)
    likes = models.ForeignKey(Like, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.caption

    def get_image_url(self, obj):
        return obj.image.url

    class Meta:
        ordering = ["-created_at"]




