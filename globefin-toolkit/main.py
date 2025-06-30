import csv
import os

XCHANGE_INPUT_FILE = "./API_PA.NUS.FCRF_DS2_en_csv_v2_123253.csv"
XCHANGE_OUTPUT_FILE = "../output/output-exchange-rate-history-INR-SGD-USD.csv"

INFLATION_INPUT_FILE = "./API_FP.CPI.TOTL.ZG_DS2_en_csv_v2_127296.csv"
INFLATION_OUTPUT_FILE = "../output/output-inflation-rate-history-INR-SGD-USD.csv"

def generate_exchange_rates_csv(input_csv_path, output_csv_path):
    """
    Reads exchange rate data from an input CSV, calculates SGD-to-INR rates,
    and writes the results along with USD-to-SGD and USD-to-INR rates to a new CSV.
    """
    exchange_rates = {}
    all_years = []
    data_rows = []

    with open(input_csv_path, mode='r', newline='', encoding='utf-8-sig') as infile:
        reader = csv.reader(infile)
        
        # Skip metadata rows and the empty row before the header
        for _ in range(4):
            next(reader)

        header = next(reader) # This should now be the actual header

        # Extract all possible years from the header
        all_years = [year for year in header[4:] if year.isdigit()]

        # Read all data rows into a list
        for row in reader:
            data_rows.append(row)

    # Process data rows to extract exchange rates for SGP, IND, USA
    for row in data_rows:
        if len(row) < 4:
            continue

        country_code = row[1]
        indicator_code = row[3]

        if indicator_code == "PA.NUS.FCRF": # Official exchange rate (LCU per US$)
            rates = {}
            for i, year in enumerate(all_years):
                try:
                    rate = float(row[i + 4]) # Rates start from the 5th column
                    rates[year] = rate
                except (ValueError, IndexError):
                    rates[year] = None # Handle empty, non-numeric, or missing values

            if country_code == "SGP":
                exchange_rates['SGP'] = rates
            elif country_code == "IND":
                exchange_rates['IND'] = rates
            elif country_code == "USA":
                exchange_rates['USA'] = rates

    # Filter years to only include those where all three currencies have data
    # and start from 1991 as SGP data begins then.
    valid_years = []
    for year in all_years:
        if int(year) >= 1991 and \
           exchange_rates.get('SGP') and exchange_rates['SGP'].get(year) is not None and \
           exchange_rates.get('IND') and exchange_rates['IND'].get(year) is not None and \
           exchange_rates.get('USA') and exchange_rates['USA'].get(year) is not None:
            valid_years.append(year)

    if not valid_years:
        print("Error: No common years with complete exchange rate data found for SGP, IND, and USA from 1991 onwards.")
        return

    output_data = []
    output_data.append(['Year', 'SGD-to-INR', 'USD-to-SGD', 'USD-to-INR'])

    for year in valid_years:
        usd_to_ind = exchange_rates['IND'][year]
        usd_to_sgp = exchange_rates['SGP'][year]
        usd_to_usa = 1.0 # USD to USD is always 1.0

        sgd_to_inr = None
        if usd_to_sgp != 0:
            sgd_to_inr = usd_to_ind / usd_to_sgp

        output_data.append([
            year,
            f"{sgd_to_inr:.4f}" if sgd_to_inr is not None else '',
            f"{usd_to_sgp:.4f}",
            f"{usd_to_ind:.4f}"
        ])

    output_dir = os.path.dirname(output_csv_path)
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    with open(output_csv_path, mode='w', newline='', encoding='utf-8') as outfile:
        writer = csv.writer(outfile)
        writer.writerows(output_data)

    print(f"Successfully generated {output_csv_path}")



def generate_inflation_rates_csv(input_csv_path, output_csv_path):
    """
    Reads inflation rate data from an input CSV for SGD, INR, and USD,
    and writes the yearly inflation rates from 1991 to a new CSV.
    """
    inflation_rates = {}
    all_years = []
    data_rows = []

    with open(input_csv_path, mode='r', newline='', encoding='utf-8-sig') as infile:
        reader = csv.reader(infile)
        
        # Skip metadata rows and the empty row before the header
        for _ in range(4):
            next(reader)

        header = next(reader) # This should now be the actual header

        # Extract all possible years from the header
        all_years = [year for year in header[4:] if year.isdigit()]

        # Read all data rows into a list
        for row in reader:
            data_rows.append(row)

    # Process data rows to extract inflation rates for SGP, IND, USA
    for row in data_rows:
        if len(row) < 4:
            continue

        country_code = row[1]
        indicator_code = row[3]

        if indicator_code == "FP.CPI.TOTL.ZG": # Inflation, consumer prices (annual %)
            rates = {}
            for i, year in enumerate(all_years):
                try:
                    rate = float(row[i + 4]) # Rates start from the 5th column
                    rates[year] = rate
                except (ValueError, IndexError):
                    rates[year] = None # Handle empty, non-numeric, or missing values

            if country_code == "SGP":
                inflation_rates['SGP'] = rates
            elif country_code == "IND":
                inflation_rates['IND'] = rates
            elif country_code == "USA":
                inflation_rates['USA'] = rates

    # Filter years to only include those where all three currencies have data from 1991
    valid_years = []
    for year in all_years:
        if int(year) >= 1991 and \
           inflation_rates.get('SGP') and inflation_rates['SGP'].get(year) is not None and \
           inflation_rates.get('IND') and inflation_rates['IND'].get(year) is not None and \
           inflation_rates.get('USA') and inflation_rates['USA'].get(year) is not None:
            valid_years.append(year)

    if not valid_years:
        print("Error: No common years with complete inflation rate data found for SGP, IND, and USA from 1991 onwards.")
        return

    output_data = []
    output_data.append(['Year', 'SGD Inflation (%)', 'INR Inflation (%)', 'USD Inflation (%)'])

    for year in valid_years:
        sgd_inflation = inflation_rates['SGP'][year]
        inr_inflation = inflation_rates['IND'][year]
        usd_inflation = inflation_rates['USA'][year]

        output_data.append([
            year,
            f"{sgd_inflation:.4f}",
            f"{inr_inflation:.4f}",
            f"{usd_inflation:.4f}"
        ])

    print(f"Inflation output_csv_path: {output_csv_path}")
    output_dir = os.path.dirname(output_csv_path)
    print(f"Inflation output_dir: {output_dir}")
    if not os.path.exists(output_dir):
        print(f"Creating directory: {output_dir}")
        os.makedirs(output_dir)

    if not output_data:
        print("Warning: No inflation data to write.")
        return

    with open(output_csv_path, mode='w', newline='', encoding='utf-8') as outfile:
        writer = csv.writer(outfile)
        writer.writerows(output_data)

    print(f"Successfully generated {output_csv_path}")

if __name__ == "__main__":
    generate_exchange_rates_csv(XCHANGE_INPUT_FILE, XCHANGE_OUTPUT_FILE)
    generate_inflation_rates_csv(INFLATION_INPUT_FILE, INFLATION_OUTPUT_FILE)
