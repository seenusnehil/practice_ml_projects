import pandas as pd
from flask import Flask, render_template
import pandas

app = Flask(__name__)
data = pd.read_csv('Cleaned_data.csv')


@app.route('/')
def index():
    locations = sorted(data['location'].unique())
    print(locations)
    return render_template('index.html', locations=locations)


if __name__ == "__main__":
    app.run(debug=True, port=5001)
