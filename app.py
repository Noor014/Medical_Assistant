from flask import Flask, render_template,request,redirect,url_for,session
import pickle

app = Flask(__name__)

#load the model
model = pickle.load(open('disease_pred_LogisticModel.sav', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():


if __name__ == '__main__':
    app.run(debug=True)
