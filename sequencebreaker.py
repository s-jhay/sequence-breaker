# TODO: check that sequences are at least 60 chars long, change using modulo if not
# TODO: write sequence to output of choice, working one block at a time

INPUT_FILE = "input.txt"
OUTPUT_FILE = "output.txt" # accepts .txt or .csv
BLOCK_LENGTH = 60

print("Starting...")
sequences = {}
seq_name = None
seq_lines = []

print(f"Looking for input file: {INPUT_FILE}...")
with open(INPUT_FILE, "r", encoding="utf-8") as file:

    print("File found.")
    for line in file:
        # print(line)
        line = line.strip()

        if line.startswith(">"):
            # save previous sequence
            if seq_name is not None:
                sequences[seq_name] = "".join(seq_lines)
            
            # start new sequence
            seq_name = line[1:] # removes ">"
            seq_lines = []

        else:
            # continue reading sequence
            seq_lines.append(line)

    # last record
    if seq_name is not None:
        sequences[seq_name] = "".join(seq_lines)

    print("Sequences loaded.")

length_map = {name: len(seq) for name, seq in sequences.items()}
lengths = set(length_map.values())

if len(lengths) != 1:
    raise ValueError(
        "Sequences are not aligned.\n"
        f"Lengths per sequence: {length_map}"
    )





