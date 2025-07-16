import re

def preprocess_text(text):
    # Split text into paragraphs or lines
    lines = text.split('\n')

    # Define keywords to filter out lines containing ads or unrelated sections
    unwanted_keywords = [
        'advertisement',
        'subscribe',
        'click here',
        'terms and conditions',
        'follow us',
        'related articles',
        'share this',
        'sponsored',
        'read more',
        'powered by',
        'privacy policy',
        'cookie policy'
    ]

    clean_lines = []
    for line in lines:
        line_lower = line.strip().lower()
        # Skip lines that are empty or too short
        if len(line_lower) < 10:
            continue
        # Skip lines with unwanted keywords
        if any(keyword in line_lower for keyword in unwanted_keywords):
            continue
        # Skip lines that look like URLs or email addresses
        if re.match(r'(https?://|www\.)', line_lower) or '@' in line_lower:
            continue

        clean_lines.append(line.strip())

    # Join back into cleaned text
    cleaned_text = ' '.join(clean_lines)

    # Optionally: replace multiple spaces with a single space
    cleaned_text = re.sub(r'\s+', ' ', cleaned_text)

    return cleaned_text
