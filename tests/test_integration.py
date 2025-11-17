class TestIntegration:

    def test_no_accounts_from_start(self, person1, bank1):
        assert not person1.accounts
        assert not bank1.accounts

    def test_create_account(self, person1, bank1):
        account = bank1.open_account(person1)
        assert account.balance == 0

    def test_account_saved(self, person1, bank1):
        assert person1.accounts
        assert bank1.accounts

    def test_deposit_account(self, person1, bank1):
        person1.get_first_account().deposit(1000)
        assert person1.total_money == 1000
        assert bank1.total_money == 1000

    def test_more_clients(self, bank1, person2, person1):
        account = bank1.open_account(person2)
        account.deposit(520)
        assert bank1.total_money == 1520
        # assert person1.total_money == 3333333


