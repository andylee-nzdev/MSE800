from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/calculate', methods=['POST'])
def calculate():
    weight = float(request.form['weight'])
    height = float(request.form['height'])
    bmi = round(weight / (height ** 2), 2)

    if bmi < 18.5:
        classification = "Underweight"
    elif bmi < 25:
        classification = "Normal weight"
    elif bmi < 30:
        classification = "Overweight"
    else:
        classification = "Obese"

    return render_template('result.html', bmi=bmi, classification=classification)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
