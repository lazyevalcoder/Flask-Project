from flask import Flask, render_template, request
import subprocess

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('home.html')

@app.route('/run', methods=['POST'])
def run_code():
    code = request.form['code']
    try:
        output = subprocess.check_output(['python', '-c', code], universal_newlines=True, stderr=subprocess.STDOUT)
    except subprocess.CalledProcessError as e:
        return render_template('home.html', output=str(e))
    return render_template('home.html', output=output)

if __name__ == "__main__":
    app.run(debug=True)