# -*- coding: utf-8 -*-
"""Loan Qualifier Application.

This is a command line application to match applicants with qualifying loans.

Example:
    $ python app.py
"""
import sys
import fire
import questionary
import pandas as pd
from pathlib import Path

from qualifier.utils.fileio import load_csv

from qualifier.utils.calculators import (
    calculate_monthly_debt_ratio,
    calculate_loan_to_value_ratio,
)

from qualifier.filters.max_loan_size import filter_max_loan_size
from qualifier.filters.credit_score import filter_credit_score
from qualifier.filters.debt_to_income import filter_debt_to_income
from qualifier.filters.loan_to_value import filter_loan_to_value


def load_bank_data():
    """Ask for the file path to the latest banking data and load the CSV file.
    Returns:
        The bank data from the data rate sheet CSV file.
    """

    csvpath = questionary.text("Enter a file path to a rate-sheet (.csv):").ask()
    csvpath = Path(csvpath)
    if not csvpath.exists():
        sys.exit(f"Oops! Can't find this path: {csvpath}")

    return load_csv(csvpath)


def get_applicant_info():
    """Prompt dialog to get the applicant's financial information.

    Returns:
        Returns the applicant's financial information.
    """

    credit_score = questionary.text("What's your credit score?").ask()
    debt = questionary.text("What's your current amount of monthly debt?").ask()
    income = questionary.text("What's your total monthly income?").ask()
    loan_amount = questionary.text("What's your desired loan amount?").ask()
    home_value = questionary.text("What's your home value?").ask()

    credit_score = int(credit_score)
    debt = float(debt)
    income = float(income)
    loan_amount = float(loan_amount)
    home_value = float(home_value)

    return credit_score, debt, income, loan_amount, home_value


def find_qualifying_loans(bank_data, credit_score, debt, income, loan, home_value):
    """Determine which loans the user qualifies for.

    Loan qualification criteria is based on:
        - Credit Score
        - Loan Size
        - Debit to Income ratio (calculated)
        - Loan to Value ratio (calculated)

    Args:
        bank_data (list): A list of bank data.
        credit_score (int): The applicant's current credit score.
        debt (float): The applicant's total monthly debt payments.
        income (float): The applicant's total monthly income.
        loan (float): The total loan amount applied for.
        home_value (float): The estimated home value.

    Returns:
        A list of the banks willing to underwrite the loan.

    """

    # Calculate the monthly debt ratio
    monthly_debt_ratio = calculate_monthly_debt_ratio(debt, income)
    print(f"The monthly debt to income ratio is {monthly_debt_ratio:.02f}")

    # Calculate loan to value ratio
    loan_to_value_ratio = calculate_loan_to_value_ratio(loan, home_value)
    print(f"The loan to value ratio is {loan_to_value_ratio:.02f}.")

    # Run qualification filters
    bank_data_filtered = filter_max_loan_size(loan, bank_data)
    bank_data_filtered = filter_credit_score(credit_score, bank_data_filtered)
    bank_data_filtered = filter_debt_to_income(monthly_debt_ratio, bank_data_filtered)
    bank_data_filtered = filter_loan_to_value(loan_to_value_ratio, bank_data_filtered)

    print(f"Found {len(bank_data_filtered)} qualifying loans")

    return bank_data_filtered

def save_csv(qualifying_loans):
    # prompt - ask csv file name and path to save as: 
    csvpath = questionary.text("Enter an output file path to save the qualifying data as a file(.csv):").ask()
    csvpath = Path(csvpath)
    
    try:
        # saving the qualifying data as a csv file.
        # header same as original data
    
    
        header = ['Lender','MaxLoanAmount','MaxLTV','MaxDTI','MinCreditScore','InterestRate']
    
        df_qalifyingloans = pd.DataFrame(qualifying_loans, columns = header)
    
        # Save as csv
        df_qalifyingloans.to_csv(csvpath, index = False)
            
    except Exception as e:
        print("Failed saving the output file. {0}".format(e))
        #raise exceptions error
    print(f"Successfully saved the output file at {csvpath}")
    
def save_qualifying_loans(qualifying_loans):
    """Saves the qualifying loans to a CSV file.
    Args:
        qualifying_loans (list of lists): The qualifying bank loans.
    """
    
    # Only save prompt if qualifying loans exist (>0)
    if len(qualifying_loans) > 0 :
        answer = questionary.text("Would you like to save your qualifying loans? (Enter yes or no)").ask()
        answer = answer.strip() #Trim whitespaces
        answer = answer.lower() #Lower case
        # if answer is yes, then 'save_csv' function
        if answer == "yes":
            save_csv(qualifying_loans)  
        elif answer == "no":
            print("No: Skipped saving the output file")
        else:
            print("Error: Invalid answer (neither yes nor no) - skipped saving the output file ")
    else:
        # if not found, then no need to ask prompt
        print("No data to save (0 qulifying loans)")
    

def run():
    """The main function for running the script."""

    # Load the latest Bank data
    bank_data = load_bank_data()

    # Get the applicant's information
    credit_score, debt, income, loan_amount, home_value = get_applicant_info()

    # Find qualifying loans
    qualifying_loans = find_qualifying_loans(
        bank_data, credit_score, debt, income, loan_amount, home_value
    )

    # Save qualifying loans
    save_qualifying_loans(qualifying_loans)


if __name__ == "__main__":
    fire.Fire(run)
