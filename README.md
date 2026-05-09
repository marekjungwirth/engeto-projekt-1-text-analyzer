# Projekt 1: Textový analyzátor

Tento projekt je jednoduchý textový analyzátor napsaný v Pythonu. Program si nejprve vyžádá přihlašovací údaje uživatele a po úspěšném ověření mu umožní analyzovat jeden ze tří předpřipravených textů.

## Funkce programu
* **Ověření uživatele:** Přístup je povolen pouze registrovaným uživatelům po zadání správného jména a hesla.
* **Analýza textu:** Program u vybraného textu spočítá a vypíše:
  * Celkový počet slov.
  * Počet slov začínajících velkým písmenem (Titlecase).
  * Počet slov psaných pouze velkými písmeny (Uppercase).
  * Počet slov psaných pouze malými písmeny (Lowercase).
  * Počet čísel (numerických řetězců) a jejich celkový součet.
* **Sloupcový graf:** Program v terminálu vygeneruje jednoduchý textový graf pomocí hvězdiček, který vizuálně reprezentuje četnost jednotlivých délek slov v textu.

## Jak program spustit
Skript stačí spustit z terminálu. Nejsou vyžadovány žádné externí knihovny, program využívá pouze standardní funkce Pythonu.

```bash
python3 main.py
```

## Registrovaní uživatelé
Pro testování programu jsou k dispozici následující přístupové údaje (uživatel: heslo):
* `bob`: `123`
* `ann`: `pass123`
* `mike`: `password123`
* `liz`: `pass123`