from django.db import models
from django.contrib.auth.models import User

class Team(models.Model):
    # User as a foreign key to represent the team head
    team_head = models.ForeignKey(User, on_delete=models.CASCADE)

    # Six member fields (3 of them can be blank)
    member1 = models.CharField(max_length=255, blank=True, null=True)
    member2 = models.CharField(max_length=255, blank=True, null=True)
    member3 = models.CharField(max_length=255, blank=True, null=True)
    member4 = models.CharField(max_length=255, blank=True, null=True)
    member5 = models.CharField(max_length=255, blank=True, null=True)
    member6 = models.CharField(max_length=255, blank=True, null=True)
    
    
    member1_picture = models.ImageField(upload_to='team_pictures/', blank=True, null=True)
    member2_picture = models.ImageField(upload_to='team_pictures/', blank=True, null=True)
    member3_picture = models.ImageField(upload_to='team_pictures/', blank=True, null=True)
    member4_picture = models.ImageField(upload_to='team_pictures/', blank=True, null=True)
    member5_picture = models.ImageField(upload_to='team_pictures/', blank=True, null=True)
    member6_picture = models.ImageField(upload_to='team_pictures/', blank=True, null=True)

    # Choice field for subject selection
    SUBJECT_CHOICES = [
        ('commers', 'Commers'),
        ('physics', 'Physics'),
        ('computers', 'Computers'),
        ('chemistry', 'Chemistry'),
        ('art', 'Art'),
        ('bio', 'Biology'),
        ('maths', 'Mathematics'),
    ]

    # At least one subject must be selected, default to 'computers'
    subject1 = models.CharField(max_length=10, choices=SUBJECT_CHOICES, default='computers')
    subject2 = models.CharField(max_length=10, choices=SUBJECT_CHOICES, default='computers')
    subject3 = models.CharField(max_length=10, choices=SUBJECT_CHOICES, default='computers')
    
    winner = models.BooleanField(default=False)

    def __str__(self):
        return f'Team Head: {self.team_head.username}'

class News(models.Model):
    news = models.CharField(max_length=500, blank=True)
    

class Org_team(models.Model):
    org_member1_name = models.CharField(max_length=100)
    org_member1_profile_pic = models.ImageField(upload_to='team_pics/')
    org_member1_role = models.CharField(max_length=100)

    org_member2_name = models.CharField(max_length=100)
    org_member2_profile_pic = models.ImageField(upload_to='team_pics/')
    org_member2_role = models.CharField(max_length=100)

    org_member3_name = models.CharField(max_length=100)
    org_member3_profile_pic = models.ImageField(upload_to='team_pics/')
    org_member3_role = models.CharField(max_length=100)

    org_member4_name = models.CharField(max_length=100)
    org_member4_profile_pic = models.ImageField(upload_to='team_pics/')
    org_member4_role = models.CharField(max_length=100)

    org_member5_name = models.CharField(max_length=100)
    org_member5_profile_pic = models.ImageField(upload_to='team_pics/')
    org_member5_role = models.CharField(max_length=100)

    org_member6_name = models.CharField(max_length=100)
    org_member6_profile_pic = models.ImageField(upload_to='team_pics/')
    org_member6_role = models.CharField(max_length=100)

    org_member7_name = models.CharField(max_length=100)
    org_member7_profile_pic = models.ImageField(upload_to='team_pics/')
    org_member7_role = models.CharField(max_length=100)

    org_member8_name = models.CharField(max_length=100)
    org_member8_profile_pic = models.ImageField(upload_to='team_pics/')
    org_member8_role = models.CharField(max_length=100)

