import rpa
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


filepath = "transactions.csv"
transactions_data = pd.read_csv(filepath)


def account_reconciliation(filepath):
    transactions_data = pd.read_csv(filepath)
    transactions_data = transactions_data.sort_values(
        by=['Date'], ascending=True)
    transactions_data['Running_Balance'] = transactions_data['Amount'].cumsum()
    return transactions_data


def fraud_detection(transactions_data):
    mean_balance = transactions_data['Running_Balance'].mean()
    std_balance = transactions_data['Running_Balance'].std()

    transactions_data['debit'] = transactions_data['Amount'].where(
        transactions_data['Amount'] < 0, 0)
    transactions_data['credit'] = transactions_data['Amount'].where(
        transactions_data['Amount'] > 0, 0)

    mean_debit_credit_ratio = transactions_data['debit'].mean(
    ) / transactions_data['credit'].abs().mean()
    std_debit_credit_ratio = transactions_data['debit'].std(
    ) / transactions_data['credit'].abs().std()

    fraud_data = transactions_data[((transactions_data['Running_Balance'] < (mean_balance - 2 * std_balance)) |
                                    (transactions_data['Running_Balance'] > (mean_balance + 2 * std_balance))) &
                                   ((transactions_data['debit'] / transactions_data['credit'].abs() > (mean_debit_credit_ratio + 2 * std_debit_credit_ratio)) |
                                    (transactions_data['debit'] / transactions_data['credit'].abs() < (mean_debit_credit_ratio - 2 * std_debit_credit_ratio)))]
    fraud_data = fraud_data[['ID_Number', 'First_Name', 'Last_Name', 'Address',
                             'Date', 'Amount', 'debit', 'credit', 'Running_Balance', 'Description']]
    return fraud_data


def generate_report(fraud_data):
    plt.bar(fraud_data.index, fraud_data['Running_Balance'])
    plt.xlabel('Transaction Number')
    plt.ylabel('Running Balance')
    plt.title('Fraud Detection Report')
    plt.show()
    fraud_data.to_csv('fraud_detection_report.txt', sep='\t')


def compliance_reporting(transactions_data, fraud_data):
    compliant_data = transactions_data[~transactions_data.index.isin(
        fraud_data.index)]
    report_data = pd.concat([compliant_data.describe(), fraud_data.describe(
    )], axis=1, keys=['Compliant Transactions', 'Fraudulent Transactions'])
    with open('compliance_report.txt', 'w') as f:
        f.write(report_data.to_string())
    return report_data


def main():
    transactions = pd.read_csv(filepath)
    reconciled_data = account_reconciliation(filepath)
    fraud_data = fraud_detection(reconciled_data)
    fraud_indexes = fraud_data.index.tolist()
    print("Fraudulent transactions detected for the following accounts:")
    for i in range(len(fraud_indexes)):
        print("Account Name:", transactions.iloc[fraud_indexes[i], 3])
        print("ID Number:", transactions.iloc[fraud_indexes[i], 4])
        print()
    generate_report(fraud_data)
    compliance_report = compliance_reporting(transactions, fraud_data)

    # Use RPA to automate the steps
    fraud_detected = False
    if len(fraud_indexes) > 0:
        fraud_detected = True
        # Automate the sending of a notification or alert to the relevant parties
        rpa.send_notification(fraud_detected)

    if fraud_detected:
        # Automate the opening of the fraud detection report
        rpa.open_file('fraud_detection_report.txt')

        # Automate the opening of the compliance report
        rpa.open_file('compliance_report.txt')


if __name__ == "__main__":
    main()
