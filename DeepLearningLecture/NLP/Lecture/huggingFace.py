# - **Model**: a trained neural network that maps input text to output text or labels.
# - **Weights / checkpoint**: the learned parameters of that model (the big files we download).
# - **Tokenizer**: converts text → **tokens** (subwords/IDs) for the model, and back again.
# - **Tokens**: pieces of text (not necessarily full words). Length limits and speeds are
#   measured in tokens, so “max_new_tokens” is about subwords, not words.
# - **Transformer (architecture)**: the neural network design (self-attention, etc.) used
#   by most state-of-the-art language models.
# - **Transformers (library)**: the Hugging Face Python library we import to use models.
# - **Pipeline**: a prebuilt function (e.g., `pipeline("sentiment-analysis")`) that handles
#   tokenizer + model + decoding for a common task.
# - **Inference** vs **training**:
#   * Inference = using a trained model to make predictions.
#   * Training/fine-tuning = updating weights with data.
# - **Encoder–decoder** vs **decoder-only**:
#   * Encoder–decoder (e.g., T5/BART): good for text-to-text tasks (summarize/translate).
#   * Decoder-only (e.g., GPT-style): good for next-token text continuation.
# - **Deterministic decoding** (beam search, no sampling): stable, repeatable outputs.
# - **Sampling** (temperature, top-p): more creative/varied but less predictable.
 
# "How a pipeline call works (mental model):"
#   1) Your input text → **tokenizer** → token IDs.
#   2) Token IDs → **model** (forward pass on CPU) → output logits.
#   3) **Decoding** turns logits into text (beam search or sampling).
#   4) Output tokens → detokenize → final string.

from transformers import pipeline

#------------------------------------------------------------------------------------------
# Part 1 - First pipeline: Text Generation with FLAN-T5-base (local, CPU)
#------------------------------------------------------------------------------------------

gen = pipeline("text2text-generation", model="google/flan-t5-base")

prompt = (
    "Produce exactly ONE family-friendly joke. "
    "One sentence, 10-20 words, end with a period."
)

print("\n--- TEXT GENERATION (FLAN-T5-base, deterministic) ---\n")
print(gen(
    prompt,
    max_new_tokens=32,
    num_beams=5,  # beam search for deterministic output
    no_repeat_ngram_size=3,  # avoid repeating phrases
    do_sample=False,  # no randomness, always pick highest-probability tokens
)[0]['generated_text'])

#------------------------------------------------------------------------------------------
# Part 2 - Second pipeline: Sentiment Analysis (DistilBERT model) 
#------------------------------------------------------------------------------------------

# Positive
# Negative


sentiment = pipeline("sentiment-analysis", 
                     model="distilbert-base-uncased-finetuned-sst-2-english")

# under the hood: tokenizer -> DistilBERT forward pass -> softmax -> label -> score 

print("\n--- SENTIMENT ANALYSIS (DistilBERT) ---\n")

examples = [
    "I love this movie! It's fantastic and heartwarming.",
    "This film was terrible. I hated every minute of it."
]
for text in examples:
    result = sentiment(text)[0] # returns a list of dicts, we take the first one
    print(f"Text: {text}\n-> Label: {result['label']}, Score: {result['score']:.3f}\n")

#------------------------------------------------------------------------------------------
# Part 3 - Summarization (local, CPU) with DistilBART CNN 
#------------------------------------------------------------------------------------------

summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")

article = [
    "Python is a popular programming language known for readability and a rich ecosystem. "
    "Hugging Face Transformers lets developers run state-of-the-art AI models locally. "
    "With pipelines, tasks like text generation, sentiment analysis, and summarization "
    "become easy to prototype."
]

summary = summarizer(article, max_length=50, min_length=15, do_sample=True)[0]["summary_text"]

print("Original:", article)
print("\n Summary: ", summary)

#------------------------------------------------------------------------------------------
# Part 4 - Translation (En -> SV) with OPUS-MT (local, CPU) 
#------------------------------------------------------------------------------------------

print("\n--- Translation (En -> SV) ---\n")

translator = pipeline("translation", model="Helsinki-NLP/opus-mt-en-sv")

english = "Transformers pipelines make it simple to try models locally"
swedish = translator(english)[0]["translation_text"]

print("En:", english)
print("SV:", swedish)

