#coding=utf8
from django.shortcuts import render, render_to_response
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib import auth
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from forms import *
from models import *
from PIL import Image
from django.utils.timezone import timedelta
import datetime
from django.db.models import Q
from django.core.mail import send_mail
from mysite.settings import EMAIL_HOST_USER
# Create your views here.
# the test
# the second git test
@csrf_exempt
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():

            user = form.save()
            #return HttpResponseRedirect("/login/")
            user.is_active = False
            user.save()
            send_mail( "驴友推荐网站",
                       "http://localhost:8000/ensure/?username=%s&password=%s"%(user.username,user.password),
                       "1275288367@qq.com",
                        [user.email]
                        )
            return HttpResponseRedirect("/login/")
    else:
        form = RegisterForm()
    return render_to_response("register.html", {'form': form,})

@csrf_exempt 
def ensure(request):
    if request.method =='GET':
        username=request.GET.get("username")
        password=request.GET.get("password")
        if User.objects.filter(username=username).exists():
            user = User.objects.get(username=username)
            if user.is_active==False:
                user.is_active = True
                user.save()
                return HttpResponseRedirect("/login/")
            else:
                return HttpResponse("未激活成功！！！")
        else:
            return HttpResponse("用户不存在！！！")
    return HttpResponse("Nothing Happened")

