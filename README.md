# Toto Analyzer

Tämä sovellus hakee Toto-tilastoja ja esittää tuloksia eri näkökulmista. Sovellus koostuu kahdesta erillisestä osasta: toto_analyzer.py ja data_fetch.py. progress_bar.py on apufunktio edistymispalkin tulostamiseen, mitä data_fetch.py-tiedosto käyttää. data_fetch.py hakee Veikkauksen APIsta Toto-tulokset halutulta aikaväliltä ja tallentaa ne json-tiedostoon. toto_analyzer.py tarjoaa käyttäjälle konsolikäyttöliittymän json-tiedoston datan tarkastelua varten.

## data_fetch.py
Kun ohjelman käynnistää, se aloittaa tietojen hakemisen heti ja esittää etenemisen edistymispalkissa. Haun päätyttyä konsoliin tulostetaan hylättyjen tasapelien määrä (jos samalla sijalla on enemmän kuin yksi hevonen), lähtöjen määrä ilman tuloksia (nämä hypättiin yli) ja eri kombinaatioiden määrä haetussa datassa.
Tiedoston ensimmäisillä riveillä määritellään muuttujat startDate ja endDate. Ohjelma hakee näiden kahden päivämäärän väliseltä ajalta kaikki Suomen Toto-tulokset ja tallentaa ne json-tiedostoon. Ohjelma tallentaa jokaisesta lähdöstä kolme ensimmäistä hevosta maaliintulojärjestyksessä ja tiedon oliko lähtö voltti- vai autolähtö. Tiedoista muodostetaan Pythonin dictionary, jonka avaimena toimii kolmen ensimmäisen hevosen numerot ja tieto lähdön tyypistä pilkuilla eroteltuna. Dictionaryn arvona on kokonaisluku, joka kuvastaa montako kertaa kyseinen avain esiintyi haetussa datassa. Lopuksi ohjelma kirjoittaa data.json-nimisen tiedoston, joka sisältää dictionaryn ja tallentaa sen samaan tiedostosijaintiin, jossa data_fetch.py sijaitsee. 

## toto_analyzer.py
Jos data.json-tiedostoa ei ole samassa tiedostosijainnissa tämän tiedoston kanssa, ohjelma tulostaa rivin, jossa tämä ilmoitetaan ja päättyy. Datan löytyessä ohjelma tulostaa konsoliin vaihtoehdot, joista käyttäjä voi valita, miten haluaa haettuja tuloksia tarkastella. Konsoliin tulostetaan yhdeksän numeroitua vaihtoehtoa ja rivi, jolle käyttäjä voi syöttää halutun numeron. Tämän jälkeen konsoliin tulostetaan 20 datassa eniten esiintyvää yhdistelmää tai numeroa. Lopuksi käyttäjä voi aloittaa ohjelman alusta tai lopettaa sen. Mahdolliset valinnat datan tarkastelua varten ovat:
**1. Voittaja:** Tulostaa numerot, jotka ovat voittaneet eniten lähtöjä.
**2. Kaksari:** Tulostaa kaksariparit, jotka esiintyivät eniten datassa.
**3. Troikka:** Tulostaa troikkayhdistelmät, jotka esiintyivät eniten datassa.
**4. Voittaja (volttilähtö):** Ottaa huomioon vain volttilähtöjen voittajat.
**5. Voittaja (autolähtö):** Ottaa huomioon vain autolähtöjen voittajat.
**6. Kaksari (volttilähtö):** Ottaa huomioon vain volttilähtöjen kaksariparit.
**7. Kaksari (autolähtö):** Ottaa huomioon vain autolähtöjen kaksariparit.
**8. Troikka (volttilähtö):** Ottaa huomioon vain volttilähtöjen troikkayhdistelmät.
**9. Troikka (autolähtö):** Ottaa huomioon vain autolähtöjen troikkayhdistelmät.
