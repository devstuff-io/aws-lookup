from unittest import TestCase

from aws_lookup import core


class CoreTest(TestCase):

    def test_filter_objects_rtn_list(self):
        res = core.filter_objects(
            [
                {'foo': "this is a value"},
                {'foo': "bar"},
            ],
            '*is*',
            'foo'
        )
        self.assertListEqual(res, ["this is a value"])

    def test_filter_objects_rtn_dict(self):
        res = core.filter_objects(
            [
                {'foo': "this is a value"},
                {'foo': "bar"},
            ],
            'bar',
            'foo',
            True
        )
        self.assertListEqual(res, [{'foo': "bar"}])

    def test_filter_objects_no_key(self):
        res = core.filter_objects(
            [
                "this is a value",
                "bar",
            ],
            '*lue'
        )
        self.assertListEqual(res, ['this is a value'])
