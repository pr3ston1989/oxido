from flask import Flask, render_template
from dotenv import load_dotenv
import requests
from openai import OpenAI
import os

article_url = 'https://cdn.oxido.pl/hr/Zadanie%20dla%20JJunior%20AI%20Developera%20-%20tresc%20artykulu.txt'

# Prompt z instrukcjami dotyczącymi edycji treści artykułu.
ai_prompt = '''create article with proper tags,
            fix encoding, in suitable spots place img tags with captions and with
            polish prompts in alt attributes to create accurate images,
            as src leave "image_placeholder.jpg" for text below,
            create only html after <body> and before </body>:'''

def load_article_data():
    """Funkcja wczytuje plik z linku i zwraca treść w formie stringu."""
    response = requests.get(article_url)
    response.raise_for_status()
    content = response.text
    return content

load_dotenv()
# Wczytanie zmiennej środowiskowej zawierającej klucz API do OpenAI
API_KEY = os.getenv('API_KEY')

client = OpenAI(api_key=API_KEY)


def create_article(prompt, content):
    """
    Funkcja przekazująca prompt wraz z treścią artykułu do OpenAI API
    w celu wygenerowania gotowego kodu HTML.
    """
    article_html = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": f"{prompt} {content}"},
        ],
        )
    return article_html.choices[0].message.content

def save_as_html(data):
    """Funkcja zapisująca kod HTML z artykułem do pliku."""
    with open("./files/artykul.html", "w", encoding="utf-8") as file:
        file.write(data)


app = Flask(__name__)

article_data = load_article_data()
# Zapisanie treści do zmiennej i usunięcie backticków z danych zwróconych przez API.
article = create_article(ai_prompt, article_data).removeprefix("```html")[:-3]
save_as_html(article)

@app.route("/")
def home():
    """Ścieżka do strony głównej - wyświetla stronę ze sformatowanym artykułem."""
    return render_template("szablon.html", data=article)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

