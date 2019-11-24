import spacy
import numpy as np
import random
from paths import *
from simpleneighbors import SimpleNeighbors


def vec(s):
    return nlp.vocab[s].vector


def meanv(vecs):
    total = np.sum(vecs, axis=0)
    return total / len(vecs)


nlp = spacy.load('en_core_web_lg')

lookup = SimpleNeighbors(300)
for item in nlp.vocab:
    if item.has_vector and item.prob > -15 and item.is_lower:
        lookup.add_one(item.text, item.vector)
lookup.build()

desire_text = nlp(open(desire).read())
eyes_text = nlp(open(eyes).read())
memory_text =  nlp(open(memory).read())
names_text =  nlp(open(names).read())
signs_text =  nlp(open(signs).read())
dead_text =  nlp(open(dead).read())
sky_text =  nlp(open(sky).read())
continuous_text =  nlp(open(continuous).read())
hidden_text =  nlp(open(hidden).read())
thin_text =  nlp(open(thin).read())
trading_text =  nlp(open(trading).read())
narrative_text =  nlp(open(narrative).read())
full_text = nlp(open(full).read())

# tint with target
target_word = 'blood'
factor = 0.25

output = []
for word in eyes_text:
    if word.is_alpha and word.pos_ in ('NOUN', 'ADJ'):
        new_word = random.choice(lookup.nearest((word.vector*(1-factor)) + (vec(target_word)*factor)))
        output.append(new_word)
    else:
        output.append(word.text)
    output.append(word.whitespace_)
quarter = ''.join(output)
print(quarter)

factor = 0.33

output = []
for word in eyes_text:
    if word.is_alpha and word.pos_ in ('NOUN', 'ADJ'):
        new_word = random.choice(lookup.nearest((word.vector*(1-factor)) + (vec(target_word)*factor)))
        output.append(new_word)
    else:
        output.append(word.text)
    output.append(word.whitespace_)
third = ''.join(output)
print(third)

factor = 0.4

output = []
for word in eyes_text:
    if word.is_alpha and word.pos_ in ('NOUN', 'ADJ'):
        new_word = random.choice(lookup.nearest((word.vector*(1-factor)) + (vec(target_word)*factor)))
        output.append(new_word)
    else:
        output.append(word.text)
    output.append(word.whitespace_)
point_four = ''.join(output)
print(point_four)

factor = 0.5

output = []
for word in eyes_text:
    if word.is_alpha and word.pos_ in ('NOUN', 'ADJ'):
        new_word = random.choice(lookup.nearest((word.vector*(1-factor)) + (vec(target_word)*factor)))
        output.append(new_word)
    else:
        output.append(word.text)
    output.append(word.whitespace_)
half = ''.join(output)
print(half)

factor = 0.66

output = []
for word in eyes_text:
    if word.is_alpha and word.pos_ in ('NOUN', 'ADJ'):
        new_word = random.choice(lookup.nearest((word.vector*(1-factor)) + (vec(target_word)*factor)))
        output.append(new_word)
    else:
        output.append(word.text)
    output.append(word.whitespace_)
point_six = ''.join(output)
print(point_six)

factor = 0.75

output = []
for word in eyes_text:
    if word.is_alpha and word.pos_ in ('NOUN', 'ADJ'):
        new_word = random.choice(lookup.nearest((word.vector*(1-factor)) + (vec(target_word)*factor)))
        output.append(new_word)
    else:
        output.append(word.text)
    output.append(word.whitespace_)
three_quarters = ''.join(output)
print(three_quarters)