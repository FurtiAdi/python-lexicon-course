from transformers import pipeline

#--------------------------------------------------------------------------------
# Task 1 - 1
#---------------------------------------------------------------------------------
gen = pipeline("text2text-generation", model="google/flan-t5-base")
user_input = input("Enter english sentence: ")

prompt = (
    "Rewrite the following sentence in simpler English. "
    "One sentence, 8-24 words, end with a period."
    f"Sentence: {user_input}"
)
result = gen(
    prompt,
    max_new_tokens=40,
    num_beams=5,
    no_repeat_ngram_size=3,
    do_sample=False,
)

output = result[0]["generated_text"].strip()
print("\n--- TEXT GENERATION (FLAN-T5-base, deterministic) ---\n")
print(output)

# Constraint checking
words = output.split()
is_one_sentence = output.count(".") == 1
ends_with_period = output.endswith(".")
word_count_valid = 8 <= len(words) <= 24

if is_one_sentence and ends_with_period and word_count_valid:
    print("\nConstraints satisfied")
else:
    print("\nConstraint not satisfied")
    

#--------------------------------------------------------------------------------
# Task 1 - 2
#---------------------------------------------------------------------------------

sentiment = pipeline("sentiment-analysis", 
                     model="distilbert-base-uncased-finetuned-sst-2-english")

user_input = input("Enter three sentence separated by comma (,): ")
sentences = [s.strip() for s in user_input.split(',')]


print("\n--- SENTIMENT ANALYSIS (DistilBERT) ---\n")
for sentence in sentences:
    result = sentiment(sentence)[0] 
    print(f"Text: {sentence}\n -> Label: {result['label']}, Score: {result['score']:.3f}\n")

print("Explanation:")
print(
    "The DistilBERT SST-2 model is trained on a dataset that only contains two classes: "
    "positive and negative sentiment. Because of this, the model cannot predict a neutral "
    "class. This means that even sentences that are neutral  will be forced "
    "into either positive or negative categories, which can reduce accuracy for balanced "
    "or unclear text."
)