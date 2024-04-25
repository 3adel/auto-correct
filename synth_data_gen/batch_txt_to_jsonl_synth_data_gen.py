#batch processign of txt to json to reduce GPU load.
import json
import ollama

def show_common_typos_ollama(words):
    # Construct batch prompts for each word
    prompt = [f"List only ten common non-word spelling errors for the word '{word}'. These errors should be common typos that an English native speaker would make regularly. The errors should not form real English words. The typos should be more than 1 characters long each. Only provide a comma-separated list of these errors. Ensure the list does never include the word '{word}' or synonyms of the word '{word}'. Ensure that the answer never include any additional text. The list of errors should be ranked from most common to the least common" for word in words]
    
    # Call to the Ollama API using the llama3 model in batch
    responses = ollama.generate(
        model='llama3', 
        prompt=prompt,
        options={
            "temperature": 0.1,
        })
    return responses


# def save_typos_to_jsonl(source_file_path, output_file_path, number_of_words, batch_size=3):
#     with open(source_file_path, "r") as file, open(output_file_path, "w") as outfile:
#         words = []
#         total_words_processed = 0

#         for line in file:
#             word = line.strip()
#             words.append(word)

#             if len(words) == batch_size:
#                 # Get responses for batch
#                 typo_responses = show_common_typos_ollama(words)
                
#                 # Process each response and write to file
#                 for word, response in zip(words, typo_responses):
#                     typos_list = response['response'].split(",")
#                     json_line = json.dumps({
#                         "correct_word": word,
#                         "misspellings": typos_list
#                     })
#                     outfile.write(json_line + "\n")
#                     print(total_words_processed, word, "->", typos_list)

#                 total_words_processed += len(words)
#                 words = []  # Reset batch

#                 if total_words_processed >= number_of_words:
#                     break
        
#         # Process any remaining words in the last batch
#         if words:
#             typo_responses = show_common_typos_ollama(words)
#             for word, response in zip(words, typo_responses):
#                 typos_list = response['response'].split(",")
#                 json_line = json.dumps({
#                     "correct_word": word,
#                     "misspellings": typos_list
#                 })
#                 outfile.write(json_line + "\n")
#                 print(total_words_processed, word, "->", typos_list)
#             total_words_processed += len(words)


# # Define file paths
# source_file_path = "/Users/adel/adel/dev/training_data/auto-correct/gwords/raw/raw_words.txt"
# output_file_path_100_words = "/Users/adel/adel/dev/training_data/auto-correct/gwords/jsonified/frequency-alpha-alldicts_100_words.jsonl"
# output_file_path_1000_words = "/Users/adel/adel/dev/training_data/auto-correct/gwords/jsonified/frequency-alpha-alldicts_1000_words.jsonl"
# output_file_path_10000_words = "/Users/adel/adel/dev/training_data/auto-correct/gwords/jsonified/frequency-alpha-alldicts_10000_words.jsonl"

# # Call the function to process and save typos
# save_typos_to_jsonl(source_file_path, output_file_path_1000_words,100,3)
# # save_typos_to_jsonl(source_file_path, output_file_path_1000_words,1000)
# # save_typos_to_jsonl(source_file_path, output_file_path_10000_words,10000)

