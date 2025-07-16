from transformers import T5ForConditionalGeneration, T5Tokenizer

model_name = "t5-small"
tokenizer = T5Tokenizer.from_pretrained(model_name)
model = T5ForConditionalGeneration.from_pretrained(model_name)

def chunk_text(text, max_tokens=512):
    tokens = tokenizer.tokenize(text)
    chunks = []
    for i in range(0, len(tokens), max_tokens):
        chunk = tokens[i:i + max_tokens]
        chunk_text = tokenizer.convert_tokens_to_string(chunk)
        chunks.append(chunk_text)
    return chunks

def summarize_text(text):
    # Chunk text if too long
    chunks = chunk_text(text, max_tokens=512)

    chunk_summaries = []
    for chunk in chunks:
        input_text = "summarize: " + chunk.strip().replace("\n", " ")
        inputs = tokenizer.encode(input_text, return_tensors="pt", max_length=512, truncation=True)
        outputs = model.generate(
            inputs,
            max_length=180,           # max tokens in summary
            min_length=60,            # min tokens in summary
            length_penalty=2.0,
            num_beams=5,
            early_stopping=True,
            no_repeat_ngram_size=3,   # avoid repetition
        )
        summary = tokenizer.decode(outputs[0], skip_special_tokens=True)
        chunk_summaries.append(summary)

    # Combine chunk summaries into one text and optionally summarize again
    combined_summary = " ".join(chunk_summaries)

    # Optional: do a final summarization pass on combined summary if too long
    if len(tokenizer.tokenize(combined_summary)) > 512:
        input_text = "summarize: " + combined_summary.strip().replace("\n", " ")
        inputs = tokenizer.encode(input_text, return_tensors="pt", max_length=512, truncation=True)
        outputs = model.generate(
            inputs,
            max_length=180,
            min_length=60,
            length_penalty=2.0,
            num_beams=5,
            early_stopping=True,
            no_repeat_ngram_size=3,
        )
        combined_summary = tokenizer.decode(outputs[0], skip_special_tokens=True)

    return combined_summary
