from django.db import models


class Subscribe(models.Model):
    email = models.EmailField()

    class Meta:
        db_table = "web_subscribe"
        ordering = ["-id"]
    
    def __str__(self):
        return self.email
    


class Customer(models.Model):
    image = models.FileField(upload_to="customers/")

    class Meta:
        db_table = "web_customer"
        ordering = ["-id"]
    
    def __str__(self):
        return str(self.id)