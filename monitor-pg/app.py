
from flask import Flask, Response
from prometheus_client import Counter, generate_latest, CONTENT_TYPE_LATEST

app = Flask(__name__)

# Count total requests
REQUESTS = Counter(
    "app_requests_total",
    "Total number of application requests"
)

@app.route("/")
def home():
    REQUESTS.inc()
    return "Monitoring Demo Running!"

@app.route("/students")
def students():
    REQUESTS.inc()
    return {"students": ["Vinay", "Rahul"]}

@app.route("/metrics")
def metrics():
    return Response(
        generate_latest(),
        mimetype=CONTENT_TYPE_LATEST
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
