from django.db import models
# from django.contrib.auth.models import User

# Create your models here.

# just call this Crypto in the actual app
class CryptoCurrency(models.Model):
    symbol = models.CharField(max_length=100)
   
    def __str__(self):
        return self.symbol

class Wallet(models.Model):
    name = models.CharField(max_length=100)
    # do we need this?
    location = models.CharField(max_length=100)
    # typo here but it's just a test so it's fine
    crpto = models.ManyToManyField(CryptoCurrency, through='Amount')
    # we'll have a user attribute for our actual app
    # user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} at {self.location}"

class Amount(models.Model):
    wallet = models.ForeignKey(Wallet, on_delete=models.CASCADE)
    # probably shouldn't even be able to delete crypto because it would remove it from each wallet it's in
    crypto = models.ForeignKey(CryptoCurrency, on_delete=models.CASCADE)
    amount = models.FloatField()

    def __str__(self):
        return f"{self.amount} of {self.crypto} in {self.wallet}"
