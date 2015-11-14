#coding=utf8
from django.shortcuts import render, render_to_response
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib import auth
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from forms import LogForm, ProfileForm, StrategyForm, HopeForm
from models import Log, Profile, Strategy, Hope
from PIL import Image
from django.utils.timezone import timedelta
import datetime
from django.db.models import Q 
# Create your views here.
# the test
@csrf_exempt
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            return HttpResponseRedirect("/login/")
    else:
        form = UserCreationForm()
    return render_to_response("register.html", {'form': form,})
@csrf_exempt
@login_required
def index(request):
    u = request.user
    username = u.username
    p = Profile.objects.get_or_create(user = u)[0]
    img_mark = p.is_img
    logs = u.log_set.all().order_by('-date')
    strgys = Strategy.objects.all()
    return render_to_response("index.html", locals())

@csrf_exempt
@login_required
def ensure_logout(request):
    u = request.user
    username = u.username
    p = Profile.objects.get_or_create(user = u)[0]
    img_mark = p.is_img
    if request.method == 'POST':
        if request.POST.has_key('ensure'):
            auth.logout(request)
            return HttpResponseRedirect("/login/")
        else:
            return HttpResponseRedirect("/index/")
    return render_to_response("logout.html", locals())

@csrf_exempt
@login_required
def addlog(request):
    u = request.user
    username = u.username
    p = Profile.objects.get_or_create(user = u)[0]
    img_mark = p.is_img
    if request.method == 'POST':
        form = LogForm(request.POST)
        if form.is_valid():
            log = Log()
            log.content = form.cleaned_data["content"]
            log.title = form.cleaned_data["title"]
            log.user = request.user
            log.save()
            return HttpResponseRedirect("/index/")
    else:
        form = LogForm()
    return render_to_response('addlog.html', locals())

@csrf_exempt
@login_required

def mylog(request, id):
    u = request.user
    username = u.username
    p = Profile.objects.get_or_create(user = u)[0]
    img_mark = p.is_img
    mylog = u.log_set.all().get(title = id)
    logs = u.log_set.all().order_by('-date') 
    return render_to_response('mylog.html', locals())
@csrf_exempt
@login_required
def myprofile(request):
    u = request.user
    #User.profile = property(lambda u: Profile.objects.get_or_create(user = u)[0])
    p = Profile.objects.get_or_create(user = u)[0]
    username = p.user.username
    img_mark = p.is_img
    if request.method == 'POST':       
        form = ProfileForm(request.POST, instance = p)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/profile/")
    else:
        form = ProfileForm(instance = p)
    return render_to_response('profile.html', locals())

@csrf_exempt
@login_required
def passwd_change(request):
    u = request.user
    username = u.username
    p = Profile.objects.get_or_create(user = u)[0]
    img_mark = p.is_img
    if request.method == 'POST':
        if request.POST.has_key('cancel'):
            return HttpResponseRedirect("/index/")
        else:
            old_passwd = request.POST.get('old_passwd')
            new_passwd = request.POST.get('new_passwd')
            new_passwd2 = request.POST.get('new_passwd2')
            if u.check_password(old_passwd):
                if new_passwd == new_passwd2:
                    u.set_password(new_passwd)
                    u.save()
                    return HttpResponseRedirect("/index/")
                else:
                    return HttpResponseRedirect("/passwd_change/")
            else:
                return HttpResponseRedirect("/passwd_change/")
    return render_to_response('passwd_change.html', locals())
            
  
@csrf_exempt
@login_required
def img(request):
    u = request.user
    username = u.username
    p = Profile.objects.get_or_create(user = u)[0]
    img_mark = p.is_img
    if request.method == 'POST':       
        if 'image' in request.FILES:
            image=request.FILES["image"]
            img=Image.open(image)
            img.thumbnail((112,54),Image.ANTIALIAS)
            name='./static/imgs/'+username+'.png'
            img.save(name,"png")
            p.is_img = 1
            p.save()
            return HttpResponseRedirect("/index/")
    return render_to_response('img.html', locals())
    '''
    if request.method == 'POST':
        form = ImgForm(request.POST, request.FILES)
        if form.is_valid():
            p.img = form.cleaned_data['image']
            p.save()
            return HttpResponseRedirect("/index/")
    return render_to_response('img.html', locals())
'''
@csrf_exempt
@login_required
def addstrgy(request):
    u = request.user
    username = u.username
    p = Profile.objects.get_or_create(user = u)[0]
    img_mark = p.is_img
    if request.method == 'POST':
        form = StrategyForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/index/")
    else:
        form = StrategyForm()
    return render_to_response('addstrgy.html', locals())
    
@csrf_exempt
@login_required

def showstrgy(request, id):
    u = request.user
    username = u.username
    p = Profile.objects.get_or_create(user = u)[0]
    img_mark = p.is_img
    strgy = Strategy.objects.all().get(title = id)
    strgys = Strategy.objects.all().order_by('date')
    return render_to_response('showstrgy.html', locals())

@csrf_exempt
@login_required

def myhope(request):
    u = request.user
    username = u.username
    p = Profile.objects.get_or_create(user = u)[0]
    img_mark = p.is_img
    h = Hope.objects.get_or_create(user = u)[0]
    if request.method == 'POST':       
        form = HopeForm(request.POST, instance = h)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/myhope/")
    else:
        form = HopeForm(instance = h)
    return render_to_response('myhope.html', locals())
    
@csrf_exempt
@login_required
def design(request):
    u = request.user
    username = u.username
    p = Profile.objects.get_or_create(user = u)[0]
    img_mark = p.is_img
    return render_to_response('design.html', locals())
    
@csrf_exempt
@login_required
def result(request, id1, id2):
    u = request.user
    username = u.username
    p = Profile.objects.get_or_create(user = u)[0]
    img_mark = p.is_img
    home1 = id1
    home2 = id2
    return render_to_response('result.html', locals())

@csrf_exempt
@login_required
def advice(request):
    u = request.user
    username = u.username
    p = Profile.objects.get_or_create(user = u)[0]
    img_mark = p.is_img
    h = Hope.objects.get_or_create(user = u)[0]
    print h.start_date
    print h.end_date
    hlist = Hope.objects.filter(home__contains = h.home).filter(goal__contains = h.goal).filter(busy = 0)\
            .exclude(Q(end_date__lt = h.start_date)|Q(start_date__gt = h.end_date))
    return render_to_response('advice.html', locals())

@csrf_exempt
@login_required
def myfriend(request, id):
    u = request.user
    username = u.username
    p = Profile.objects.get_or_create(user = u)[0]
    img_mark = p.is_img
    h = Hope.objects.get_or_create(user = u)[0]
    hlist = Hope.objects.filter(home__contains = h.home).filter(goal__contains = h.goal).filter(busy = 0)\
            .exclude(Q(end_date__lt = h.start_date)|Q(start_date__gt = h.end_date))
    target_user = User.objects.get(username = id)
    target_hope = target_user.hope
    return render_to_response('myfriend.html', locals())










    
