from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
import logging 

from .models import Account, Trade, Tick, Transfer, newTrade



# Create your views here.
def index(request):
    return HttpResponse("OK!")

def odb(request, payload):
    response = Tick(symbol = payload, time=datetime.now(),ask=0.00,bid=0.00,acct=0)
    response.save()
    return HttpResponse("OK!")

def check(request , acct):
    response = Account.objects.filter(acctNumber = acct).first()
    return render(request, 'elpheba/check.html', {'response' : response})

def start(request , acct):
    response = Account.objects.filter(acctNumber = acct).first()
    if(response.awaitingTransfer==int(1)):
      return HttpResponse("awaiting transfer after close up completed")
    return render(request, 'elpheba/detail.html', {'response' : response})
    

def completed(request , acct, intEquity):
    newEquity = float(int(intEquity)/100)
    response = Account.objects.filter(acctNumber = acct).first()
    oldEquity = response.equity
    #respone.closeUp = response.closeUp + float(1.00)
    response.equity = float(newEquity)
    response.awaitingTransfer = int(1) 
    response.save()
    return render(request, 'elpheba/detail.html', {'response' : response})

def withdrawl(request , acct, intEquity, intWithdrawl):
    newEquity = float(int(intEquity)/100)
    response = Account.objects.filter(acctNumber = acct).first()
    oldWithdrawl = response.withdrawls
    oldEquity = response.equity
    newWithdrawl = float(float(newEquity) - float(oldEquity))
    if(newWithdrawl>20.00):
      newWithdrawl = 20.00
    newEquity = float(newEquity) - (float(newWithdrawl) + float(oldWithdrawl))
    response.withdrawls = float(float(newWithdrawl) + float(oldWithdrawl))
    response.equity = float(newEquity) 
    response.closeUp = float(float(newEquity) + float(20))
    response.save()
    moveMoney= Transfer(fromAcct = acct, toAcct=987654321, withdrawls=newWithdrawl)
    moveMoney.save()
    return render(request, 'elpheba/detail.html', {'response' : response})

def transfer(request, fromAcct, amount, toAcct):
    newTransfer = float(int(amount)/100)
    fromACCT = Account.objects.filter(acctNumber = fromAcct).first()
    toACCT = Account.objects.filter(acctNumber = toAcct).first()
    transferRecord = Transfer(fromAcct = fromACCT, toAcct=toACCT, withdrawls=newTransfer)
    fromACCT.withdrawls = float(fromACCT.withdrawls) + float(newTransfer)
    fromACCT.awaitingTransfer = int(0) 
    toACCT.deposits = float(toACCT.deposits) + float(newTransfer)
    if(((float(fromACCT.balance) + float(fromACCT.deposits) - float(fromACCT.withdrawls)) < 0) and fromAcct!=20195014):
      return HttpResponse("Transfer failed, would give negative balance in FROM account")
    if((float(toACCT.balance) + float(toACCT.deposits) - float(toACCT.withdrawls)) < 0):
      return HttpResponse("Transfer failed, would give negative balance in TO account")
    transferRecord.save()
    fromACCT.save()
    toACCT.save()
    return HttpResponse("Transferred")

def newOrders(request,fromAccount):
    response = newTrade.objects.filer(read = false).first();
    respose.read = false;
    response.save()	
    return render(request, 'elpheba/detail.html', {'response' : response})

