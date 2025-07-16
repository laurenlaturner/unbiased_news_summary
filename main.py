from article_extraction import get_article_text
from preprocessing import preprocess_text

def main():
    url = input("Enter the news article URL: ")
    article_data = get_article_text(url)
    if article_data:
        print(f"\nTitle: {article_data['title']}")
        print(f"Authors: {article_data['authors']}")
        print(f"Published on: {article_data['publish_date']}")
        text = preprocess_text(article_data['text'])
        print("\n Extract Clean Article Test: \n", article_data['text'][:500]) # Print first 500 characters
    else:
        print("Failed to extract article data.")

if __name__ == "__main__":
    main()