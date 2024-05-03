# import os

# source_file_path = "/Users/adel/adel/dev/training_data/auto-correct/100k_wikidictionary_most_used_english_words/raw/raw_wiki-100k.txt"
# lines_count = 0
# with open(source_file_path, "r") as file:
#     for line in file:
#         lines_count += 1
#         print(lines_count,line.strip())


import os

source_file_path = "/Users/adel/adel/dev/training_data/auto-correct/100k_wikidictionary_most_used_english_words/raw/raw_wiki-100k.txt"
target_file_path = "/Users/adel/adel/dev/training_data/auto-correct/100k_wikidictionary_most_used_english_words/cleaned/clean_wiki-100k.txt"

with open(source_file_path, "r") as source_file, open(target_file_path, "w") as target_file:
    for line in source_file:
        if not line.startswith('#'):
            target_file.write(line)





