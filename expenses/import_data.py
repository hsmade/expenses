__author__ = 'wfournier'
from expenses.lib import rabo
from expenses.models import Month, Deposit, DepositType, Withdrawal, WithdrawalType


def import_rabo(file_name, month):
    data = rabo.CSVExport(file_name)
    try:
        new_deposit_type = DepositType.objects.get(name='New')
    except:
        new_deposit_type = DepositType.objects.create(name='New')
    try:
        new_withdrawal_type = WithdrawalType.objects.get(name='New')
    except:
        new_withdrawal_type = WithdrawalType.objects.create(name='New')

    for transaction in data.transactions:
        print 'Handling {}'.format(transaction.description)
        if transaction.credit:
            new_deposit = Deposit.objects.create(
                month=month,
                description=transaction.description,
                account_number=transaction.account_number,
                date=transaction.booking_date,
                amount=transaction.amount,
                deposit_type=new_deposit_type
            )
            new_deposit.save()
        elif transaction.debet:
            new_withdrawal = Withdrawal.objects.create(
                month=month,
                description=transaction.description,
                account_number=transaction.account_number,
                date=transaction.booking_date,
                amount=transaction.amount,
                withdrawal_type=new_withdrawal_type
            )
            new_withdrawal.save()

