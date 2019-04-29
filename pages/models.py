from django.db import models


class Article(models.Model):
    """文章模型"""
    # 自动添加id
    # article_id = models.AutoField(primary_key=True)
    title = models.CharField(verbose_name='标题',max_length=200)
    content = models.TextField(verbose_name='内容')
    create_time = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)
    update_time = models.DateTimeField(verbose_name='最后修改时间', auto_now=True)
    # tags = models.ManyToManyField(verbose_name='别名', 'Tag', through='ArticleTags', related_name='articles', blank=True)
    # 多对多关联（语法糖）through: 关联
    tags = models.ManyToManyField('Tag', through='ArticleTags')

    def __str__(self):
        return self.title

    # 元类
    class Meta:
        # 此类在后台管理时的别名
        verbose_name = '文章'
        verbose_name_plural = '文章'
        app_label = 'pages'

class Tag(models.Model):
    """标签模型"""
    # 自动添加id
    # tag_id = models.AutoField(verbose_name='内容', primary_key=True)
    name = models.CharField(verbose_name='标签名', max_length=30)
    articles = models.ManyToManyField('Article', through='ArticleTags')

    def __str__(self):
        return self.name 

    class Meta:
        # 唯一约束
        # unique_together = ('name',)
        verbose_name = '标签'
        verbose_name_plural = '标签'
        app_label = 'pages'

class ArticleTags(models.Model):
    """文章标签关联模型"""
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)

    def __str__(self):
        return '{0}[{1}]'.format(self.article.title, self.tag.name)

    class Meta:
        verbose_name = '文章标签'
        verbose_name_plural = '文章标签'
        app_label = 'pages'

class Sentence(models.Model):
    rhesis = models.TextField(verbose_name='名句')
    author = models.CharField(verbose_name="作者", max_length=30)

    def __str__(self):
        return '{0}'.format(self.rhesis)

    class Meta:
        verbose_name = "句子"
        verbose_name_plural = '句子'
        app_label = 'pages'


# 业务
#     Article(文章)
#         id
#         title(标题)
#         content(内容)
#         create_time(创建时间)
#         upate_time(最后修改时间)
#     Tag(标签)
#         id
#         name(标签名)
#     ArticleTags(文章-标签关联)
#         article_id(文章id)
#         tag_id(标签id)