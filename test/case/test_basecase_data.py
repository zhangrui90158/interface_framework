from data_driver_interface_framework.test.case.basecase import BaseCaseRequest
import os
import json
import unittest
from data_driver_interface_framework.config.conf import *
import requests

class MyUnittest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        pass

    @staticmethod
    def get_test_data_calss(self):
        pass

    def setUp(self):
        pass

    def test_get_juhe_caipiao(self):
        self.case_data = BaseCaseRequest("juhe_caipiao")
        self.assert_test(self.case_data)

    def test_baidu(self):
        self.case_data = BaseCaseRequest("baidu")
        self.assert_test(self.case_data)

    def test_juhe_ip(self):
        self.case_data = BaseCaseRequest("juhe_ip")
        self.assert_test(self.case_data)

    def assert_test(self,case_data):
        res = case_data.send_requests()
        expect_res = case_data.expect_res
        return self.assertEqual(res,expect_res)


if __name__ == '__main__':
    unittest.main()
