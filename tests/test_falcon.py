from __future__ import absolute_import, division, print_function

import json

import crochet

from falcon import testing
from ssce import server

class APITest(testing.TestCase):

    def setUp(self):
        super(APITest, self).setUp()
        crochet.setup()

    def test_endpoint_works(self):
        result = self.simulate_get('/threaded')
        print(result.json)

        serialized = json.loads(result)
        keys = serialized.keys()
        expected = ['statuses', 'alarm-state', 'last-update']
        self.assertEqual(expected, keys)
