from django.db import models

# Create your models here.

class ChatUser(models.Model):
    # nickname = models.CharField(max_length=25)
    email = models.EmailField(unique=True)

    def __str__(self):
        return f'User: {self.email}>'


class Message(models.Model):
    text = models.CharField(max_length=100)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(null=True)
    author = models.ForeignKey(ChatUser, on_delete=models.CASCADE)

    def __str__(self):
        return f'Message: <{self.text} by {self.author.email}>'
    
    def get_email(self):
        return self.author.email
    
