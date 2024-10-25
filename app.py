from flask import Flask, request, render_template_string
import random

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        label = random.choice(['1', '0'])  # '1' for spam, '0' for not spam
        message = f'Prediction: {label} (1 for Spam, 0 for Not Spam)'
    else:
        message = ''

    form = '''
    <h1>Fraud Detection Model Prediction</h1>
    <form method="post">
        <label>Account Length:</label><input type="text" name="Account Length"><br>
        <label>VMail Message:</label><input type="text" name="VMail Message"><br>
        <label>Day Mins:</label><input type="text" name="Day Mins"><br>
        <label>Day Calls:</label><input type="text" name="Day Calls"><br>
        <label>Day Charge:</label><input type="text" name="Day Charge"><br>
        <label>Eve Mins:</label><input type="text" name="Eve Mins"><br>
        <label>Eve Calls:</label><input type="text" name="Eve Calls"><br>
        <label>Eve Charge:</label><input type="text" name="Eve Charge"><br>
        <label>Night Mins:</label><input type="text" name="Night Mins"><br>
        <label>Night Calls:</label><input type="text" name="Night Calls"><br>
        <label>Night Charge:</label><input type="text" name="Night Charge"><br>
        <label>Intl Mins:</label><input type="text" name="Intl Mins"><br>
        <label>Intl Calls:</label><input type="text" name="Intl Calls"><br>
        <label>Intl Charge:</label><input type="text" name="Intl Charge"><br>
        <label>CustServ Calls:</label><input type="text" name="CustServ Calls"><br>
        <input type="submit" value="Predict">
    </form>
    <h2>Prediction Result:</h2>
    <div style="color: blue; font-size: 16px;">{{message}}</div>
    '''
    return render_template_string(form, message=message)

if __name__ == '__main__':
    app.run(debug=True)
