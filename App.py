from flask import Flask, render_template, request
import pickle
from sklearn.preprocessing import Normalizer, LabelEncoder, MinMaxScaler, StandardScaler
from keras.models import Sequential
from keras.layers import Dense, Flatten, Dropout, BatchNormalization, Activation
import tensorflow as tf

app = Flask(__name__)

def matrix_prediction(parameters):
    model = pickle.load(open('model2.pkl', 'rb'))
    pred = model.predict([parameters])
    return pred

@app.route('/', methods=['POST', 'GET'])
def matrix_form():
    message = ''
    if request.method == 'POST':
        parameters_list = ('dens', 'elast', 'hard', 'epoxy', 'temp', 'surf', 'mod', 'tens', 'tar', 'angle', 'step', 'denn')
        parameters = []
        for i in parameters_list:
            entry = request.form.get(i)
            parameters.append(entry)
        parameters = [float(i.replace(',', '.')) for i in parameters]

        message = f'Рекомендуемое cоотношение: {matrix_prediction(parameters)}'
    return render_template('index.html', message=message)

if __name__ == "__main__":
    app.run(debug=True)







