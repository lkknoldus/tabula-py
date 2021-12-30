import os
import pandas as pd
import numpy as np
import dill as pickle
import string
import json
from flask import Flask, jsonify, request
app = Flask(__name__)


@app.route('/predict', methods=['POST'])


def apicall():
            """Pandas dataframe will sent as a payload to API Call"""
            try:
                        test_json = json.dumps(request.get_json())
                        print (test_json)


                        test = pd.read_json(test_json, orient='records')
                        print(test)


            except Exception as e:


                        raise e
                        clf = 'example_model.pk'


            if test.empty:
                        return(bad_request())


            else:
                        #Load the saved model
                        print("Loading the model...")
                        loaded_model = None
                        with open('/home/webonise/flask-app/models/'+clf,'rb') as f:
                                    loaded_model = pickle.load(f)


                        print("The model has been loaded...doing predictions now...")
                        prediction = loaded_model.predict(test)


                        pre_df=pd.DataFrame(np.array(prediction))


                        with app.app_context():


                                    responses = jsonify(pre_df.to_json(orient="records"))


                        responses.status_code = 200


                        return (responses)


@app.errorhandler(400)


def bad_request(error=None):


            message = {
            'status': 400, 'message': 'Bad Request: ' + request.url + '--> Please check your data payload...',
            }


            resp = jsonify(message)
            resp.status_code = 400


            return (resp)