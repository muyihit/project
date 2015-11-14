#coding=utf8
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User)
    nickname = models.CharField(max_length = 16, blank = True)
    age = models.IntegerField(default = 0)
    sex = models.IntegerField(choices = ((1, '男'), (0, '女')), default = 1)
    phone = models.CharField(max_length = 20, blank = True)
    qq = models.CharField(max_length = 20, blank = True)
    #myemail = models.EmailField(verbose_name = '邮箱', blank = True,)
    travellike = models.CharField(max_length = 50, blank = True)
    question = models.CharField(max_length = 50, blank = True)
    answer = models.CharField(max_length = 50, blank = True)
    #img = models.ImageField(blank = True)
    is_img = models.IntegerField(default = 0)
    def __unicode__(self):
        return self.user.username

    
class Site(models.Model):
    siteID = models.IntegerField(primary_key = True)
    name = models.CharField(max_length = 20)
    price = models.IntegerField()

class Log(models.Model):
    user = models.ForeignKey(User)
    title = models.CharField(max_length = 50, verbose_name = '日志题目')
    content = models.CharField(max_length = 1000, verbose_name = '内容')
    date = models.DateTimeField(verbose_name = '日期', primary_key = True, auto_now_add = True)
    def __unicode__(self):
        return self.title + '_...' + self.content[0:10] + '..._' + str(self.date)

class Strategy(models.Model):
    title = models.CharField(max_length = 50)
    content = models.CharField(max_length = 1000)
    date = models.DateTimeField(verbose_name = '日期', primary_key = True, auto_now_add = True)
    def __unicode__(self):
        return self.title + '_...' + self.content[0:10] + '..._' + str(self.date)

class Hope(models.Model):
    user = models.OneToOneField(User)
    home = models.CharField(max_length = 50, blank = True)
    goal = models.CharField(max_length = 50, blank = True)
    start_date = models.DateField(blank = True, null = True)
    end_date = models.DateField(blank = True, null = True)
    price = models.IntegerField(default = 0)
    number = models.IntegerField(default = 0)
    landtype = models.CharField(verbose_name = '目的地类型', max_length = 10, choices = (('any', '随意'),
        ('plain', '平原'), ('mountain', '山林'), ('water', '湖海'), ('interest', '名胜'),
        ('scenery', '景区'), ('explore', '探险')), default = 'any')
    busy = models.IntegerField(verbose_name = '是否空闲', choices = ((1, '忙碌'), (0, '空闲')), default = 0)
    hopesry = models.CharField(max_length = 50, blank = True)
    tip = models.CharField(max_length = 128, blank = True)
    def __unicode__(self):
        return self.user.username + "\'s hope"

    
class Friends(models.Model):
    user = models.OneToOneField(User)
    friend = models.ManyToManyField('self', related_name = "friend")
    
