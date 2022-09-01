"""
Tests for main.py
# TODO: write tests
"""
from unittest import TestCase, mock

# NB: avoid relative imports when you will write your code
from .. import main


class MainFunctionTestCase(TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        main.app.testing = True
        cls.client = main.app.test_client()

    def test_return_400_date_param_missed_path_param_missed(self):
        """
        When src_parquet_path param missed, 400 error return
        """
        resp = self.client.post(
            '/',
            json={
                'target_dir': '/foo/bar/',
                # no 'date' set
            },
        )

        self.assertEqual(400, resp.status_code)

    @mock.patch('main.storage.save_to_disk')
    @mock.patch('main.api.get_sales')
    def test_api_get_sales_called(
            self,
            get_sales_mock: mock.MagicMock,
            save_to_disk: mock.MagicMock,
    ):
        """
        Test whether api.get_sales is called with proper params
        """
        fake_date = '1970-01-01'
        self.client.post(
            '/',
            json={
                'date': fake_date,
                'target_dir': '/foo/bar/',
            },
        )

        get_sales_mock.assert_called_with(fake_date)
