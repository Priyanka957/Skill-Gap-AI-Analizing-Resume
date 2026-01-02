import re

def clean_text(text):
    # Remove (cid:xxx) or (cidxxx)
    text = re.sub(r'\(cid[:]*\d+\)', '', text, flags=re.IGNORECASE)

    # Fix missing spaces between words
    text = re.sub(r'([a-z])([A-Z])', r'\1 \2', text)

    # Normalize spaces but keep line breaks
    text = re.sub(r'[ \t]+', ' ', text)

    # Remove unwanted characters
    text = re.sub(r'[^A-Za-z0-9.,@+\-()\n ]', '', text)

    # Remove too many blank lines
    text = re.sub(r'\n{3,}', '\n\n', text)

    return text.strip()