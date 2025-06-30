# Session Documentation: CPI Inflation Python Program Development

This document summarizes the development of a Python program (`gen-exchange-ccy.py`) to process inflation rate data from a CSV file and generate a new CSV with specific country inflation rates.

## Steps Followed:

1.  **Initial Request & Context Setup:** The session began with the user requesting a new function in the existing Python file to read inflation data and generate a new CSV.
2.  **Code Modification:**
    *   A new function `generate_inflation_rates_csv` was added to `reference-data/src/gen-exchange-ccy.py`.
    *   This function reads `reference-data/API_FP.CPI.TOTL.ZG_DS2_en_csv_v2_127296.csv`.
    *   It extracts yearly inflation rates for Singapore (SGP), India (IND), and United States (USA) from 1991 onwards.
    *   The output is written to `output/output-inflation-rate-history-INR-SGD-USD.csv`.
    *   The `if __name__ == "__main__":` block was updated to call both `generate_exchange_rates_csv` and `generate_inflation_rates_csv`.
