
from random import choices
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
#from  django.utils.translation import ngettext_lazy as _
from django.utils.text import slugify


# Create your models here.

TYPE_OF_PERSON=(
    ('M',"Male"),
    ('F',"Female")
)

class Profile(models.Model):

    DOCTOR_IN = (
    
        ('جلدية',"جلدية"),
        ('اسنان',"اسنان"),
        ('نفسي',"نفسي"),
        ('اطفال حديثي الولادة',"اطفال حديثي الولادة"),
        ('مخ واعصاب',"مخ واعصاب"),
        ('عظام',"عظام"),
        ('نساء وتوليد',"نساء وتوليد"),
        ('انف واذن وحنجرة',"انف واذن وحنجرة"),
        ('قلب واوعية دموية',"قلب واوعية دموية"),
        ('امراض دم',"امراض دم"),
        ('اورام',"اورام"),
        ('باطنه',"باطنه"),
        ('تخسيس وتغذية',"تخسيس وتغذية"),
        ('جراحة اطفال',"جراحة اطفال"),
        ('جراحة اورام',"جراحة اورام"),
        ('جراحة اوعية دموية',"جراحة اوعية دموية"),
        ('جراحة تجميل',"جراحة تجميل"),
        ('جراحه سمنة ومناظير ',"جراحه سمنة ومناظير "),
       

    )

    user = models.OneToOneField(User, verbose_name="user", on_delete=models.CASCADE)
    name = models.CharField("name",max_length=50)
    subtitle = models.CharField("subtitle",max_length=50)
    address = models.CharField("government",max_length=50)
    address_detail = models.CharField("cureent_address",max_length=50)
    number_phone =  models.CharField("Phone_number",max_length=50)
    working_hours = models.CharField("Working_time",max_length=50) 
    waiting_time = models.IntegerField("waiting_time",blank = True , null = True)
    who_i = models.TextField("who_i",max_length=50,blank = True , null = True)     
    price = models.IntegerField("price",blank = True , null = True)
    facebook= models.CharField("facebook",max_length=50,blank = True , null = True)
    twitter= models.CharField("twitter",max_length=50,blank = True , null = True)
    google= models.CharField("google",max_length=50,blank = True , null = True)
    #join_new = models.DateTimeField("join at",auto_now_add=True ,blank = True , null = True)
    type_of_person = models.CharField("gender", choices= TYPE_OF_PERSON ,max_length=50)
    doctor = models.CharField("doctor?",choices= DOCTOR_IN ,max_length=50,blank = True , null = True)

    image = models.ImageField("Persomal_image", upload_to='profile',blank = True , null = True)
    Specialist_doctor = models.CharField("Specialist_doctor",max_length=50,blank = True , null = True)
    slug = models.SlugField("slug",blank = True , null = True)
    

    def save(self , *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.user.username)
        super(Profile,self).save(*args,**kwargs)    

    class Meta:
        verbose_name = "Profile"
        verbose_name_plural = "Profiles"

    def __str__(self):
        return  '%s'%(self.user.username)
def create_profile(sender , **kwargs):
    if kwargs['created']:
        Profile.objects.create(user = kwargs['instance'])
post_save.connect(create_profile, sender =User )        
    
