import argparse
import csv

def main(args):
    # Open both files and read the lines
    with open(args.incorrect_file, 'r') as inc_file:
        incorrect_sentences = inc_file.readlines()
    
    with open(args.correct_file, 'r') as cor_file:
        correct_sentences = cor_file.readlines()
    
    # Ensure that both files have the same number of lines
    if len(incorrect_sentences) != len(correct_sentences):
        raise ValueError("The number of lines in both files must be identical.")
    
    # Pair each incorrect sentence with the correct sentence
    sentence_pairs = []
    for inc_sent, cor_sent in zip(incorrect_sentences, correct_sentences):
        # Strip newline characters and create a tuple
        pair = (inc_sent.strip(), cor_sent.strip())
        sentence_pairs.append(pair)
    
    # Write the pairs to a CSV file
    with open(args.output_csv, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Incorrect Sentence", "Correct Sentence"])  # Optional: write headers
        writer.writerows(sentence_pairs)

if __name__ == "__main__":
    # Define and parse program input
    parser = argparse.ArgumentParser(description="Process two files and save pairs in a CSV.")
    parser.add_argument("incorrect_file", help="The path to the file containing incorrect sentences.")
    parser.add_argument("correct_file", help="The path to the file containing corrected sentences.")
    parser.add_argument("output_csv", help="The path to the output CSV file where the sentence pairs will be saved.")
    args = parser.parse_args()
    main(args)
