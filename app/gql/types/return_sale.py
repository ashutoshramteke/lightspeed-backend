


from graphene import ObjectType,String,Int,List,Float,Field,Boolean
import graphene


class TaxComponent(ObjectType):
    rate_id=String()
    total_tax=Int()

class SalesTax(graphene.ObjectType):
    id = graphene.String()
    name = graphene.String()
    rate = graphene.Float()
    amount = graphene.Float()
    total_tax = graphene.Float()

class LineItems(graphene.ObjectType):
    id = graphene.String()
    product_id = graphene.String()
    quantity = graphene.Float()
    price = graphene.Float()
    unit_price = graphene.Float()
    price_total = graphene.Float()
    total_price = graphene.Float()
    discount = graphene.Float()
    unit_discount = graphene.Float()
    discount_total = graphene.Float()
    total_discount = graphene.Float()
    loyalty_value = graphene.Float()
    unit_loyalty_value = graphene.Float()
    total_loyalty_value = graphene.Float()
    cost = graphene.Float()
    unit_cost = graphene.Float()
    cost_total = graphene.Float()
    total_cost = graphene.Float()
    tax = graphene.Float()
    unit_tax = graphene.Float()
    tax_total = graphene.Float()
    total_tax = graphene.Float()
    tax_id = graphene.String()
    tax_components = graphene.List(TaxComponent)
    promotions = graphene.List(graphene.String)
    price_set = graphene.Boolean()
    sequence = graphene.Int()
    note = graphene.String()
    status = graphene.String()
    is_return = graphene.Boolean()

class sales(graphene.ObjectType):
    id = graphene.String()
    outlet_id = graphene.String()
    register_id = graphene.String()
    user_id = graphene.String()
    customer_id = graphene.String()
    invoice_number = graphene.String()
    receipt_number = graphene.String()
    invoice_sequence = graphene.Int()
    receipt_sequence = graphene.Int()
    status = graphene.String()
    note = graphene.String()
    short_code = graphene.String()
    return_for = graphene.String()
    created_at = graphene.String()
    total_price = graphene.Float()
    total_loyalty = graphene.Float()
    total_tax = graphene.Float()
    updated_at = graphene.String()
    sale_date = graphene.String()
    deleted_at = graphene.String()
    line_items = graphene.List(LineItems)
    payments = graphene.List(graphene.String)  # You need to define Payment type
    taxes = graphene.List(SalesTax)  # You need to define Tax type
    adjustments = graphene.List(graphene.String)  # You need to define Adjustment type
    version = graphene.Int()

# Define the Query or Mutation if needed
class Model3(graphene.ObjectType):
    data = graphene.Field(sales)