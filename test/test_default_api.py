# coding: utf-8

"""
    Safaricom APIs

    # Introduction  What does your API do?  # Overview  Things that the developers should know about  # Authentication  What is the preferred way of using the API?  # Error Codes  What errors and status codes can a user expect?  # Rate limit  Is there a limit to the number of requests an user can send?  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import mpesa_client
from mpesa_client.apis.default_api import DefaultApi  # noqa: E501
from mpesa_client.rest import ApiException


class TestDefaultApi(unittest.TestCase):
    """DefaultApi unit test stubs"""

    def setUp(self):
        self.api = DefaultApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_mpesa_accountbalance_v1_query_post(self):
        """Test case for mpesa_accountbalance_v1_query_post

        Make an Account Balance query  # noqa: E501
        """
        pass

    def test_mpesa_b2b_v1_paymentrequest_post(self):
        """Test case for mpesa_b2b_v1_paymentrequest_post

        Make a B2B Payment Request  # noqa: E501
        """
        pass

    def test_mpesa_b2c_v1_paymentrequest_post(self):
        """Test case for mpesa_b2c_v1_paymentrequest_post

        Make a B2C Payment Request  # noqa: E501
        """
        pass

    def test_mpesa_c2b_v1_registerurl_post(self):
        """Test case for mpesa_c2b_v1_registerurl_post

        Register C2B Confirmation and Validation URLs  # noqa: E501
        """
        pass

    def test_mpesa_c2b_v1_simulate_post(self):
        """Test case for mpesa_c2b_v1_simulate_post

        Simulate a C2B Payment  # noqa: E501
        """
        pass

    def test_mpesa_reversal_v1_request_post(self):
        """Test case for mpesa_reversal_v1_request_post

        Reverse an M-Pesa Transaction  # noqa: E501
        """
        pass

    def test_mpesa_stkpush_v1_processrequest_post(self):
        """Test case for mpesa_stkpush_v1_processrequest_post

        Initiate a Lipa na M-Pesa Online Payment  # noqa: E501
        """
        pass

    def test_mpesa_stkpushquery_v1_query_post(self):
        """Test case for mpesa_stkpushquery_v1_query_post

        Query the status of a Lipa na M-Pesa Online Payment  # noqa: E501
        """
        pass

    def test_mpesa_transactionstatus_v1_query_post(self):
        """Test case for mpesa_transactionstatus_v1_query_post

        Query the Transaction Status of an M-Pesa Transaction  # noqa: E501
        """
        pass

    def test_oauth_v1_generate_get(self):
        """Test case for oauth_v1_generate_get

        Generate an OAuth Access Token  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
