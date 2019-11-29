import random

from paths import *

#Markov routines -- constructed from Allison Parrish's "Reading and Writing Electronic Text" course: http://rwet.decontextualize.com
def ngrams_for_sequence(n, seq):
    return [tuple(seq[i:i+n]) for i in range(len(seq)-n+1)]


def add_to_model(model, n, seq):
    # make a copy of seq and append None to the end
    seq = list(seq[:]) + [None]
    for i in range(len(seq)-n):
        # tuple because we're using it as a dict key!
        gram = tuple(seq[i:i+n])
        next_item = seq[i+n]
        if gram not in model:
            model[gram] = []
        model[gram].append(next_item)


def markov_model(n, seq):
    model = {}
    add_to_model(model, n, seq)
    return model


def gen_from_model(n, model, start=None, max_gen=100):
    if start is None:
        start = random.choice(list(model.keys()))
    output = list(start)
    for i in range(max_gen):
        start = tuple(output[-n:])
        next_item = random.choice(model[start])
        if next_item is None:
            break
        else:
            output.append(next_item)
    return output


def markov_model_from_sequences(n, sequences):
    model = {}
    for item in sequences:
        add_to_model(model, n, item)
    return model


def markov_generate_from_sequences(n, sequences, count, max_gen=100):
    starts = [item[:n] for item in sequences if len(item) >= n]
    model = markov_model_from_sequences(n, sequences)
    return [gen_from_model(n, model, random.choice(starts), max_gen)
           for i in range(count)]


def markov_generate_from_lines_in_file(n, filehandle, count, level='char', max_gen=100):
    glue = ''
    sequences = []
    if level == 'char':
        glue = ''
        sequences = [item.strip() for item in filehandle.readlines()]
    elif level == 'word':
        glue = ' '
        sequences = [item.strip().split() for item in filehandle.readlines()]
    generated = markov_generate_from_sequences(n, sequences, count, max_gen)
    return [glue.join(item) for item in generated]


# Markovs
# for item in markov_generate_from_lines_in_file(3, open(names), 5, 'word'):
#     print(item)
#     print("")
#
# print("-------")

# new_names = open("new-city-names-markov.txt",'w')
# for item in markov_generate_from_lines_in_file(2, open(cities), 50, 'char', 1000):
#     print(item)
#     new_names.write(item + "\n")
# new_names.close()