"""
author: Berkay Ertuğrul
blog: berkayertugrul.site
email: berkay.ertugrul@hotmail.com
github: github.com/clopylol
---------------------------------
Flask ve Bootstrap kullanarak geliştirildi.
---------------------------------
MIT license.
"""

from flask import Flask, render_template, request, redirect, url_for
import http.client
import json
import time
import requests
import random
from datetime import datetime
from requests.api import get

app = Flask(__name__)
@app.route("/")
def index():
    #Cihaz IP'sinden konum tespiti için bu API'yı kullanacağız.Buradan aldığımız konum bilgisini farklı bir API'da kullanarak Ezan Saatlerini çekeceğiz.
    ip = get('https://api.ipify.org').text
    conn = http.client.HTTPSConnection("api.collectapi.com")
    headers = {
        'content-type': "application/json",
        'authorization': "~Your API Key~"
    }

    istekIP = "/ip/ipToLocation?data.ip="+ip
    conn.request("GET", istekIP, headers=headers)
    res = conn.getresponse()
    data = res.read()
    dataYeni = json.loads(data)
    konum = (dataYeni["result"]["regionname"])


    # Bu API'ı kullanarak da tespit edilen konumun ezan saatlerini çekeceğiz.
    istekEzan = "/pray/all?data.city="+konum.lower()
    conn.request("GET", istekEzan, headers=headers)
    res = conn.getresponse()
    data = res.read()
    dataYeni = json.loads(data)

    konum = konum.upper()

    imsakVakit = (dataYeni["result"][0]["saat"])
    gunesVakit = (dataYeni["result"][1]["saat"])
    ogleVakit = (dataYeni["result"][2]["saat"])
    ikindiVakit = (dataYeni["result"][3]["saat"])
    aksamVakit = (dataYeni["result"][4]["saat"])
    yatsiVakit = (dataYeni["result"][5]["saat"])

    t = time.localtime()
    saat = time.strftime("%H:%M", t)

    imsakVakit2 = time.strftime(imsakVakit)
    günesVakit2 = time.strftime(gunesVakit)
    ogleVakit2 = time.strftime(ogleVakit)
    ikindiVakit2 = time.strftime(ikindiVakit)
    aksamVakit2 = time.strftime(aksamVakit)
    yatsiVakit2 = time.strftime(yatsiVakit)

    ezanVakitleri = (imsakVakit2, günesVakit2, ogleVakit2,ikindiVakit2, aksamVakit2, yatsiVakit2)

    FMT = '%H:%M'
    if((saat >= imsakVakit2) and (saat < günesVakit2)):
        suanVakit = "Sabah Namazı"
        kalanVakit = datetime.strptime(günesVakit2, FMT) - datetime.strptime(saat, FMT)
    elif((saat >= ogleVakit2) and (saat < ikindiVakit2)):
        suanVakit = "Öğle Namazı"
        kalanVakit = datetime.strptime(ikindiVakit2, FMT) - datetime.strptime(saat, FMT)
    elif((saat >= ikindiVakit2) and (saat < aksamVakit2)):
        suanVakit = "İkindi Namazı"
        kalanVakit = datetime.strptime(aksamVakit2, FMT) - datetime.strptime(saat, FMT)
    elif((saat >= aksamVakit2) and (saat < yatsiVakit2)):
        suanVakit = "Akşam Namazı"
        kalanVakit = datetime.strptime(yatsiVakit2, FMT) - datetime.strptime(saat, FMT)
    else:
        suanVakit = "Yatsı Namazı"
        kalanVakit = datetime.strptime(imsakVakit2, FMT) - datetime.strptime(saat, FMT)

    # Hadisler
    url = "http://berkayertugrul.site/EzanApp/Hadisler.json"
    res = requests.get(url)
    res.encoding
    dataHadis = res.json()
    sayi = random.randint(0, 100)
    hadis = (dataHadis["hadisler"][sayi]["hadis"])  
    hadisKaynak = (dataHadis["hadisler"][sayi]["hadisKaynagi"])  



    return render_template("index.html", ezanVakitleri=ezanVakitleri, konum=konum, saat=saat, suanVakit=suanVakit, kalanVakit=kalanVakit, hadis=hadis, hadisKaynak=hadisKaynak)

@app.route("/il", methods = ["POST"])
def sorgu():
    conn = http.client.HTTPSConnection("api.collectapi.com")
    headers = {
        'content-type': "application/json",
        'authorization': "~Your API Key~"
        }

    konum = request.form.get("il")
    konum.lower()
    istekEzan = "/pray/all?data.city="+konum.lower()
    conn.request("GET", istekEzan, headers=headers)
    res = conn.getresponse()
    data = res.read()
    dataYeni = json.loads(data)

    konum = konum.upper()

    imsakVakit = (dataYeni["result"][0]["saat"])
    gunesVakit = (dataYeni["result"][1]["saat"])
    ogleVakit = (dataYeni["result"][2]["saat"])
    ikindiVakit = (dataYeni["result"][3]["saat"])
    aksamVakit = (dataYeni["result"][4]["saat"])
    yatsiVakit = (dataYeni["result"][5]["saat"])

    t = time.localtime()
    saat = time.strftime("%H:%M", t)

    imsakVakit2 = time.strftime(imsakVakit)
    günesVakit2 = time.strftime(gunesVakit)
    ogleVakit2 = time.strftime(ogleVakit)
    ikindiVakit2 = time.strftime(ikindiVakit)
    aksamVakit2 = time.strftime(aksamVakit)
    yatsiVakit2 = time.strftime(yatsiVakit)

    ezanVakitleri = (imsakVakit2, günesVakit2, ogleVakit2,ikindiVakit2, aksamVakit2, yatsiVakit2)

    FMT = '%H:%M'
    if((saat >= imsakVakit2) and (saat < günesVakit2)):
        suanVakit = "Sabah Namazı"
        kalanVakit = datetime.strptime(günesVakit2, FMT) - datetime.strptime(saat, FMT)
    elif((saat >= ogleVakit2) and (saat < ikindiVakit2)):
        suanVakit = "Öğle Namazı"
        kalanVakit = datetime.strptime(ikindiVakit2, FMT) - datetime.strptime(saat, FMT)
    elif((saat >= ikindiVakit2) and (saat < aksamVakit2)):
        suanVakit = "İkindi Namazı"
        kalanVakit = datetime.strptime(aksamVakit2, FMT) - datetime.strptime(saat, FMT)
    elif((saat >= aksamVakit2) and (saat < yatsiVakit2)):
        suanVakit = "Akşam Namazı"
        kalanVakit = datetime.strptime(yatsiVakit2, FMT) - datetime.strptime(saat, FMT)
    else:
        suanVakit = "Yatsı Namazı"
        kalanVakit = datetime.strptime(imsakVakit2, FMT) - datetime.strptime(saat, FMT)

    # Hadisler
    url = "http://berkayertugrul.site/EzanApp/Hadisler.json"
    res = requests.get(url)
    res.encoding
    dataHadis = res.json()
    sayi = random.randint(0,100)
    hadis = (dataHadis["hadisler"][sayi]["hadis"])  
    hadisKaynak = (dataHadis["hadisler"][sayi]["hadisKaynagi"])  

    return render_template("index.html", ezanVakitleri = ezanVakitleri, konum = konum, saat = saat, suanVakit = suanVakit, kalanVakit = kalanVakit, hadis=hadis, hadisKaynak=hadisKaynak)

if __name__ == "__main__":
    app.run(debug=True)

