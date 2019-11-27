import spacy
import numpy as np
import random
import string_swap
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

def vector_tint(target,source,factor):
    output = []
    for w in source:
        if w.is_alpha and w.pos_ in ('NOUN', 'ADJ'):
            new_word = random.choice(lookup.nearest((w.vector * (1 - factor)) + (vec(target) * factor)))
            output.append(new_word)
        else:
            output.append(w.text)
        output.append(w.whitespace_)
    new_text = ''.join(output)
    return(new_text)