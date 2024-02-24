from flask import Flask, render_template, request
import random
import string

app = Flask(__name__)

def passwordGenerator(u, n, s):
    lowerchars = list(string.ascii_lowercase)
    upperchars = list(string.ascii_uppercase)
    specialchars = ['&', '!', '*', '@', '$']
    numericchars = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

    # Making sure that the requested counts are at least 1
    u = max(1, u)
    n = max(1, n)
    s = max(1, s)

    remaining_length = 10 - (u + n + s)
    password = ""

    # Randomly add lowercase characters to meet the remaining length
    for _ in range(remaining_length):
        password += random.choice(lowerchars)

    # Add one character from each category to the password
    password += random.choice(upperchars) + random.choice(specialchars) + random.choice(numericchars)

    # Add remaining characters randomly
    for _ in range(u - 1):
        password += random.choice(upperchars)
    for _ in range(s - 1):
        password += random.choice(specialchars)
    for _ in range(n - 1):
        password += random.choice(numericchars)

    # Shuffle the password to make the order random
    password_list = list(password)
    random.shuffle(password_list)
    password = ''.join(password_list)
    #print(password)
    return str(password)


@app.route("/", methods = ["GET" , "POST"] )
def home():
    password = None
    if request.method == 'POST':
        u = int(request.form['upper'])
        n = int(request.form['numeric'])
        s = int(request.form['special'])
        password = passwordGenerator(u,n,s)

    return render_template("dynamic_index.html", content = password)


if __name__ == "__main__":
    app.run(debug=True, port=5001)