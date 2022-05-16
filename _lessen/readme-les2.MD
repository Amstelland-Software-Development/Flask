# Pyhton Flash

## Beautiful Soup

### Ophalen informatie van alle stagebedrijven

```html 
https://stagemarkt.nl/vacatures/?`Termen=Software+developer+(25604)&PlaatsPostcode=amsterdam&Straal=0&Land=e883076c-11d5-11d4-90d3-009027dcddb5&ZoekenIn=A&Page=1&Longitude=&Latitude=&Regio=&Plaats=&Niveau=&SBI=&Kwalificatie=&Sector=&RandomSeed=743&Leerweg=&Internationaal=&Beschikbaarheid=&AlleWerkprocessenUitvoerbaar=&LeerplaatsGewijzigd=&Sortering=0&Bron=STA&Focus=&LeerplaatsKenmerk=&OrganisatieKenmerk=
```
### Interessante HTML blokken bekijken in devtools en class/ids noteren

```html
<a aria-label="" class="c-link-blocks-single" href="/stages/stage/amsterdam/the-next-software/stage-9da1696d-b914-4b24-8036-0b2d44ebcee7-25604" onclick="vueSearchForm.searchClickLink()">
<div class="c-link-blocks-single-info">
<h2>Software developer</h2>
<h3>The Next Software</h3>
<ul class="u-reset-ul">
<li><i aria-hidden="true" class="icon-location-marker"></i><span class="sr-only">Plaats</span> <span>Amsterdam </span></li>
<li><i aria-hidden="true" class="fas fa-user-graduate fas-c-link-blocks"></i><span class="sr-only">Leerweg</span> <span>bol</span></li>
<li><i aria-hidden="true" class="fas fa-tachometer-alt fas-c-link-blocks"></i><span class="sr-only">Niveau</span> <span>MBO niveau 4</span></li>
</ul>
<p>Wij zijn continu opzoek naar enthousiaste studenten die graag in de sales, after-sales en accountmanagement ervaring willen op doen. Wij bedienen honderden klanten, van ondernemer tot aan grote accountantskantoren.
Wil ..</p>
<div><span class="btn btn--orange-gradient">bekijk stage</span></div>
</div>
<div class="c-link-blocks-single-company">
<div><img alt="Logo van The Next Software" onerror="this.src='/images/transparent.gif';this.onerror=''" src="/photos/b/f7ca36e1-3bb0-e811-80e8-0050568f0ca6"/></div>
<p>
                                    The Next Software<br/>
<span onclick="window.open('http://www.thenextsoftware.io')">Website</span>
</p>
</div>
</a>

```
### Class gevonden die alle info van een stagebdrijf bevat
```css
c-link-blocks-single
```

### Ophalen van de informatie van een enkel bedrijf met Beautiful Soup
```python
@app.route("/scrape")
def scrape():
    url = "https://stagemarkt.nl/vacatures/?Termen=Software+developer+(25604)&PlaatsPostcode=amsterdam&Straal=0&Land=e883076c-11d5-11d4-90d3-009027dcddb5&ZoekenIn=A&Page=1&Longitude=&Latitude=&Regio=&Plaats=&Niveau=&SBI=&Kwalificatie=&Sector=&RandomSeed=743&Leerweg=&Internationaal=&Beschikbaarheid=&AlleWerkprocessenUitvoerbaar=&LeerplaatsGewijzigd=&Sortering=0&Bron=STA&Focus=&LeerplaatsKenmerk=&OrganisatieKenmerk="

    request = requests.get(url)
    html = str(request.text)
    soup = BeautifulSoup(html, 'html.parser')
    
    output = soup.find(class_="c-link-blocks-single")
    return str(output)
```

### Alleen de bedrijfsnaam ophalen
```python
return str(output.h3)
```
### Nu zonder HTML tags
```python
return str(output.h3.text)
```
### En nu van alle bedrijven op de 1ste resultaten pagina

```python
import json
#...
vacaturesHTML = soup.find_all(class_="c-link-blocks-single")
vacatureList = []
for vacature in vacaturesHTML:
    vacatureDict = {
        "title": str(vacature.h2.text),
        "bedrijf": str(vacature.h3.text)
    }
    vacatureList.append(vacatureDict)
return json.dumps(vacatureList)
```

### Vind de link die verwijst naar de vacature pagina en voeg die toe aan een lijst / de vacature dictionary

```python
    vacaturesHTML = soup.find_all(class_="c-link-blocks-single")
    vacatureList = []
    for vacature in vacaturesHTML:
        vacatureDict = {
            "title": str(vacature.h2.text),
            "bedrijf": str(vacature.h3.text),
            "link": str("http://www.stagemarkt.nl" + vacature['href'])
        }
        vacatureList.append(vacatureDict)
    return json.dumps(vacatureList)
```

### Loop door de lijst met links met vacatures en haal die op met requests

```python
    for vacature in vacatureList:
        request = requests.get(vacature['link'])
        html = request.text
        soup = BeautifulSoup(html, 'html.parser')
        return str(soup) #return enkele vacature - stop met de for loop om te zien wat je terugkrijgt
```

### Zoek interessante inhoud in de HTML en voeg die toe aan de vacature dict
```css
c-detail-company
```

### Gebruik de BeautifulSoup::find() functie
```python
    for vacature in vacatureList:
        request = requests.get(vacature['link'])
        html = request.text
        soup = BeautifulSoup(html, 'html.parser')
        
        companyDetails = soup.find(class_="c-detail-company")
        return str(companyDetails)
```
### Informatie ophalen wanneer er geen class/id is te vinden

```python
    for vacature in vacatureList:
        request = requests.get(vacature['link'])
        html = request.text
        soup = BeautifulSoup(html, 'html.parser')
        
        companyDetails = soup.find(class_="c-detail-company")
        return str(companyDetail.contents)
```



### Haal de juiste elementen op
```python
        return str(companyDetails.contents[3])
```
```python
        return str(companyDetails.contents[3].contents[3].text) # toont de straat en huisnummer
```
```python
        vacature['straat'] = str(companyDetails.contents[3].contents[3].text) # slaat deze string op in de vacature dict onder key 'straat'
```

```python
        i = 0
        for item in companyDetails.contents:
            print(str(i) + " - " + str(item) + "<br>")
            i = i +1
```

#### OPDRACHT: Sla de onderstaande gegevens op in de vacature dictionary
* contactpersoon
* telefoonnummer
* contactpersoon_email
* bedrijfs_email
* leerbedrijfID
* postcode
* stad
* straathuisnummer

> output de hele vacature list
```python
json.dumps(vacatureList)
```
  