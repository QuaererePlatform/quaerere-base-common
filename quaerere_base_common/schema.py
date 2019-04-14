__all__ = ['BaseSchema']

from marshmallow import Schema, post_load


class BaseSchema(Schema):
    model_class = None

    @post_load
    def make_web_site(self, data):
        if self.model_class is None:
            return data
        return self.model_class(**data)
