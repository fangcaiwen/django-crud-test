from django.db import models


# Create your models here.

class Article(models.Model):
    # 文章唯一Id
    article_id = models.AutoField(primary_key=True)
    # 文章标题
    title = models.TextField()
    # 文章的摘要
    brief_content = models.TextField()
    # 文章的主要内容
    content = models.TextField()
    # 文章的发布日期
    publish_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    user_name = models.TextField()
    user_age = models.IntegerField()
    user_phone = models.TextField()
    user_address = models.TextField()

    def __str__(self):
        return [self.user_name, self.user_age]
