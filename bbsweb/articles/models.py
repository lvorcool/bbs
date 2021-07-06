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
    user_id = models.ForeignKey(User, related_name='articles', on_delete=models.CASCADE, verbose_name='作者ID')
    title = models.CharField(max_length=50, blank=False, verbose_name='文章标题')
    main_body = models.TextField(blank=False, default='', verbose_name='文章正文')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    is_del = models.BooleanField(default=False)

    class Meta:
        ordering = ['create_time']


class Comments(models.Model):
    user_id = models.ForeignKey(User, related_name='comments', on_delete=models.CASCADE, verbose_name='评论者ID')
    article_id = models.ForeignKey(Articles, related_name='comments', on_delete=models.CASCADE, verbose_name='文章编写者ID')
    content = models.TextField(blank=False, default='', verbose_name='评论内容')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    class Meta:
        ordering = ['create_time']
