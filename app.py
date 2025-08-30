from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from chatbot.logic import get_response

app = Flask(__name__, static_folder="static", template_folder="templates")
CORS(app)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/student")
def student_page():
    return render_template("student.html")


@app.route("/professional")
def professional_page():
    return render_template("professional.html")


# Chat endpoint used by JS front-end (both pages call this)
@app.route("/chat", methods=["POST"])
def chat_api():
    data = request.get_json() or {}
    message = data.get("message", "").strip()
    mode = data.get("mode", "student")  # 'student' or 'professional'
    if not message:
        return jsonify({"error": "No message provided"}), 400

    reply = get_response(message, mode)
    return jsonify({"reply": reply})


if __name__ == "__main__":
    app.run(debug=True)
