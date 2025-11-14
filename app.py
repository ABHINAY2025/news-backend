from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
from services.rss_service import fetch_rss_news
import requests
from io import BytesIO

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

RSS_FEEDS = {
    "india": "https://www.thehindu.com/news/national/feeder/default.rss",
    "world": "https://www.thehindu.com/news/international/feeder/default.rss",
    "telangana": "https://www.thehindu.com/news/national/telangana/feeder/default.rss",
    "andhra": "https://www.thehindu.com/news/national/andhra-pradesh/feeder/default.rss",
    "tamilnadu": "https://www.thehindu.com/news/national/tamil-nadu/feeder/default.rss",
    "karnataka": "https://www.thehindu.com/news/national/karnataka/feeder/default.rss",
    "kerala": "https://www.thehindu.com/news/national/kerala/feeder/default.rss",
    "maharashtra": "https://www.thehindu.com/news/national/maharashtra/feeder/default.rss"
}

@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "News Backend Running!"})

@app.route("/test", methods=["GET"])
def test_route():
    return jsonify({"message": "Test route working!"})

@app.route("/rss-news", methods=["POST"])
def rss_news():
    data = request.json
    region = data.get("region")

    if not region:
        return jsonify({"error": "Region is required"}), 400

    region = region.lower()
    if region not in RSS_FEEDS:
        return jsonify({"error": "Invalid region"}), 400

    feed_url = RSS_FEEDS[region]
    articles = fetch_rss_news(feed_url)

    return jsonify({
        "status": "success",
        "region": region,
        "articles": articles
    })

@app.route("/proxy-image")
def proxy_image():
    image_url = request.args.get("url")
    if not image_url:
        return "Missing URL", 400

    try:
        response = requests.get(image_url, timeout=10)
        content_type = response.headers.get("Content-Type", "image/jpeg")
        return send_file(BytesIO(response.content), mimetype=content_type)
    except Exception as e:
        print("Proxy image error:", e)
        return "Error loading image", 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
