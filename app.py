from flask import Flask, request, render_template
import sklearn
import pickle
import pandas as pd

app = Flask(__name__)
model = pickle.load(open("body_fat.pkl", "rb"))



@app.route("/")
def home():
    return render_template("home1.html")




@app.route("/predict", methods = ["GET", "POST"])
def predict():
    if request.method == "POST":

        Density = int(request.form["Density"])
        Age = int(request.form["Age"])
        Weight = int(request.form["Weight"])
        Height = int(request.form["Height"])
        Neck = int(request.form["Neck"])
        Chest = int(request.form["Chest"])
        Abdomen = int(request.form["Abdomen"])
        Hip = int(request.form["Hip"])
        Thigh = int(request.form["Thigh"])
        Knee = int(request.form["Knee"])
        Ankle = int(request.form["Ankle"])
        Biceps = int(request.form["Biceps"])
        Forearm = int(request.form["Forearm"])
        Wrist = int(request.form["Wrist"])

        prediction=model.predict([[
            Density,
            Age,
            Weight,
            Height,
            Neck,
            Chest,
            Abdomen,
            Hip,
            Thigh,
            Knee,
            Ankle,
            Biceps,
            Forearm,
            Wrist
            
        ]])

        output=round(prediction[0],2)

        return render_template('home1.html',prediction_text="Your Body Fat is {}".format(output))


    return render_template("home1.html")




if __name__ == "__main__":
    app.run(debug=True)

