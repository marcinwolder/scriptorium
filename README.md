# 🪶 Scriptorium

Scriptorium to autorski, eksperymentalny język programowania inspirowany składnią języków imperatywnych (takich jak Python czy C), wyposażony w własny parser, leksykalizator oraz interpreter oparty na ANTLR4. Obsługuje zmienne, funkcje (z rekurencją), pętle i kontrolę przepływu. Projekt służy jako baza do nauki budowy języków programowania, analiz składniowych i semantycznych, a także jako narzędzie dydaktyczne.

---

## 📦 Instalacja i konfiguracja

### ⚙ Wymagania systemowe

- Python **3.13**
- System: Windows, Linux lub macOS
- Java (wymagany przez ANTLR): min. Java 8

---

### 📚 Instalacja zależności

1. **Utwórz środowisko wirtualne** (rekomendowane):

```bash
py -3.13 -m venv venv
source venv/Scripts/activate       # Windows
# lub
source venv/bin/activate           # Linux/macOS
````

2. **Zainstaluj wymagane moduły**:

```bash
pip install -r requirements.txt
```

> 📄 Upewnij się, że plik `requirements.txt` zawiera:
>
> * `antlr4-tools`
> * `antlr4-python3-runtime`
> * `antlr-denter`

---

### 🛠️ Kompilacja gramatyki ANTLR

Parser i visitor są generowane z pliku gramatyki `Scriptorium.g4`. Aby zbudować projekt:

```bash
cd ./Scriptorium
antlr4 ./Scriptorium.g4 -visitor -Dlanguage=Python3
```

Po tej operacji w folderze powinny pojawić się pliki:

* `ScriptoriumParser.py`
* `ScriptoriumLexer.py`
* `ScriptoriumVisitor.py`
* `ScriptoriumListener.py`

---

### 🎮 Uruchomienie programu

1. Stwórz plik źródłowy w języku Scriptorium z rozszerzeniem `.cr7`:

```bash
touch hello.cr7
```

2. W katalogu głównym uruchom interpreter:

```bash
python main.py hello.cr7
```

---

### 🧪 Przykładowa sesja

```bash
$ python main.py hello.cr7
CULPA: linea 1:18 - missing NL at 'numerus'
```

---

### 🧰 Narzędzia developerskie

Jeśli używasz edytora kodu jak VSCode, możesz skorzystać z rozszerzeń do:

* Obsługi składni `.g4` (ANTLR)
* Obsługi środowisk `venv`
* Debuggera dla Pythona

---

### 🔧 Problemy i debugowanie

* Jeśli nie masz polecenia `antlr4` w terminalu, dodaj ANTLR do zmiennych środowiskowych.
* Upewnij się, że Twoja wersja Javy jest aktualna (`java -version`).
* Jeśli ANTLR generuje pliki do innego folderu — użyj flagi `-o .` w komendzie:

```bash
antlr4 -Dlanguage=Python3 -visitor -o . Scriptorium.g4
```

---

Gotowe! Teraz możesz pisać programy w `.cr7` i uruchamiać je za pomocą własnego interpretera 🎉


## 🧾 Składnia i podstawy

Scriptorium to eksperymentalny język programowania inspirowany klasyczną łaciną. Używa pełnych słów jako operatorów i struktur kontrolnych. Bazuje na wcięciach (podobnie jak Python), wspiera funkcje, warunki, pętle oraz typowanie statyczne.

---

### 📌 Zmienne

Zmienne deklaruje się za pomocą typu (`numerus`, `fractio`, `veritas`, `sententia`) i słowa kluczowego `esto`:

```cr7
numerus a esto 10.
sententia powitanie esto "salve".
````

Deklaracja bez przypisania:

```cr7
fractio zmienna.
```

---

### 📌 Wypisywanie

Służy do tego słowo kluczowe `scribere`. Można łączyć wiele wartości za pomocą `et`:

```cr7
scribere "Wynik: " et a et ".".
```

---

### 📌 Funkcje

Funkcje definiujemy przez `munus`, podając typ zwracany, nazwę, parametry i blok działań:

```cr7
numerus munus suma(numerus a, numerus b):
    reddere a adde b.
```

Wywołanie funkcji:

```cr7
numerus wynik esto suma(5, 10).
```

---

### 📌 Warunki

Instrukcja warunkowa `si`, opcjonalnie `aliter si`, zakończona `aliter`.

```cr7
si a aequalis 10:
    scribere "Dziesięć.".
aliter si a minor quam 10:
    scribere "Mniej niż dziesięć.".
aliter:
    scribere "Więcej niż dziesięć.".
```

---

### 📌 Pętle

#### 🔁 `repetere` — pętla `for`

```cr7
repetere i ex 1 ad 5:
    scribere i.
```

