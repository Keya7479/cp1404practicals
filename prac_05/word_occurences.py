"""
Word Occurrences
Estimate: 20 minutes
Actual:   15 minutes
"""

word_to_instances = {}
text = input("Text: ").split()

for word in sorted(text):
    if word in word_to_instances:
        word_to_instances[word] += 1
    else:
        word_to_instances[word] = 1

sorted(word_to_instances)

max_length = max(len(word) for word in list(word_to_instances.keys()))
for word, instance in word_to_instances.items():
    print(f"{word:{max_length}} : {instance}")
