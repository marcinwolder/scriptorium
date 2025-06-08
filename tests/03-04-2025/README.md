# 03-04-2025

#### 1. Przygotować (wstępną) gramatykę Państwa języka w formacie narzędzia do generowania parserów, którego będziecie używać (np. antlr, bison, itp.)

[Gramatyka](/Scriptorium/Scriptorium.g4)

#### 2. Przygotować obsługę podstawowych instrukcji z tworzonego języka (np. poruszanie robotem/żółwiem, itp.) Na razie nie trzeba implementować deklarowania funkcji, pętli, itp. Ma być to minimalistyczna wersja w której da się pisać elementarne programy typu „hello world”. Na tym etapie należy zdecydować czy implementujecie Państwo translator, interpreter czy kompilator. W razie wątpliwości sugeruję wybór interpretera (będzie najlepszy w większości przypadków)

**Zaimplementowano:**

* `scribere` - wypisuje zawartość do konsoli
* `rogare` - wczytuje zawartość z konsoli
* Poprawne działania matematyczne 
* Zapisywanie i odczytywanie zmiennych

#### 3. Przygotować wstępną wersję wizualizująca działanie programu (np. jeśli jest to program typu „logo” to należy dodać rysowanie planszy pokazywanie żółwia na danej pozycji, itp.).

Program działający w konsoli - polecenie `scriptorium`

#### 4. Zaimplementować prostą obsługę błędów syntaktycznych – jeśli program nie jest zgodny z gramatyką języka nie należy próbować go wykonywać tylko poinformować użytkownika, że program jest syntaktycznie niepoprawny (dobrze też poinformować w której linii kodu źródłowego jest błąd – ale ten element nie jest obowiązkowy na tym etapie prac).

[error](/03-04-2025/error.cr7)  
[error2](/03-04-2025/error2.cr7)  
[error3](/03-04-2025/error3.cr7)  

#### 5. Przygotować proste programy typu „hello world” i przetestować czy Państwa interpreter/translator/kompilator działa poprawnie dla tych programów.

[hello_world_1](/03-04-2025/program.cr7)  
[hello_world_2](/03-04-2025/program2.cr7)  
[hello_world_3](/03-04-2025/program3.cr7)  
[zmienne](/03-04-2025/var.cr7)  
[zmienne_2](/03-04-2025/var2.cr7)  
[if](/03-04-2025/if.cr7)  
[while](/03-04-2025/while.cr7)  
[for](/03-04-2025/for.cr7)  
[func](/03-04-2025/func.cr7)   