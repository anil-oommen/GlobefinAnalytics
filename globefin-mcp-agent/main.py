import csv
import os
from server import mcp

PROJECT_OUTPUT = os.path.join(os.path.dirname(__file__), '..', 'output')
XCHANGE_DATA_FILE = "output-exchange-rate-history-INR-SGD-USD.csv"
INFLATION_DATA_FILE = "output-inflation-rate-history-INR-SGD-USD.csv"


@mcp.tool()
def get_exchange_rate_history(from_currency: str, to_currency: str) -> list[dict]:
    """
    Returns historical currency exchange rates from 1991 to 2024 for specified currencies.
    Args:
        from_currency (str): The currency to convert from (e.g., 'USD', 'SGD', 'INR').
        to_currency (str): The currency to convert to (e.g., 'USD', 'SGD', 'INR').
    Returns:
        list[dict]: A list of dictionaries, each containing the 'Year' and the calculated
                    exchange rate for the specified currency pair.
    Raises:
        ValueError: If invalid currencies are provided or if from_currency and to_currency are the same.
    """
    valid_currencies = {'SGD', 'INR', 'USD'}

    if from_currency not in valid_currencies or to_currency not in valid_currencies:
        raise ValueError("Invalid currency. Must be SGD, INR, or USD.")

    if from_currency == to_currency:
        raise ValueError("From and To currencies cannot be the same.")

    file_path = os.path.join(os.path.dirname(__file__), '..', 'output', XCHANGE_DATA_FILE)
    all_data = []
    try:
        with open(file_path, 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                all_data.append({k: float(v) if k != 'Year' else int(v) for k, v in row.items()})
    except FileNotFoundError:
        print(f"Error: CSV file not found at {file_path}")
        return []

    results = []
    for year_data in all_data:
        year = year_data['Year']
        rate = None

        # Direct conversions from CSV
        if from_currency == 'USD' and to_currency == 'SGD':
            rate = year_data['USD-to-SGD']
        elif from_currency == 'USD' and to_currency == 'INR':
            rate = year_data['USD-to-INR']
        elif from_currency == 'SGD' and to_currency == 'INR':
            rate = year_data['SGD-to-INR']
        # Inverse conversions
        elif from_currency == 'SGD' and to_currency == 'USD':
            rate = 1 / year_data['USD-to-SGD']
        elif from_currency == 'INR' and to_currency == 'USD':
            rate = 1 / year_data['USD-to-INR']
        elif from_currency == 'INR' and to_currency == 'SGD':
            rate = 1 / year_data['SGD-to-INR']

        if rate is not None:
            results.append({'Year': year, f'{from_currency}-to-{to_currency}': rate})

    return results


@mcp.tool()
def get_inflation_rate_history(for_currency: str) -> list[dict]:
    """
    Returns historical inflation rates from 1991 to 2024 for a specified currency.
    Args:
        for_currency (str): The currency for which to get the inflation rate (e.g., 'USD', 'SGD', 'INR').
    Returns:
        list[dict]: A list of dictionaries, each containing the 'Year' and the inflation rate
                    for the specified currency.
    Raises:
        ValueError: If an invalid currency is provided.
    """
    valid_currencies = {'SGD', 'INR', 'USD'}

    if for_currency not in valid_currencies:
        raise ValueError("Invalid currency. Must be SGD, INR, or USD.")

    file_path = os.path.join(os.path.dirname(__file__), '..', 'output', INFLATION_DATA_FILE)
    all_data = []
    try:
        with open(file_path, 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                all_data.append({k: float(v) if k != 'Year' else int(v) for k, v in row.items()})
    except FileNotFoundError:
        print(f"Error: CSV file not found at {file_path}")
        return []

    results = []
    for year_data in all_data:
        year = year_data['Year']
        rate = None

        if for_currency == 'USD':
            rate = year_data['USD Inflation (%)']
        elif for_currency == 'SGD':
            rate = year_data['SGD Inflation (%)']
        elif for_currency == 'INR':
            rate = year_data['INR Inflation (%)']

        if rate is not None:
            results.append({'Year': year, f'Inflation-Rate-{for_currency}': rate})

    return results


if __name__ == "__main__":
     print("Starting the MCP server...",PROJECT_OUTPUT)
     #print(get_exchange_rate_history('SGD', 'INR'))
     mcp.run()
