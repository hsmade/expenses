from django.db import models
from django.utils.translation import ugettext as T
# TODO implement tags for payments (mortgage, energy, etc)


class Month(models.Model):
    """
    A 'month' represents the period starting on the date of payment of salary to the next.
    I will most likely run from 25th to 25th and is named after the second month in the period
    The balance will start with the ending balance of the previous month
    """
    year = models.IntegerField()
    month = models.IntegerField()
    # balance = models.DecimalField(max_digits=6, decimal_places=2)

    def balance(self):
        balance = 0
        deposits = Deposit.objects.filter(month=self)
        withdrawals = Withdrawal.objects.filter(month=self)
        for deposit in deposits:
            balance += deposit.amount
        for withdrawal in withdrawals:
            balance -= withdrawal.amount
        return balance

    def __unicode__(self):
        return unicode('{}/{}'.format(self.year, self.month))

    def __str__(self):
        return self.__unicode__()


class DepositType(models.Model):
    """
    A type of deposit, like:
     - tax return
     - salary
    """
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)

    def __unicode__(self):
        return unicode(self.name)

    def __str__(self):
        return self.__unicode__()


class Deposit(models.Model):
    month = models.ForeignKey(Month)
    description = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=6, decimal_places=2)
    date = models.DateField(T('date deposited'))
    deposit_type = models.ForeignKey(DepositType, null=True, blank=True, default=None)
    account_number = models.CharField(T('opposite account number, if any'), max_length=34, blank=True, null=True)

    def __unicode__(self):
        return unicode('({}) {}'.format(self.date, self.description))

    def __str__(self):
        return self.__unicode__()


class WithdrawalType(models.Model):
    """
    A type of withdrawal, like:
     - recurring payment
     - allowance
    """
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    max_allowed = models.IntegerField(default=0)

    def __unicode__(self):
        return unicode(self.name)

    def __str__(self):
        return self.__unicode__()


class Withdrawal(models.Model):
    month = models.ForeignKey(Month)
    description = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=6, decimal_places=2)
    date = models.DateField('date deposited')
    withdrawal_type = models.ForeignKey(WithdrawalType, null=True, blank=True, default=None)
    account_number = models.CharField(T('opposite account number, if any'), max_length=34, blank=True, null=True)

    def __unicode__(self):
        return '({}) {}'.format(self.date, self.description)

    def __str__(self):
        return self.__unicode__()


class Reservation(models.Model):
    """
    A reservation for a future payment or a reserve.
    Can have a due date, and can have an automatic increase (monthly)
    """
    description = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=6, decimal_places=2)
    due_date = models.DateField(blank=True, null=True)
    automatic_increase = models.IntegerField(default=0)

    def __unicode__(self):
        return unicode(self.description)

    def __str__(self):
        return self.__unicode__()


