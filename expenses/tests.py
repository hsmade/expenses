from django.test import TestCase
from django.utils import timezone
from .models import Month, Withdrawal, Deposit, DepositType, WithdrawalType
from django.core.urlresolvers import reverse
from django.core.exceptions import ObjectDoesNotExist


class ExpensesViewTest(TestCase):
    def test_index_view(self):
        _ = Month.objects.create(year=2015, month=1)
        response = self.client.get(reverse('expenses:index'))
        self.assertContains(response, '2015/1: 0')

    def test_month_detail(self):
        month = Month.objects.create(year=2015, month=1)
        deposit_type = DepositType(name='deposit type')
        deposit_type.save()
        withdrawal_type = WithdrawalType(name='withdrawal type')
        withdrawal_type.save()
        _ = Deposit.objects.create(month=month, amount=20.0, description='test deposit',
                                   date=timezone.now(), deposit_type=deposit_type)
        _ = Withdrawal.objects.create(month=month, amount=5.0, description='test withdrawal',
                                      date=timezone.now(), withdrawal_type=withdrawal_type)
        response = self.client.get(reverse('expenses:month', args=(month.id,)))
        # print response.content
        self.assertContains(response, '2015/1')
        self.assertContains(response, '15.00')
        self.assertContains(response, 'test deposit')
        self.assertContains(response, 'test withdrawal')

    def test_add_withdrawal(self):
        month = Month.objects.create(year=2015, month=1)
        month.save()
        withdrawal_type = WithdrawalType.objects.create(name='withdrawal type')
        withdrawal_type.save()
        response = self.client.post(reverse('expenses:withdrawal', args=(month.id, -1)), {
            'description': 'description',
            'amount': 10,
            'date': timezone.now().date(),
            'withdrawal_type': withdrawal_type.id,
            'account_number': '1234',
        })
        print response
        self.assertEqual(response.status_code, 302)
        withdrawal = Withdrawal.objects.get(month=month, withdrawal_type=withdrawal_type)
        self.assertTrue(withdrawal)
        self.assertEqual(withdrawal.description, 'description')
        self.assertEqual(withdrawal.amount, 10.0)
        self.assertEqual(withdrawal.date, timezone.now().date())
        self.assertEqual(withdrawal.withdrawal_type, withdrawal_type)
        self.assertEqual(withdrawal.account_number, '1234')

    def test_update_withdrawal(self):
        month = Month.objects.create(year=2015, month=1)
        month.save()
        withdrawal_type = WithdrawalType.objects.create(name='withdrawal type')
        withdrawal_type.save()
        withdrawal1 = Withdrawal.objects.create(
            month=month,
            description='description',
            amount=10,
            date=timezone.now().date(),
            withdrawal_type=withdrawal_type,
            account_number='1234',
        )
        withdrawal1.save()
        response = self.client.post(reverse('expenses:withdrawal', args=(month.id, withdrawal1.id)), {
            'description': 'description2',
            'amount': 11,
            'date': timezone.now().date(),
            'withdrawal_type': withdrawal_type.id,
            'account_number': '12345',
        })
        print response
        self.assertEqual(response.status_code, 302)
        withdrawal = Withdrawal.objects.get(month=month, withdrawal_type=withdrawal_type)
        self.assertTrue(withdrawal)
        self.assertEqual(withdrawal.description, 'description2')
        self.assertEqual(withdrawal.amount, 11.0)
        self.assertEqual(withdrawal.date, timezone.now().date())
        self.assertEqual(withdrawal.withdrawal_type, withdrawal_type)
        self.assertEqual(withdrawal.account_number, '12345')

    def test_delete_withdrawal(self):
        month = Month.objects.create(year=2015, month=1)
        month.save()
        withdrawal_type = WithdrawalType.objects.create(name='withdrawal type')
        withdrawal_type.save()
        withdrawal = Withdrawal.objects.create(
            month=month,
            description='description',
            amount=10,
            date=timezone.now().date(),
            withdrawal_type=withdrawal_type,
            account_number='1234',
        )
        withdrawal.save()
        withdrawal_id = withdrawal.id
        response = self.client.get(reverse('expenses:withdrawal-delete', args=(month.id, withdrawal.id)))
        self.assertEqual(response.status_code, 302)
        # Withdrawal.objects.get(pk=withdrawal_id)
        try:
            Withdrawal.objects.get(pk=withdrawal_id)
        except ObjectDoesNotExist:
            pass
        else:
            self.assertTrue(False, msg='Withdrawal object not removed')

    def test_add_deposit(self):
        month = Month.objects.create(year=2015, month=1)
        month.save()
        deposit_type = DepositType.objects.create(name='deposit type')
        deposit_type.save()
        response = self.client.post(reverse('expenses:deposit', args=(month.id, -1)), {
            'description': 'description',
            'amount': 10,
            'date': timezone.now().date(),
            'deposit_type': deposit_type.id,
            'account_number': '1234',
        })
        print response
        self.assertEqual(response.status_code, 302)
        deposit = Deposit.objects.get(month=month, deposit_type=deposit_type)
        self.assertTrue(deposit)
        self.assertEqual(deposit.description, 'description')
        self.assertEqual(deposit.amount, 10.0)
        self.assertEqual(deposit.date, timezone.now().date())
        self.assertEqual(deposit.deposit_type, deposit_type)
        self.assertEqual(deposit.account_number, '1234')

    def test_update_deposit(self):
        month = Month.objects.create(year=2015, month=1)
        month.save()
        deposit_type = DepositType.objects.create(name='deposit type')
        deposit_type.save()
        deposit1 = Deposit.objects.create(
            month=month,
            description='description',
            amount=10,
            date=timezone.now().date(),
            deposit_type=deposit_type,
            account_number='1234',
        )
        deposit1.save()
        response = self.client.post(reverse('expenses:deposit', args=(month.id, deposit1.id)), {
            'description': 'description2',
            'amount': 11,
            'date': timezone.now().date(),
            'deposit_type': deposit_type.id,
            'account_number': '12345',
        })
        print response
        self.assertEqual(response.status_code, 302)
        deposit = Deposit.objects.get(month=month, deposit_type=deposit_type)
        self.assertTrue(deposit)
        self.assertEqual(deposit.description, 'description2')
        self.assertEqual(deposit.amount, 11.0)
        self.assertEqual(deposit.date, timezone.now().date())
        self.assertEqual(deposit.deposit_type, deposit_type)
        self.assertEqual(deposit.account_number, '12345')

    def test_delete_deposit(self):
        month = Month.objects.create(year=2015, month=1)
        month.save()
        deposit_type = DepositType.objects.create(name='deposit type')
        deposit_type.save()
        deposit = Deposit.objects.create(
            month=month,
            description='description',
            amount=10,
            date=timezone.now().date(),
            deposit_type=deposit_type,
            account_number='1234',
        )
        deposit.save()
        deposit_id = deposit.id
        response = self.client.get(reverse('expenses:deposit-delete', args=(month.id, deposit.id)))
        self.assertEqual(response.status_code, 302)
        # Withdrawal.objects.get(pk=deposit_id)
        try:
            Withdrawal.objects.get(pk=deposit_id)
        except ObjectDoesNotExist:
            pass
        else:
            self.assertTrue(False, msg='Withdrawal object not removed')
