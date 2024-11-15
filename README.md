# Zadanie rekrutacyjne Oxido

Projekt we Flask pobierający treść artykułu i generujący odpowiednio
sformatowany kod HTML z pomocą OpenAI API.

## Plik wygenerowany przez AI:

[Zobacz plik z artykułem](./files/artykul.html)

## Instalacja

W wieszu polecenia / terminalu wprowadź poniższe komendy:

### Krok 1: Sklonowanie repozytorium

```sh
git clone https://github.com/pr3ston1989/oxido.git
cd oxido
```

### Krok 2: Utworzenie środowiska wirtualnego i instalacja zależności

#### Windows:

```sh
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

#### Linux: 

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Krok 3: Ustawienie zmiennej środowiskowej dla klucza API

Zamień klucz_api na swój klucz i uruchom polecenie.

#### Windows:

```sh
set API_KEY="klucz_api"
```

#### Linux: 

```bash
export API_KEY="klucz_api"
```

Opcjonalnie można umieścić klucz API w pliku .env w formacie API_KEY=klucz_api.

Plik musi znajdować się w katalogu głównym projektu.

### Krok 4: Uruchomienie aplikacji

```sh
flask run
```

Aplikacja domyślnie działa na porcie 5000 i będzie dostępna pod [tym](http://127.0.0.1:5000/) adresem.