from django.db import models
# Create your models here.

class cms_dj_login(models.Model):
    id = models.IntegerField(max_length=11,primary_key=True)
    cms_dj_username = models.CharField(max_length=20)
    cms_dj_password = models.CharField(max_length=20)
    def __str__(self):
        return self.cms_dj_username

class cms_dj_artical(models.Model):
    id = models.IntegerField(max_length=11,primary_key=True)
    cms_dj_url = models.CharField(max_length=20)
    cms_dj_tag = models.CharField(max_length=20)
    cms_dj_tag_special = models.CharField(max_length=20)
    cms_dj_addtime = models.CharField(max_length=20)
    cms_dj_author = models.CharField(max_length=20)
    cms_dj_imgsrc = models.CharField(max_length=128)

from ckeditor_uploader.fields import RichTextUploadingField
class Entry(models.Model):
    body = RichTextUploadingField() #RichTextField()

from ckeditor.fields import RichTextField
class Post(models.Model):
    content = RichTextField()

