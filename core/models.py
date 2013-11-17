#coding=gbk
from django.db import models
from tools.helper import GuidFileName


def upload_to(instance, filename):
    return GuidFileName(filename)


class Users(models.Model):
    uname = models.CharField(verbose_name='用户名', max_length=25)
    pwd = models.CharField(verbose_name='密码', max_length=12)
    sex = models.CharField(verbose_name='性别', choices=(("M", "男"), ("F", "女")), max_length=1)
    email = models.CharField(max_length=25)
    last_login_ip = models.IPAddressField(verbose_name='最后登录IP')
    last_login_date = models.DateTimeField(verbose_name='最后登录日期')
    logo = models.ImageField(verbose_name='头像', upload_to=upload_to)

    #重载meta模块,修改Admin后台中显示的名称
    class Meta:
        verbose_name = '用户'
        verbose_name_plural = '用户列表'

    def __unicode__(self):
        return self.uname


class EssayType(models.Model):
    tname = models.CharField(verbose_name='文章类名', max_length=25)
    ptype = models.ForeignKey('self', 'id', null=True, blank=True, verbose_name='所属类别')

    class Meta:
        verbose_name = '文章类型'
        verbose_name_plural = '文章类型列表'
        #按名称排序
        ordering = ['tname']

    def __unicode__(self):
        return self.tname


class Essay(models.Model):
    """文章列表,verbose_name就是等下再后台中字段的名称"""
    eType = models.ForeignKey(EssayType, verbose_name='所属类别')
    title = models.CharField(max_length=25, verbose_name='文章标题')
    content = models.TextField(max_length=2000, verbose_name='文章内容')
    abstract = models.TextField(max_length=150, verbose_name='文章摘要')
    pub_date = models.DateTimeField(verbose_name='发表日期')
    view_count = models.IntegerField(verbose_name='浏览次数', default=0)


    class Meta:
        verbose_name = '文章'
        verbose_name_plural = '文章列表'
        #按时间排序
        ordering = ['-pub_date']

    def __unicode__(self):
        return self.title


class Comment(models.Model):
    uname = models.CharField(max_length=25, verbose_name='回复者名称')
    email = models.EmailField(max_length=25, verbose_name='回复者Email')
    content = models.TextField(max_length=200, verbose_name='回复内容')
    pub_date = models.DateTimeField(verbose_name='回复日期')
    essay = models.ForeignKey(Essay, related_name='essay_comment')
    reply_to = models.ForeignKey('self', 'id', null=True, blank=True, verbose_name='所属类别')

    class Meta:
        verbose_name = '回复'
        verbose_name_plural = '回复信息列表'

    def __unicode__(self):
        return self.uname


class LevelMsg(models.Model):
    """留言信息表"""
    uname = models.CharField(max_length=25, verbose_name='留言者名称')
    content = models.TextField(max_length=200, verbose_name='留言内容')
    email = models.EmailField(max_length=25, verbose_name='留言者Email')

    class Meta:
        verbose_name = '留言板'
        verbose_name_plural = '留言信息列表'

    def __unicode__(self):
        return self.uname


class Archive(models.Model):
    essay = models.ForeignKey(Essay, related_name='archive_essay')
    pub_date = models.DateTimeField(verbose_name='存档日期')

    class Meta:
        verbose_name = '存档信息'
        verbose_name_plural = '存档信息列表'

    def __unicode__(self):
        return str(self.pub_date) + "(" + self.essay.title + ")"