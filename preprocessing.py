import re

def preprocess_text(text, max_char_length=75000):
    text = re.sub(r"[\t\n]+", " ", text) # Replaces tabs and new lines with a space
    
    text = re.sub(r"\s{2,}", " ", text) # Replaces multiple spaces with a single space
    
    text = text.strip() # Removes leading and trailing spaces

    # Truncate text to max character length
    if len(text) > max_char_length:
        text = text[:max_char_length]
        print(f"Warning: Text truncated to {max_char_length} characters.")
    return text
    
    