"""
Word Occurrences
Estimate: 20 minutes
Actual:   15 minutes
"""

word_to_instances = {}
text = input("Text: ").split()

for word in sorted(text):
    instance = word_to_instances.get(word, 0)
    word_to_instances[word] = instance + 1

max_length = max(len(word) for word in list(word_to_instances.keys()))
for word, instance in word_to_instances.items():
    print(f"{word:{max_length}} : {instance}")
