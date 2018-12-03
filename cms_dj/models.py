from django.db import models
# Create your models here.

class cms_dj_login(models.Model):
    id = models.IntegerField(max_length=11,primary_key=True)
    cms_dj_username = models.CharField(max_length=255)
    cms_dj_password = models.CharField(max_length=255)
    def __str__(self):
        return self.cms_dj_username

class cms_dj_artical(models.Model):
    id = models.IntegerField(max_length=11,primary_key=True)
    cms_dj_url = models.CharField(max_length=255)
    cms_dj_url = models.CharField(max_length=255)
    cms_dj_tag = models.CharField(max_length=255)
    cms_dj_addtime = models.CharField(max_length=255)
    cms_dj_author = models.CharField(max_length=255)
