# -*- coding: utf-8 -*-
from tests import BaseTestCase as TestCase


class TestMainViews(TestCase):

    def test_empty_index_view(self):
        resp = self.client.get("/")
        assert resp.status_code == 200
        assert "jquery" in resp.data
        assert "bootstrap.min.css" in resp.data
        assert "base.css" in resp.data
