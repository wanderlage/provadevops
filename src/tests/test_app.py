"""This package has all tests of DevOps resource

"""

import json
from unittest import TestCase
from api.app import APP, DevOps


class DevOpsTestCase(TestCase):
    """This class has all tests of DevOps resource class

    """

    def setUp(self):
        """Create the client for this test

        """
        self.client = APP.test_client()

    def test_get(self):
        """Test the return of get method

        """
        resp = self.client.get('/')

        self.assertEqual(resp.status_code, 200)

        data = json.loads(resp.data)

        self.assertDictEqual(
            data,
            {
                'candidate': 'Welcome to the DevOps test'
            }
        )
