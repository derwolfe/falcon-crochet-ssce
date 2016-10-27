from __future__ import absolute_import, division, print_function

import json

import crochet

from falcon import testing
from ssce import server

class APITest(testing.TestCase):

    def setUp(self):
        super(APITest, self).setUp()
        self.app = server.api()
        crochet.setup()

    def test_endpoint_works(self):
        result = self.simulate_get('/threaded')

        expected = sorted(['statuses', 'alarm-state', 'last-update'])
        received = sorted(result.json.keys())
        self.assertEqual(expected, received)
