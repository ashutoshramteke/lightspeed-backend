import requests
import json
from fastapi import Depends, HTTPException, status
from graphql import GraphQLError



async def create_sale(sale,authorization_header : str = Depends(lambda x: x.headers.get("Authorization")),domain_prefix: str = Depends(lambda x: x.headers.get("domain_prefix", ""))):
  try:
        # Check authorization header
    if not authorization_header or not authorization_header.startswith("Bearer "):
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Authorization header missing or invalid")

        # Check domain prefix
    if not domain_prefix:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Domain-Prefix header missing")
    
    
    access_token1 = authorization_header.split(" ")[1]
   
    url = f"https://{domain_prefix}.retail.lightspeed.app/api/users"
    headers1 = {
         "accept": "application/json",
         "authorization": f"Bearer {access_token1}"
     }
    response1 = requests.get(url, headers=headers1)
    data=json.loads(response1.content)
    user_data = data['users'][0]
    user_id = user_data['id']
    
    
    
    api_url = f"https://{domain_prefix}.vendhq.com/api/register_sales"
    headers = {
        "accept": "application/json",
        "authorization": f"Bearer {access_token1}"
    }
    payload = {
    "status": "AWAITING_DISPATCH",
    "source": "online platforms",
    "user_id": f"{user_id}",
    
    "customer": {
    "company_name":sale.customer.company_name,
   }
    }
    payload[ "register_sale_products"] =[]
    for sale in sale.register_sale_products:
        payload[ "register_sale_products"].append(
        {
            "price_set":sale.price_set,
            "product_id": sale.product_id,
            "quantity": sale.quantity,
            "price": sale.price,
            "tax": sale.tax,
            
        },
        )

    # Send the API request
    response = requests.post(api_url, json=payload, headers=headers)
    # Check for successful response
    if response.status_code == 200:
        return json.loads(response.content)
    elif response.status_code == 401:
         raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Authorization header or domain_prefic invalid")
    else:
        error_message = json.loads(response.content)['error'][0]['info']
        raise GraphQLError(f"Error: {error_message}")
       



  except requests.RequestException as e:
        raise GraphQLError(f'Request failed: {e}')
  except HTTPException as e:
        raise e  # Re-raise HTTPException   
  except Exception as e:
        raise GraphQLError(f'An unexpected error occurred: {str(e)}')