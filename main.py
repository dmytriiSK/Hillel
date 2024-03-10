from flask import Flask
import pandas as pd
import random
import string

app = Flask(__name__)

@app.route("/generate_password")
def generate_password():
    password_length = random.randint(10, 20)
    symbols = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(symbols) for _ in range(password_length))

    return password

@app.route('/calculate_average')
def calculate_average():
    csv_filepath = 'hw.csv'
    df = pd.read_csv(csv_filepath)
    height_mean = df.iloc[:, 1].mean()
    weight_mean = df.iloc[:, 2].mean()

    return f"The average height is {height_mean:.2f} inch, the average weight is {weight_mean:.2f} lb"

