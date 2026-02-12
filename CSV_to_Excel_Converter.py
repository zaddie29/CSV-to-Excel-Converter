import pandas as pd
import argparse
import logging
import os

logging.basicConfig(
    filename='Cleaned_dataset.csv',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def clean_data(df):
    """Clean and normalize the dataframe"""

    df = df.drop_duplicates()

    df = df.fillna("N/A")

    for col in df.columns:
        try:
            df[col] = pd.to_datetime(df[col])
        except:
            pass

    df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

    return df


def convert_csv_to_excel(input_file, output_file):
    """Convert CSV to Excel with cleaning"""

    try:
        if not os.path.exists(input_file):
            logging.error("File does not exist.")
            print(" Error: Input file not found.")
            return

        df = pd.read_csv(input_file)
        logging.info("CSV file loaded successfully.")

        df = clean_data(df)

        df.to_excel(output_file, index=False, engine='openpyxl')
        logging.info("File converted successfully.")

        print(f" Conversion successful! File saved as {output_file}")

    except Exception as e:
        logging.error(f"Error occurred: {e}")
        print(" Something went wrong. Check converter.log")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="CSV to Excel Converter")

    parser.add_argument("input", help="Path to input CSV file")
    parser.add_argument("output", help="Path to output Excel file")

    args = parser.parse_args()

    convert_csv_to_excel(args.input, args.output)