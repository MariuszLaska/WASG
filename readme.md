# Mapa COVID-19
## _Projekt z Wybrancych Aplikacji Systemów Geoinformatycznych_
#####  Mariusz Laska

&nbsp;

### Aplikacja
Aplikacja pozwala nam na przeglądanie mapy świata, na której umieszczone są dane o epidemii choroby COVID-19.
Użytkownik może wybrać spośród
- sumy przypadków zakażeń
- sumy śmierci spowodowanych przez COVID-19
- sumy sczepień przeciwko chorobie

Na mapie użytkownik widzi okręgi o wielkości wprost proporcjonalnej do ilości przypadków w danym kraju.
Po najechaniu na okrąg pojawia się dymek z nazwą kraju oraz liczbą przypadków

### Użyte narzędzia
#### Język programowania

Do zaprogramowania aplikacji skorzystałem z języka ***Python***. Stwierdziłem, iż jest to idealny język do tego zadania gdyż:
- pozwala on na łatwe operowanie na dużej ilości danych np. o zachorowaniach
- ilość kodu potrzebnego do implementacji jest względnie mała
- wspiera rozwiązania webowe
- jest bogaty w biblioteki do obsługi map

### Biblioteki
Do stworzenia mapy wykorzystałem bibliotekę ***folium***. Pozwala ona na łatwą wizualizację danych na mapach oraz generuje mapę w formacie HTML.

Dodatkowo, aby stworzyć widget wyboru danych wykorzystałem bibliotekę ***branca***.

### Dane
Do zdobycia danych o zakażeniach wykorzystałem otwartą bazę danych ze strony *ourworldindata.org*
Pobrałem dane w formacie CSV, a dzięki użyciu języka Python łatwo zwizualizowałem je w aplikacji.

Dodatkowo wykorzystałem znalezioną w internecie bazę danych ze współrzędnymi geofraficznymi środków geometrycznych państw.
Dane te również były w formacie CSV. Wykorzystałem je, aby poprwawnie umiejscowić środki okręgów symboilzujących ilość.
