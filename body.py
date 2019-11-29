import vector_tinting
import paths
import string_swap
import analysis
import markov
from textgenrnn import textgenrnn

textgen = textgenrnn()

mgens = markov.markov_generate_from_lines_in_file(7, open(paths.desire), 1, 'char', analysis.desire_new_length*10)

# textgen.train_on_texts(open(paths.desire).readlines(), num_epochs=18)
# rgens = textgen.generate(10, temperature=0.6,return_as_list=True)

print(mgens)
# print(rgens)