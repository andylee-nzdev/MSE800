# BMI Calculator

A web application built with Flask that calculates Body Mass Index (BMI).

## BMI Formula

```
BMI = weight (kg) / height (m)²
```

## BMI Classifications

| BMI Range | Classification |
|-----------|----------------|
| < 18.5    | Underweight    |
| 18.5 - 24.99 | Normal weight |
| 25 - 29.99 | Overweight    |
| >= 30     | Obese          |

## How to Run

```bash
pip install flask
python app.py
```

Then open http://localhost:5000 in your browser.

## Usage

1. Enter your weight in kilograms
2. Enter your height in meters
3. Click "Calculate BMI"
4. The result and classification will appear below the form
