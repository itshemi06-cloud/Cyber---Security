
from flask import Flask, render_template, request
import hashlib
import socket

app = Flask(__name__)


# Home Page
@app.route('/')
def home():
    return render_template('index.html')


# Password Strength Checker
@app.route("/password", methods=["GET", "POST"])
def password_checker():
    strength = ""

    if request.method == "POST":
        h_password = request.form.get("password", "")
        score = 0

        if len(h_password) >= 8:
            score += 1

        if any(char.isdigit() for char in h_password):
            score += 1

        if any(char.isupper() for char in h_password):
            score += 1

        if any(char.islower() for char in h_password):
            score += 1

        if any(not char.isalnum() for char in h_password):
            score += 1

        if score <= 2:
            strength = "Weak"
        elif score <= 4:
            strength = "Medium"
        else:
            strength = "Strong"

    return render_template("password.html", strength=strength)


# Password Hash Generator
@app.route("/hash", methods=["GET", "POST"])
def hash_generator():
    hash_value = ""

    if request.method == "POST":
        password = request.form["password"]
        hash_value = hashlib.sha256(password.encode()).hexdigest()

    return render_template("hash.html", hash_value=hash_value)


# Port Scanner
@app.route("/port-scan", methods=["GET", "POST"])
def port_scanner():

    result = []

    if request.method == "POST":

        target = request.form["target"].strip()

        ports = [21, 22, 23, 25, 53, 80, 110, 443]

        try:
            target_ip = socket.gethostbyname(target)

            result.append("Target IP: " + target_ip)
            result.append("Scanning common ports...")

            for port in ports:

                sock = socket.socket(
                    socket.AF_INET,
                    socket.SOCK_STREAM
                )

                sock.settimeout(1)

                connection_result = sock.connect_ex(
                    (target_ip, port)
                )

                if connection_result == 0:
                    result.append(
                        "Port " + str(port) + " OPEN"
                    )
                else:
                    result.append(
                        "Port " + str(port) + " CLOSED"
                    )

                sock.close()

        except socket.gaierror:
            result.append(
                "Invalid IP address or hostname."
            )

        except KeyboardInterrupt:
            result.append(
                "Scan interrupted by user."
            )

    return render_template(
        "port_scanner.html",
        result=result
    )


# Run Flask Application
if __name__ == "__main__":
    app.run(debug=True)

