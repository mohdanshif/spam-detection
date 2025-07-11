from flask import Flask, request, render_template
import pickle

app = Flask(__name__)

# load model
with open('spam_classifier.pkl', 'rb') as f:
    model = pickle.load(f)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        message = request.form['message']
        prediction = model.predict([message])[0]
        return render_template('index.html', message=message, prediction=prediction)

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000,debug=True)

