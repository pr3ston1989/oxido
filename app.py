from flask import Flask, render_template
from dotenv import load_dotenv
import requests


article_url = 'https://cdn.oxido.pl/hr/Zadanie%20dla%20JJunior%20AI%20Developera%20-%20tresc%20artykulu.txt'

ai_prompt = '''create html with proper tags to paste into body,
            correct text, place img tags with captions and with
            polish prompts in alt attributes to create accurate images,
            as src leave "image_placeholder.jpg"'''

def load_article_data():
    response = requests.get(article_url)
    response.raise_for_status()
    content = response.text
    return content

load_dotenv()

# app = Flask(__name__)


# @app.route("/")
# def home():
#     data = load_article_data()
#     """Ścieżka do strony głównej - wyświetla stronę ze sformatowanym artykułem."""
#     print(data)
#     return render_template("index.html", data=data)


# if __name__ == "__main__":
#     app.run(host="0.0.0.0", port=5000)

print(load_article_data())