# -*- coding: utf-8 -*-
"""Helper functions to load and save CSV data.

This contains a helper function for loading and saving CSV files.

"""
import csv


def load_csv(csvpath):
    """Reads the CSV file from path provided.

    Args:
        csvpath (Path): The csv file path.

    Returns:
        A list of lists that contains the rows of data from the CSV file.

    """
    with open(csvpath, "r") as csvfile:
        data = []
        csvreader = csv.reader(csvfile, delimiter=",")

        # Skip the CSV Header
        next(csvreader)

        # Read the CSV data
        for row in csvreader:
            data.append(row)
    return data

def save_csv(loan_data, csvpath):
    """Saves the CSV file to the path provided.
    
    Args:
        loan_data (List[List]): The qualifying bank loans.
        csvpath (Path)        : The csv file path.
        
    Returns:
        None
    
    """
    # get the header from a static reference
    with open("data/daily_rate_sheet.csv", "r") as rate_sheet:
        header = rate_sheet.readline().strip().split(',')

    with open(csvpath, "w", newline="") as csvfile:
        w = csv.writer(csvfile)
        w.writerow(header)
        w.writerows(loan_data)
