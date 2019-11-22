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

theme_added_vecs = vec('desire') + vec('eyes') + vec('memory')
theme_added_vecs_2 = vec('sky') + vec('continuous') + vec('hidden')
theme_added_vecs_3 =  vec('names') + vec('signs') + vec('dead')
theme_added_vecs_4 =  vec('thin') + vec('trading')

theme_added_vecs_5 = vec('thin') + vec('continuous') + vec('memory')
theme_added_vecs_6 = vec('desire') + vec('signs') + vec('dead')
theme_added_vecs_7 =  vec('sky') + vec('trading') + vec('hidden')
theme_added_vecs_8 =  vec('names') + vec('eyes')

theme_added_vecs_9 = vec('thin') + vec('signs') + vec('memory')
theme_added_vecs_10 = vec('desire') + vec('trading') + vec('dead')
theme_added_vecs_11 =  vec('sky') + vec('eyes') + vec('hidden')
theme_added_vecs_12 =  vec('names') + vec('continuous')

theme_added_vecs_13 = vec('thin') + vec('eyes') + vec('dead')
theme_added_vecs_14 = vec('desire') + vec('continuous') + vec('hidden')
theme_added_vecs_15 =  vec('sky') + vec('signs') + vec('memory')
theme_added_vecs_16 =  vec('names') + vec('trading')

theme_added_vecs_17 = vec('sky') + vec('desire') + vec('continuous')
theme_added_vecs_18 = vec('eyes') + vec('memory') + vec('hidden')
theme_added_vecs_19 =  vec('trading') + vec('signs') + vec('thin')
theme_added_vecs_20 =  vec('dead') + vec('names')

theme_added_vecs_21 = vec('dead') + vec('memory') + vec('continuous')
theme_added_vecs_22 = vec('sky') + vec('signs') + vec('thin')
theme_added_vecs_23 =  vec('eyes') + vec('names') + vec('hidden')
theme_added_vecs_24 =  vec('trading') + vec('desires')

theme_added_vecs_25 = vec('dead') + vec('signs') + vec('continuous')
theme_added_vecs_26 = vec('sky') + vec('names') + vec('thin')
theme_added_vecs_27 =  vec('eyes') + vec('desires') + vec('hidden')
theme_added_vecs_28 =  vec('trading') + vec('memory')

theme_added_vecs_29 = vec('dead') + vec('signs') + vec('thin')
theme_added_vecs_30 = vec('sky') + vec('memory') + vec('hidden')
theme_added_vecs_31 =  vec('eyes') + vec('names') + vec('continuous')
theme_added_vecs_32 =  vec('trading') + vec('desires')

print(lookup.nearest(theme_added_vecs, 12))
print(lookup.nearest(theme_added_vecs_2,12))
print(lookup.nearest(theme_added_vecs_3, 12))
print(lookup.nearest(theme_added_vecs_4,12))
print(lookup.nearest(theme_added_vecs_5, 12))
print(lookup.nearest(theme_added_vecs_6,12))
print(lookup.nearest(theme_added_vecs_7, 12))
print(lookup.nearest(theme_added_vecs_8,12))
print(lookup.nearest(theme_added_vecs_9, 12))
print(lookup.nearest(theme_added_vecs_10,12))
print(lookup.nearest(theme_added_vecs_11, 12))
print(lookup.nearest(theme_added_vecs_12,12))
print(lookup.nearest(theme_added_vecs_13, 12))
print(lookup.nearest(theme_added_vecs_14,12))
print(lookup.nearest(theme_added_vecs_15, 12))
print(lookup.nearest(theme_added_vecs_16,12))
print(lookup.nearest(theme_added_vecs_17, 12))
print(lookup.nearest(theme_added_vecs_18,12))
print(lookup.nearest(theme_added_vecs_19, 12))
print(lookup.nearest(theme_added_vecs_20,12))
print(lookup.nearest(theme_added_vecs_21, 12))
print(lookup.nearest(theme_added_vecs_22,12))
print(lookup.nearest(theme_added_vecs_23, 12))
print(lookup.nearest(theme_added_vecs_24,12))
print(lookup.nearest(theme_added_vecs_25, 12))
print(lookup.nearest(theme_added_vecs_26,12))
print(lookup.nearest(theme_added_vecs_27, 12))
print(lookup.nearest(theme_added_vecs_28,12))
print(lookup.nearest(theme_added_vecs_29, 12))
print(lookup.nearest(theme_added_vecs_30,12))
print(lookup.nearest(theme_added_vecs_31, 12))
print(lookup.nearest(theme_added_vecs_32,12))
new_themes = open("new-themes.txt",'w')
new_themes.write(str(lookup.nearest(theme_added_vecs, 12)) + "\n")
new_themes.write(str(lookup.nearest(theme_added_vecs_2, 12)) + "\n")
new_themes.write(str(lookup.nearest(theme_added_vecs_3, 12)) + "\n")
new_themes.write(str(lookup.nearest(theme_added_vecs_4, 12)) + "\n")
new_themes.write(str(lookup.nearest(theme_added_vecs_5, 12)) + "\n")
new_themes.write(str(lookup.nearest(theme_added_vecs_6, 12)) + "\n")
new_themes.write(str(lookup.nearest(theme_added_vecs_7, 12)) + "\n")
new_themes.write(str(lookup.nearest(theme_added_vecs_8, 12)) + "\n")
new_themes.write(str(lookup.nearest(theme_added_vecs_9, 12)) + "\n")
new_themes.write(str(lookup.nearest(theme_added_vecs_10, 12)) + "\n")
new_themes.write(str(lookup.nearest(theme_added_vecs_11, 12)) + "\n")
new_themes.write(str(lookup.nearest(theme_added_vecs_12, 12)) + "\n")
new_themes.write(str(lookup.nearest(theme_added_vecs_13, 12)) + "\n")
new_themes.write(str(lookup.nearest(theme_added_vecs_14, 12)) + "\n")
new_themes.write(str(lookup.nearest(theme_added_vecs_15, 12)) + "\n")
new_themes.write(str(lookup.nearest(theme_added_vecs_16, 12)) + "\n")
new_themes.write(str(lookup.nearest(theme_added_vecs_17, 12)) + "\n")
new_themes.write(str(lookup.nearest(theme_added_vecs_18, 12)) + "\n")
new_themes.write(str(lookup.nearest(theme_added_vecs_19, 12)) + "\n")
new_themes.write(str(lookup.nearest(theme_added_vecs_20, 12)) + "\n")
new_themes.write(str(lookup.nearest(theme_added_vecs_21, 12)) + "\n")
new_themes.write(str(lookup.nearest(theme_added_vecs_22, 12)) + "\n")
new_themes.write(str(lookup.nearest(theme_added_vecs_23, 12)) + "\n")
new_themes.write(str(lookup.nearest(theme_added_vecs_24, 12)) + "\n")
new_themes.write(str(lookup.nearest(theme_added_vecs_25, 12)) + "\n")
new_themes.write(str(lookup.nearest(theme_added_vecs_26, 12)) + "\n")
new_themes.write(str(lookup.nearest(theme_added_vecs_27, 12)) + "\n")
new_themes.write(str(lookup.nearest(theme_added_vecs_28, 12)) + "\n")
new_themes.write(str(lookup.nearest(theme_added_vecs_29, 12)) + "\n")
new_themes.write(str(lookup.nearest(theme_added_vecs_30, 12)) + "\n")
new_themes.write(str(lookup.nearest(theme_added_vecs_31, 12)) + "\n")
new_themes.write(str(lookup.nearest(theme_added_vecs_32, 12)) + "\n")

