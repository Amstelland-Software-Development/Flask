# Flask

## Forken & clonen

Maak een fork van de github repository. Maak een clone van jouw fork en open deze in VS Code.

Toevoegen van de `origin` remote in VS code

```command
git add remote
```

## 1. Scraper updaten met alle gegevens:

* Vacature gegevens:
   * Vacature Titel
   * Vacature Tekst
   * Locatie
   * Periode
   * Laatste Wijziging
   * Beschikbaarheid
* Bedrijfs gegevens:
   * Adres
      * Straat
      * Nummer
      * Postcode
      * Stad
    * Telefoonnummer
    * email
    * website
    * LeerbedrijfId
* Contactpersoon
  * Voornaam
  * Achternaam
  * Telefoonnummer
  * Email

## 2. `setup_database.py` updaten zodat alle gegevens een plek hebben in de database

## 3. `db.py` updaten zodat alle gegevens kunnen worden weggeschreven

## 4. `app.py` updaten zodat alle gegevens worden getoond in de `/show` route
