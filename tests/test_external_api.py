from unittest.mock import patch, Mock
import requests
from src.external_api import amount_transaction


@patch('requests.get')
@patch('src.external_api.financial_transaction')
def test_external_api(mock_financial, mock_get):
    # Мок для financial_transaction
    mock_financial.return_value = [
        {
            "id": 41428829,
            "operationAmount": {
                "amount": 100.0,
                "currency": {
                    "code": "USD"
                }
            }
        }
    ]

    # Мок для API конвертации
    mock_response = Mock()
    mock_response.json.return_value = {"result": 682353.912941}
    mock_response.status_code = 200
    mock_get.return_value = mock_response

    result = amount_transaction(41428829)
    assert result == 682353.912941
