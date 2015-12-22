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
    friend = models.ManyToManyField('self')
    def __unicode__(self):
        return self.user.username
    
class Site(models.Model):
    siteID = models.AutoField(primary_key = True)
    name = models.CharField(verbose_name = '景点名', max_length = 20)
    content = models.CharField(verbose_name = '描述', max_length = 50, blank = True)
    price = models.IntegerField(verbose_name = '价格')
    is_img = models.IntegerField(default = 0)

class Log(models.Model):
    logID = models.AutoField(primary_key = True)
    user = models.ForeignKey(User)
    title = models.CharField(max_length = 50, verbose_name = '日志题目')
    content = models.CharField(max_length = 1000, verbose_name = '内容')
    date = models.DateTimeField(verbose_name = '日期', auto_now = True)
    is_img = models.BooleanField(default = False)
    img_name = models.CharField(max_length = 50, default = '')
    def __unicode__(self):
        return self.title + '_...' + self.content[0:10] + '..._' + str(self.date) + u'作者' + str(self.user.username)

class Strategy(models.Model):
    strgyID = models.AutoField(primary_key = True)
    title = models.CharField(max_length = 50)
    content = models.CharField(max_length = 1000)
    date = models.DateTimeField(verbose_name = '日期', auto_now_add = True)
    user = models.ForeignKey(User, related_name = 'user_strgy_set')
    site = models.ForeignKey(Site, blank = True, null = True, related_name = 'site_strgy_set')
    def __unicode__(self):
        return self.title + '_...' + self.content[0:10] + '..._' + str(self.date)

class Hope(models.Model):
    user = models.OneToOneField(User)
    home = models.CharField(max_length = 50, blank = True)
    goal = models.CharField(max_length = 50, blank = True)
    start_date = models.DateField(blank = True, null = True)
    end_date = models.DateField(blank = True, null = True)
    price = models.IntegerField(blank = True, null = True)
    busy = models.IntegerField(verbose_name = '是否空闲', choices = ((1, '忙碌'), (0, '空闲')), default = 0)
    landtype = models.CharField(verbose_name = '目的地类型', max_length = 10, choices = (('any', '随意'),
        ('plain', '平原'), ('mountain', '山林'), ('water', '湖海'), ('interest', '名胜'),
        ('scenery', '景区'), ('explore', '探险')), default = 'any')
    hopesry = models.CharField(max_length = 50, blank = True)
    is_commit = models.BooleanField(default = False)
    tip = models.CharField(max_length = 128, blank = True)
    def __unicode__(self):
        return self.user.username + "\'s hope"

class Messages(models.Model):
    msgID = models.AutoField(primary_key = True)
    go = models.ForeignKey(User, related_name = 'go_set')
    come = models.ForeignKey(User, related_name = 'come_set')
    msg_type = models.IntegerField()
    msg_deal = models.IntegerField(default = 3)
    is_req = models.BooleanField()
    is_read = models.BooleanField(default = False)
    date = models.DateTimeField(auto_now_add = True)
    def __unicode__(self):
        return str(self.date) + "from" + str(self.come.username) + "to" + str(self.go.username)


class Activity(models.Model):
    actID = models.AutoField(primary_key = True)
    title = models.CharField(max_length = 20, blank = True)
    content = models.CharField(max_length = 100, blank = True)
    author = models.ForeignKey(User, related_name = 'author_set')
    start_date = models.DateField(blank = True, null = True)
    end_date = models.DateField(blank = True, null = True)
    is_valid = models.BooleanField(default = True)
    is_end = models.BooleanField(default = False)
    date = models.DateTimeField(auto_now = True)
    def __unicode__(self):
        return str(self.author.username) + "\'s activity..." + str(self.date)



class Person(models.Model):
    user = models.OneToOneField(User)
    act = models.ForeignKey(Activity, related_name = 'person_set')
    date = models.DateTimeField(verbose_name = '日期', auto_now = True)
    def __unicode__(self):
        return str(self.user.username) + "\'s person"



class Describe(models.Model):
    dscrbID = models.AutoField(primary_key = True)
    content = models.CharField(max_length = 20, blank = True)
    user = models.ManyToManyField(User)
    def __unicode__(self):
        return self.content

class SiteImg(models.Model):
    siteID = models.AutoField(primary_key = True)
    name = models.CharField(max_length = 20, blank = True)
    site = models.ForeignKey(Site)
    def __unicode__(self):
        return self.name
    
class SiteCommit(models.Model):
    scID = models.AutoField(primary_key = True)
    content = models.CharField(max_length = 50)
    site = models.ForeignKey(Site, related_name = 'site_sitecommit_set')
    user = models.ForeignKey(User, related_name = 'user_sitecommit_set')
    date = models.DateTimeField(auto_now_add = True, blank = True)
    def __unicode__(self):
        return self.content




    
