print("hello This is a practise flask deployment MACHINE LEARNING MODEL ")

from flask import Flask, render_template, request
import pickle
from pre_process import preprocess_text

app = Flask(__name__)

# Load the trained logistic regression model
with open('models/LRmodel.pkl', 'rb') as f:
    model = pickle.load(f)

# Define a route to render the index.html template
@app.route('/', methods=['GET', 'POST'])
def index():
    sentiment = None
    try:
        if request.method == 'POST':
            # Get the tweet text from the form
            tweet_text = request.form['tweet_text']
            print(tweet_text)
            # Preprocess the tweet text
            processed_text = preprocess_text(tweet_text)
            # Make predictions using the loaded model
            prediction = model.predict([processed_text])[0]
            # Determine the sentiment based on the prediction
            print(prediction)
            sentiment = 'Positive' if prediction == 1 else 'Negative'
            print(sentiment)
    except Exception as e:
        print(f"An error occurred: {e}")
        # Optionally, you can set 'sentiment' to a default error message to display to the user
        sentiment = "An error occurred while processing your request. Please try again."
    return render_template('index.html', sentiment=sentiment ,tweet_text=tweet_text, preprocess_text=preprocess_text)
if __name__ == '__main__':
    app.run(debug=False)
