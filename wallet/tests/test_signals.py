from pytest import mark

from wallet.models import Wallet


@mark.django_db
class TestWallet:
    def test_new_user_gets_one_wallet(self, user):
        assert Wallet.objects.filter(user=user).count() == 1

    def test_updating_user_does_not_create_another_wallet(self, user):
        user.first_name = 'Updated'
        user.save()

        assert Wallet.objects.filter(user=user).count() == 1
