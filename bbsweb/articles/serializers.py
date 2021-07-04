from rest_framework import serializers

from .models import Articles, Comments


class ArticlesSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='user_id.username')

    class Meta:
        model = Articles
        fields = ['url', 'id', 'user_id', 'title', 'create_time', 'main_body', 'owner']


class ArticlesSerializerV2(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='user_id.username')

    class Meta:
        model = Articles
        fields = ['url', 'id', 'user_id', 'title', 'main_body', 'owner']


class CommentsSerializer(serializers.HyperlinkedModelSerializer):
    articles = serializers.PrimaryKeyRelatedField(many=True, queryset=Articles.objects.all())

    class Meta:
        model = Comments
        fields = ['url', 'id', 'user_id', 'article_id', 'content']


'''
from articles.models import Articles
from django.contrib.auth.models import User
from articles.serializers import ArticlesSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

article1 = Articles(user_id=User(id=2),title='请党放心 强哥有我', main_body='庆祝党建100周年')
article1.save()

serializer1 = ArticlesSerializer(article1)
serializer1.data

'''
