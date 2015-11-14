# -*- coding: utf-8 -*-
from django import forms
from models import Log, Profile, Strategy, Hope
class LogForm(forms.ModelForm):
    title = forms.CharField(label = (u"标题"), max_length = 50, widget = forms.TextInput(attrs = {"placeholder":"日志标题"}))
    content = forms.CharField(label = (u"内容"), max_length = 1000, widget = forms.Textarea(attrs = {"placeholder":"请再此输入您的日志内容，不超过1000字..."}))
    class Meta:
        model = Log
        widgets = {
            "content": forms.Textarea(attrs={"col":10,"row":25},)
            }
        exclude = ['user', ]
class ProfileForm(forms.ModelForm):
    nickname = forms.CharField(label = (u"昵称"), max_length = 16, required = False,
                               widget = forms.TextInput(attrs = {"placeholder":"请输入昵称，不超过16个字，可不写"}))
    age = forms.IntegerField(label = (u"年龄"),
                             widget=forms.TextInput(attrs={"placeholder":"请输入年龄"}), required = False)
    phone = forms.CharField(label = (u"联系电话"), max_length = 20,
                            widget=forms.TextInput(attrs={"placeholder":"请输入联系方式"}), required = False)
    qq = forms.CharField(label = (u"QQ"), max_length = 20,
                         widget=forms.TextInput(attrs={"placeholder":"请输入QQ"}), required = False)
    travellike = forms.CharField(label = (u"旅游爱好"), max_length = 50, required = False,
                               widget = forms.Textarea(attrs={"placeholder":"请在此输入旅游爱好，可不写，不超过50字"}))
    #myemail = forms.EmailField(widget=forms.TextInput(attrs={"placeholder":"请输入联系邮箱"}))
    question = forms.CharField(label = (u"密保问题"), max_length = 50, required = False,
                               widget = forms.Textarea(attrs={"placeholder":"请在此输入密保问题，可不写，不超过50字"}))
    answer = forms.CharField(label = (u"密保问题答案"), max_length = 50, required = False,
                             widget = forms.Textarea(attrs={"placeholder":"请在此输入密保问题答案，可不写，不超过50字"})) 
    class Meta:
        model = Profile
        fields = ['nickname', 'age', 'sex', 'phone', 'qq', 'question', 'answer', 'travellike', ]
        widgets = {
            "question": forms.Textarea(attrs={"col":10,"row":25, }, ), 
            "answer": forms.Textarea(attrs={"col":10,"row":25},),
            "travellike": forms.Textarea(attrs={"col":10,"row":25},),
        }
class StrategyForm(forms.ModelForm):
    title = forms.CharField(label = (u"旅游攻略主题"), max_length = 50,
                            widget = forms.TextInput(attrs = {"placeholder":"旅游攻略主题"}))
    content = forms.CharField(label = (u"内容"), max_length = 1000,
                              widget = forms.Textarea(attrs = {"placeholder":"请再此编辑内容，不超过1000字..."}))
    class Meta:
        model = Strategy
        fields = '__all__'
        widgets = {
            "content": forms.Textarea(attrs={"col":10,"row":25},)
            }
class HopeForm(forms.ModelForm):
    home = forms.CharField(label = (u"出发地"), max_length = 50,
                           widget=forms.TextInput(attrs={"placeholder":"请输入出发地"}),
                           error_messages = {"required": "出发地一定要写哦"})
    goal = forms.CharField(label = (u"目的地"), max_length = 50,
                           widget=forms.TextInput(attrs={"placeholder":"请输入目的地"}),
                           error_messages = {"required": "目的地一定要写哦"})
    start_date = forms.DateField(label = (u"出发日期范围起点"),
                           widget=forms.TextInput(attrs={"placeholder":"请输入出发日期范围起点"}),
                           error_messages = {"required": "一定要写哦"})
    end_date = forms.DateField(label = (u"出发日期范围终点"),
                           widget=forms.TextInput(attrs={"placeholder":"请输入出发日期范围终点"}),
                           error_messages = {"required": "一定要写哦"})
    price = forms.IntegerField(label = (u"旅行预算"),
                               widget=forms.TextInput(attrs={"placeholder":"请输入您的旅行预算"}),
                               error_messages = {"required": "预算一定要写哦"})
    number = forms.IntegerField(label = (u"期望团队人数"),
                                widget=forms.TextInput(attrs={"placeholder":"请输入您希望的团队人数"}),
                                error_messages = {"required": "团队人数一定要写哦"})
    hopesry = forms.CharField(label = (u"期望去的景点"), max_length = 50, required = False,
                          widget = forms.TextInput(attrs={"placeholder":"请在此输入期望去的景点,不超过50字"}))
    tip = forms.CharField(label = (u"备注信息"), max_length = 128, required = False,
                          widget = forms.Textarea(attrs={"placeholder":"请在此输入备注信息，可不写，不超过128字"}))
    class Meta:
        model = Hope
        exclude = ['user', ]
        widgets = {
            "tip": forms.Textarea(attrs={"col":10,"row":25},),
        }
        
    
    
