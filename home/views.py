from django.shortcuts import redirect, render
from django.http.response import HttpResponse
from django.shortcuts import render
# from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
import pickle
import numpy as np
import pandas as pd
import keras


# Create your views here.
def getPrediction(request):
    # load the lstm model
    pickle_in = open('lstmModel.pickle', 'rb')
    properties = pickle.load(pickle_in)

    model = keras.models.load_model("regressor")
    # properties['model']
    scaler = properties['scaler']
    dataPickled = properties['data']

    # start making prediction
    def predictor(day_Range=1):
        # load the past 60 days data
        past_60_data = dataPickled.tail(60)
        # prepare total data if future is to be predicted
        full_data = past_60_data
        predicted_value = []
        for i in range(0, day_Range):
            # scale the data
            inputs = scaler.transform(full_data)
            # create a special data structure
            X_test = []
            X_test.append(inputs[i:60+i])
            X_test = np.array(X_test)
            # predict the value
            Y_pred = model.predict(X_test)
            Y_pred_scaled = scaler.inverse_transform(Y_pred)
            # here y_pred_scaled is a numpy array so we have to concert it to dataframe for
            # concatination
            Y_pred_scaled_dataframe = pd.DataFrame(
                Y_pred_scaled, columns=['High', 'Low', 'Open', 'Close'])
            # update the dataset for next value prediction
            full_data = full_data.append(
                Y_pred_scaled_dataframe, ignore_index=True)
            # store the predicted value
            predicted_value.append(Y_pred_scaled[0])
        return predicted_value
    values = predictor(3)
    return HttpResponse(values)


@login_required(login_url='/account/login/')
def index(request):
    if request.method == 'POST':
        days = request.POST['days']
        # load the lstm model
        pickle_in = open('lstmModel.pickle', 'rb')
        properties = pickle.load(pickle_in)

        model = keras.models.load_model("regressor")
        # properties['model']
        scaler = properties['scaler']
        dataPickled = properties['data']

        # start making prediction
        def predictor(day_Range=1):
            # load the past 60 days data
            past_60_data = dataPickled.tail(60)
            # prepare total data if future is to be predicted
            full_data = past_60_data
            predicted_value = []
            for i in range(0, day_Range):
                # scale the data
                inputs = scaler.transform(full_data)
                # create a special data structure
                X_test = []
                X_test.append(inputs[i:60+i])
                X_test = np.array(X_test)
                # predict the value
                Y_pred = model.predict(X_test)
                Y_pred_scaled = scaler.inverse_transform(Y_pred)
                # here y_pred_scaled is a numpy array so we have to concert it to dataframe for
                # concatination
                Y_pred_scaled_dataframe = pd.DataFrame(
                    Y_pred_scaled, columns=['High', 'Low', 'Open', 'Close'])
                # update the dataset for next value prediction
                full_data = full_data.append(
                    Y_pred_scaled_dataframe, ignore_index=True)
                # store the predicted value
                predicted_value.append(Y_pred_scaled[0])
            return predicted_value
        values = predictor(int(days))
        return render(request, 'index.html', {'values': values})

    return render(request, 'index.html')


def contact(request):
    return render(request, 'contact.html')
