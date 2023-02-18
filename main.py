from flask import Flask, request, jsonify, redirect, render_template
from flask_cors import CORS
import pickle
import numpy as np

app=Flask(__name__, template_folder='templates')
CORS(app)

@app.route("/")
def root():
    return "Root of api."

@app.route("/home")
def home():
    return render_template("index.html")

@app.route("/predict_house_price", methods=["POST"])
def california_house_price():
    try:
        ## Loading Model
        regmodel = pickle.load(open('ml/regmodel.pkl', 'rb'))

        ## Loading scaler for transformation
        scaler = pickle.load(open('ml/scaler.pkl', 'rb'))

        data = [ float(x) for x in request.json.values()]
        
        final_input = scaler.transform(np.array(data).reshape(1, -1))
        print(final_input)
        output = regmodel.predict(final_input)[0]
        return {"result": round(output,2)}

    except Exception as Error:
        print(Error)
        return {"Error": str(Error)}
    
# {
#     "MedInc":1111.0,
#     "HouseAge" : 11.0,
#     "AveRooms" : 11.0,
#     "AveBedrms" : 11.0,
#     "Population" : 11.0,
#     "AveOccup" : 11.0,
#     "Latitude" : 11.0,
#     "Longitude" : 11.0
# }

if __name__ == "__main__":
    app.run(debug=False,
    host='0.0.0.0',
    port=10000)
