# Session Documentation: Exchange Rate Python Program Development

This document summarizes the development of a Python program (`generate_exchange_rates_csv.py`) to process exchange rate data from a CSV file and generate a new CSV with specific currency conversions.

## Steps Followed:

1.  **Initial Request & Context Setup:** The session began with the user providing detailed context about their environment, including the working directory and file structure.
2.  **Initial Data Extraction & Debugging:**
    *   The user requested a Python program to extract SGD-to-INR, USD-to-SGD, and USD-to-INR exchange rates from `reference-data/API_PA.NUS.FCRF_DS2_en_csv_v2_123253.csv`.
    *   An initial version of the script was provided.
    *   **Issue 1: `IndexError`:** The script initially failed due to incorrect skipping of metadata rows.
    *   **Resolution 1:** The script was updated to skip the first 3 metadata rows.
    *   **Issue 2: Empty Output CSV / "No common years" error:** The script ran but produced an empty CSV, indicating no data was being extracted for the target currencies (SGP, IND, USA).
    *   **Debugging 1:** Added print statements to inspect the `exchange_rates` dictionary, confirming it was empty.
    *   **Debugging 2:** Refactored the script to read all data rows into a list before processing.
    *   **Debugging 3:** Added more targeted print statements to trace `country_code`, `indicator_code`, and raw exchange rate values during processing.
    *   **Issue 3: Header and Years not read:** Debugging revealed `Header: []` and `All Years: []`, indicating the CSV header was not being read correctly. This was suspected to be due to a Byte Order Mark (BOM).
    *   **Resolution 3:** Changed the file opening encoding to `utf-8-sig` to handle the BOM.
    *   **Issue 4: Still empty header/years:** Even with `utf-8-sig`, the header was empty. Further inspection of the CSV revealed an empty line between the metadata and the actual header.
    *   **Resolution 4:** Increased the number of skipped rows from 3 to 4 to account for the empty line.
    *   **Verification:** After these changes, the script successfully generated the output CSV.
3.  **Code Refinement & Project Structure:**
    *   Removed all debugging print statements from the script.
    *   Updated the script to use relative paths for input and output files.
    *   Converted input and output file paths to static variables (`INPUT_FILE`, `OUTPUT_FILE`) at the beginning of the script.
    *   Changed the output filename to `reference-data/output-exchange-rate-history-INR-SGD-USD.csv`.
    *   Moved the Python program to `reference-data/src/gen-exchange-ccy.py`.
    *   Updated relative paths within `gen-exchange-ccy.py` to reflect its new location.
    *   Created a `README.md` file in `reference-data/` with instructions on how to run the Python program and where to download the input file.
    *   Updated `gen-exchange-ccy.py` to create the output directory (`reference-data/output/`) if it doesn't exist.
    *   Updated `README.md` to remove absolute paths.
    *   Created a `.gitignore` file in the project root to exclude all `.csv` and `.xlsx` files.
    *   Handled the `currency-a-side` directory, which was initially added as a submodule, by removing its `.git` directory and adding its files directly to the main project repository.

## User Prompts for Future Gemini Interactions:

*   "Generate a Python program to calculate SGD-to-INR, USD-to-SGD, and USD-to-INR exchange rates from `reference-data/API_PA.NUS.FCRF_DS2_en_csv_v2_123253.csv` and output to `exchange_rates_summary.csv`."
*   "The script is failing with an IndexError, it seems to be reading metadata as data."
*   "The script is generating an empty CSV, and printing 'Error: No common years with complete exchange rate data found'."
*   "The header and years are not being read correctly from the CSV."
*   "Update the program to use only relative paths for both source dataset and output dataset."
*   "Both input and output should be static variables declared at the start of the python code."
*   "Output file should be `reference-data/output-exchange-rate-history-INR-SGD-USD.csv`."
*   "Move the python program to `reference-data/src` and rename to `gen-exchange-ccy.py`."
*   "Create a `README.md` file inside `reference-data/` on how to run the python file and reference to where the input file should be downloaded from https://data.worldbank.org/indicator/PA.NUS.FCRF?locations=AF. The `python3` should be run from the `reference-data/` folder and the output should be generated in the `reference-data/output` folder. Create output folder if the folder is missing when executing the python program."
*   "Update readme and all files no absolute path or sensitive information."
*   "Create a `.gitignore` to exclude all csv excel files."
*   "Remove the `.git` from the `currency-a-side/` and add its files to the main project."