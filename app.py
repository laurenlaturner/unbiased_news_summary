import streamlit as st
from article_extraction import get_article_text
from preprocessing import preprocess_text
from summarization import summarize_text
from bias_detection import detect_and_neutralize_bias

def main():
    st.title("Unbiased News Summarizer")

    url = st.text_input("Enter a news article URL:")

    if url:
        with st.spinner("Processing..."):
            article_data = get_article_text(url)

            if article_data:
                st.subheader("Article Title")
                st.write(article_data['title'])

                clean_text = preprocess_text(article_data['text'])
                summary = summarize_text(clean_text)

                # st.subheader("Original Summary")
                # st.write(summary)

                neutral_summary, label, bias_score = detect_and_neutralize_bias(summary)

                st.subheader("Detected Bias")
                st.write(f"{label} (Confidence: {bias_score:.2f})")

                st.subheader("Final Neutralized Summary")
                st.write(neutral_summary)

            else:
                st.error("Failed to extract article data. Please check the URL and try again.")

if __name__ == "__main__":
    main()
