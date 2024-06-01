from graphene import ObjectType,String,Int,List,Field,Float,Boolean


class TaxComponent(ObjectType):
    rate_id=String()
    total_tax=Float()


class LineItem(ObjectType):
    id=String()
    product_id=String()
    tax_id=String()
    discount_total=Int()
    discount=Int()
    price_total=Float()
    price=Float()
    cost_total=Int()
    cost=Int()
    tax_total=Float()
    tax=Float()
    quantity=Int()
    loyalty_value=Float()
    price_set=Boolean()
    status=String()
    sequence=Int()
    tax_components=List(TaxComponent)
    unit_cost=Int()
    unit_discount=Int()
    unit_loyalty_value=Float()
    unit_price=Float()
    unit_tax=Float()
    total_cost=Int()
    total_discount=Int()
    total_loyalty_value=Float()
    total_price=Float()
    total_tax=Float()
    is_return=Boolean()


class Payment(ObjectType):
    id=String()
    register_id=String()
    outlet_id=String()
    retailer_payment_type_id=String()
    payment_type_id=String()
    name=String()
    amount=Float()
    payment_date=String()
    external_attributes=List(String)


class Tax(ObjectType):
    amount=Float()
    id=String()


class Datum(ObjectType):
    id=String()
    outlet_id=String()
    register_id=String()
    user_id=String()
    customer_id=String()
    invoice_number=String()
    status=String()
    note=String()
    short_code=String()
    total_price=Float()
    total_tax=Float()
    total_loyalty=Float()
    created_at=String()
    updated_at=String()
    sale_date=String()
    line_items=List(LineItem)
    payments=List(Payment)
    version=Float()
    receipt_number=String()
    adjustments=List(String)
    taxes=List(Tax)


class Version(ObjectType):
    min=Float()
    max=Float()


class Model3(ObjectType):
    data=List(Datum)
    version= Field( Version)
