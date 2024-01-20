from django.db import models

class User(models.Model):
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username

class Item(models.Model):
    name = models.CharField(max_length=255)
    width = models.FloatField()
    height = models.FloatField()
    depth = models.FloatField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='items')

    def __str__(self):
        return self.name

class Layout(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='layouts')
    image = models.ImageField(upload_to='uploads/')
    suggested_layout = models.JSONField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Layout for {self.user.username} at {self.created_at.strftime('%Y-%m-%d %H:%M')}"