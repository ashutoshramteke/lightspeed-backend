

from graphene import ObjectType,String,Int,List,Field

class Contact(ObjectType):
    company_name=String()
    phone=String()
    email=String()


class CustomerRes(ObjectType):
    id=String()
    name=String()
    customer_group_name=String()
    loyalty_balance=String()
    updated_at=String()
    deleted_at=String()
    balance=String()
    year_to_date=String()
    contact: Contact
    customer_code=String()
    customer_group_id=String()
    first_name=String()
    last_name=String()
    company_name=String()
    phone=String()
    mobile=String()
    fax=String()
    email=String()
    twitter=String()
    website=String()
    physical_address1=String()
    physical_address2=String()
    physical_suburb=String()
    physical_city=String()
    physical_postcode=String()
    physical_state=String()
    physical_country_id=String()
    postal_address1=String()
    postal_address2=String()
    postal_suburb=String()
    postal_city=String()
    postal_postcode=String()
    postal_state=String()
    postal_country_id=String()
    enable_loyalty=Int()
    date_of_birth=String()
    sex=String()
    custom_field_1=String()
    custom_field_2=String()
    custom_field_3=String()
    custom_field_4=String()
    note=String()


class Attribute(ObjectType):
    name=String()
    value=String()


class RegisterSaleProductRes(ObjectType):
    id=String()
    handle=String()
    sku=String()
    name=String()
    tax_name=String()
    tax_rate=Int()
    tax_total=Int()
    price_total=Int()
    product_id=String()
    register_id=String()
    sequence=Int()
    quantity=Int()
    price=Int()
    cost=Int()
    price_set=Int()
    discount=Int()
    loyalty_value=Int()
    tax=Int()
    tax_id=String()
    status=String()
    attributes= List(Attribute)


class RegisterSalePayment(ObjectType):
    id=String()
    register_id=String()
    retailer_payment_type_id=String()
    payment_date=String()
    amount=Int()
    payment_type_id=String()
    name=String()
    label=String()


class Totals(ObjectType):
    total_tax=Int()
    total_price=Int()
    total_payment=Int()
    total_to_pay=Int()


class Tax(ObjectType):
    id=String()
    tax=Int()
    name=String()
    rate=Int()


class RegisterSale(ObjectType):
    id=String()
    source=String()
    source_id=String()
    customer_name=String()
    customer = Field(CustomerRes)
    user_name=String()
    created_at=String()
    updated_at=String()
    total_price=Int()
    total_cost=Int()
    total_tax=Int()
    tax_name=String()
    return_for=String()
    register_id=String()
    customer_id=String()
    user_id=String()
    sale_date=String()
    note=String()
    status=String()
    short_code=String()
    invoice_number=String()
    accounts_transaction_id=String()
    register_sale_products= List(RegisterSaleProductRes)
    register_sale_payments= List(RegisterSalePayment)
    totals=Field( Totals)
    taxes= List(Tax)


class Model(ObjectType):
    register_sale=Field(RegisterSale)
