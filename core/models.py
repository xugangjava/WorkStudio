#coding=gbk
from django.db import models
from tools.helper import GuidFileName


def upload_to(instance, filename):
    return GuidFileName(filename)


class Users(models.Model):
    uname = models.CharField(verbose_name='�û���', max_length=25)
    pwd = models.CharField(verbose_name='����', max_length=12)
    sex = models.CharField(verbose_name='�Ա�', choices=(("M", "��"), ("F", "Ů")), max_length=1)
    email = models.CharField(max_length=25)
    last_login_ip = models.IPAddressField(verbose_name='����¼IP')
    last_login_date = models.DateTimeField(verbose_name='����¼����')
    logo = models.ImageField(verbose_name='ͷ��', upload_to=upload_to)

    #����metaģ��,�޸�Admin��̨����ʾ������
    class Meta:
        verbose_name = '�û�'
        verbose_name_plural = '�û��б�'

    def __unicode__(self):
        return self.uname


class EssayType(models.Model):
    tname = models.CharField(verbose_name='��������', max_length=25)
    ptype = models.ForeignKey('self', 'id', null=True, blank=True, verbose_name='�������')

    class Meta:
        verbose_name = '��������'
        verbose_name_plural = '���������б�'
        #����������
        ordering = ['tname']

    def __unicode__(self):
        return self.tname


class Essay(models.Model):
    """�����б�,verbose_name���ǵ����ٺ�̨���ֶε�����"""
    eType = models.ForeignKey(EssayType, verbose_name='�������')
    title = models.CharField(max_length=25, verbose_name='���±���')
    content = models.TextField(max_length=2000, verbose_name='��������')
    abstract = models.TextField(max_length=150, verbose_name='����ժҪ')
    pub_date = models.DateTimeField(verbose_name='��������')
    view_count = models.IntegerField(verbose_name='�������', default=0)


    class Meta:
        verbose_name = '����'
        verbose_name_plural = '�����б�'
        #��ʱ������
        ordering = ['-pub_date']

    def __unicode__(self):
        return self.title


class Comment(models.Model):
    uname = models.CharField(max_length=25, verbose_name='�ظ�������')
    email = models.EmailField(max_length=25, verbose_name='�ظ���Email')
    content = models.TextField(max_length=200, verbose_name='�ظ�����')
    pub_date = models.DateTimeField(verbose_name='�ظ�����')
    essay = models.ForeignKey(Essay, related_name='essay_comment')
    reply_to = models.ForeignKey('self', 'id', null=True, blank=True, verbose_name='�������')

    class Meta:
        verbose_name = '�ظ�'
        verbose_name_plural = '�ظ���Ϣ�б�'

    def __unicode__(self):
        return self.uname


class LevelMsg(models.Model):
    """������Ϣ��"""
    uname = models.CharField(max_length=25, verbose_name='����������')
    content = models.TextField(max_length=200, verbose_name='��������')
    email = models.EmailField(max_length=25, verbose_name='������Email')

    class Meta:
        verbose_name = '���԰�'
        verbose_name_plural = '������Ϣ�б�'

    def __unicode__(self):
        return self.uname


class Archive(models.Model):
    essay = models.ForeignKey(Essay, related_name='archive_essay')
    pub_date = models.DateTimeField(verbose_name='�浵����')

    class Meta:
        verbose_name = '�浵��Ϣ'
        verbose_name_plural = '�浵��Ϣ�б�'

    def __unicode__(self):
        return str(self.pub_date) + "(" + self.essay.title + ")"