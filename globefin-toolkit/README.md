# Data Transformation Program

This directory contains the Python script `main.py` for processing and transforming financial data.

## Functions

The script performs two main functions:

1.  **Exchange Rate Data Processing:**
    *   Reads exchange rate data from `API_PA.NUS.FCRF_DS2_en_csv_v2_123253.csv`.
    *   Calculates SGD-to-INR, USD-to-SGD, and USD-to-INR exchange rates.
    *   Outputs to `output/output-exchange-rate-history-INR-SGD-USD.csv`.

2.  **Inflation Rate Data Processing:**
    *   Reads inflation rate data from `API_FP.CPI.TOTL.ZG_DS2_en_csv_v2_127296.csv`.
    *   Extracts yearly inflation rates for SGD, INR, and USD from 1991 onwards.
    *   Outputs to `output/output-inflation-rate-history-INR-SGD-USD.csv`.

## Input Data

Please download the following CSV files and place them directly in this `globefin-toolkit` directory:

*   **Exchange Rate Data:** `API_PA.NUS.FCRF_DS2_en_csv_v2_123253.csv` from the World Bank Data website:
    [https://data.worldbank.org/indicator/PA.NUS.FCRF?locations=AF](https://data.worldbank.org/indicator/PA.NUS.FCRF?locations=AF)

*   **Inflation Rate Data:** `API_FP.CPI.TOTL.ZG_DS2_en_csv_v2_127296.csv` from the World Bank Data website:
    [https://data.worldbank.org/indicator/FP.CPI.TOTL.ZG?locations=IN](https://data.worldbank.org/indicator/FP.CPI.TOTL.ZG?locations=IN)

## Setup

This project uses `uv` for package management. To set up the virtual environment, run the following commands from within the `globefin-toolkit` directory:

```bash
uv venv
source .venv/bin/activate
```

## How to Run the Python Program

Once the virtual environment is activated, run the Python script from within the `globefin-toolkit` directory:

```bash
python main.py
```

## Output

The program will generate two output CSV files inside the `output` directory at the project root:

*   `output-exchange-rate-history-INR-SGD-USD.csv`
*   `output-inflation-rate-history-INR-SGD-USD.csv`

The `output` directory will be created automatically if it does not exist.