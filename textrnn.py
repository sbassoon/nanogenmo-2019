from textgenrnn import textgenrnn

from paths import *

textgen = textgenrnn()

textgen.train_on_texts(open(desire).readlines(), num_epochs=20)

text = textgen.generate(20, temperature=0.8,return_as_list=True)

for line in text:
    print(line.strip())