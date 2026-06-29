import time

INPUT_FILE = "input.txt"
OUTPUT_FILE = "output.txt" # accepts .txt or .csv
BLOCK_LENGTH = 60

start_time = time.perf_counter()
print("Starting...")

sequences = {}
seq_name = None
seq_lines = []

print(f"Looking for input file: {INPUT_FILE}...")
with open(INPUT_FILE, "r", encoding="utf-8") as file:

    print("File found.")
    for line in file:
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

    print(f"{len(sequences.keys())} sequences loaded.")

length_map = {name: len(seq) for name, seq in sequences.items()}
lengths = set(length_map.values())

if len(lengths) != 1:
    raise ValueError(
        "Sequences are not aligned.\n"
        f"Lengths per sequence: {length_map}"
    )

lengths_count = lengths.pop()
if lengths_count < BLOCK_LENGTH:
    print(f"Setting Block length to {lengths_count}")
    BLOCK_LENGTH = lengths_count
print(f"Block length set to {BLOCK_LENGTH}.")

name_max_length = max(len(name) for name in sequences.keys())
with open("output.txt", "w") as output:
    for line_start in range(0, lengths_count, BLOCK_LENGTH):
        line_end = min(line_start + BLOCK_LENGTH, lengths_count)
        sequence_blocks = [sequence[line_start:line_end] for sequence in sequences.values()]

        consensus_line = []
        for column in zip(*sequence_blocks):
            if len(set(column)) == 1:
                consensus_line.append("*")
            else:
                consensus_line.append(".")
        
        consensus_line = "".join(consensus_line)

        for name, block in zip(sequences.keys(), sequence_blocks):
            output.write(f"{name:<{name_max_length}} {block} {line_end}\n")
        
        output.write(f"{'':<{name_max_length}} {consensus_line}\n\n")

elapsed = time.perf_counter() - start_time
print(f"Done! Completed in {elapsed:.3f} seconds.")
print(f"Output written to output file: {OUTPUT_FILE}")

