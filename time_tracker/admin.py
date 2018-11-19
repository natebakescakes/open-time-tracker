from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import MemberCreationForm, MemberChangeForm
from .models import Category, WorkLog, Member


class MemberAdmin(UserAdmin):
    add_form = MemberCreationForm
    form = MemberChangeForm
    model = Member
    list_dispaly = ['username', 'team', 'email']


# Register your models here.
admin.site.register(Category)
admin.site.register(WorkLog)
admin.site.register(Member, MemberAdmin)
