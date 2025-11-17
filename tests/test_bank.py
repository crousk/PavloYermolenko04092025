class TestBank:
    def test_bank(self, bank1):
        assert bank1.name
        assert not bank1.accounts
        assert bank1.name.startswith("PAT ")

    def test_bank2(self, bank1):
        assert bank1.name
        assert not bank1.accounts
        assert bank1.name.startswith("PAT ")