from flask import Flask, render_template, request
import wolframalpha

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    answer = None
    if request.method == 'POST':
        question = request.form['question']

        # Your Wolfram Alpha App ID
        app_id = "497HRL-9KK6HYR33X"

        # Initialize Wolfram Alpha client
        client = wolframalpha.Client(app_id)

        # Query Wolfram Alpha
        res = client.query(question)

        # Get the first result as text
        answer = next(res.results).text

    return render_template('index.html', answer=answer)

if __name__ == '__main__':
    app.run(debug=True)
