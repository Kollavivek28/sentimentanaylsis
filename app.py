from flask import Flask, render_template, request, jsonify
from textblob import TextBlob
import nltk

app = Flask(__name__)
nltk.download('punkt')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    lines = request.json['text']
    results = []

    for line in lines:
        blob = TextBlob(line)
        polarity = round(blob.sentiment.polarity, 2)
        subjectivity = round(blob.sentiment.subjectivity, 2)

        if polarity > 0:
            sentiment = 'Positive'
        elif polarity < 0:
            sentiment = 'Negative'
        else:
            sentiment = 'Neutral'

        results.append({
            'original': line,
            'sentiment': sentiment,
            'polarity': polarity,
            'subjectivity': subjectivity
        })

    return jsonify(results)

 if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

