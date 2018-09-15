from django.db import models

# Create your models here.

class Trade(models.Model):
    symbol = models.CharField(max_length=8)
    openDate = models.DateTimeField('trade opened')
    closeDate = models.DateTimeField('trade closed')
    ticketId = models.PositiveIntegerField()
    acctNumber = models.PositiveIntegerField()
    type = models.PositiveSmallIntegerField()
    openPrice = models.DecimalField(max_digits=12, decimal_places=5)
    closePrice = models.DecimalField(max_digits=12, decimal_places=5)
    profit = models.DecimalField(max_digits=12, decimal_places=2)
    def __int__(self):
        return self.ticketId


class Tick(models.Model):
    symbol = models.CharField(max_length=8)
    time = models.DateTimeField()
    ask = models.DecimalField(max_digits=12, decimal_places=6)
    bid = models.DecimalField(max_digits=12, decimal_places=6)
    acct = models.PositiveIntegerField()

class Account(models.Model):
    acctNumber = models.PositiveIntegerField()
    brokerName = models.CharField(max_length=32)
    closeUp = models.DecimalField(max_digits=12, decimal_places=2)
    equity = models.DecimalField(max_digits=12, decimal_places=2)
    balance = models.DecimalField(max_digits=12, decimal_places=2)
    withdrawls = models.DecimalField(max_digits=12, decimal_places=2)
    deposits = models.DecimalField(max_digits=12, decimal_places=2)
    lots = models.DecimalField(max_digits=12, decimal_places=2)
    BuyPoint=models.PositiveIntegerField()  
    SellPoint=models.PositiveIntegerField() 
    tp = models.PositiveIntegerField()
    dp = models.PositiveIntegerField() 
    sl = models.PositiveIntegerField() 
    max_trades=models.PositiveIntegerField() # max trades per symbol pair 
    bufferEquity=models.PositiveIntegerField() # use this to emulate transfers between accounts. Start with 200, add 10,000. Only 200 will be seen by EA 
    instant_close=models.BooleanField()
    openTrades=models.BooleanField()  
    closeTrades=models.BooleanField()
    awaitingTransfer=models.BooleanField()
    def __int__(self):
        return self.acctNumber

class Transfer(models.Model):
    fromAcct = models.PositiveIntegerField()
    toAcct = models.PositiveIntegerField()
    withdrawls = models.DecimalField(max_digits=12, decimal_places=2)
    timeStamp = models.DateTimeField(auto_now = True)

class newTrade(models.Model):
    timeStamp = models.DateTimeField(auto_now = True)
    symbol = models.CharField(max_length=8)
    type = models.CharField(max_length=4)
    openPrice = models.DecimalField(max_digits=12, decimal_places=5)
    closePrice1 = models.DecimalField(max_digits=12, decimal_places=5)
    closePrice2 = models.DecimalField(max_digits=12, decimal_places=5)
    stopPrice = models.DecimalField(max_digits=12, decimal_places=5)
    size = models.DecimalField(max_digits=12, decimal_places=2)
    read = models.BooleanField()
    def __int__(self):
        return self.timeStamp
