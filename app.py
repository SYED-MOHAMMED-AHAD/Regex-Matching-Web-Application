from flask import Flask, render_template, request
import re

app = Flask(__name__)

# Home route to clear any previous data when the page is first loaded (GET request)
@app.route('/')
def home():
    return render_template('sample.html', matches=None, email_valid=None)

# Route to handle regex matching form submission (POST request)
@app.route('/results', methods=['POST'])
def results():
    test_string = request.form['test_string']
    regex_pattern = request.form['regex']
    matched_strings = re.findall(regex_pattern, test_string)
    # Always clear the email_valid to ensure it doesn't persist across requests
    return render_template('sample.html', matches=matched_strings, email_valid=None)

# Route to handle email validation form submission (POST request)
@app.route('/validate_email', methods=['POST'])
def validate_email():
    email = request.form['email']
    is_valid = bool(re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email))
    # Always clear the matches to ensure they don't persist across requests
    return render_template('sample.html', email_valid=is_valid, matches=None)

if __name__ == '__main__':
    app.run(debug=True)
