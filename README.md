# Installatie

Dit kan je normaal gezien doen.
`python` zal dankzij `pipenv` (en de `Pipfile` in deze repository) ook automatisch naar Python 3 verwijzen. Het is niet nodig om `python3` te gebruiken.

```
git clone https://github.com/vbrh-immalle/flasker
cd flasker
pipenv install
pipenv shell
python main.py
```

Wanneer `pipenv` niet je in je `PATH` aanwezig is, je kan het altijd starten met `python -m pipenv`, de commando's worden dan:

```
python -m pipenv install
python -m pipenv shell
```

# Uitvoering en te proberen

Eens in de virtuele omgeving, kan je de flask webserver dus opstarten met

    python main.py

Deze is zo geconfigureerd dat:

- de debug-versie wordt opgestart zodat je extra loggings op de console en foutmeldingen ziet in de browser
- IP-adres `127.0.0.2` wordt gebruikt zodat je bij het analyseren van het (TCP-)verkeer beter kan zien wat IP-adres van de **server** is

Als je met een webbrowser de site bezoekt, zet dan zeker ook de development-tools (b.v. de Network-tab) open, zodat je de HTTP-methods kan zien bij b.v. `/redirect-me`.
