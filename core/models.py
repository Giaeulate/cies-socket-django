from django.db.models import *
import uuid


# class BaseModel(Model):
#     id = UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#     active = BooleanField(default=True)
#     created_at = DateTimeField(auto_now_add=True)
#     updated_at = DateTimeField(auto_now=True)

#     class Meta:
#         abstract = True


# class UserSocket(BaseModel):
#     name = CharField(max_length=150)
#     thumb = JSONField(blank=True, null=True)
#     is_online = BooleanField(default=False)
#     is_logged = BooleanField(default=False)

#     class Meta:
#         db_table = 'user_socket'
#         ordering = ('id',)
#         verbose_name = 'UserSocket'
#         verbose_name_plural = 'UserSocket'

#     def __str__(self):
#         return self.name


# class UserDevice(BaseModel):
#     name = CharField(max_length=150)
#     platform = CharField(max_length=30)
#     push_token = TextField(blank=True, null=True)
#     user_socket = ForeignKey(UserSocket, on_delete=CASCADE)

#     class Meta:
#         db_table = 'user_device'
#         ordering = ('id',)
#         verbose_name = 'UserDevice'
#         verbose_name_plural = 'UserDevice'

#     def __str__(self):
#         return self.name


# class TypeMessage(BaseModel):
#     name = CharField(max_length=150)
#     description = TextField(blank=True, null=True)

#     class Meta:
#         db_table = 'type_message'
#         ordering = ('id',)
#         verbose_name = 'TypeMessage'
#         verbose_name_plural = 'TypeMessage'

#     def __str__(self):
#         return self.name


# class Attachment(BaseModel):
#     name = CharField(max_length=150)
#     thumb = JSONField(blank=True, null=True)

#     class Meta:
#         db_table = 'attachment'
#         ordering = ('id',)
#         verbose_name = 'Attachment'
#         verbose_name_plural = 'Attachment'

#     def __str__(self):
#         return self.name


# class Channel(BaseModel):
#     name = CharField(max_length=255)
#     thumb = JSONField(blank=True, null=True)
#     description = TextField(blank=True, null=True)

#     class Meta:
#         db_table = 'channel'
#         ordering = ('id',)
#         verbose_name = 'Channel'
#         verbose_name_plural = 'Channel'

#     def __str__(self):
#         return self.name


# class Message(BaseModel):
#     message = CharField(max_length=150)
#     thumb = JSONField(blank=True, null=True)
#     url = URLField(blank=True, null=True)
#     is_sent = BooleanField(default=False)
#     attachment = ForeignKey(
#         Attachment, on_delete=CASCADE, blank=True, null=True)
#     channel = ForeignKey(Channel, on_delete=CASCADE)
#     type_message = ForeignKey(TypeMessage, on_delete=CASCADE)
#     user_socket = ForeignKey(UserSocket, on_delete=CASCADE)

#     class Meta:
#         db_table = 'message'
#         ordering = ('id',)
#         verbose_name = 'Message'
#         verbose_name_plural = 'Message'

#     def __str__(self):
#         return str(self.id)

class AttachmentModel(Model):
    id = CharField(primary_key=True, max_length=150, default=uuid.uuid4, editable=False)
    name = CharField(max_length=150)
    thumb = JSONField(blank=True, null=True)
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)
    active = BooleanField(default=True)

    class Meta:
        managed = False
        db_table = 'socket_attachment_model'
        
    def __str__(self):
        return self.name


class ChannelModel(Model):
    id = CharField(primary_key=True, max_length=150, default=uuid.uuid4)
    name = CharField(max_length=150)
    description = TextField(blank=True, null=True)
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)
    active = BooleanField(default=True)
    is_main = BooleanField(default=False)
    thumb = JSONField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'socket_channel_model'
        
    def __str__(self):
        return self.name


class ChannelModelUserSocket(Model):
    id = CharField(primary_key=True, max_length=150, default=uuid.uuid4, editable=False)
    channelmodel = ForeignKey(ChannelModel, DO_NOTHING)
    usersocketmodel = ForeignKey('UserSocketModel', DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'socket_channel_model_user_socket'


class MessageModel(Model):
    id = CharField(primary_key=True, max_length=150, default=uuid.uuid4, editable=False)
    message = CharField(max_length=150)
    url = CharField(max_length=200, blank=True, null=True)
    is_sent = BooleanField(default=False)
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)
    active = BooleanField(default=True)
    attachment = ForeignKey(AttachmentModel, DO_NOTHING, blank=True, null=True)
    channel = ForeignKey(ChannelModel, DO_NOTHING)
    type_message = ForeignKey('TypeMessageModel', DO_NOTHING)
    user_socket = ForeignKey('UserSocketModel', DO_NOTHING)
    thumb = JSONField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'socket_message_model'
        
    def __str__(self):
        return str(self.id)


class MessageModelIsRead(Model):
    id = CharField(primary_key=True, max_length=150, default=uuid.uuid4, editable=False)
    message = ForeignKey(MessageModel, DO_NOTHING)
    usersocketmodel = ForeignKey('UserSocketModel', DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'socket_message_model_is_read'


class TypeMessageModel(Model):
    id = CharField(primary_key=True, max_length=150, default=uuid.uuid4)
    name = CharField(max_length=150)
    description = TextField(blank=True, null=True)
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)
    active = BooleanField(default=True)
    thumb = JSONField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'socket_type_message_model'
        
    def __str__(self):
        return self.name


class UserDeviceModel(Model):
    id = CharField(primary_key=True, max_length=255, default=uuid.uuid4, editable=False)
    name = CharField(max_length=150)
    platform = CharField(max_length=150, blank=True, null=True)
    push_token = CharField(max_length=255, blank=True, null=True)
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)
    active = BooleanField(default=True)
    user_socket = ForeignKey('UserSocketModel', DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'socket_user_device_model'
        
    def __str__(self):
        return self.name


class UserSocketModel(Model):
    id = CharField(primary_key=True, max_length=150, default=uuid.uuid4)
    name = CharField(max_length=150)
    is_online = BooleanField()
    is_logged = BooleanField()
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)
    active = BooleanField(default=True)
    thumb = JSONField(blank=True, null=True)
    
    def __str__(self):
        return self.name

    class Meta:
        managed = False
        db_table = 'socket_user_socket_model'