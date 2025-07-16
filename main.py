from article_extraction import get_article_text
from preprocessing import preprocess_text
from summarization import summarize_text
from bias_detection import detect_and_neutralize_bias

def main():
    url = input("Enter news article URL: ")
    article_data = get_article_text(url)
    if article_data:
        print(f"\nTitle: {article_data['title']}")

        # Preprocess the text
        clean_text = preprocess_text(article_data['text'])

        # Generate summary
        summary = summarize_text(clean_text)
        print("\nOriginal Summary:")
        print(summary)

        # Bias detection and neutralization
        neutral_summary, label, bias_score = detect_and_neutralize_bias(summary)
        print(f"\nDetected Bias: {label} (Confidence: {bias_score:.2f})")
        print("\nFinal Neutralized Summary:")
        print(neutral_summary)
    else:
        print("Failed to extract article data.")

if __name__ == "__main__":
    main()