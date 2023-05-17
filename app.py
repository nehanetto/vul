from flask import Flask, render_template, request
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('./index.html')

@app.route('/check_vulnerabilities', methods=['POST'])
def check_vulnerabilities():
    code = request.form['code']

    # Save the code to a temporary file
    with open('temp.c', 'w') as file:
        file.write(code)

    # Run flawfinder to check for vulnerabilities
    output = subprocess.check_output(['flawfinder', 'temp.c'], universal_newlines=True)

    # Check if any vulnerabilities were found
    if output:
        vulnerabilities = output.splitlines()
        return render_template('./result.html', vulnerabilities=vulnerabilities)
    else:
        return render_template('./result.html', vulnerabilities=None)

if __name__ == '__main__':
    app.run(debug=True)
