# Vaatimusmäärittely 

## Sovelluksen tarkoitus

Budjettisovelluksella voi määritellä haluamansa pituisia kalenteriajanjaksoja, 
joille on mahdollista kohdistaa vapaavalintaisia tulo- ja menoeriä. 
Sovellus laskee, paljonko rahaa jää käytettäväksi päivää kohti.

## Käyttäjät 

Ensimmäinen versio sovelluksesta on tarkoitettu yhden 
käyttäjän henkilökohtaiseen käyttöön eli on vain yksi käyttäjärooli, _peruskäyttäjä_.

## Käyttöliittymäluonnos

Sovelluksessa on yksi näkymä

<img src="https://github.com/ahpasila/ot-harjoitustyo/blob/master/kuvat/kayttisluonnos.png" width="750">

## Perusversion tarjoama toiminnallisuus
- käyttäjä voi luoda uuden budjetointijaksokohteen antamalla käyttöliittymässä alku- ja loppupäivämäärän
- käyttöliittymässä käyttäjä näkee joko käynnissä olevan jakson tai seuraavaksi alkavan jakson
- luomisen jälkeen jaksoa voi muokata, minkä jälkeen se pitää tallentaan, halutessaan sen voi myös poistaa
- käyttäjä voi lisätä vapaavalintaisen uuden tulo- tai menokohteen, kuten palkka tai ruokaostokset
- sovellus ilmoittaa käyttäjälle jakson yhteenlasketut tulot ja menot, näiden erotuksen sekä päiväkohtaisen käyttöbudjetin erotuksen pohjalta
- käyttäjä voi käyttöliittymässä siirtyä tarkastelemaan seuraavaa tai edeltävää budjetointijaksoa

## Jatkokehitysideoita

- järjestelmän suojaaminen kirjautumistoiminnolla, jotta omat tiedot voi pitää suojattuna
- budjetointijakson sisällön kopioiminen toiselle budjetointijaksolle pohjaksi
- mahdollisuus kirjata tulo- ja menokohteiden toteutumia kullekin ajanjaksolle
- sovellus esittää erotuksen toteuneen ja budjetoidun kohteen välillä
- lisätään validointisääntöjä päivämäärien määrittelylle ja muille toiminnoille
- käyttäjä voi lisätä tiedot säästöistään, jotta miinukselle meneviin budjetointeihin voi kiinnittää säästöjä
- käyttäjälle tarjotaan analytiikkaa tiedoistaan eli visualisointeja tuloista sekä menoista ja budjetoinnin osuvuudesta