@csrf_exempt
def find_password(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        email = request.POST.get("email")
        if User.objects.filter(username=username).exists() and User.objects.get(username=username).email== email:
            user = User.objects.get(username=username)
            if user.is_active == True:
                send_mail("find password",
                          "http://localhost:8000/rewrite_password/?username=%s&password=%s"%(username,user.password),
                          "1275288367@qq.com",
                          [email]
                        )
                return HttpResponse("find email")
            else:
                return HttpResponse("the user is not active")
        else:
            return HttpResponse("the user is not exist")
    return render_to_response("find_password.html",locals())

@csrf_exempt
def rewrite_password(request):
    username = request.GET.get("username")
    password = request.GET.get("password")
    if username and password and User.objects.filter(username=username).exists():
        user = User.objects.get(username=username)
        if request.method == 'POST':
            if request.POST.get("password1") == request.POST.get("password2"):
                newuser = User.objects.get(username=username)
                newuser.set_password(request.POST.get("password1"))
                newuser.save()
                return HttpResponseRedirect("/login/")
            else:
                return HttpResponse("the two passwords should be same")
        return render_to_response("rewrite_password.html",locals())
    return HttpResponse("Invalid operation")

@csrf_exempt
@login_required
def index(request):
    u = request.user
    p = Profile.objects.get_or_create(user = u)[0]
    logs = u.log_set.all().order_by('-date')
    logs_num = len(logs)
    strgys = Strategy.objects.all().order_by('-date')
    info_num = len(Messages.objects.filter(go = u, is_read = False))
    messages = Messages.objects.filter(go = u, is_read = False).order_by('-date')
    
    friends = p.friend.all()
    friends_u = []
    for friend in friends:
        friends_u.append(friend.user)
    friends_logs = Log.objects.filter(user__in = friends_u).order_by('-date')

    has_act = True
    if Person.objects.filter(user = u):
        has_act = False
        
    acts = Activity.objects.all().filter(is_end = False).order_by('-date').exclude(author = u)
    
    if request.method == 'GET':
        if request.GET.has_key('ignore'):
            msgID = request.GET['msgID']
            m = Messages.objects.get(msgID = msgID)
            m.is_read = True
            m.save()
        if request.GET.has_key('actID'):
            actID = request.GET['actID']
            target_act = Activity.objects.get(actID = actID)
            target_user = target_act.author
            msg = Messages()
            msg.go = target_user
            msg.come = u
            msg.msg_type = 2
            msg.is_req = True
            msg.save()
    return render_to_response("index.html", locals())

@csrf_exempt
@login_required
def ensure_logout(request):
    u = request.user
    if request.method == 'POST':
        if request.POST.has_key('ensure'):
            auth.logout(request)
            return HttpResponseRedirect("/login/")
    return render_to_response("logout.html", locals())

@csrf_exempt
@login_required
def addlog(request):
    u = request.user
    if request.method == 'POST':
        form = LogForm(request.POST)
        if form.is_valid():
            log = Log()
            log.content = form.cleaned_data["content"]
            log.title = form.cleaned_data["title"]
            log.user = request.user
            log.save()
            return HttpResponseRedirect("/is_add_logimg/" + str(log.logID))
    else:
        form = LogForm()
    return render_to_response('addlog.html', locals())

@csrf_exempt
@login_required

def mylog(request, id):
    u = request.user
    mylog = u.log_set.all().get(logID = id)
    logs = u.log_set.all().order_by('-date') 
    return render_to_response('mylog.html', locals())
@csrf_exempt
@login_required
def myprofile(request):
    u = request.user
    #User.profile = property(lambda u: Profile.objects.get_or_create(user = u)[0])
    p = Profile.objects.get_or_create(user = u)[0]
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
    p = Profile.objects.get_or_create(user = u)[0]
    if request.method == 'POST':       
        if 'image' in request.FILES:
            image=request.FILES["image"]
            img=Image.open(image)
            img.thumbnail((112,54),Image.ANTIALIAS)
            name='./static/imgs/'+u.username+'.png'
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
    sites = Site.objects.all().order_by('-siteID')
    imgs = []
    for i in sites:
        if i.is_img == 1:
            imgs.append(i.siteimg_set.all().order_by('siteID')[0].name)
        else:
            imgs.append(False)
    sites_info = zip(sites, imgs)
    if request.method == 'POST':
        form = StrategyForm(request.POST)
        if form.is_valid():
            strgy = Strategy()
            strgy.content = form.cleaned_data["content"]
            strgy.title = form.cleaned_data["title"]
            strgy.user = request.user
            strgy.save()
            if 'sitename' in request.POST:
                if request.POST['sitename']: 
                    name = request.POST['sitename']
                    site = Site.objects.get(name = name)
                    strgy.site = site
                    strgy.save()
            return HttpResponseRedirect("/index/")
    else:
        form = StrategyForm()
    return render_to_response('addstrgy.html', locals())
    
@csrf_exempt
@login_required
def showstrgy(request, id):
    u = request.user
    strgy = Strategy.objects.all().get(strgyID = id)
    strgys = Strategy.objects.all().order_by('-date')
    is_site = False
    is_img = False
    if strgy.site:
        site = strgy.site
        is_site = True
        if SiteImg.objects.filter(site = site):
            imgs = site.siteimg_set.all()
            is_img = True
    return render_to_response('showstrgy.html', locals())

@csrf_exempt
@login_required
def myhope(request):
    u = request.user
    h = Hope.objects.get_or_create(user = u)[0]
    if request.method == 'POST':       
        form = HopeForm(request.POST, instance = h)
        if form.is_valid():
            form.save()
            h.is_commit = True
            h.save()
            return HttpResponseRedirect("/myhope/")
    else:
        form = HopeForm(instance = h)
    return render_to_response('myhope.html', locals())
    
@csrf_exempt
@login_required
def design(request):
    u = request.user
    return render_to_response('design.html', locals())
    
@csrf_exempt
@login_required
def result(request, id1, id2):
    u = request.user
    home1 = id1
    home2 = id2
    return render_to_response('result.html', locals())

@csrf_exempt
@login_required
def advice(request):
    u = request.user
    h = Hope.objects.get_or_create(user = u)[0]
    if h.is_commit == True:
        hlist = Hope.objects.filter(home__contains = h.home[0:1]).filter(goal__contains = h.goal[0:1]).filter(busy = 0)\
                .exclude(Q(end_date__lt = h.start_date)|Q(start_date__gt = h.end_date))
    return render_to_response('advice.html', locals())

@csrf_exempt
@login_required
def my_advice_user(request, id):
    u = request.user
    p = Profile.objects.get_or_create(user = u)[0]
    h = Hope.objects.get_or_create(user = u)[0]
    hlist = Hope.objects.filter(home__contains = h.home[0:1]).filter(goal__contains = h.goal[0:1]).filter(busy = 0)\
            .exclude(Q(end_date__lt = h.start_date)|Q(start_date__gt = h.end_date))
    target_user = User.objects.get(username = id)
    target_hope = target_user.hope
    if target_user.profile in p.friend.all():
        is_friend = True
    else:
        is_friend = False
        
    
    '''
    if Activity.objects.filter(author = u, is_end = False, is_valid = True).order_by('-date'):
        act = Activity.objects.filter(author = u, is_end = False, is_valid = True).order_by('-date')[0]
        persons = act.person_set.all()
        act_users = []
        for person in persons:
            act_users.append(person.user)
        if act:
            if target_user not in act_users:
                has_act = True
    '''
    has_act = False
    if not Person.objects.filter(user = target_user):
        if Person.objects.filter(user = u):
            if u.person.act.author == u:
                has_act = True
    if request.method == 'GET':
        if request.GET.has_key('friend'):
            mf = Messages()
            mf.go = target_user
            mf.come = u
            mf.msg_type = 0
            mf.is_req = True
            mf.save()
        if request.GET.has_key('travel'):
            mt = Messages()
            mt.go = target_user
            mt.come = u
            mt.msg_type = 1
            mt.is_req = True
            mt.save()
    return render_to_response('my_advice_user.html', locals())


@csrf_exempt
@login_required
def deal_msg(request, come_username, msgID):
    u = request.user
    p = Profile.objects.get_or_create(user = u)[0]
    friend_u = User.objects.get(username = come_username)
    friend_p = Profile.objects.get_or_create(user = friend_u)[0]
    friend_h = Hope.objects.get_or_create(user = friend_u)[0]
    target_msg = Messages.objects.get(msgID = msgID)
    if request.method == 'GET':
        if target_msg.msg_type == 0:
            
            if request.GET.has_key('cancelf'):
                message_readed = Messages.objects.filter(come = friend_u, go = u, msg_type = 0, is_req = True)
                for message in message_readed:
                    message.is_read = True
                    message.save()
                result_m = Messages.objects.create(go = friend_u, come = u, msg_type = 0, is_req = False)
            elif request.GET.has_key('ensuref'):
                p.friend.add(friend_p)
                message_readed = Messages.objects.filter(come = friend_u, go = u, msg_type = 0, is_req = True)
                for message in message_readed:
                    message.is_read = True
                    message.save()
                result_m = Messages.objects.create(go = friend_u, come = u, msg_type = 0, is_req = False)
                result_m.msg_deal = 0
                result_m.save()
                    
        elif target_msg.msg_type == 1:
            
            if request.GET.has_key('cancelt'):
                message_readed = Messages.objects.filter(come = friend_u, go = u, msg_type = 1, is_req = True)
                for message in message_readed:
                    message.is_read = True
                    message.save()
                result_m = Messages.objects.create(go = friend_u, come = u, msg_type = 1, is_req = False)    
            elif request.GET.has_key('ensuret'):
                act = Activity.objects.filter(author = friend_u, is_end = False, is_valid = True).order_by('-date')[0]
                person = Person.objects.get_or_create(user = u, act = act)[0]
                message_readed = Messages.objects.filter(come = friend_u, go = u, msg_type = 1, is_req = True)
                for message in message_readed:
                    message.is_read = True
                    message.save()
                result_m = Messages.objects.create(go = friend_u, come = u, msg_type = 1, is_req = False)
                result_m.msg_deal = 1
                result_m.save()
        elif target_msg.msg_type == 2:
            
            if request.GET.has_key('cancela'):
                message_readed = Messages.objects.filter(come = friend_u, go = u, msg_type = 2, is_req = True)
                for message in message_readed:
                    message.is_read = True
                    message.save()
                result_m = Messages.objects.create(go = friend_u, come = u, msg_type = 2, is_req = False)
            elif request.GET.has_key('ensurea'):
                message_readed = Messages.objects.filter(come = friend_u, go = u, msg_type = 2, is_req = True)
                for message in message_readed:
                    message.is_read = True
                    message.save()
                act = Activity.objects.filter(author = u, is_end = False, is_valid = True).order_by('-date')[0]
                person = Person.objects.get_or_create(user = friend_u, act = act)[0]
                result_m = Messages.objects.create(go = friend_u, come = u, msg_type = 2, is_req = False)
                result_m.msg_deal = 2
                result_m.save()
                
    else:
        return HttpResponseRedirect("/index/")
    return render_to_response('deal_msg.html', locals())
    
@csrf_exempt
@login_required    
def is_add_logimg(request, id):
    u = request.user
    if request.method == 'POST':
        if request.POST.has_key('ensure'):
            return HttpResponseRedirect("/logimg/" + str(id))
        else:
            return HttpResponseRedirect("/index/")
    return render_to_response("is_add_logimg.html", locals())
    

@csrf_exempt
@login_required
def logimg(request, id):
    u = request.user
    log = Log.objects.get(logID = id)
    if request.method == 'POST':       
        if 'image' in request.FILES:
            image=request.FILES["image"]
            img=Image.open(image)
            img.thumbnail((1080,720),Image.ANTIALIAS)
            name='./static/imgs/' + u.username + str(log.logID) + 'log.png'
            img.save(name,"png")
            nameurl = u.username + str(log.logID) + 'log'
            log.img_name = nameurl
            log.is_img = True
            log.save()
            return HttpResponseRedirect("/index/")
    return render_to_response('img.html', locals())


@csrf_exempt
@login_required
def friend_logimgs(request, id):
    u = request.user
    friend_u = User.objects.get(username = id)
    friend_logs = friend_u.log_set.all().filter(is_img = True).order_by('-date')
    logimgs_num = len(friend_logs)
    return render_to_response('friend_logimgs.html', locals())

    
@csrf_exempt
@login_required
def group(request):
    u = request.user
    h = Hope.objects.get_or_create(user = u)[0]
    if h.is_commit == True:
        hlist = Hope.objects.filter(home__contains = h.home[0:1]).filter(goal__contains = h.goal[0:1]).filter(busy = 0)\
                .exclude(Q(end_date__lt = h.start_date)|Q(start_date__gt = h.end_date))
    acts = Activity.objects.filter(author = u).order_by('-date')
    if Person.objects.filter(user = u):
        has_act = False
        my_act = u.person.act
    else:
        has_act = True
    if has_act:
        if request.method == 'POST':
            new_act = Activity(author = u)
            form = ActForm(request.POST, instance = new_act)
            if form.is_valid():
                form.save()
                new_act.start_date = h.start_date
                new_act.end_date = h.end_date
                new_act.save()
                me = Person.objects.create(user = u, act = new_act)
                is_create_act = False
                return HttpResponseRedirect("/group/")
        else:
            form = ActForm()
    return render_to_response('group.html', locals())



@csrf_exempt
@login_required
def myfriend(request):
    u = request.user
    p = Profile.objects.get_or_create(user = u)[0]
    friends = p.friend.all()
    friends_num = len(friends)
    has_friend = True
    if request.method == 'GET':
        if request.GET.has_key('goal'):
            goal_username = request.GET['goal']
            goal_user = User.objects.get(username = goal_username)
    else:
        if friends_num:
            goal_user = User.objects.get(username = friends[0].user.uername)
        else:
            has_friend = False
    return render_to_response('myfriend.html', locals())



@csrf_exempt
@login_required
def deal_act(request):
    u = request.user
    p = Profile.objects.get_or_create(user = u)[0]
    msg_disread = False
    if Messages.objects.filter(go = u, msg_type = 2, is_req = True, is_read = False):
        msg_disread = True
    if request.method == 'GET':
        if request.GET.has_key('actID'):
            actID = request.GET['actID']
            act = Activity.objects.get(actID = actID)
            persons = act.person_set.all().order_by('-date')
        if request.GET.has_key('end'):
            if msg_disread == False:
                actID = request.GET['actID']
                act = Activity.objects.get(actID = actID)
                act.is_end = True
                act.save()
                ps = act.person_set.all()
                for p in ps:
                    p.delete()
    return render_to_response('deal_act.html', locals())


@csrf_exempt
@login_required
def site(request):
    u = request.user
    sites = Site.objects.all().order_by('-siteID')
    imgs = []
    for i in sites:
        if i.is_img == 1:
            imgs.append(i.siteimg_set.all().order_by('siteID')[0].name)
        else:
            imgs.append(False)
    sites_info = zip(sites, imgs)
    if request.method == 'POST':
        form = SiteForm(request.POST)
        if form.is_valid():
            site = form.save()
            form = SiteForm()
            if 'images' in request.FILES:
                images = request.FILES.getlist('images')
                i = 1
                for image in images:
                    img=Image.open(image)
                    img.thumbnail((1080,720),Image.ANTIALIAS)
                    name='./static/siteimgs/' + str(site.siteID) + '-' + str(i) + '.png'
                    img.save(name,"png")
                    nameurl = str(site.siteID) + '-' + str(i)
                    siteimg = SiteImg()
                    siteimg.name = nameurl
                    siteimg.site = site
                    siteimg.save()
                    i += 1
                site.is_img = 1
                site.save()
            return HttpResponseRedirect("/site/")
    else:
        form = SiteForm()
    return render_to_response('site.html', locals())

@csrf_exempt
@login_required
def mysite(request, siteID):
    u = request.user
    site = Site.objects.get(siteID = siteID)
    imgs = site.siteimg_set.all().order_by('siteID')
    commits = site.site_sitecommit_set.all().order_by('-scID')
    if request.method == 'POST':
        form = SiteCommitForm(request.POST)
        if form.is_valid():
            content = form.cleaned_data["content"]
            sitecommit = SiteCommit()
            sitecommit.content = content
            sitecommit.site = site
            sitecommit.user = u
            sitecommit.save()
            form = SiteCommitForm()
        return HttpResponseRedirect("/mysite/" + str(siteID) + '/')
    else:
        form = SiteCommitForm()
    
    return render_to_response('mysite.html', locals())




