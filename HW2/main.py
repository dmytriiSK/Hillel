from flask import Flask
import pandas as pd
import random
import string

app = Flask(__name__)

@app.route("/generate_password")
def generate_password():
    password_length = random.randint(10, 20)
    uppercase_letters = string.ascii_uppercase
    lowercase_letters = string.ascii_lowercase
    digits = string.digits
    symbols = string.punctuation
    required_symbols = random.choice(uppercase_letters) + random.choice(lowercase_letters) + random.choice(digits) + random.choice(symbols)
    remaining_length = password_length - len(required_symbols)
    remaining_password = ''.join(random.choice(uppercase_letters + lowercase_letters + digits + symbols) for _ in range(remaining_length))
    password = required_symbols + remaining_password
    return password

@app.route('/calculate_average')
def calculate_average():
    csv_filepath = 'hw.csv'
    df = pd.read_csv(csv_filepath)
    height_mean = df.iloc[:, 1].mean()
    weight_mean = df.iloc[:, 2].mean()

    return f"The average height is {height_mean:.2f} inch, the average weight is {weight_mean:.2f} lb"

