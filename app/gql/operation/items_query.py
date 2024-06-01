import graphene
from gql.types.items import Model
from graphql import GraphQLError
from sp_api.get_all_items import get_all_items
from gql.types.items import Model2
from sp_api.get_items_byid import get_item_byid
class Query(graphene.ObjectType):
    all_items = graphene.Field(Model,page_size=graphene.Int(default_value=1000))
    items_byid = graphene.Field(Model2,product_id=graphene.String(required=True))
    async def resolve_all_items(self, info,page_size):
        try:
            response = await get_all_items(page_size, info.context["request"].headers.get("Authorization"),info.context["request"].headers.get("domain_prefix", ""))
            return response
        except Exception as e:
            if e == "URL has an invalid label":
                raise GraphQLError(f"Error: Invalid domain_prefix")
            else:
                raise GraphQLError(f"Error: {e}")
    async def resolve_items_byid(self, info,product_id):
        try:
            response = await get_item_byid(product_id,info.context["request"].headers.get("Authorization"),info.context["request"].headers.get("domain_prefix", ""))
            return response
        except Exception as e:
            raise GraphQLError(f"Error: {e}")

schema = graphene.Schema(query=Query)