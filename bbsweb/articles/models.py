from django.contrib.auth.models import User
from django.db import models

# Create your models here.
'''
第一步在此建 articles 表模型
第二步 setting.py 增加 articles.apps.ArticlesConfig
第三步 python manage.py makemigrations articles
第四步 python manage.py migrate
'''


class Articles(models.Model):
    user_id = models.ForeignKey(User, related_name='articles', on_delete=models.CASCADE)
    title = models.CharField(max_length=50, blank=False)
    main_body = models.TextField(blank=False, default='')
    create_time = models.DateTimeField(auto_now_add=True)
    is_del = models.BooleanField(default=False)

    class Meta:
        ordering = ['create_time']


class Comments(models.Model):
    user_id = models.ForeignKey(User, related_name='comments', on_delete=models.CASCADE)  # 评论者ID
    article_id = models.ForeignKey(Articles, related_name='comments', on_delete=models.CASCADE)  # 文章编写者ID
    content = models.TextField(blank=False, default='')
    create_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['create_time']
