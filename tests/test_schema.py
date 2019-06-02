from marshmallow import Schema


from quaerere_base_common.schema import BaseSchema


def test_base_schema():
    assert issubclass(BaseSchema, Schema)
    test = BaseSchema()
    assert test.model_class is None
