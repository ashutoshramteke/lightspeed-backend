

from graphene import ObjectType,String,Int,List,Float,Field

class Datum(ObjectType):
    id=String()
    outlet_id=String()
    product_id=String()
    inventory_level=Int()
    current_amount=Int()
    version=Float()
    deleted_at=String()
    average_cost=Int()
    reorder_point=Int()
    reorder_amount=Int()


class Version(ObjectType):
    min = Float()
    max = Float()


class Model(ObjectType):
    data= List(Datum)
    version= Field(Version)