i = 0

while i < 22:
    new_themes.write(str(random.randint(1,4)) + "\n")
    i += 1

new_themes.close()

# print(lookup.nearest(vec('basketball')))
# print(lookup.nearest(meanv([vec('day'), vec('night')])))
# print(lookup.nearest(vec("wine") - vec("beer")))
# print(lookup.nearest(vec("wine") - vec("alcohol")))
# print(lookup.nearest(vec("water") - vec("wet")))

# noun chunk lookup
# chunk_lookup = SimpleNeighbors(300)
# for chunk in full_text.noun_chunks:
#     chunk_lookup.add_one(chunk.text.replace("\n", " "), chunk.vector)
# chunk_lookup.build()
# print(chunk_lookup.nearest(nlp("minaret").vector))

# adjective lookup
# adj_lookup = SimpleNeighbors(300)
# for word in eyes_doc:
#     if word.tag_ == 'JJ' and word.text not in adj_lookup.corpus:
#         adj_lookup.add_one(word.text, word.vector)
# adj_lookup.build()
# print(chunk_lookup.nearest(nlp("poor").vector))

# replace from another text
# output = []
# for word in desire_doc:
#     if word.is_alpha and word.pos_ == 'NOUN':
#         new_word = random.choice(chunk_lookup.nearest(word.vector, 5))
#         output.append(new_word)
#     elif word.is_alpha and word.tag_ == 'JJ':
#         new_word = random.choice(adj_lookup.nearest(word.vector, 5))
#         output.append(new_word)
#     else:
#         output.append(word.text)
#     output.append(word.whitespace_)
# print(''.join(output))

# sentence lookup
# sentence_lookup = SimpleNeighbors(300)
# for sent in desire_doc.sents:
#     sentence_lookup.add_one(sent.text.replace("\n", " "), sent.vector)
# sentence_lookup.build()
#
# print(sentence_lookup.nearest(nlp("What a mood.").vector))

# replace with synonyms
# output = []
# for word in desire_doc:
#     if word.is_alpha and word.pos_ in ('NOUN', 'VERB', 'ADJ'):
#         new_word = random.choice(lookup.nearest(word.vector, 3))
#         output.append(new_word)
#     else:
#         output.append(word.text)
#     output.append(word.whitespace_)
# print(''.join(output))

# tint with target
# target_word = 'jealousy'
# factor = 0.25
#
# output = []
# for word in desire_doc:
#     if word.is_alpha and word.pos_ in ('NOUN', 'ADJ'):
#         new_word = random.choice(lookup.nearest((word.vector*(1-factor)) + (vec(target_word)*factor)))
#         output.append(new_word)
#     else:
#         output.append(word.text)
#     output.append(word.whitespace_)
# print(''.join(output))

