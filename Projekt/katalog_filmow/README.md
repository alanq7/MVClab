# Katalog kolekcji filmów

Projekt zaliczeniowy wykonany w Django w ramach zadania 12 — Katalog kolekcji filmów.

## Spis treści

1. [Opis projektu](#opis-projektu)
2. [Funkcjonalności](#funkcjonalności)
3. [Technologie](#technologie)
4. [Struktura MVC/MVT](#struktura-mvcmvt)
5. [Instrukcja uruchomienia](#instrukcja-uruchomienia)
6. [Struktura projektu](#struktura-projektu)
7. [Dane i pliki media](#dane-i-pliki-media)

## Opis projektu

Aplikacja webowa służąca do zarządzania katalogiem kolekcji filmów. Użytkownik może przeglądać listę filmów, sprawdzać szczegóły pojedynczego filmu, dodawać nowe filmy, edytować istniejące, usuwać filmy oraz wyszukiwać je po tytule lub reżyserze.

Każdy film posiada tytuł, reżysera, ocenę oraz opcjonalny plakat. Aplikacja posiada ciemny, ostylowany interfejs inspirowany serwisami filmowymi.

## Funkcjonalności

- wyświetlanie listy filmów,
- wyświetlanie szczegółów pojedynczego filmu,
- dodawanie nowego filmu,
- edycja filmu,
- usuwanie filmu po potwierdzeniu,
- wyszukiwanie filmów po tytule lub reżyserze,
- sortowanie filmów od najwyżej ocenionych,
- walidacja danych formularza,
- obsługa opcjonalnych plakatów filmów,
- panel administratora Django,
- ostylowany interfejs użytkownika.

## Technologie

- Python
- Django
- SQLite
- HTML
- CSS
- Pillow

## Struktura MVC/MVT

Projekt został wykonany w Django, które formalnie korzysta ze wzorca MVT, jednak struktura projektu odpowiada założeniom MVC:

- Model: `movies/models.py`
- Controller: `movies/views.py`, `movies/urls.py`, `config/urls.py`
- View: `movies/templates/movies/` oraz `movies/static/movies/style.css`

Model `Movie` odpowiada za strukturę danych filmu. Widoki w `views.py` obsługują żądania HTTP, pobierają dane z modelu, zapisują formularze i przekazują dane do szablonów HTML. Szablony HTML oraz plik CSS odpowiadają za prezentację danych użytkownikowi.

## Instrukcja uruchomienia

Aby uruchomić projekt lokalnie, wykonaj poniższe kroki.

### 1. Sklonuj repozytorium

```bash
git clone ADRES_REPOZYTORIUM
```

Po sklonowaniu przejdź do folderu projektu:

```bash
cd katalog_filmow 
```

### 2. Utwórz środowisko wirtualne

```bash
python3 -m venv venv 
```

### 3. Aktywuj środowisko wirtualne

Na systemie macOS/Linux:

```bash
source venv/bin/activate 
```

Na systemie Windows:

```bash
venv\Scripts\activate 
```

Po aktywacji środowiska wirtualnego w terminalu powinna pojawić się nazwa środowiska, np. (venv).

### 4. Zainstaluj wymagane paczki

```bash
pip install -r requirements.txt 
```

Plik requirements.txt zawiera biblioteki potrzebne do działania projektu, między innymi Django oraz Pillow.

### 5. Wykonaj migracje bazy danych

```bash
python manage.py migrate 
```

Ta komenda utworzy potrzebne tabele w lokalnej bazie danych SQLite.

### 6. Utwórz konto administratora

```bash
python manage.py createsuperuser 
```

Po wykonaniu komendy należy podać nazwę użytkownika, adres e-mail oraz hasło. Konto administratora pozwala zalogować się do panelu Django pod adresem /admin/.

### 7. Uruchom serwer developerski

```bash
python manage.py runserver 
```

Po uruchomieniu serwera aplikacja będzie dostępna pod adresem:

```text
http://127.0.0.1:8000/ 
```

Panel administratora Django będzie dostępny pod adresem:

```text
http://127.0.0.1:8000/admin/ 
```

### 8. Dodawanie danych

Filmy można dodawać na dwa sposoby:

- przez aplikację, klikając przycisk Dodaj film,
- przez panel administratora Django pod adresem /admin/.

Każdy film posiada tytuł, reżysera, ocenę oraz opcjonalny plakat. Plakaty dodane przez formularz są zapisywane w folderze media/posters/.

## Struktura projektu
```text
katalog_filmow/
├── config/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── movies/
│   ├── migrations/
│   │   ├── __init__.py
│   │   ├── 0001_initial.py
│   │   └── 0002_movie_poster.py
│   │
│   ├── static/
│   │   └── movies/
│   │       └── style.css
│   │
│   ├── templates/
│   │   └── movies/
│   │       ├── base.html
│   │       ├── movie_list.html
│   │       ├── movie_detail.html
│   │       ├── movie_form.html
│   │       └── movie_confirm_delete.html
│   │
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
│
├── media/
│   └── posters/
│
├── db.sqlite3
├── manage.py
├── README.md
└── requirements.txt
```
Najważniejsze elementy projektu:

- config/ — główna konfiguracja projektu Django.
- config/settings.py — ustawienia projektu, aplikacji, bazy danych, plików statycznych oraz plików media.
- config/urls.py — główna mapa adresów URL projektu.
- movies/ — główna aplikacja odpowiedzialna za katalog filmów.
- movies/models.py — model Movie, czyli struktura danych filmu.
- movies/forms.py — formularz dodawania i edycji filmu wraz z walidacją.
- movies/views.py — logika aplikacji: lista filmów, szczegóły, dodawanie, edycja i usuwanie.
- movies/urls.py — adresy URL aplikacji filmów.
- movies/templates/movies/ — szablony HTML odpowiedzialne za widoki użytkownika.
- movies/static/movies/style.css — plik CSS odpowiedzialny za wygląd aplikacji.
- media/posters/ — folder, w którym zapisywane są plakaty filmów dodane przez formularz.
- db.sqlite3 — lokalna baza danych SQLite.
- requirements.txt — lista bibliotek wymaganych do uruchomienia projektu.

## Dane i pliki media

Dane filmów są przechowywane w lokalnej bazie danych SQLite w pliku db.sqlite3.

Każdy film posiada następujące dane:

- tytuł,
- reżysera,
- ocenę,
- automatycznie generowany slug używany w adresie URL,
- opcjonalny plakat.

Plakaty filmów są obsługiwane przez pole ImageField w modelu Movie. Plik plakatu nie jest zapisywany bezpośrednio w bazie danych. W bazie przechowywana jest jedynie ścieżka do pliku, natomiast sam obraz znajduje się w folderze:

```text
media/posters/ 
```

Przykładowo, jeżeli film posiada plakat whiplash.webp, może on zostać zapisany jako:

```text
media/posters/whiplash.webp 
```

Aplikacja obsługuje dodawanie plakatów dzięki konfiguracji:

- MEDIA_URL i MEDIA_ROOT w pliku config/settings.py,
- obsłudze plików media w pliku config/urls.py,
- polu poster w modelu Movie,
- request.FILES w widokach dodawania i edycji filmu,
- enctype="multipart/form-data" w formularzu HTML.

Plakaty są opcjonalne. Jeżeli film nie posiada plakatu, aplikacja wyświetla informację Brak plakatu.