#### 🔁 `dum` — pętla `while`

```cr7
dum a minor quam 100:
    a esto a adde 1.
```

---

### 📌 Operatory

Operatory w Scriptorium to pełne słowa:

#### Arytmetyczne

| Symboliczny | Scriptorium  |
| ----------- | ------------ |
| `+`         | `adde`       |
| `-`         | `minue`      |
| `*`         | `multiplica` |
| `/`         | `divide`     |
| `//`        | `totum`      |
| `%`         | `residuum`   |
| `^`         | `potentia`   |

#### Porównania

| Symboliczny | Scriptorium      |
| ----------- | ---------------- |
| `==`        | `aequalis`       |
| `!=`        | `inaequale`      |
| `<`         | `minor quam`     |
| `<=`        | `minor aequalis` |
| `>`         | `maior quam`     |
| `>=`        | `maior aequalis` |

#### Logiczne

| Symboliczny | Scriptorium |    |       |
| ----------- | ----------- | -- | ----- |
| `&&`        | `etiam`     |    |       |
| \`          |             | \` | `aut` |
| `!`         | `non`       |    |       |

---

### 📌 Specjalne instrukcje

* `culpa`: wypisanie błędu

```cr7
culpa "To nie powinno się wydarzyć!".
```

* `reddere`: zwraca wartość z funkcji
* `exire`: przerywa pętlę (`break`)
* `perge`: kontynuuje kolejną iterację (`continue`)
* `rogare`: pobiera dane od użytkownika (input)

---

### 📌 Komentarze

Komentarze jednoliniowe rozpoczynają się od `//`:

```cr7
// To jest komentarz
numerus x esto 10.
```


## 🧩 Struktury danych

Scriptorium wspiera **statycznie typowane** zmienne czterech głównych typów danych oraz wartość pustą `nihil`.

---

### 📦 Typy danych

| Typ           | Słowo kluczowe | Przykład              | Opis                        |
|---------------|----------------|------------------------|-----------------------------|
| Liczba całkowita   | `numerus`      | `numerus a esto 10.`     | Odpowiada typowi `int`     |
| Liczba zmiennoprzecinkowa | `fractio`     | `fractio x esto 3,14.`   | Używa przecinka zamiast kropki |
| Łańcuch znaków | `sententia`   | `sententia s esto "hej".`| Typ tekstowy (`string`)     |
| Wartość logiczna | `veritas`     | `veritas v esto verum.`  | `verum` lub `falsum`        |
| Wartość pusta | `nihil`        | `nihil munus brak(): ...`| Odpowiednik `None` / `void` |

---

### 🧮 Przypisanie wartości

Zmienne przypisuje się za pomocą `esto`:

```cr7
numerus wiek esto 25.
fractio pi esto 3,14.
sententia powitanie esto "salve!".
veritas aktywne esto verum.
````

---

### 🔄 Dynamiczna wartość, statyczny typ

Typ zmiennej jest **ustalany w momencie deklaracji** i nie może zostać zmieniony. Przykład niepoprawny:

```cr7
numerus x esto 5.
x esto "pięć".  // ❌ Błąd – typ `sententia` niezgodny z `numerus`
```

---

### 📥 Wczytywanie danych

Można używać `rogare` do wczytywania danych użytkownika. Wynik to zawsze `sententia`.

```cr7
sententia imie esto rogare "Podaj imię: ".
```

---

### 🔀 Konwersje (jawne)

Obecnie język nie obsługuje rzutowania typów bezpośrednio w kodzie – wszystkie konwersje należy przeprowadzać jawnie po stronie interpretera.

---

### 🔐 Zakres zmiennych

Zmienne są widoczne tylko w **najbliższym bloku** (`if`, `for`, `munus` itd.). Dostęp do zmiennych z wyższych poziomów odbywa się zgodnie z zasadą zagnieżdżonego zasięgu.

```cr7
numerus globalna esto 5.

munus test():
    scribere globalna.  // ✔ dostęp do zmiennej wyżej
```

---

### 🧠 Zmienna funkcyjna (`munus` jako obiekt)

Funkcje w Scriptorium są reprezentowane jako zmienne typu `FuncVar` (wewnętrznie). Można je wywoływać tak samo jak zmienne:

```cr7
numerus munus dodaj(numerus a, numerus b):
    reddere a adde b.

