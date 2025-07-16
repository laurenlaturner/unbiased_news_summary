from newspaper import Article

def get_article_text(url):
    try:
        article = Article(url)
        article.download()
        article.parse()
    except Exception as e:
        print(f"Error downloading or parsing the article: {e}")
        return None
    
    title = article.title if article.title else ""
    text = article.text.strip() if article.text else ""
    authors = article.authors if article.authors else []
    publish_date = article.publish_date if article.publish_date else ""

    if not text:
        print("Warning: Article text is empty.")
        return None
    return {
        "title": title,
        "text": text,
        "authors": authors,
        "publish_date": publish_date
    }