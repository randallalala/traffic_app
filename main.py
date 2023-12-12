from flask import Flask, render_template
import redis

app = Flask(__name__)

redis_client = redis.Redis(host='redis', port=6379)

@app.route("/")
def index():
    count = int(redis_client.get('visitor_count') or 0) + 1
    redis_client.set('visitor_count', count)
    return render_template("index.html", count=count)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)

