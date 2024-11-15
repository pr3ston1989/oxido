from flask import Flask, render_template
from dotenv import load_dotenv
import requests
import openai
from openai import OpenAI
import os

article_url = 'https://cdn.oxido.pl/hr/Zadanie%20dla%20JJunior%20AI%20Developera%20-%20tresc%20artykulu.txt'

ai_prompt = '''create article with proper tags ready to paste between body tags,
            nothing more, fix encoding, place img tags with captions and with
            polish prompts in alt attributes to create accurate images,
            as src leave "image_placeholder.jpg" for text below:'''

def load_article_data():
    response = requests.get(article_url)
    response.raise_for_status()
    content = response.text
    return content

load_dotenv()
API_KEY = os.getenv('API_KEY')
client = OpenAI(api_key=API_KEY)


def create_article(prompt, content):
    article_html = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": f"{prompt} {content}"},
        ],
        )
    return article_html.choices[0].message.content

def save_as_html(data):
    with open("./files/artykul.html", "w", encoding="utf-8") as file:
        file.write(data)


app = Flask(__name__)


@app.route("/")
def home():
    """Ścieżka do strony głównej - wyświetla stronę ze sformatowanym artykułem."""
    article_data = load_article_data()
    article = create_article(ai_prompt, article_data)
    save_as_html(article)
    return render_template("index.html", data=article)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

