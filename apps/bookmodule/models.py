from django.db import models

#lab 7
class Book(models.Model):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    price = models.FloatField(default=0.0)
    edition = models.SmallIntegerField(default=1)

#lab 8
class Address(models.Model):
    city = models.CharField(max_length=100)
    
    
    def __str__(self):
        return self.city
    
class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='images/', blank=True, null=True)


    def __str__(self):
        return self.name

#lab 10
class Address2(models.Model):
    city = models.CharField(max_length=100)
    
    def __str__(self):
        return self.city

class Student2(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    addresses = models.ManyToManyField(Address2, related_name="students")
    profile_picture = models.ImageField(upload_to='images/', blank=True, null=True)

    def __str__(self):
        return self.name

class ProfilePicture(models.Model):
    student = models.OneToOneField(Student, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/')
