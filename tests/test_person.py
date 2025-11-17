import pytest
from pytest import raises
from models import Person


class TestPerson:
    def test_new_person(self, person1):
        print(person1)
        assert person1.name
        assert person1.ipn
        assert not person1.accounts
        assert person1.name == 'Alex'
        person1.name = 'Bob'

    def test_new_persons_diff_ipn(self, person1, person2):
        print(person1)
        assert person1.ipn != person2.ipn


class TestCreateNewPerson:
    # def test_create_person_no_name(self):
    #     with raises(ValueError):
    #         Person("")
    #
    # def test_create_person_name_as_whitespaces(self):
    #     with raises(ValueError):
    #         Person("              ")

    @pytest.mark.parametrize("wrong_name", ["", "        ", '\n', '\t    '])
    def test_wrong_name(self, wrong_name: str):
        with raises(ValueError):
            Person(wrong_name)

    def test_new_person(self, person1):
        print(person1)
        assert person1.name
        assert person1.ipn
        assert not person1.accounts


