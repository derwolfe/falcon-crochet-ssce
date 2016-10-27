from __future__ import absolute_import, division, print_function

import crochet

from falcon import testing
from ssce import server

class APITest(testing.TestCase):

    def setUp(self):
        super(APITest, self).setUp()
        crochet.setup()

    def test_endpoint_works(self):
        result = self.simulate_get('/threaded')
        self.assertGreater(0, len(result.content))
