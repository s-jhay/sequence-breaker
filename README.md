# Sequence Breaker

### A simple console script for parsing and comparing nucleotide and protein sequences

This script takes in pre-aligned sequences within a text file in FASTA format and outputs a comparison file in a format similar to that expected from [Clustal Omega](https://www.ebi.ac.uk/jdispatcher/msa/clustalo). 

***NOTE:** The script assumes that the input sequences are already aligned and the same length. The script will not work if either conditions are not met.*

---

## Requirements

You need **Python 3** installed on your computer.

### Windows

1. Go to https://www.python.org/downloads/

2. Download the latest (and not pre-release) version of Python 3.

3. Run the installer.

4. **Important:** On the first installation screen, check the box that says:

   ```
   Add Python to PATH
   ```

5. Click **Install Now**.

6. When the installation finishes, close the installer.

---

## Files

Place these files in the same folder:

* `sequencebreaker.py`
* `input.txt`

Your folder should look something like this:

```
MyFolder/
│
├── sequencebreaker.py
└── input.txt
```

### Input File

By default, the script will look for an input file called `input.txt`. This can be changed later within the script as needed. The file contents should look similar to the following:

```
>seq1
MFVFLVLLPLVSSQCVNLTTRTQLPPAYTNSFTRGVYYPDKVFRSSVLHSTQDLFLPFFSNVTWFHVISG
TNGTKRFDNPVLPFNDGVYFASIEKSNIIRGWIFGTTLDSKTQSLLIVNNATNVVIKVCEFQFCNDPFLD
...
VLKGVKLHYT

>seq2
MFVFLVLLPLVSSQCVNLITRTQSYTNSFTRGVYYPDKVFRSSVLHSTQDLFLPFFSNVTWFHAIHVSGT
NGTKRFDNPVLPFNDGVYFASTEKSNIIRGWIFGTTLDSKTQSLLIVNNATNVVIKVCEFQFCNDPFLDV
...
VLKGVKLHYT
```

---

## Configuration

Upon opening the script, near the top, global configurations can be found that can be changed as needed:

| Global Name  | Description                       | Default value |
| ------------ | --------------------------------- | ------------- |
| INPUT_FILE   | Expected input file name          | input.txt     |
| OUTPUT_FILE  | Expected output file name         | output.txt    |
| BLOCK_LENGTH | Sequence character limit per line | 60            |

---

## Running the Program

### Windows

1. Open the folder containing the files.

2. Click in the address bar at the top of File Explorer.

3. Type:

   ```
   cmd
   ```

4. Press **Enter**.

A Command Prompt window will open.

5. Type:

   ```
   python sequencebreaker.py
   ```

6. Press **Enter**.

If that doesn't work, try:

```
py sequencebreaker.py
```

---

## Output

When the program finishes, you'll see a message similar to:

```
Done! Completed in 0.010 seconds.
Output written to output file: output.txt
```

A new file named `output.txt` will appear in the same folder.

The output file will be formatted similar to the following:

```
seq1  MFVFLVLLPLVSSQCVNLTTRTQLPPAYTNSFTRGVYYPDKVFRSSVLHSTQDLFLPFFS 60
seq2  MFVFLVLLPLVSSQCVNLITRTQSYTNSFTRGVYYPDKVFRSSVLHSTQDLFLPFFSNVT 60
...
seq20 MFVFLVLLPLVSSQCVNLITRTQSYTNSFTRGVYYPDKVFRSSVLHSTQDLFLPFFSNVT 60
      ******************.****...............................*.....

seq1  NVTWFHVISGTNGTKRFDNPVLPFNDGVYFASIEKSNIIRGWIFGTTLDSKTQSLLIVNN 120
seq2  WFHAIHVSGTNGTKRFDNPVLPFNDGVYFASTEKSNIIRGWIFGTTLDSKTQSLLIVNNA 120
...
seq20 WFHAIHVSGTNGTKRFDNPVLPFNDGVYFASTEKSNIIRGWIFGTTLDSKTQSLLIVNNA 120
      .....**..............................*.......*........*...*.
```

---

## Troubleshooting

### "python is not recognized"

Python is either not installed or was installed without selecting **Add Python to PATH**.

Try:

```
py sequencebreaker.py
```

If that also fails, reinstall Python and make sure **Add Python to PATH** is checked during installation.

---

### "FileNotFoundError: input.txt"

The program could not find `input.txt`.

Make sure:

* `input.txt` exists.
* It is in the same folder as `sequencebreaker.py`.
* The file name is spelled exactly `input.txt`.