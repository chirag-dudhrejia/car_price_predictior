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
    # all_data_list = get_all_data()
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

    prediction = model.predict(pd.DataFrame(data=[[car_model, year, kms_driven, fuel, drive]],
                                            columns=["Car_name", "Year", "Distance", "Fuel_type", "Drive"]))
    prediction = round(prediction[0])
    return render_template("prediction_page.html",
                           prediction=prediction,
                           car_model=car_model,
                           year=year,
                           fuel=fuel,
                           drive=drive,
                           kms_driven=kms_driven)


# def get_all_data():
#     car_names = sorted(car_data["Car_name"].unique())
#     years = sorted(car_data["Year"].unique())
#     distance = sorted(car_data["Distance"].unique())
#     fuel_type = car_data["Fuel_type"].unique()
#     drive = car_data["Drive"].unique()
#     return [car_names, years, distance, fuel_type, drive]


if __name__ == "__main__":
    app.run(debug=True, port=8000)