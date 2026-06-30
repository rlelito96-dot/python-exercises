# Unit
def calculate_fee(amount):
    if amount > 1000:
        return 50
    return 10


def test_calculate_fee_high_amount():
    assert calculate_fee(2000) == 50

# Integration tests
def test_transaction_saved(db_session):
    tx = Transaction(amount=100)
    repo = TransactionRepository(db_session)

    repo.add(tx)

    result = db_session.query(Transaction).first()
    assert result.amount == 100

# API(endpoint tests)
def test_create_transaction(client):
    response = client.post(
        "/transactions",
        json={"amount": 100}
    )

    assert response.status_code == 201

# E2E (end-to-end)
def test_full_fraud_flow(client):
    response = client.post(
        "/transactions",
        json={"amount": 5000}
    )

    assert response.json()["decision"] == "BLOCK"

# Parametrize(pytest feature)
import pytest

@pytest.mark.parametrize(
    "amount,expected",
    [
        (50, "ALLOW"),
        (1500, "REVIEW"),
        (5000, "BLOCK"),
    ]
)
def test_fraud_decisions(amount, expected):
    service = FraudService()
    tx = Transaction(amount=amount)

    assert service.check(tx) == expected

# mock(unittest.mock / pytest-mock)
def test_redis_called(mocker):
    redis = mocker.Mock()
    redis.get.return_value = None

    assert redis.get("key") is None