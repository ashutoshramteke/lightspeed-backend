from fastapi import FastAPI
from starlette_graphene3 import GraphQLApp
import uvicorn
from gql.operation.items_query import schema as all_items_schema
from gql.operation.sale_mutation import schema1 as sale_mutation
from gql.operation.inventory_query import schema as get_inventory_schema

app = FastAPI()


app.add_route("/getallitems", GraphQLApp(schema=all_items_schema))
# app.add_route("/getitembyid", GraphQLApp(schema=item_byidschema))

app.add_route("/sale", GraphQLApp(schema=sale_mutation))

app.add_route("/getinventory", GraphQLApp(schema=get_inventory_schema))


if __name__ == "__main__":

    uvicorn.run("main:app", host="0.0.0.0", port=8000,reload=True)