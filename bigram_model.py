from collections import defaultdict

corpus = [
    ["<s>", "I", "love", "NLP", "</s>"],
    ["<s>", "I", "love", "deep", "learning", "</s>"],
    ["<s>", "deep", "learning", "is", "fun", "</s>"]
]

unigram = defaultdict(int)
bigram = defaultdict(int)

# counts
for sent in corpus:
    for i in range(len(sent)):
        unigram[sent[i]] += 1
        if i > 0:
            bigram[(sent[i-1], sent[i])] += 1

# bigram probabilities
bigram_prob = {}
for (w1, w2), count in bigram.items():
    bigram_prob[(w1, w2)] = count / unigram[w1]

def sentence_prob(sentence):
    prob = 1
    for i in range(1, len(sentence)):
        prob *= bigram_prob.get((sentence[i-1], sentence[i]), 0)
    return prob

s1 = ["<s>", "I", "love", "NLP", "</s>"]
s2 = ["<s>", "I", "love", "deep", "learning", "</s>"]

p1 = sentence_prob(s1)
p2 = sentence_prob(s2)

print("P(S1):", p1)
print("P(S2):", p2)

if p1 > p2:
    print("Model prefers S1 (more frequent bigrams)")
else:
    print("Model prefers S2")
