import unittest

from pyramid import testing


class ViewTests(unittest.TestCase):
    def setUp(self):
        self.config = testing.setUp()

    def tearDown(self):
        testing.tearDown()

    def test_home_view(self):
        from pacific.views import home
        request = testing.DummyRequest()
        info = home(request)
        self.assertEqual(info['project'], 'Pacific')
