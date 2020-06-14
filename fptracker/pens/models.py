from django.db import models
from users.models import Profile

# Create your models here.
class Ink(models.Model):
    brand_name = models.CharField(max_length = 100)
    color = models.CharField(max_length = 7)
    color_name = models.CharField(max_length = 100)
    rating = models.IntegerField(default = None)

    def __str__(self):
        return self.brand_name+" "+self.color_name +"("+ str(self.rating)+")"
    
def get_default_user():
    try:
        return Profile.objects.get(user__username="Admin").id
    except Profile.DoesNotExist:
        return Profile.objects.all().first().id

class Pen(models.Model):
    brand_name = models.CharField(max_length = 100)
    model_name = models.CharField(max_length = 100)
    color = models.CharField(max_length = 7)
    date_purchased = models.DateField()
    current_ink = models.ForeignKey(Ink, on_delete=models.SET_NULL, null = True, blank = True)
    added_by = models.ForeignKey(Profile, on_delete=models.SET_DEFAULT,default = get_default_user)
    owners = models.ManyToManyField(Profile, related_name='pens')
    NIB_SIZES = (
        ('B','Broad'),
        ('M','Medium'),
        ('F','Fine'),
        ('EF','Extra Fine')
    )
    nib_size = models.CharField(
        max_length = 2,
        choices = NIB_SIZES
    )


