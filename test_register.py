# -*- coding:utf-8 -*-
from testingpo.index import Index


class TestRigester:
    def setup(self):
        self.index=Index()
    def test_rigester(self):
        self.index.goto_login().goto_register()