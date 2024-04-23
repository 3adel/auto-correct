# synth_data_gen/synth_data_gen_from_txt_batch_processing.py







import json
import ollama

def batch_process_typos(words):
    # Prepare messages for batch request
    messages = [{"role": "user", "content": f"List the top 10 common non-word spelling errors for the word '{word}'."} for word in words]

    # Call to the Ollama API using the llama3 model
    responses = ollama.chat(model='llama3', messages=messages)
    return responses

def save_typos_to_jsonl(source_file_path, output_file_path):
    # Define batch size
    batch_size = 10

    with open(source_file_path, "r") as file, open(output_file_path, "w") as outfile:
        words = []
        

        for line in file:
            word = line.strip()
            words.append(word)
            print("Words:", words)
            if len(words) == batch_size:
                typo_responses = batch_process_typos(words)
                print("Typo responses:", typo_responses)
                
                for word, typo_response in zip(words, typo_responses):
                    print("Typos response:", typo_response['message']['content'])

                    typos_list = typo_response['message']['content']
                    print(words_count, word, "->", typos_list)

                    # Create a JSON object for each line and write to the output file
                    json_line = json.dumps({"word": word, "typos": typos_list})
                    outfile.write(json_line + "\n")

                    words_count += 1
                    
                words = []  # Reset the batch

# Define file paths
source_file_path = "/Users/adel/adel/dev/training_data/auto-correct/100k_wikidictionary_most_used_english_words/cleaned/clean_wiki-100k.txt"
output_file_path = "/Users/adel/adel/dev/training_data/auto-correct/100k_wikidictionary_most_used_english_words/cleaned/clean_wiki-100k.jsonl"

# Call the function to process and save typos
save_typos_to_jsonl(source_file_path, output_file_path)
