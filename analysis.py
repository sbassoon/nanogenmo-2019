from random import gauss
import statistics
import csv

from paths import *

num_words, num_parts = 0,0


def get_word_count_list(filename):
    parts = []
    with open(filename, 'r') as f:
        text = f.read()
        result = text.split("|")
        for x in result:
            words = x.split()
            parts.append(len(words))
    return parts


desire_parts = get_word_count_list(desire)
desire_average = statistics.mean(desire_parts)
desire_stdev = statistics.pstdev(desire_parts)

eyes_parts = get_word_count_list(eyes)
eyes_average = statistics.mean(eyes_parts)
eyes_stdev = statistics.pstdev(eyes_parts)

memory_parts = get_word_count_list(memory)
memory_average = statistics.mean(memory_parts)
memory_stdev = statistics.pstdev(memory_parts)

names_parts = get_word_count_list(names)
names_average = statistics.mean(names_parts)
names_stdev = statistics.pstdev(names_parts)

signs_parts = get_word_count_list(signs)
signs_average = statistics.mean(signs_parts)
signs_stdev = statistics.pstdev(signs_parts)

dead_parts = get_word_count_list(dead)
dead_average = statistics.mean(dead_parts)
dead_stdev = statistics.pstdev(dead_parts)

sky_parts = get_word_count_list(sky)
sky_average = statistics.mean(sky_parts)
sky_stdev = statistics.pstdev(sky_parts)

continuous_parts = get_word_count_list(continuous)
continuous_average = statistics.mean(continuous_parts)
continuous_stdev = statistics.pstdev(continuous_parts)

hidden_parts = get_word_count_list(hidden)
hidden_average = statistics.mean(hidden_parts)
hidden_stdev = statistics.pstdev(hidden_parts)

thin_parts = get_word_count_list(thin)
thin_average = statistics.mean(thin_parts)
thin_stdev = statistics.pstdev(thin_parts)

trading_parts = get_word_count_list(trading)
trading_average = statistics.mean(trading_parts)
trading_stdev = statistics.pstdev(trading_parts)

narrative_parts = get_word_count_list(narrative)
narrative_average = statistics.mean(narrative_parts)
narrative_stdev = statistics.pstdev(narrative_parts)

desire_new_length = round(gauss(desire_average,desire_stdev))
print(desire_new_length)

# with open('lengths.csv','w',newline='') as csvfile:
#     csvwriter = csv.writer(csvfile, delimiter=";")
#     csvwriter.writerow(['Desire'] + desire_parts)
#     csvwriter.writerow(['Eyes'] + eyes_parts)
#     csvwriter.writerow(['Memory'] + memory_parts)
#     csvwriter.writerow(['Names'] + names_parts)
#     csvwriter.writerow(['Signs'] + signs_parts)
#     csvwriter.writerow(['Dead'] + dead_parts)
#     csvwriter.writerow(['Sky'] + sky_parts)
#     csvwriter.writerow(['Continuous'] + continuous_parts)
#     csvwriter.writerow(['Hidden'] + hidden_parts)
#     csvwriter.writerow(['Thin'] + thin_parts)
#     csvwriter.writerow(['Trading'] + trading_parts)
#     csvwriter.writerow(['Narrative'] + narrative_parts)