from django.contrib import admin
from .models import *


@admin.register(UserSocketModel)
class UserSocketModelAdmin(admin.ModelAdmin):
    list_display = [x.name for x in UserSocketModel._meta.fields]


@admin.register(UserDeviceModel)
class UserDeviceModelAdmin(admin.ModelAdmin):
    list_display = [x.name for x in UserDeviceModel._meta.fields]


@admin.register(TypeMessageModel)
class TypeMessageModelAdmin(admin.ModelAdmin):
    list_display = [x.name for x in TypeMessageModel._meta.fields]


@admin.register(MessageModelIsRead)
class MessageModelIsReadAdmin(admin.ModelAdmin):
    list_display = [x.name for x in MessageModelIsRead._meta.fields]


@admin.register(MessageModel)
class MessageModelAdmin(admin.ModelAdmin):
    list_display = [x.name for x in MessageModel._meta.fields]


@admin.register(ChannelModelUserSocket)
class ChannelModelUserSocketAdmin(admin.ModelAdmin):
    list_display = [x.name for x in ChannelModelUserSocket._meta.fields]


@admin.register(AttachmentModel)
class AttachmentModelAdmin(admin.ModelAdmin):
    list_display = [x.name for x in AttachmentModel._meta.fields]


@admin.register(ChannelModel)
class ChannelModelAdmin(admin.ModelAdmin):
    list_display = [x.name for x in ChannelModel._meta.fields]
