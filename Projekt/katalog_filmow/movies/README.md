# Katalog kolekcji filmów

## Spis treści

1. [Opis projektu](#opis-projektu)
2. [Zastosowany wzorzec MVC](#zastosowany-wzorzec-mvc)
3. [Funkcjonalności](#funkcjonalności)
4. [Technologie](#technologie)
5. [Instrukcja uruchomienia](#instrukcja-uruchomienia)
6. [Struktura projektu](#struktura-projektu)
7. [Autor](#autor)

---

## Opis projektu

Projekt **Katalog kolekcji filmów** jest aplikacją webową stworzoną w języku Python z użyciem frameworka Django.

Aplikacja umożliwia zarządzanie prostą kolekcją filmów. Każdy film posiada tytuł, reżysera oraz ocenę. Projekt został wykonany zgodnie z założeniami zadania 12, w którym wymagany model zawiera pola: tytuł, reżyser i ocena.

Projekt realizuje podstawowe operacje na danych oraz wykorzystuje wzorzec architektoniczny MVC.

---

## Zastosowany wzorzec MVC

Projekt został wykonany zgodnie z architekturą MVC.

W projekcie Django poszczególne elementy odpowiadają następującym częściom wzorca:

### Model

Model znajduje się w pliku:

```text
movies/models.py