import csv
import sys

# Initialize an empty dictionary to store the amino acid data
AMINOACIDS = {}

# Open the file and load data correctly
with open('aminoacids.csv', 'r') as file:
    reader = csv.reader(file)
    header = next(reader)  # Read the header row

    # Process each row in the CSV
    for line in reader:
        # Skip rows that do not have enough columns
        if len(line) < 22:
            print(f"Skipping incomplete line: {line}")
            continue
        
        # Safely create a dictionary entry for each amino acid
        aminoacid_data = {
            'Name':              line[0],
            'Abbr':              line[1],
            'Letter':            line[2],
            'Molecular Weight':  line[3],
            'Molecular Formula': line[4],
            'Residue Formula':   line[5],
            'Residue Weight':    line[6],
            'pKa1':              line[7] if line[7] else None,  
            'pKb2':              line[8] if line[8] else None, 
            'pKx3':              line[9] if line[9] else None, 
            'pl4':               line[10] if line[10] else None,
            'H':                 line[11] if line[11] else None,
            'VSC':               line[12] if line[12] else None,
            'P1':                line[13] if line[13] else None,
            'P2':                line[14] if line[14] else None,
            'SASA':              line[15] if line[15] else None,
            'NCISC':             line[16] if line[16] else None,
            'carbon':            line[17] if line[17] else None,
            'hydrogen':          line[18] if line[18] else None,
            'nitrogen':          line[19] if line[19] else None,
            'oxygen':            line[20] if line[20] else None,
            'sulfur':            line[21] if len(line) > 21 else None
        }

        # Add the amino acid entry to the main dictionary
        # Assuming 'Name' is unique, we'll store each amino acid by its 'Name' key
        AMINOACIDS[line[0]] = aminoacid_data
        AMINOACIDS[line[1]] = aminoacid_data
        AMINOACIDS[line[2]] = aminoacid_data

# List of all the columns to print
ALL_COLUMNS = ['Name', 'Abbr', 'Letter', 'Molecular Weight', 'Molecular Formula',
               'Residue Formula', 'Residue Weight', 'pKa1', 'pKb2', 'pKx3',
               'pl4', 'H', 'VSC', 'P1', 'P2', 'SASA', 'NCISC', 'carbon',
               'hydrogen', 'nitrogen', 'oxygen', 'sulfur']

# Justifying the columns by finding the longest string in ALL_COLUMNS
LONGEST_COLUMN = max(len(key) for key in ALL_COLUMNS)

# Display amino acid properties to the user
print("Amino acids properties loaded successfully!")
print('Enter the name, symbol or three letter code of the aminoacid or "quit" to exit')

while True:
    response = input('> ').title()

    if response.lower() == "quit":
        sys.exit()  # Exit the program when the user types "Quit"

    # Check if the response matches a key in AMINOACIDS
    if response in AMINOACIDS:
        # Loop through all columns and display the properties of the requested amino acid
        for key in ALL_COLUMNS:
            keyJustified = key.rjust(LONGEST_COLUMN)
            value = AMINOACIDS[response].get(key, 'N/A')  # Use 'N/A' if the key is missing
            print(f"{keyJustified}: {str(value) if value is not None else 'N/A'}")
        
        input('Press Enter to continue...')
    else:
        print("Amino acid not found. Please enter a valid symbol or 'Quit' to exit.")
