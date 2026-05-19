from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "ShadowCraftMC VPS 24/7 Running By OriHost Enjoy 🚀"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
