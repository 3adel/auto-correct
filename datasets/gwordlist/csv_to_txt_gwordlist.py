import csv

# Replace 'yourfile.csv' with the path to your CSV file
csv_file_path = '/Users/adel/adel/dev/training_data/auto-correct/gwords/raw/raw_frequency-alpha-alldicts.csv'
text_file_path = '/Users/adel/adel/dev/training_data/auto-correct/gwords/raw/raw_words.csv'

# Open the CSV file
with open(csv_file_path, newline='') as csvfile:
    reader = csv.DictReader(csvfile)  # Using DictReader to access columns by name
    words = [row['WORD'] for row in reader]  # Extract words from the 'word' column

# Write the words to a text file
with open(text_file_path, 'w') as txtfile:
    for word in words:
        txtfile.write(word + '\n')  # Write each word on a new line

print("Words have been written to", text_file_path)
