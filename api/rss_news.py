import json
from services.rss_service import fetch_rss_news

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

def handler(request, response):

    body = request.get_json()
    region = body.get("region") if body else None

    if not region:
        response.status_code = 400
        return response.set_body({"error": "Region is required"})

    region = region.lower()
    if region not in RSS_FEEDS:
        response.status_code = 400
        return response.set_body({"error": "Invalid region"})

    articles = fetch_rss_news(RSS_FEEDS[region])

    response.status_code = 200
    response.set_body({
        "status": "success",
        "region": region,
        "articles": articles
    })
