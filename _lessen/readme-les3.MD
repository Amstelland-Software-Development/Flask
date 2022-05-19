# Flask Les 3

- [Flask Les 3](#flask-les-3)
  - [Scraper gegevens opslaan in een database](#scraper-gegevens-opslaan-in-een-database)
    - [Opzetten SQLite database](#opzetten-sqlite-database)
    - [Los scraper script opzetten (app.py -> scraper.py)](#los-scraper-script-opzetten-apppy---scraperpy)
    - [Opslaan van de scraper gegevens in de database](#opslaan-van-de-scraper-gegevens-in-de-database)

## Scraper gegevens opslaan in een database

> Is een Python standaard library, dus geen `pip install ... `  
> Database opgeslagen in bestand met `.sqlite` extensie

### Opzetten SQLite database
> Aanmaken van de los python scripts om een SQLite database aan te maken met daarin een tabel en de juiste kolommen om gegevens in op te slaan.

!!! note Note
    test



1. Maak een nieuwe bestand genaamd: `setup_database.py`

    ```python
    import sqlite3

    file = "database.sqlite"
    try:
        conn = sqlite3.connect(file)
        print("database created")
    except:
        print("database not created")
    ```

2. Run `setup_database.py` **TIP**: gebruik TAB voor autocomplete in de terminal
    ```cmd
    prompt:> python setup_database.py
    ```
3. Als het goed is wordt er nu een lege database file aangemaakt: `database.sqlite`
   
4. Installeer de `SQLite Viewer` extensie van `Florian Klampfer` in VSCode. 

5. Selecteer/open de `database.sqlite` in de Explorer in VSCode.
   > Je ziet een lege database: `Tables(0)`

6. Pas de `setup_database.py` om een eerste tabel aan te maken:
   
    ```python
    import sqlite3

    file = "database.sqlite"
    try:
        conn = sqlite3.connect(file)
        print("database created")
    except:
        print("database not created")
    
    conn.execute("CREATE TABLE vacature (title TEXT NOT NULL, bedrijf TEXT NULL, link TEXT NOT NULL);")
    
    conn.commit() # uitgevoerde SQL statements worden weggeschreven in de database
    conn.close() # de verbinding met de database wordt afgesloten
    ```
        Datatypes in SQLite: NULL, INTEGER, REAL, TEXT, BLOB

7. Insert wat test gegevens in de vacature tabel:
    ```python
    # Bepaal zelf waar in de code de insert SQL statements worden uitgevoerd
    conn.execute("INSERT INTO vacature (title, bedrijf, link) VALUES ('testtitle', 'testbedrijf', 'http://testlink.com')")

    ```

8. Open `database.sqlite` in VSCode om te zien of het gelukt is.

### Los scraper script opzetten (app.py -> scraper.py)
> Scraper code verplaatsen van de @route naar eigen `.py` bestand en zorgen dat deze werkt los van `app.py`. 

9. Maak een bestand genaamd `scraper.py` aan en zet de code die nu in `app.py` onder de `@route("/scrape)` staat erin. 
    
    * Letop de onderstaande punten:
      * De `scrape()` functie laten we achterwege
      * Dus.. de `return` statement aan het eind van de functie werkt niet meer
      * Gebruik `print()` statements om output te tonen in de VSCode terminal
      * Bekijk welke `imports` je nodig hebt om alleen de webscraping te laten werken

10. Run `scraper.py` in de terminal
    ```cmd
    prompt:> python scraper.py
    ```
    > Foutmeldingen? Los deze op en probeer het nog een keer tot de scraper werkt als los python script.

11. Voeg wat feedback toe aan `scraper.py` zodat je ziet hoe lang het script duurt ongeveer. Straks gaan we _honderden_ vacatures / bedrijven af, dus fijn als je ziet dat hij bezig is. Gebruik `print()` statements in je loops.

    file: `scraper.py`
    ```python
    import requests
    import json
    from bs4 import BeautifulSoup

    url = "https://stagemarkt.nl/vacatures/?Termen=Software+developer+(25604)&PlaatsPostcode=amsterdam&Straal=0&Land=e883076c-11d5-11d4-90d3-009027dcddb5&ZoekenIn=A&Page=1&Longitude=&Latitude=&Regio=&Plaats=&Niveau=&SBI=&Kwalificatie=&Sector=&RandomSeed=743&Leerweg=&Internationaal=&Beschikbaarheid=&AlleWerkprocessenUitvoerbaar=&LeerplaatsGewijzigd=&Sortering=0&Bron=STA&Focus=&LeerplaatsKenmerk=&OrganisatieKenmerk="

    request = requests.get(url)
    html = str(request.text)
    soup = BeautifulSoup(html, 'html.parser')

    vacaturesHTML = soup.find_all(class_="c-link-blocks-single")
    vacatureList = []

    for vacature in vacaturesHTML:
        vacatureDict = {
            "title": str(vacature.h2.text),
            "bedrijf": str(vacature.h3.text),
            "link": str("http://www.stagemarkt.nl" + vacature['href'])
        }
        vacatureList.append(vacatureDict)

    counter = 0
    for vacature in vacatureList:
        print("fetching vacature nr: " + str(counter)) #progress feedback
        request = requests.get(vacature['link'])
        html = request.text
        soup = BeautifulSoup(html, 'html.parser')
        companyDetails = soup.find(class_="c-detail-company")
        counter += 1

    print("complete") #scrape complete
    print(json.dumps(vacatureList))
    ```

### Opslaan van de scraper gegevens in de database
> Combineren van het werk dat we hebben gedaan. Vanuit `scraper.py` gegevens opslaan in de database.

12. Maak vanuit `scraper.py` een oproep naar de database om een losse vacature op te slaan.

> Het wordt steeds rommeliger. Goed moment om even wat tijd te steken in het opruimen van de code en ervoor te zorgen dat deze herbruikbaar en makkelijk is om te onderhouden. We gaan de code die we gebruiken om de database aan te spreken afscheiden door deze in een class te zetten.

13. Maak een bestand genaamd `db.py` 

bestand: `db.py` 
```python
import sqlite3

class database:    
    def __init__(Self, file):
        Self.conn = sqlite3.connect(file)

    def insertVacature(Self, title, bedrijf, link):
        values = [title, bedrijf, link] 
        Self.conn.execute("INSERT INTO vacature (title, bedrijf, link) VALUES (?, ?, ?)", values)
        Self.conn.commit()
```

14. We kunnen nu in `scraper.py` het volgende toevoegen:

```python
from db import database

for vacature in vacatureList:
    db = database("database.sqlite")
    db.insertVacature(vacature['title'], vacature['bedrijf'], vacature['link'])
```

15. Voeg een method toe aan de db class om de output van een enkele tablen te tonen in de console


bestand: `db.py` 
```python
    def showTable(Self):
        result = Self.conn.execute("SELECT * FROM vacature")
        Self.conn.commit()
        for row in result:
            print(row)
```
16. We kunnen deze nu toevoegen aan de `scraper.py` aan het einde om te checken of alles goed is opgeslagen in de database.

```python
db.showTable()
```