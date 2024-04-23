import csv

# Open the input file and the output CSV file
input_file_path = '/Users/adel/adel/dev/training_data/auto-correct/gwords/raw_frequency-alpha-alldicts.txt'
output_file_path = '/Users/adel/adel/dev/training_data/auto-correct/gwords/raw_frequency-alpha-alldicts.csv'

with open(input_file_path, 'r') as infile, open(output_file_path, 'w', newline='') as outfile:
    # Create a CSV writer object
    csv_writer = csv.writer(outfile)

    # Write the header to the CSV file
    csv_writer.writerow(['RANKING', 'WORD', 'COUNT', 'PERCENT', 'CUMULATIVE'])

    # Read the file line by line
    for line in infile:
        # Skip lines that start with '#' (like comments or headers in your file)
        if line.startswith('#'):
            continue
        
        # Split the line into parts based on whitespace
        parts = line.split()
        if parts:
            # Reassemble the data to ensure proper CSV structure
            ranking = parts[0]
            word = parts[1]
            count = parts[2].replace(',', '')  # Remove commas from the count for proper number formatting
            percent = parts[3].strip('%')      # Remove the percent sign
            cumulative = parts[4].strip('%')   # Remove the percent sign

            # Write to the CSV
            csv_writer.writerow([ranking, word, count, percent, cumulative])

# Inform the user that the process is complete
print("Conversion to CSV completed successfully.")
