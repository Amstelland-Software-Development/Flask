# Python Flask

## Flask installeren

### 1. Routing

#### 1.1. in de CMD terminal in VS code: (letop, powershell werkt anders)
```cmd
python --version
```

#### 1.2. Maak een virtuele omgeving in de map genaamd `app`

```cmd
python -m venv app
```

#### 1.3. Activeer de virtuele omgeving

```cmd
app\scripts\activate
```

> De prompt veranderd - er staat (app) voor de standaard prompt om aan te geven dat je in de virtuele omgeving werkt.

#### 1.4. Gebruik de python packagemanager (PIP) om Flask te installeren.

> Check eerst welke packages al zijn geinstalleerd 
```cmd
pip list
```
> installeer Flask
```cmd
pip install flask
```
#### 1.5. Maak een nieuw bestand aan genaamd `app.py` en open deze in VS Code. Vul deze met onderstaande code:

```python
from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "hello world!"

if __name__ == "__main__":
    app.run()
```
In de CMD terminal in VS Code:
```cmd
python app.py
```
> Er wordt nu een development webserver gestart. Ga in je browser naar `http://localhost:5000/` om te testen of je Hello World ziet.
> Gelukt? gebruik CTRL-C in de CMD terminal in VS Code om de webserver te stoppen.


#### 1.6. Pas de `index` route aan naar een meer uitnodigende tekst. 

```python
from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "<h1>Welkom!</h1>"

@app.route("/helloWorld")
def helloworld():
    return "Hello World"

if __name__ == "__main__":
    app.run()
```
> We hebben nu een route die een string teruggeeft en eentje die HTML teruggeeft.


#### 1.7. Voeg een 'dynamische' route toe genaamd `getUser`

```python
from flask import Flask

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

if __name__ == "__main__":
    app.run()
```
> Test de `getUser` route door in je browser te gaan naar: `http://localhost:5000/user/????`

#### 1.8. Templates

Maak een map genaamd `Templates` met daarin een bestand genaamd `login.html`

```html
<html>
   <body>
      <form action="http://localhost:5000/login" method="post">
         Username:
         <input type="text" name="name" />
         <input type="submit" value="submit" />
      </form>
   </body>
</html>
```
Importeer de nodige onderdelen uit flask en pas `app.py` aan:
```python
from flask import Flask
from flask import render_template
from flask import redirect, url_for, request

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

if __name__ == "__main__":
    app.run(debug = True)
```

### 2. Requests library

#### 2.1 Installeer Requests

```cmd
pip install requests
```

#### 2.2 Maak een nieuwe route in `app.py`

```python
import requests

@app.route("/scrape")
def scrape():
    request = requests.get("http://www.stagemarkt.nl")
    return str(request.status_code)
    return str(request.text)

```

### 3. Beautiful Soup library


#### 3.1 Installeer Beautiful Soup 4 met PIP 

```cmd
pip install beautifulsoup4
```

#### 3.2 Output alle links van stagemarkt.nl

```python
from bs4 import BeautifulSoup

@app.route("/scrape")
def scrape():
    request = requests.get("http://www.stagemarkt.nl")
    html = str(request.text)
    # return str(request.status_code)
    # return str(request.text)

    soup = BeautifulSoup(html)
    links = soup.find_all("a")
    output = ""
    for link in links:
        output += str(link)
    return output
```