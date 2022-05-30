from flask import Flask
from flask import render_template
from flask import redirect, url_for, request
from bs4 import BeautifulSoup
import requests
import json
from db import database

app = Flask(__name__)

@app.route("/")
def index():
    return "<h1>Welkom!</h1>"

@app.route("/helloworld")
def helloWorld():
    return "Hello World"

@app.route("/user/<name>/")
def getUser(name):
    return "User is " + name

@app.route("/login", methods = ["POST", "GET"])
def login():
    if request.method == "POST":
        user = request.form["name"]
        return redirect(url_for("getUser", name = user))
    else:
        user = request.args.get('name')
        return render_template('login.html')

@app.route("/scrape")
def scrape():
    url = "https://stagemarkt.nl/vacatures/?Termen=Software+developer+(25604)&PlaatsPostcode=amsterdam&Straal=0&Land=e883076c-11d5-11d4-90d3-009027dcddb5&ZoekenIn=A&Page=1&Longitude=&Latitude=&Regio=&Plaats=&Niveau=&SBI=&Kwalificatie=&Sector=&RandomSeed=743&Leerweg=&Internationaal=&Beschikbaarheid=&AlleWerkprocessenUitvoerbaar=&LeerplaatsGewijzigd=&Sortering=0&Bron=STA&Focus=&LeerplaatsKenmerk=&OrganisatieKenmerk="

    request = requests.get(url)
    html = str(request.text)
    soup = BeautifulSoup(html, 'html.parser')
    
    vacaturesHTML = soup.find_all(class_="c-link-blocks-single")
    vacatureList = []

    for vacature in vacaturesHTML:
        # vacatureLinks.append(str("http://www.stagemarkt.nl" + vacature['href']))
        vacatureDict = {
            "title": str(vacature.h2.text),
            "bedrijf": str(vacature.h3.text),
            "link": str("http://www.stagemarkt.nl" + vacature['href'])
        }
        vacatureList.append(vacatureDict)

    for vacature in vacatureList:
        request = requests.get(vacature['link'])
        html = request.text
        soup = BeautifulSoup(html, 'html.parser')

        companyDetails = soup.find(class_="c-detail-company")
        
        i = 0
        for item in companyDetails.contents[3]:
            print(str(i) + " - " + str(item))
            i += 1

        return str(companyDetails.contents[3].contents[3].text)
    return json.dumps(vacatureList)

@app.route("/showtable")
def showtable():
    db = database("database.sqlite")
    data = db.showTable()
    return render_template('show.html', data=data)


    
if __name__ == "__main__":
    app.run(debug = True)

