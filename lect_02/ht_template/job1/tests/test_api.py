"""
Tests api.py
# TODO: write tests
"""
from unittest import TestCase, mock

# NB: avoid relative imports when you will write your code:
from ..api import get_sales
from lect_02.ht_template.job1.api import get_sales

class GetSalesTestCase(TestCase):
    @mock.patch('lect_02.ht_template.job1.api.save_to_disk')
    @mock.patch("lect_02.ht_template.job1.api.get_response")

    def test_get_response(self, mock_save: mock.MagicMock, mock_responce: mock.MagicMock):
        get_sales('some data json')
        mock_responce.return_value = mock()
        mock_responce.assert_called_with('some data json')
        mock_save.assert_called_with('some_ content', 'some_path')
    """
    Test api.get_sales function.
    # TODO: implement
    """
    pass
