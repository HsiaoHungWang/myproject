from django import forms
from .models import Member

# Form API
class MemberForm(forms.Form):
    member_name =  forms.CharField(label='姓名', max_length=100)
    member_email = forms.CharField(label='電子郵件', max_length=200)

# Forms By Model
class UserForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ['member_name','member_birth','member_email']