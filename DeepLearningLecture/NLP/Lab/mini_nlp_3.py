#---------------------------------------------------------------------------------------
# Task 3 
# 1. Read file (--infile)
# 2. For each line:
#       → rewrite (beam → retry with sampling)
#       → summarize (beam → retry)
#       → sentiment (add neutral)
# 3. Store results
# 4. Print metrics
#---------------------------------------------------------------------------------------

from transformers import pipeline
import argparse

# Models 
gen = pipeline("text2text-generation", model="google/flan-t5-base")
sentiment = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")
summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")

#---------------------------------------------------------------------------------------
# Helper functions
#---------------------------------------------------------------------------------------
def build_prompt(line):
    return(
        "Rewrite the sentence in simpler English. "
        "Do not copy the original sentence. "
        "Write exactly one sentence, 8 to 24 words, ending with a period.\n\n"
        f"Sentence: {line}"
    )

def count_tokens(line):
    return len(line.split())

def check_constraints(text):
    words = text.split()

    if text.count(".") != 1:
        return False
    if not text.endswith("."):
        return False
    if len(words) < 8 or len(words) > 24:
        return False

    return True


def neutral_label(label, score):
    if 0.4 <= score <= 0.6:
        return "NEUTRAL"
    return label

#---------------------------------------------------------------------------------------
# Main
#---------------------------------------------------------------------------------------

parser = argparse.ArgumentParser()
parser.add_argument("--infile")
args = parser.parse_args()

lines = [line.strip() for line in open(args.infile, 'r')]
results = []

for text in lines:

    #------------------ REWRITE ------------------
    prompt = build_prompt(text)

    # Beam
    beam_out = gen(prompt, max_new_tokens=32, no_repeat_ngram_size=3, num_beams=5, do_sample=False)[0]["generated_text"]
    beam_passed = check_constraints(beam_out)
    
    retry_fixed = False
    sampling_passed = False
    final_output = beam_out

    # Retry with sampling
    if not beam_passed:
        sample_out = gen(prompt, max_new_tokens=32, do_sample=True, temperature=0.7, top_p=0.9)[0]["generated_text"]
        sampling_passed = check_constraints(sample_out)

        if sampling_passed:
            final_output = sample_out
            retry_fixed= True

    results.append({
        "task": "rewrite",
        "beam_passed": beam_passed,
        "sampling_passed": sampling_passed,
        "retry_fixed": retry_fixed,
        "tokens": count_tokens(final_output)
    })

    #------------------ SUMMARY ------------------
    summary = summarizer(text, max_length=50, min_length=51, do_sample=False)[0]["summary_text"]
    eam_passed = check_constraints(summary)

    sampling_passed = False
    retry_fixed = False
    final_summary = summary

    if not beam_passed:
        summary2 = summarizer(text, max_length=50, min_length=51, do_sample=True, temperature=0.7, top_p=0.9)[0]["summary_text"]
        sampling_passed = check_constraints(summary2)

        if sampling_passed:
            final_summary = summary2
            retry_fixed = True

    results.append({
        "task": "summary",
        "beam_passed": beam_passed,
        "sampling_passed": sampling_passed,
        "retry_fixed": retry_fixed,
        "tokens": count_tokens(final_summary)
    })

    #------------------ SENTIMENT ------------------
    result = sentiment(text)[0]
    
    label = result["label"]
    score = result["score"]
    final_label = neutral_label(label, score)

    results.append({
        "task": "sentiment",
        "raw_label": label,
        "score": score,
        "final_label": final_label
    })

#---------------------------------------------------------------------------------------
# Mini report
#---------------------------------------------------------------------------------------

gen_tasks = [row for row in results if row["task"] in ["rewrite", "summary"]]

print("\n---------Mini report------------\n")

# Pass rate 
beam_passed = [row for row in gen_tasks if row["beam_passed"]]
sampling_passed = [row for row in gen_tasks if row["sampling_passed"]]
retry_fixed = [row for row in gen_tasks if row["retry_fixed"]]

print("Beam pass rate: ", (len(beam_passed) / len(gen_tasks)) * 100, "%")
print("Sampling pass rate: ", (len(sampling_passed) / len(gen_tasks)) * 100, "%")
print("Retry fixed rate: ", (len(retry_fixed) / len(gen_tasks)) * 100, "%")

# Average tokens
token_sum = 0

for row in gen_tasks:
    token_sum += row["tokens"]

print("Average tokens: ", token_sum / len(gen_tasks))

#---------------------------------------------------------------------------------------
# Reflection
#---------------------------------------------------------------------------------------

print("\nReflection:")
print(f"Beam achieved a pass rate of {(len(beam_passed)/len(gen_tasks))*100:.1f}%, showing strong control over constraints.")
print(f"Sampling achieved {(len(sampling_passed)/len(gen_tasks))*100:.1f}%, but struggled due to more randomness.")
print(f"Retry fixed {(len(retry_fixed)/len(gen_tasks))*100:.1f}% of cases, showing how sampling can help when beam fails.")
print("The neutral sentiment band does not help handle uncertain predictions near score 0.5.")

#------------------ Sentiment ------------------

sentiment_rows = [row for row in results if row["task"] == "sentiment"]
raw_counts = {}
final_counts = {}

for row in sentiment_rows:
    raw = row["raw_label"]
    final = row["final_label"]

    if raw in raw_counts:
        raw_counts[raw] += 1
    else:
        raw_counts[raw] = 1

    if final in final_counts:
        final_counts[final] += 1
    else:
        final_counts[final] = 1

print("\nSentiment (raw): ", raw_counts)
print("Sentiment (with neutral): ", final_counts)


