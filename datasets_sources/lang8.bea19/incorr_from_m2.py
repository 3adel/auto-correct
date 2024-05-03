import argparse

def main(args):
    with open(args.m2_file, 'r') as file:
        m2_content = file.read().strip().split("\n\n")
    
    with open(args.out, 'w') as out:
        for segment in m2_content:
            lines = segment.split("\n")
            # Extract the sentence after 'S ' and before any edits
            if lines[0].startswith("S "):  # Check if the line starts with 'S '
                # Split the first line, skip the first element 'S', and join the rest
                sentence = " ".join(lines[0].split()[1:])
                out.write(sentence + "\n")

if __name__ == "__main__":
    # Define and parse program input
    parser = argparse.ArgumentParser()
    parser.add_argument("m2_file", help="The path to an input m2 file.")
    parser.add_argument("-out", help="A path to where we save the output corrected text file.", required=True)
    args = parser.parse_args()
    main(args)
