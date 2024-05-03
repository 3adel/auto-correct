import json
import csv

# Specify the path to the JSONL file and the output CSV file
input_file_path = '/Users/adel/adel/dev/training_data/auto-correct/gwords/jsonified/frequency-alpha-alldicts_4000_words.jsonl'
output_csv_path = '/Users/adel/adel/dev/training_data/auto-correct/gwords/jsonified/frequency-alpha-alldicts_4000`_words.csv'

# Open the JSONL file and the CSV file
with open(input_file_path, 'r') as jsonl_file, open(output_csv_path, 'w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    # Write the header row
    csv_writer.writerow(['misspelling','correct_word'])
    
    # Process each line in the JSONL file
    for line in jsonl_file:
        if line.strip():
            # Load the JSON data from the line
            data = json.loads(line)

            

            correct_word = data.get('correct_word')
            
            misspellings = data.get('misspellings', [])
            

            
            # Write each misspelling to the CSV file
            for misspelling in misspellings:
                csv_writer.writerow([misspelling,correct_word])

print("CSV file has been created with the misspellings.")
