# 29-04-2025

### Należy rozszerzyć implementację swojego języka o następujące elementy:

#### Typ numeryczny i co najmniej podstawowe operacje arytmetyczne (dodawanie, odejmowanie, mnożenie, dzielenie, nawiasowanie) na stałych typu numerycznego.

#### Typ logiczny (`true`/`false`) i co najmniej podstawowe operacje logiczne (`and`, `or`, `not`, nawiasowanie) na  stałych oraz porównywanie stałych typu numerycznego (`<`, `>` , `==`, `!=`) co w wyniku powinno dawać typ logiczny

#### Obsługa globalnej przestrzeni nazw dla zmiennych (zgodnie z tym, o czym mówiłem na ostatnich ćwiczeniach). Należy zaimplementować 2-przebiegowy proces użycia zmiennych. W pierwszym przebiegu rejestrujemy (np. w mapie/słowniku) deklaracje wszystkich zmiennych wraz z ich typami (w tym przebiegu należy zgłosić błąd jeśli nastąpiła redeklaracja zmiennej). W tym przebiegu wygodnie jest użyć listenera. W drugim przebiegu wykonujemy (podstawowe)  operacje na zmiennych (opisane powyżej w zadaniu - dodawanie, odejmowanie, itd.). W tym przebiegu należy zgłosić błąd jeśli użyta zmienna nie została zarejestrowana (w globalnej przestrzeni zmiennych).