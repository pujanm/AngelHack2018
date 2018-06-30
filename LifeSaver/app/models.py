from django.db import models
from django.contrib.auth.models import User
# Create your models here.


choices = (
    ('Food', 'Food'),
    ('Shelter', 'Shelter'),
    ('Crowdfunding', 'Crowdfunding')
)
class Victim(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='persons')
    photo = models.FileField(upload_to="profile pics/", null=True, blank=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.IntegerField()
    contact_no = models.CharField(max_length=10)
    latitude = models.CharField(max_length=50, default="18.910334")
    longitude = models.CharField(max_length=50, default="72.810383")
    help_required = models.BooleanField(default=False)
    type_of_help = models.CharField(max_length=50, choices=choices, default="Food")

    def __str__(self):
        return self.user.username



class HospitalUser(models.Model):
    users_recieving_help = models.ManyToManyField(Victim, related_name='hospitals_helping', blank=True, null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='hospitals')
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200, null=True, blank=True)
    contact_no = models.CharField(max_length=10)
    latitude = models.CharField(max_length=50, default="18.910334")
    longitude = models.CharField(max_length=50, default="72.810383")

    def __str__(self):
        return self.name

class Hospitals(models.Model):
    name = models.CharField(max_length=200)
    latitude = models.CharField(max_length=50)
    longitude = models.CharField(max_length=50)

    def __str__(self):
        return "{0}".format(self.name)


choices = (
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),
)
class Disaster(models.Model):
    users_associated = models.ManyToManyField(Victim, related_name='users_disaster')
    hospitals_associated = models.ManyToManyField(HospitalUser, related_name='hospitals_disaster')
    type_disaster = models.CharField(max_length=100)
    latitude = models.CharField(max_length=50, default="18.910334")
    longitude = models.CharField(max_length=50, default="72.810383")
    level = models.CharField(max_length=5, choices=choices, default=1)

    def __str__(self):
        return self.type_disaster
