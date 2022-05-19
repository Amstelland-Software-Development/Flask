# Flask les 4

We hebben nu de basis voor een applicatie neergezet.

De applicatie bestaat uit de volgende onderdelen:

| Doel            | bestand      | verantwoordelijk voor                    | opmerkingen                     |
| --------------- | ------------ | ---------------------------------------- | ------------------------------- |
| Presentatie     | `app.py`     | routing / templating / applicatie logica | Interface gebruiker via browser |
| Data verzamelen | `scraper.py` | webscraping van stagemarkt.nl            | Ophalen / verversen van data |
| Database opzetten | `setup_database.py` | Database aanmaken | SQLite database `database.sqlite` |
| Database gebruiken | `db.py` | CRUD uitvoeren | Abstractie, gebruikt door `scraper.py` / `app.py` |


## Volgende stappen

![](/_lessen/img/flow.drawio.png)


## Waar ga je verder?

1. Eerst `scraper.py` aanpassen zodat alle gegevens die je wilt verzamelen van een vacature worden opgehaald
2. Eerst `scraper.py` aanpassen zodat alle zoekresultaten worden verwerkt (met een minimaal aantal opgehaalde gegevens per vacature)
3. Eerst `setup_database.py` aanpassen zodat er een plek in de database is voor alle gegevens
4. Eerst `db.py` aanpassen zodat alle gegevens kunnen worden weggeschreven naar de database
5. Eerst `app.py` aanpassen zodat je de gegevens die je hebt van een vacature kunt laten zien in de browser (in bv een tabel)

### 1. Hoe halen we alle pagina's met zoekresultaten op?

### 2. Welke gegevens willen we allemaal ophalen van een vacature?

### 3. Hoe willen we de database setup uitbreiden zodat we alle gegevens van een vacature kunnen opslaan?

### 4. Welke gegevens wil je wegschrijven in de database? Wil je meerdere tabellen aanmaken daarvoor?

### 5. Hoe wil je de gegevens die je hebt presenteren aan de gebruiker?


