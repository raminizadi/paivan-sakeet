# Päivän säkeet

Heikki Pursiaisen Twitterissä ja X:ssä julkaisemia runoja. Toteuttanut Ramin Izadi x Astra 6.1.

**Sivusto:** https://runot.heikkipursiainen.fi/

## Muokkaaminen GitHubissa

Avaa `data/edition.json` ja valitse tiedoston muokkaus (kynäkuvake). Etsi runo otsikolla tai `id`-tunnuksella. Muokkaa `title`-otsikkoa, `preface`-taustajohdantoa, `excerpt`-alkua sekä tarvittaessa lähdepareja `sourceTitle` / `sourceUrl` ja `secondaryTitle` / `secondaryUrl`. Rinnakkaisjulkaisun kentät ovat `crosspost` ja `crossLabel`.

Säilytä olemassa olevan julkaisun `id`, `date` ja `url`. Uusi tietue tarvitsee yksilöllisen `id`-merkkijonon, Suomen päivämäärän muodossa `YYYY-MM-DD`, alkuperäisen X-osoitteen sekä kentät `title`, `excerpt` ja `preface` (voi olla tyhjä). Säilytä listan aikajärjestys. Tarkista alkuperäinen julkaisu ja johdannon lähteet itse.

Säilytä JSONin lainausmerkit ja pilkut. Rivinvaihto merkitään `\n` ja tekstin lainausmerkki `\"`. Tallenna muutos kuvaavalla viestillä. Omassa haarassa tehty muutos voidaan tarkistaa ennen yhdistämistä `main`-haaraan.

`data/collection.json` sisältää menetelmäkuvauksen (`method`), tarkistuspäivän (`reviewed`), viimeisimmän päivityspäivän (`updated`) ja päivitettyjen runojen tunnukset (`updatedPoems`). Sivumallia ja Kokoelmasta-tekstejä muokataan tiedostossa `templates/book-template.html`.

## Automaattinen julkaisu

Jokainen `main`-haaraan tallennettu muutos käynnistää `.github/workflows/pages.yml`-työnkulun. Se rakentaa sivut toimitetusta aineistosta ja julkaisee vain `dist/`-hakemiston GitHub Pagesiin. GitHubin Pages-asetuksen julkaisulähteen tulee olla **GitHub Actions**. Työn voi käynnistää myös Actions-välilehden **Run workflow** -toiminnolla. Tarkista työn onnistuminen Actions-välilehdeltä ja valmis sivusto selaimessa.

Rakennetut `dist/`, `outputs/` ja `work/` eivät kuulu Gitiin.

## Paikallinen esikatselu

Tarvitset Python 3:n. Ulkoisia paketteja ei tarvita. Aja tämän hakemiston juuressa:

```powershell
python scripts/build_book.py --site-dir dist --output-file outputs/Paivan-sakeet.html
python -m http.server 8000 --directory dist
```

Avaa http://localhost:8000/ ja tarkista lukija, sisällys ja Kokoelmasta-sivu. Sivut voidaan rakentaa ilman verkkoyhteyttä. Kokonaiset runot tulevat X-upotuksista ja tarvitsevat verkkoyhteyden sekä saatavilla olevan alkuperäisjulkaisun.

Tässä varastossa on toimitettu aineisto ja lyhyet alut, ei tutkimusarkistoa tai kokonaisia runotekstivälimuisteja. Runojen oikeudet kuuluvat oikeudenhaltijoille; avoimen lähdekoodin tai aineiston lisenssiä ei ole määritelty.