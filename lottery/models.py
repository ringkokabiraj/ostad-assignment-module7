from django.db import models



class Category(models.Model):
    name = models.CharField(max_length=255)
    
    def __str__(self) -> str:
        return self.name
    



class Lottery(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to="Lottery/")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True,blank=True)
    cash_alternative = models.IntegerField(null=True,blank=True)
    draw_in = models.DateTimeField()
    price = models.DecimalField(decimal_places = 2, max_digits=10)
    total_available_ticket = models.IntegerField()
    total_sold = models.IntegerField(default=0)
    max_entries_per_user = models.IntegerField(default=1)
    def __str__(self) -> str:
        return self.name
    
class LotteryImage(models.Model):
    lottery = models.ForeignKey(Lottery,on_delete=models.CASCADE)
    image = models.ImageField(upload_to="Lottery/")

    def __str__(self):
        return self.lottery.name