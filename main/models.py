from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class TimeStampModel(models.Model):
    """Inherit from this class to add timestamp fields in the model class"""

    created_at = models.DateTimeField(auto_now_add=True)
    """datetime: date on which the instance is created."""
    updated_at = models.DateTimeField(auto_now=True)
    """datetime: date on which the instance is updated."""
    
    class Meta:
        abstract = True


class Record(TimeStampModel):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete= models.CASCADE,related_name='user_record')
    
    def __str__(self) -> str:
        return self.name
    

class Category(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self) -> str:
        return self.name


class Expenses(TimeStampModel):
    METHOD = (
        (0,"Cash"),
        (1,"Online")
    )
    record = models.ForeignKey(Record, on_delete= models.CASCADE,related_name='record')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category')
    amount = models.DecimalField(decimal_places=2, max_digits=10)
    remark = models.CharField(max_length=250)
    image = models.ImageField(upload_to='', null=True, blank=True)
    payment_method = models.IntegerField(choices=METHOD, default=0)
    date = models.DateField()
    
    def __str__(self) -> str:
        return f'{self.category}/{self.amount}'