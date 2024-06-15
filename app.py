from flask import Flask,request,render_template
import numpy as np
import pandas as pd
from Abalone_Age_Prediction.pipeline.predict import CustomData,PredictPipeline

application = Flask(__name__) #it gives us the entry point

app = application

## Route for a home page

#@app.route('/')
#def index():
#    return render_template('index.html')

#@app.route('/predictdata', methods = ['GET', 'POST'])
@app.route('/', methods = ['GET', 'POST'])
def predict_datapoint():
    if request.method == 'GET':
        return render_template('index.html')
    else:
        data=CustomData(
            Sex=request.form.get('Sex'),
            Length=request.form.get('Length'),
            Diameter=request.form.get('Diameter'),
            Height=request.form.get('Height'),
            Whole_weight=request.form.get('Whole weight'),
            Shucked_weight=float(request.form.get('Shucked weight')),
            Viscera_weight=float(request.form.get('Viscera weight')),
            Shell_weight=float(request.form.get('Shell weight'))

        )
        pred_df=data.get_data_as_data_frame()
        print(pred_df)
        predict_pipeline = PredictPipeline()
        results = predict_pipeline.predict(pred_df) # i need a predict_pipeline because i can scale properly the data
                                            # and perform all neded operations
        pred_df["Rings"] = round(results[0],2)                                
        print(pred_df)
        return render_template('index.html', results = round(results[0]))

if __name__ =="__main__":
    app.run(host = "0.0.0.0")