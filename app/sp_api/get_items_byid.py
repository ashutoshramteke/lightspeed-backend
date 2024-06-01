import requests
import json
from graphql import GraphQLError
from fastapi import Depends, HTTPException, status
async def get_item_byid(product_id,authorization_header : str = Depends(lambda x: x.headers.get("Authorization")),domain_prefix: str = Depends(lambda x: x.headers.get("domain_prefix", ""))):
 try:
        # Check authorization header
        if not authorization_header or not authorization_header.startswith("Bearer "):
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Authorization header missing or invalid")

        # Check domain prefix
        if not domain_prefix:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Domain-Prefix header missing")
        access_token1 = authorization_header.split(" ")[1]
    
    
    
        api_url = f"https://{domain_prefix}.vendhq.com/api/2.0/products/{product_id}"
        headers = {
        "accept": "application/json",
        "authorization": f"Bearer {access_token1}"
                  }
        response = requests.get(api_url, headers=headers)

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
    