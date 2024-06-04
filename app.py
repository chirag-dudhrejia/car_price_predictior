from flask import Flask, render_template, request
import pandas as pd
import pickle

car_data = pd.read_csv("cars24_cleaned.csv")
model = pickle.load(open("CarLinearRegressionModel.pkl", "rb"))

app = Flask(__name__)


@app.route("/")
def home():
    car_names = sorted(car_data["Car_name"].unique())
    years = sorted(car_data["Year"].unique())
    distance = sorted(car_data["Distance"].unique())
    fuel_type = car_data["Fuel_type"].unique()
    drive = car_data["Drive"].unique()
    return render_template("index.html",
                           car_names=car_names,
                           years=years,
                           distance=distance,
                           fuel_type=fuel_type,
                           drive=drive)


@app.route("/performing_prediction", methods=["POST"])
def perform_prediction():
    values = request.form
    # company = values["company"]
    car_model = values["car_model"]
    year = int(values["year"])
    fuel = values["fuel_type"]
    drive = values["drive"]
    kms_driven = values["km_travelled"]
    # print(company, car_model, year, fuel, kms_driven)
    prediction = model.predict(pd.DataFrame(data=[[car_model, year, kms_driven, fuel, drive]],
                                            columns=["Car_name", "Year", "Distance", "Fuel_type", "Drive"]))
    prediction = round(prediction[0])
    return render_template("index.html", prediction=prediction)


if __name__ == "__main__":
    app.run(debug=True)