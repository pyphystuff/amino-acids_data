Amino Acid Properties Viewer

Description
The Amino Acid Properties Viewer is a command-line program that allows users to query detailed biochemical and physical properties of amino acids. It reads amino acid data from a CSV file, organizes it into a structured format, and enables the user to retrieve information by entering the amino acid's name, abbreviation, or single-letter code.

This tool is useful for students, researchers, and educators in biochemistry, molecular biology, and computational biology, providing quick access to essential amino acid data such as molecular weight, pKa values, residue formulas, and more.

Features
Load amino acid properties from a CSV file.
Search for amino acid properties by full name, three-letter abbreviation, or single-letter code.
Display properties in a clean, column-justified format for better readability.
Include attributes like molecular weight, pKa values, SASA, and elemental composition.
Exit the program gracefully by typing "Quit".
Requirements
Python 3.x
CSV file containing amino acid data (e.g., aminoacids.csv).

Installation
Ensure you have Python 3.x installed.
You can download Python from https://www.python.org/.
Place your amino acid CSV file (e.g., aminoacids.csv) in the same directory as the script.
Save the provided Python script as aminoacid_viewer.py.


Usage
Open a terminal or command prompt.
Run the program by executing the script:

python aminoacid_viewer.py

Follow the prompts. You can:
Enter the name, three-letter abbreviation, or single-letter code of an amino acid to view its properties.
Type Quit (case-insensitive) to exit the program.

Troubleshooting
File Not Found: Ensure that aminoacids.csv is in the correct directory.
Missing or Corrupted Data: Check the CSV file for missing columns or rows. Ensure it follows the required format.
Python Errors: Make sure you're using Python 3.x and the script file is correctly formatted.
License
This program is distributed under the MIT License.
