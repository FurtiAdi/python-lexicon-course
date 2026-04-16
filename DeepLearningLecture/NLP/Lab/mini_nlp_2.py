#---------------------------------------------------------------------------------------
# Task 2
#1. Get file name (--infile)
# 2. Read all lines
# 3. For each line:
#       → rewrite with beam
#       → rewrite with sampling
#       → validate
#       → count tokens
#       → store result
# 4. Save to CSV
# 5. Print summary
#---------------------------------------------------------------------------------------

from transformers import pipeline
import argparse
import csv

gen =  pipeline("text2text-generation", model="google/flan-t5-base")

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

def check_constraints(output):
    words = output.split()
    notes = []

    if output.count(".") != 1:
        notes.append(">1 sentence or missing period")

    if not output.endswith("."):
        notes.append("no period")

    if len(words) < 8:
        notes.append("too short")

    if len(words) > 24:
        notes.append("too long")
    
    passed = len(notes)== 0

    return passed, ", ".join(notes)

#---------------------------------------------------------------------------------------
# Main functions
#---------------------------------------------------------------------------------------
parser = argparse.ArgumentParser()
parser.add_argument("--infile")
args = parser.parse_args()

lines = [line.strip() for line in open(args.infile, 'r')]
results = []

# Run both decoding methods
for sentence in lines:
    prompt = build_prompt(sentence)
    
    # Beam search 
    beam_out = gen(
        prompt,
        max_new_tokens=40,
        num_beams=5,  
        do_sample=False,  
    )[0]['generated_text']

    passed, notes = check_constraints(beam_out)

    results.append({
        'input' : sentence,
        'output' : beam_out,
        'decoding': 'beam',
        'tokens_out' : count_tokens(beam_out),
        'constraint_passed' : passed,
        'notes' : notes
    })

    # Sampling
    sample_out = gen(
        prompt,
        max_new_tokens=40,
        do_sample=True,  
        temperature = 0.7,
        top_p = 0.9
    )[0]['generated_text']

    passed, notes = check_constraints(sample_out)

    results.append({
        'input' : sentence,
        'output' : sample_out,
        'decoding': 'sampling',
        'tokens_out' : count_tokens(sample_out),
        'constraint_passed' : passed,
        'notes' : notes
    })


#---------------------------------------------------------------------------------------
# Save to csv
#---------------------------------------------------------------------------------------
with open('results.csv', 'w', newline="") as file:
    header = ['input', 'output', 'decoding', 'tokens_out', 'constraint_passed', 'notes']
    w = csv.DictWriter(file, header)
    w.writeheader()
    for row in results:
        w.writerow(row)


#---------------------------------------------------------------------------------------
# Mini report
#---------------------------------------------------------------------------------------

beam_rows = [row for row in results if row["decoding"] == "beam"]
sampling_rows = [row for row in results if row["decoding"] == "sampling"]

print("\n---------Mini report------------\n")

beam_rows_passed = [row for row in beam_rows if row["constraint_passed"] == True]
sampling_rows_passed = [row for row in sampling_rows if row["constraint_passed"] == True]

# Pass rate 
print("Beam pass rate: ", (len(beam_rows_passed) / len(beam_rows)) * 100, "%")
print("Sampling pass rate: ", (len(sampling_rows_passed) / len(sampling_rows)) * 100, "%")

# Average tokens
beam_token_sum = 0
sampling_token_sum = 0

for row in beam_rows:
    beam_token_sum += row['tokens_out']

print('Average tokens_out in beam: ', beam_token_sum / len(beam_rows))

for row in sampling_rows:
    sampling_token_sum += row['tokens_out']

print('Average tokens_out in sampling: ', sampling_token_sum / len(sampling_rows))

# Reflection (required)
print("\nReflection:")
print("Beam: Higher pass rate (100%), showing better control and adherence to constraints, but slightly less diverse outputs.")
print("Sampling: Lower pass rate (100%), also meeting constraints consistently while producing slightly more varied sentences.")




