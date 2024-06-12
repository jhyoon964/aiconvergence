import datetime
from django.db import models
from django.utils import timezone
class Post(models.Model):
    postname = models.CharField(max_length=50)
    # 게시글 Post에 이미지 추가
    mainphoto = models.ImageField(blank=True, null=True)
    contents = models.TextField()

    # postname이 Post object 대신 나오기
    def __str__(self):
        return self.postname
    
    
class AdminInfo(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    
class Video(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    video_file = models.FileField(upload_to='videos/')

    def __str__(self):
        return self.title