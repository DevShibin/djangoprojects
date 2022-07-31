from django.db import models

# Create your models here.

class clsUser(models.Model):
    pk_user_id = models.IntegerField(primary_key=True)
    vhr_user_name = models.CharField(max_length=30,blank=True)
    vhr_actual_name = models.CharField(max_length=30,blank=True)
    vhr_password = models.CharField(max_length=8,blank=True)

    def __str__(self):
        return self.vhr_user_name

class clsItem(models.Model):
    pk_item_id = models.IntegerField(primary_key=True)
    vhr_item_name = models.CharField(max_length=30,blank=True)
    vhr_item_category = models.CharField(max_length=30,default='')
    txt_item_description = models.TextField()
    dbl_price = models.FloatField(default=0.0)

    def __str__(self):
        return self.vhr_item_name
