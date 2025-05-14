# 08-05-2025

### Należy rozszerzyć implementację swojego języka o następujące elementy:

#### 1. Typ numeryczny i co najmniej podstawowe operacje arytmetyczne (dodawanie, odejmowanie, mnożenie, dzielenie, nawiasowanie) na stałych typu numerycznego.

Działający typ numeryczny z podanymi wymaganiami został przygotowany na poprzedni etap.

**Naprawiono błędy**:

* **Przypisywanie zmiennych różnych typów** - teraz można do zmiennych przypisywać różne typy, które są castowane na typ docelowy lub wyrzucają wyjątek
* **Ujednolicono działania matematyczne** na typach `int` i `float` - np. 2 + 2,5

[numeric](./numeric.cr7)  
[numeric2](./numeric2.cr7)  
[numeric3](./numeric3.cr7)  

#### 2. Typ logiczny (`true`/`false`) i co najmniej podstawowe operacje logiczne (`and`, `or`, `not`, nawiasowanie) na  stałych oraz porównywanie stałych typu numerycznego (`<`, `>` , `==`, `!=`) co w wyniku powinno dawać typ logiczny

[veritas](./veritas.cr7)  
[veritas2](./veritas2.cr7)  

#### 3. Obsługa globalnej przestrzeni nazw dla zmiennych (zgodnie z tym, o czym mówiłem na ostatnich ćwiczeniach). Należy zaimplementować 2-przebiegowy proces użycia zmiennych. W pierwszym przebiegu rejestrujemy (np. w mapie/słowniku) deklaracje wszystkich zmiennych wraz z ich typami (w tym przebiegu należy zgłosić błąd jeśli nastąpiła redeklaracja zmiennej). W tym przebiegu wygodnie jest użyć listenera. W drugim przebiegu wykonujemy (podstawowe)  operacje na zmiennych (opisane powyżej w zadaniu - dodawanie, odejmowanie, itd.). W tym przebiegu należy zgłosić błąd jeśli użyta zmienna nie została zarejestrowana (w globalnej przestrzeni zmiennych).