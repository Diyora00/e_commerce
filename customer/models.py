from django.db import models


class Customer(models.Model):
    fullname = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(max_length=100, unique=True)
    phone = models.CharField(max_length=100, unique=True)
    address = models.CharField(max_length=250)
    joined = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='customer/', null=True, blank=True)

    def joined_time_format(self):
        return self.joined.strftime('%B %d, %Y at %I:%M %p')

    def __str__(self):
        return self.email

    class Meta:
        ordering = ('-id',)
