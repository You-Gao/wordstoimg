import os
import matplotlib.pyplot as plt

os.makedirs("words", exist_ok=True)

with open("words.txt") as f:
    names = f.read().splitlines()

for name in names:
    if name == "":
        continue
    words = name.split()
    for index, w in enumerate(words):
        # Skip first and last word
        if index == 0 or index == len(words) - 1:
            continue
        if len(words[index]) + len(words[index + 1]) <= 10:
            words[index] = words[index] + ' ' + words[index + 1]
            words.pop(index + 1)

    fig, ax = plt.subplots(figsize=(5, len(words)))
    for i, w in enumerate(words):
        ax.text(0.5, 1 - (i + 1) / (len(words) + 1), w, fontsize=30, ha='center', va='center')
    ax.axis('off')
    joined_words = '_'.join(words)
    plt.savefig(f"words/{joined_words.replace(':','').replace('?','').replace('/','')}.png")