from django.shortcuts import render,redirect
from django.template import loader
from django.http import HttpResponse
import json
from django.core import serializers
from django.conf import settings as djangoSettings
from django.http import JsonResponse


def index(request):
    return render(request,'nse/index.html');
def testing(request):
    return render(request,'nse/test.html');

# This view was used for testing working of json file.
def update(request):
    if request.method=="POST":
        str1=request.POST
        str1=str1.dict()
        if 'csrfmiddlewaretoken' in str1:
            del str1['csrfmiddlewaretoken']
        x=""
        y=""
        temp={}
        list1=[]
        for k,v in str1.items():
            print("Key is " + k + " Value is " + v)
            if(x==""):
                temp = {}
                x = v
            else:
                y=v
                temp = {
                "x":x,
                "y":y
                }
                x=""
                y=""
                list1.append(temp)
        json1=json.dumps(list1)
        name = "xy2"
        file = open(djangoSettings.STATIC_ROOT + '\\nse\\' + name + '.json', 'w')
        file.write(json1)
        file.close()
        return JsonResponse(list1,safe=False)

def update1(request):                                                   #Actual view for storing the post request from index page in a jason file.
    if(request.method=="POST"):                                         #if the request made was post in form of key1=val1 && key2=val2 && key3=val3.....son on
        str1=request.POST                                               #store the file as a string and then as a dictionary of elements
        str1=str1.dict()
        if 'csrfmiddlewaretoken' in str1:
            del str1['csrfmiddlewaretoken']                             #remove the csrf token
        date=""                                                         #these variables show the attribute of object to be stred in json file
        sensex=""
        nifty=""
        gold=""
        nasdaq=""
        temp={}                                                        #temp will be object to store values temprarily with above mentioned attributes
        list1=[]                                                       #list1 act as list to store temp values ,thus it will be list of object
        for k,v in str1.items():                                       #iterating over all elements in post request using k to store key and v oto store values (key1=val1)
            if(date==""):
                date=v;
            elif(sensex==""):
                sensex=v;
            elif (nifty == ""):
                nifty = v;
            elif (nasdaq == ""):
                nasdaq = v;
            elif (gold == ""):
                gold = v;
                temp={
                    "Date":date,
                    "SENSEX":sensex,
                    "NIFTY":nifty,
                    "NASDAQ":nasdaq,
                    "GOLD":gold
                }
                date=""
                sensex=""
                nifty=""
                nasdaq=""
                gold=""
                list1.append(temp)
                temp={}
        json1=json.dumps(list1)                                        #json1 now stores list1 as a json file
        name="jsonData3"                                               # name of file which stores json data
        file=open(djangoSettings.STATIC_ROOT+'\\nse\\'+name+'.json','w')# open the required file to write values
        file.write(json1)
        file.close();                                                   #close the file after writing on it
        return JsonResponse(list1,safe=False)


