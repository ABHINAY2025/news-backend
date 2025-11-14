import feedparser

def fetch_rss_news(feed_url):
    feed = feedparser.parse(feed_url)

    articles = []

    for entry in feed.entries:
        articles.append({
            "title": entry.title,
            "summary": entry.summary if "summary" in entry else "",
            "published": entry.get("published", ""),
            "link": entry.link,
            "category": entry.get("category", ""),
            "image": entry.media_content[0]["url"] if "media_content" in entry else "",
            "content": entry.get("description", "")
        })

    return articles
