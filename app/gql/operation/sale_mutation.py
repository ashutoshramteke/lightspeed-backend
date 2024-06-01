
import graphene
from graphql import GraphQLError
from gql.types.get_sales import Model3 as getsalemodel
from gql.types.sale import SaleModel
from gql.types.sale_response import Model as SaleResponse
from gql.types.return_sale import Model3 as ReturnsaleModel
from sp_api.return_sale import return_sale
from sp_api.register_sale import create_sale
from sp_api.get_sale import get_sale



class Createsale(graphene.Mutation):
    class Arguments:
        sale = graphene.Argument(SaleModel, required=True)

    response=graphene.Field(SaleResponse)

    async def mutate(self, info, sale):
        try:
            response = await create_sale(sale,info.context["request"].headers.get("Authorization"),info.context["request"].headers.get("domain_prefix", ""))
        except Exception as e:
            raise GraphQLError(f"{e}")
        return Createsale(response)

class returnsale(graphene.Mutation):
    class Arguments:
        sale_id =graphene.String(required=True) 
    response=graphene.Field(ReturnsaleModel)
    
    async def mutate(self, info, sale_id):
        try:
            response = await return_sale(sale_id,info.context["request"].headers.get("Authorization"),info.context["request"].headers.get("domain_prefix", ""))
            
        except Exception as e:
            raise GraphQLError(f"{e}")
        return returnsale(response)
    


class Mutation(graphene.ObjectType):
    create_sale_mutation = Createsale.Field()
    return_sale_mutation= returnsale.Field()


class Query(graphene.ObjectType):   
   get_sales = graphene.Field(getsalemodel,page_size=graphene.Int(default_value=1000))
    
   async def resolve_get_sales(self, info,page_size):
        try:
            response = await get_sale(page_size, info.context["request"].headers.get("Authorization"),info.context["request"].headers.get("domain_prefix", ""))
            return response
        except Exception as e:
            
            raise GraphQLError(f"Error: {e}")
       

schema1 = graphene.Schema(query=Query, mutation=Mutation)