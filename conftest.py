import pytest

from models import Person, Bank


# @pytest.fixture()
# @pytest.fixture(scope='function')
@pytest.fixture(scope='class')
# @pytest.fixture(scope='module')
# @pytest.fixture(scope='session')
def person1() -> Person:
    person = Person('Alex')
    yield person
    print(person, 'destroyed')


@pytest.fixture(scope='class')
def person2() -> Person:
    person = Person('Marta')
    return person


@pytest.fixture(scope='class')
def bank1() -> Bank:
    bank = Bank('Mono')
    return bank
