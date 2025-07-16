from transformers import T5ForConditionalGeneration, T5Tokenizer

model_name = "t5-base"
tokenizer = T5Tokenizer.from_pretrained(model_name)
model = T5ForConditionalGeneration.from_pretrained(model_name)

def summarize_text(text):
    input_text = "summarize: " + text.strip().replace("\n", " ")
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
    summary = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return summary
