from django.db import models

# Create your models here.

SEX={
    'male': 'MALE',
    'female': 'FEMALE',

}
LOCATION = {
    'nairobi': 'NAIROBI',
    'kisumu': 'KISUMU',

}
class User(models.Model):
    id = models.CharField(primary_key=True, max_length=11)
    username=models.CharField(max_length=100,null=False),
    location=models.CharField(max_length=100, choices= LOCATION,null=False),
    gender=models.CharField(max_length=100,choices=SEX),
    DOB = models.DateField()

    def __str__(self):
        return self.id + '(' + str(self.id) + ')'



class Friends(models.Model):

    user_id= models.ForeignKey(to=User,on_delete=False),
    friendship_id =models.CharField(max_length=100,auto_created=True)



    def __str__(self):
        return self.id + '(' + str(self.id) + ')'




