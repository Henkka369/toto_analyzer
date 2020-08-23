# Toto-tuloksien haku ja analysointi

Tämä sovellus koostuu kahdesta erillisestä osasta: toto_analyzer.py ja data_fetch.py. progress_bar.py on apufunktio edistymispalkin tulostamiseen, 
mitä data_fetch.py-tiedosto käyttää. data_fetch.py hakee Veikkauksen APIsta toto-tulokset halutulta aikaväliltä ja tallentaa ne json-tiedostoon.
toto_analyzer.py tarjoaa käyttäjälle konsolikäyttöliittymän json-tiedoston datan tarkastelua varten.
