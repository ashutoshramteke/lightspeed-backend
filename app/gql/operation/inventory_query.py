import graphene
from graphql import GraphQLError
from sp_api.get_all_inventory import get_all_inventory
from gql.types.inventory import Model








class Query(graphene.ObjectType):
    get_inventory = graphene.Field(Model,page_size=graphene.Int(default_value=1000))
    
    async def resolve_get_inventory(self, info,page_size):
        try:
            response = await get_all_inventory(page_size, info.context["request"].headers.get("Authorization"),info.context["request"].headers.get("domain_prefix", ""))
            return response
        except Exception as e:
            raise GraphQLError(f"Error: {e}")
   

schema = graphene.Schema(query=Query)