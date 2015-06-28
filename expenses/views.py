from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.views import generic
from .models import Month, Withdrawal, Deposit, WithdrawalType, DepositType
from collections import namedtuple
from django.core.urlresolvers import reverse
from django.forms import ModelForm
from django.forms.extras.widgets import SelectDateWidget


class DepositForm(ModelForm):
    class Meta:
        model = Deposit
        fields = '__all__'
        widgets = {
            'date': SelectDateWidget(),
        }


class WithdrawalForm(ModelForm):
    class Meta:
        model = Withdrawal
        fields = '__all__'
        widgets = {
            'date': SelectDateWidget(),
        }


class IndexView(generic.ListView):
    """
    Shows the last 6 months with their balance
    """
    template_name = 'expenses/index.html'
    context_object_name = 'months'

    def get_queryset(self):
        return Month.objects.filter(year=timezone.now().year,
                                    ).order_by('month')[:6]


def month_detail(request, pk):
    """
    Shows an overview of the month with the deposits, withdrawals, budgets and balance
    :param request:
    :param pk: the month ID
    """
    month = Month.objects.get(id=pk)
    withdrawals = Withdrawal.objects.filter(month=month)
    deposits = Deposit.objects.filter(month=month)
    withdrawal_types = WithdrawalType.objects.all()
    budgets = []
    budget = namedtuple('budget', 'type withdrawals unused')
    for withdrawal_type in withdrawal_types:
        total = 0
        tmp_withdrawals = Withdrawal.objects.filter(withdrawal_type=withdrawal_type)
        for withdrawal in tmp_withdrawals:
            total += withdrawal.amount
        if withdrawal_type.max_allowed:
            unused = withdrawal_type.max_allowed - total
        else:
            unused = 0
        budgets.append(budget(
            withdrawal_type,
            tmp_withdrawals,
            unused
        ))

    context = {
        'month': month,
        'withdrawals': withdrawals,
        'deposits': deposits,
        'budgets': budgets,
        'withdrawal_form': WithdrawalForm(initial={'date': timezone.now().date(), 'month': month.id}),
        'deposit_form': DepositForm(initial={'date': timezone.now().date(), 'month': month.id}),
    }
    return render(request, 'expenses/month.html', context)


def add_or_update_withdrawal(request, pk, month):
    """
    Adds or updates a withdrawal
    :param request.POST: a dict with the POST fields:
      amount, description, account_number, date, withdrawal_type
    :param pk: the withdrawal ID, or -1 for new
    :param month: the month ID
    """
    month = get_object_or_404(Month, pk=month)
    withdrawal_type = get_object_or_404(WithdrawalType, pk=request.POST['withdrawal_type'])
    if pk == '-1':
        print 'Creating new withdrawal'
        withdrawal = Withdrawal.objects.create(
            month=month,
            description=request.POST['description'],
            account_number=request.POST['account_number'],
            date=request.POST['date'],
            amount=float(request.POST['amount']),
            withdrawal_type=withdrawal_type
        )
    else:
        withdrawal = get_object_or_404(Withdrawal, pk=int(pk))
        withdrawal.description = request.POST['description']
        withdrawal.account_number = request.POST['account_number']
        withdrawal.date = request.POST['date']
        withdrawal.amount = float(request.POST['amount'])
        withdrawal.withdrawal_type = withdrawal_type
    withdrawal.save()
    # TODO handle errors
    return redirect(reverse('expenses:month', args=(month.id,)))


def delete_withdrawal(request, pk, month):
    month = get_object_or_404(Month, pk=month)
    withdrawal = get_object_or_404(Withdrawal, pk=pk)
    withdrawal.delete()
    # TODO handle errors
    return redirect(reverse('expenses:month', args=(month.id,)))


def add_or_update_deposit(request, pk, month):
    """
    Adds or updates a deposit
    :param request.POST: a dict with the POST fields:
      amount, description, account_number, date, deposit_type
    :param pk: the deposit ID, or -1 for new
    :param month: the month ID
    """
    month = get_object_or_404(Month, pk=month)
    deposit_type = get_object_or_404(DepositType, pk=request.POST['deposit_type'])
    if pk == '-1':
        print 'Creating new deposit'
        deposit = Deposit.objects.create(
            month=month,
            description=request.POST['description'],
            account_number=request.POST['account_number'],
            date=request.POST['date'],
            amount=float(request.POST['amount']),
            deposit_type=deposit_type
        )
    else:
        deposit = get_object_or_404(Deposit, pk=int(pk))
        deposit.description = request.POST['description']
        deposit.account_number = request.POST['account_number']
        deposit.date = request.POST['date']
        deposit.amount = float(request.POST['amount'])
        deposit.deposit_type = deposit_type
    deposit.save()
    # TODO handle errors
    return redirect(reverse('expenses:month', args=(month.id,)))


def delete_deposit(request, pk, month):
    month = get_object_or_404(Month, pk=month)
    deposit = get_object_or_404(Deposit, pk=pk)
    deposit.delete()
    # TODO handle errors
    return redirect(reverse('expenses:month', args=(month.id,)))