numerus wynik esto dodaj(1, 2).
```

---


## 🛑 Obsługa błędów i komunikaty

Scriptorium został zaprojektowany tak, aby maksymalnie ułatwić wykrywanie i diagnozowanie błędów składniowych oraz semantycznych. Błędy są zgłaszane w sposób jasny i precyzyjny, ze wskazaniem miejsca problemu w kodzie.

---

### ⚠️ Rodzaje błędów

1. **Błędy składniowe (SyntaxError)**  
   Wykrywane podczas analizy kodu przez parser.  
   Przykłady komunikatów:
   - `CULPA: linea 3:5 - syntax error at 'esto'`  
     (np. niepoprawne użycie słowa kluczowego lub operatora)
   - `CULPA: linea 5:10 - missing (")`  
     (niezamknięty łańcuch znaków)
   - `CULPA: linea 7:1 - incomplete or incorrect sentence`  
     (np. brakujący element w konstrukcji językowej)

2. **Błędy semantyczne**  
   Wykrywane podczas analizy zmiennych i funkcji w czasie parsowania (z użyciem `VariableListener`).  
   Przykłady:
   - `CULPA: linea 4:0 - multiple variable or function "x" declaration (delcared in 2:0)`  
     (powtórna deklaracja zmiennej lub funkcji o tej samej nazwie w tym samym zakresie)
   - `CULPA: linea 8:3 - no variable named "y"`  
     (użycie niezadeklarowanej zmiennej)

3. **Błędy wykonania (runtime errors)**  
   Aktualnie język nie wspiera zaawansowanych mechanizmów wyjątków, ale błędy takie jak dzielenie przez zero lub inne nieprawidłowe operacje powinny być obsłużone przez interpreter (w ramach rozszerzeń).

---

### 💬 Format komunikatu błędu

```

CULPA: linea <linia>:<kolumna> - \<opis błędu>

````

- `CULPA` — prefiks oznaczający błąd (łac. "wina").
- `linea <linia>:<kolumna>` — miejsce wystąpienia błędu w pliku źródłowym.
- `<opis błędu>` — krótki opis problemu.

---

### ⚙️ Mechanizm wykrywania błędów

- Parser i lexer korzystają ze specjalnego `ErrorListener` (rozszerzenie `antlr4`), który przechwytuje i formatuje błędy składniowe.
- Podczas parsowania słuchacz `VariableListener` buduje mapę zmiennych i funkcji, zgłaszając konflikty deklaracji lub odwołań do nieistniejących nazw.
- W `main.py` wszystkie wyjątki są łapane i wyświetlane, co umożliwia łatwe debugowanie.

---

### 📝 Przykład błędu

Kod źródłowy:

```cr7
numerus x esto 5.
numerus x esto 10.  // próba podwójnej deklaracji
````

Wynik działania interpretera:

```
CULPA: linea 2:0 - multiple variable or function "x" declaration (delcared in 1:0)
```

---

### 🔧 Wskazówki

* Dbaj o unikalność nazw zmiennych i funkcji w ramach tego samego zakresu (funkcji, pętli, bloku `if`).
* Zwracaj uwagę na poprawne zakończenie instrukcji kropką `.`.
* Sprawdzaj dokładnie format i zamknięcie łańcuchów znaków.
* W przypadku błędów składniowych zwróć uwagę na podany przez parser token, który sprawia problem.

---

## 🏗️ Architektura projektu

Projekt interpreter języka Scriptorium jest podzielony na kilka kluczowych komponentów, które współpracują, by zrealizować proces interpretacji kodu źródłowego w języku Scriptorium (z rozszerzeniem `.cr7`).

---

### 🧩 Główne moduły

| Komponent              | Opis                                                                                   |
|-----------------------|----------------------------------------------------------------------------------------|
| **`Scriptorium.g4`**   | Plik z gramatyką języka — zawiera reguły parsera i lexer, definiuje składnię i tokeny. |
| **`main.py`**          | Punkt startowy interpretera. Ładuje plik `.cr7`, inicjuje parser i odwiedzacza (visitor).|
| **`visitor.py`**       | Implementacja odwiedzacza (`Visitor`), który przechodzi po drzewie składniowym i interpretuje kod. |
| **`var.py`**           | Definicje klas zmiennych (`Var`, `FuncVar`, `ParamVar`) oraz mechanizmy zarządzania zakresami i wartościami. |
| **`VariableListener.py`** | Słuchacz (listener) budujący mapę zmiennych i funkcji oraz wykrywający błędy deklaracji. |
| **`requirements.txt`** | Lista wymaganych bibliotek i narzędzi (np. `antlr4-python3-runtime`, `antlr4-tools`, `antlr-denter`). |

---

### 🔄 Przepływ działania interpretera

1. **Wczytanie kodu**  
   Interpreter wczytuje plik `.cr7` z kodem źródłowym.

2. **Tokenizacja i parsowanie**  
   - Lexer generuje tokeny na podstawie reguł z `Scriptorium.g4`.  
   - Parser buduje drzewo składniowe (AST) zgodnie z gramatyką.

3. **Analiza zmiennych i funkcji (VariableListener)**  
   - Listener przechodzi po drzewie i tworzy mapę zmiennych i funkcji wraz z ich zakresami.  
   - Sprawdza poprawność deklaracji i zgłasza błędy.

4. **Interpretacja kodu (Visitor)**  
   - Odwiedzacz przechodzi po AST, wykonując instrukcje, obliczając wyrażenia, wywołując funkcje itd.  
   - Zarządza stanem programu, np. wartościami zmiennych, poziomem rekurencji funkcji.

5. **Wyświetlanie wyników i obsługa błędów**  
   - Interpreter wypisuje wyniki komend `scribere` (print).  
   - Błędy są wychwytywane i zgłaszane w czytelnej formie.

---

### 📁 Struktura katalogów (przykład)

```

/Scriptorium
│
├── main.py
├── visitor.py
├── var.py
├── VariableListener.py
├── Scriptorium.g4
├── requirements.txt
└── README.md

```

---

### 🛠️ Narzędzia i biblioteki

- **ANTLR4** — generowanie lexerów i parserów z pliku `.g4`.
- **antlr4-python3-runtime** — runtime do obsługi parsera w Pythonie.
- **antlr-denter** — rozszerzenie lexer'a do obsługi wcięć (indent/dedent) w stylu Pythona.
- **Python 3.13** — środowisko uruchomieniowe.

---

## FAQ — Najczęściej zadawane pytania

### 1. Jakiego rozszerzenia plików używa język Scriptorium?  
Pliki źródłowe języka Scriptorium mają rozszerzenie `.cr7`.

### 2. Jak uruchomić program napisany w Scriptorium?  
Po stworzeniu pliku `.cr7`, uruchom interpreter poleceniem:  
```bash
py main.py program.cr7
````

### 3. Co zrobić, gdy pojawia się błąd składniowy z komunikatem zaczynającym się od "CULPA"?

To jest spersonalizowany komunikat błędu składniowego w naszym języku.
Sprawdź podaną linię i kolumnę w pliku, aby zobaczyć, gdzie jest problem.
Przykładowo:

```
CULPA: linea 5:10 - syntax error at 'ad'  
```

oznacza, że na linii 5, kolumnie 10 jest błąd składniowy związany z tokenem `'ad'`.

### 4. Czy Scriptorium obsługuje programowanie obiektowe lub moduły?

Obecnie Scriptorium jest językiem proceduralnym bez wsparcia dla OOP, modułów czy bibliotek zewnętrznych.

### 5. Jak obsługiwać zmienne i typy danych?

Deklarujesz zmienne podając typ przed nazwą, np.:

```
numerus x.
```

lub z definicją:

```
numerus x esto 5.
```

Dostępne typy to: `numerus` (int), `fractio` (float), `sententia` (string), `veritas` (bool) oraz `nihil` (null).

### 6. Jak definiować i wywoływać funkcje?

Funkcje definiujesz słowem kluczowym `munus`, np.:

```
numerus munus suma(numerus a, numerus b):
    scribere a ad b.
```

Wywołujesz funkcje przez nazwę i nawiasy:

```
suma(3, 5).
```

### 7. Jak działają pętle i instrukcje warunkowe?

* Pętla `dum` (while)
* Pętla `repetere` (for)
* Instrukcje warunkowe `si`, `aliter si`, `aliter`

Przykład:

```
si x maior quam 0:
    scribere "Dodatni".
aliter:
    scribere "Niedodatni".
```

### 8. Czy jest wsparcie dla obsługi błędów?

Tak, interpreter wychwytuje błędy składniowe i semantyczne, które są raportowane z precyzyjną lokalizacją w kodzie.

### 9. Jak dodać nowe funkcjonalności lub zgłosić błąd?

Prosimy o zgłoszenie issue na GitHub lub kontakt mailowy (adres w dokumentacji projektu).

---

Jeśli masz inne pytania, zajrzyj do dokumentacji lub skontaktuj się z nami!


## Podsumowanie

Scriptorium to prosty, proceduralny język programowania stworzony z myślą o edukacji i szybkim prototypowaniu. Dzięki czytelnej składni inspirowanej łaciną i precyzyjnej obsłudze błędów, użytkownik szybko zidentyfikuje i poprawi problemy w kodzie.  

Projekt opiera się na ANTLR4 oraz Pythonie 3.13, co zapewnia łatwą rozbudowę i integrację.  
Wprowadzenie podstawowych typów danych, funkcji, pętli oraz warunków pozwala na tworzenie czytelnych i zrozumiałych programów.

Mamy nadzieję, że dokumentacja ułatwi Ci rozpoczęcie pracy z Scriptorium i sprawi, że tworzenie programów będzie przyjemnością.

Zapraszamy do eksperymentowania i rozwijania języka!
