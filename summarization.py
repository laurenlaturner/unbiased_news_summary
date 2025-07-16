from transformers import PegasusForConditionalGeneration, PegasusTokenizer

model_name = "google/pegasus-xsum"

tokenizer = PegasusTokenizer.from_pretrained(model_name)
model = PegasusForConditionalGeneration.from_pretrained(model_name)

def chunk_text(text, max_tokens=512):
    tokens = tokenizer.tokenize(text)
    chunks = []
    for i in range(0, len(tokens), max_tokens):
        chunk = tokens[i:i + max_tokens]
        chunk_text = tokenizer.convert_tokens_to_string(chunk)
        chunks.append(chunk_text)
    return chunks

def summarize_text(text):
    chunks = chunk_text(text, max_tokens=512)

    chunk_summaries = []
    for chunk in chunks:
        inputs = tokenizer(chunk, return_tensors="pt", max_length=512, truncation=True)
        summary_ids = model.generate(
            **inputs,
            max_length=150,
            min_length=40,
            length_penalty=2.0,
            num_beams=5,
            early_stopping=True,
            no_repeat_ngram_size=3
        )
        summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
        chunk_summaries.append(summary)

    combined_summary = " ".join(chunk_summaries)

    if len(tokenizer.tokenize(combined_summary)) > 512:
        inputs = tokenizer(combined_summary, return_tensors="pt", max_length=512, truncation=True)
        summary_ids = model.generate(
            **inputs,
            max_length=150,
            min_length=40,
            length_penalty=2.0,
            num_beams=5,
            early_stopping=True,
            no_repeat_ngram_size=3
        )
        combined_summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)

    return combined_summary
