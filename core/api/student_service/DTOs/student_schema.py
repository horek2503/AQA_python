from marshmallow import Schema, fields, validate


class StudentSchema(Schema):
    id = fields.Integer(required=True, strict=True, validate=validate.Range(min=1))
    name = fields.String(required=True)
    score = fields.Integer(required=True, strict=True, validate=validate.Range(min=1, max=100))
    score_name = fields.String(required=True)
    created_date = fields.Float(required=True)
    updated_date = fields.DateTime(required=True)


# st1 = {
#     'created_date': 1791832122.3969095,
#     'id': 123,
#     'name': '11',
#     'score': 99,
#     'score_name': 'GREAT',
#     'updated_date': '2026-10-12T22:08:42+0300'
# }
#
# StudentSchema().load(st1)
