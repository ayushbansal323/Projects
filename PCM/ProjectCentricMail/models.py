from django.db import models

# Create your models here.
class MessageInfo(models.Model):
    m_id = models.CharField(max_length=32)
    Sender = models.CharField(max_length=2048)
    Subject = models.CharField(max_length=128)
    Date = models.DateField()
    Snippet = models.CharField(max_length=512)
    Message_body = models.CharField(max_length=8192)
    Username = models.CharField(max_length=128)

class ProjectClassify(models.Model):
   m_id = models.ForeignKey(MessageInfo, on_delete=models.CASCADE)
   Spam = models.NullBooleanField()
   Formal = models.NullBooleanField()
   Project = models.CharField(max_length=32)

class ProjectNames(models.Model):
	username = models.CharField(max_length=32)
	projectname = models.CharField(max_length=32)
