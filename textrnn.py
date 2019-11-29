from textgenrnn import textgenrnn

from paths import *

textgen = textgenrnn()

textgen.train_on_texts(open(cities).readlines(), num_epochs=6)

text = textgen.generate(50, temperature=0.95,return_as_list=True)

# new_names = open("new-city-names.txt",'w')
# for line in text:
#     print(line.strip())
#     new_names.write(line.strip() + "\n")
# new_names.close()