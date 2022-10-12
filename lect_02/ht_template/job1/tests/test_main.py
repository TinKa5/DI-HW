"""
Tests for main.py
# TODO: write tests
"""
from unittest import TestCase, mock

# NB: avoid relative imports when you will write your code
from .. import main


class MainFunctionTestCase(TestCase):

    MISSED_DATE_MESSAGE = {"message": "Date is missed"}
    MISSED_RAWDIR_MASSAGE = {"message": "raw_dir is missed"}


    @classmethod
    def setUpClass(cls) -> None:
        main.app.testing = True
        cls.client = main.app.test_client()\


    @mock.patch('lect_02.ht_template.job1.api.get_sales')
    def test_return_400_date_param_missed_path_param_missed(
            self,
            get_sales_mock: mock.MagicMock
        ):
        """
        Raise 400 HTTP code when no 'date' param
        """
        resp = self.client.post(
            '/',
            json={
                'raw_dir': '/foo/bar/',
                # no 'date' set!
            },
        )
        self.assertEqual(400, resp.status_code)
        self.assertEqual(self.MISSED_DATE_MESSAGE, resp.json)
        get_sales_mock.assert_not_called()

    @mock.patch('lect_02.ht_template.job1.api.get_sales')
    def test_return_400_raw_dir_param_missed(self, get_sales_mock: mock.MagicMock):
        resp = self.client.post(
            '/',
            json={
                # no 'raw_dir' set!,
                'date': "2022-08-09"
            },
        )
        self.assertEqual(400, resp.status_code)
        self.assertEqual(self.MISSED_RAWDIR_MASSAGE, resp.json)
        get_sales_mock.assert_not_called()


    @mock.patch('lect_02.ht_template.job1.api.get_sales')
    def test_api_get_sales_called(
            self,
            get_sales_mock: mock.MagicMock
    ):
        """
        Test whether api.get_sales is called with proper params
        """
        fake_date = '1970-01-01'
        fake_json = {
                'date': fake_date,
                'raw_dir': '/foo/bar/',
            }
        self.client.post(
            '/',
            json= fake_json,
        )

        get_sales_mock.assert_called_once_with(fake_json)

    @mock.patch('lect_02.ht_template.job1.api.get_sales')
    def test_return_201_when_all_is_ok(
            self,
            get_sales_mock: mock.MagicMock
    ):
        fake_date = '1970-01-01'
        fake_json = {
            'date': fake_date,
            'raw_dir': '/foo/bar/',
        }
        resp = self.client.post(
            '/',
            json=fake_json,
        )

        get_sales_mock.assert_called_once_with(fake_json)
        self.assertEqual(201, resp.status_code)
        self.assertEqual({"message": "Data retrieved successfully from API"}, resp.json)
        pass
