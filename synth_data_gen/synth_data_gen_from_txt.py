import json
import ollama

def show_common_typos_ollama(word):
    # Call to the Ollama API using the llama3 model
    response = ollama.chat(model='llama3', messages=[
        {
            'role': 'user',
            "content": f"List the top 10 common non-word spelling errors for the word '{word}'. These errors should be typos that do not form real English words and should be more than 1 characters long. Provide a comma-separated list of these errors only. Ensure the list does never include '{word}', synonyms of '{word}'. Ensure that the answer never include any additinal text."
        },
    ])
    return response

def save_typos_to_jsonl(source_file_path, output_file_path):
    # Open the source file and output file
    with open(source_file_path, "r") as file, open(output_file_path, "w") as outfile:

        words_count = 0

        # Iterate over each line in the source file
        for line in file:
            word = line.strip()
            

            # Get the response from Ollama
            typo_response = show_common_typos_ollama(word)
            

            # Assuming the typo_response returns JSON with a specific structure. Adjust according to actual API response.
            typos_list = typo_response['message']['content']
            print(words_count,word,"->",typos_list)

            # Create a JSON object for each line and write to the output file
            json_line = json.dumps({
                "correct_word": word,
                "misspellings": typos_list
            })
            outfile.write(json_line + "\n")  # Write the JSON line followed by a newline character

            # Decide how many words to process
            words_count += 1
            if words_count == 100:
                break

# Define file paths
source_file_path = "/Users/adel/adel/dev/training_data/auto-correct/gwords/raw/raw_words.txt"
output_file_path = "/Users/adel/adel/dev/training_data/auto-correct/gwords/jsonified/frequency-alpha-alldicts.jsonl"

# Call the function to process and save typos
save_typos_to_jsonl(source_file_path, output_file_path)
