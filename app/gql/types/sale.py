
from graphene import InputObjectType,String,Int,List
import graphene

class RegisterSaleProduct(InputObjectType):
    price_set= Int(required=True)
    product_id= String(required=True)
    quantity= Int(required=True)
    price= Int(required=True)
    tax= Int(required=True)
    


class CustomerInput(InputObjectType):
    name = String()
    first_name = String()
    last_name = String()
    company_name = String(required=True)
    mobile = String()
    email = String()
    physical_address1 = String()
    physical_address2 = String()
    physical_suburb = String()
    physical_city = String()
    physical_postcode = String()
    physical_state = String()
    physical_country_id = String()
    postal_address1 = String()
    postal_address2 = String()
    postal_suburb = String()
    postal_city = String()
    postal_postcode = String()
    postal_state = String()
    postal_country_id = String()
    custom_field_1 = String()
    custom_field_2 = String()
    custom_field_3 = String()
    custom_field_4 = String()
    note = String()


class SaleModel(InputObjectType):
    status= String(required=True)
    source= String(required=True)
    
    register_sale_products= graphene.List(RegisterSaleProduct,required=True)
    customer= graphene.Field(CustomerInput,required=True)