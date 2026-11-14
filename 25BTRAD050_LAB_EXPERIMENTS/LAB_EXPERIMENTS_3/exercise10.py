# Frequency Counter Program

def count_word_frequency(sentence):
# Clean and split the sentence into words words =
sentence.lower().replace(".", "").replace(",", "").split() frequency =
{}

for word in words: if
word in frequency:
frequency[word] += 1
else: frequency[word]
= 1

return frequency

def count_list_frequency(items):
frequency = {} for item in items:
frequency[item] = frequency.get(item, 0) + 1
return frequency

# Test Case 1: Word frequency in a sentence sample_sentence =
"apple banana apple orange banana apple" word_counts =
count_word_frequency(sample_sentence) print("Word Frequency:",
word_counts)

# Test Case 2: Element frequency in survey responses survey_responses =
["Yes", "No", "Yes", "Maybe", "Yes", "No"] response_counts =
count_list_frequency(survey_responses) print("Survey Response Frequency:",
response_counts)
