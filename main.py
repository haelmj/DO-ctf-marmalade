from pydictionary import Dictionary
from flask import Flask, render_template, render_template_string, request, abort
import os

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():

    if request.method == 'POST':
        word = request.form['word']
        template = """
        <!DOCTYPE html><html lang="en">
        <head>
            <meta charset="UTF-8">
            <title>Marmalade</title>
        </head>
        <body>
            <h1>Welcome to Michael's dictionary!</h1>
            <form action="/", method="POST">
                <input type="text" name="word" placeholder="Enter a word">
                <button type="submit" value="Search">Search</button>
            </form>
                <p>Showing definition for: """ + word + """</p>
            
            {% if definitions %}
                <ul>
                    {% for definition in definitions %}
                        <li>{{ definition }}</li>
                    {% endfor %}
                </ul>
            {% else %}
                <p>No definitions found for found!</p>
            {% endif %}
        </body>
        </html>
            """
        dict = Dictionary(word)
        print(dict.meanings())
        definition = dict.meanings()
        bad_chars = "#;[]"
        if any(char in bad_chars for char in word):
            abort(403)
        return render_template_string(template, word=word,definitions=definition)
    return render_template('index.html', word="", definition="")


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 8080))
    app.run(debug=True, host='0.0.0.0', port=port)