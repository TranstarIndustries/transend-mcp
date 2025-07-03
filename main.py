from transend.client import TransendAPIClient
from mcp.server.fastmcp import FastMCP
import os
from uuid import UUID
from typing import Dict, List, Optional, Any

# Initialize with your API credentials
api_key = os.getenv("TRANSEND_API_KEY", "your_api_key_here")
api_token = os.getenv("TRANSEND_API_TOKEN", "your_api_token_here")
client = TransendAPIClient(api_key, api_token)

# Initialize FastMCP server
mcp = FastMCP("transend")

# BranchAPI Tools
@mcp.tool()
def get_all_branches(active: Optional[bool] = None):
    """
    Get all branches from the Transend API.
    
    Args:
        active: Optional flag to filter branches by active status
    
    Returns:
        List of branches
    """
    try:
        branches = client.branch.get_all_branches(active=active)
        return branches
    except Exception as e:
        return {"error": str(e)}
    
@mcp.tool()
def get_branch_by_number(branch_number: str):
    """
    Get a specific branch by its number from the Transend API.
    
    Args:
        branch_number: The branch number to look up
        
    Returns:
        Branch information
    """
    try:
        branch = client.branch.get_branch_by_number(branch_number)
        return branch
    except Exception as e:
        return {"error": str(e)}

# ProductAPI Tools
@mcp.tool()
def get_all_sort_types():
    """
    Get all sort types from the Transend API.
    
    Returns:
        List of sort types
    """
    try:
        return client.product.get_all_sort_types()
    except Exception as e:
        return {"error": str(e)}

@mcp.tool()
def get_all_tags():
    """
    Get all tags from the Transend API.
    
    Returns:
        List of tags
    """
    try:
        return client.product.get_all_tags()
    except Exception as e:
        return {"error": str(e)}

@mcp.tool()
def get_availability_by_item_id(item_id):
    """
    Get availability by item id.
    
    Args:
        item_id: The ID of the item to check
        
    Returns:
        Availability information for the item
    """
    try:
        return client.product.get_availability_by_item_id(item_id)
    except Exception as e:
        return {"error": str(e)}

@mcp.tool()
def get_available_quantity(item_id, branch_number: str, availability_type_id):
    """
    Get available quantity for a specific item.
    
    Args:
        item_id: The ID of the item
        branch_number: The branch number
        availability_type_id: The availability type ID
        
    Returns:
        Available quantity information
    """
    try:
        return client.product.get_available_quantity(item_id, branch_number, availability_type_id)
    except Exception as e:
        return {"error": str(e)}

@mcp.tool()
def get_brands(vhid: Optional[str] = None, phid: Optional[str] = None):
    """
    Get brands information.
    
    Args:
        vhid: Optional vehicle ID
        phid: Optional product hierarchy ID
        
    Returns:
        List of brands
    """
    try:
        return client.product.get_brands(vhid=vhid, phid=phid)
    except Exception as e:
        return {"error": str(e)}

@mcp.tool()
def get_categories(vhid: Optional[str] = None, phid: Optional[str] = None, search_id: Optional[str] = None):
    """
    Get categories information.
    
    Args:
        vhid: Optional vehicle ID
        phid: Optional product hierarchy ID
        search_id: Optional search ID
        
    Returns:
        List of categories
    """
    try:
        return client.product.get_categories(vhid=vhid, phid=phid, search_id=search_id)
    except Exception as e:
        return {"error": str(e)}

# AccountAPI Tools
@mcp.tool()
def delete_bank_account(customer_stripe_id: int):
    """
    Delete a bank account.
    
    Args:
        customer_stripe_id: The customer's Stripe ID
        
    Returns:
        Success or error message
    """
    try:
        client.account.delete_bank_account(customer_stripe_id)
        return {"success": True}
    except Exception as e:
        return {"error": str(e)}

@mcp.tool()
def update_credit_card_default(credit_card_guid: str):
    """
    Update the default credit card.
    
    Args:
        credit_card_guid: The credit card's GUID
        
    Returns:
        Success or error message
    """
    try:
        client.account.update_credit_card_default(UUID(credit_card_guid))
        return {"success": True}
    except Exception as e:
        return {"error": str(e)}

@mcp.tool()
def delete_credit_card(credit_card_guid: str):
    """
    Delete a credit card.
    
    Args:
        credit_card_guid: The credit card's GUID
        
    Returns:
        Success or error message
    """
    try:
        client.account.delete_credit_card(UUID(credit_card_guid))
        return {"success": True}
    except Exception as e:
        return {"error": str(e)}

@mcp.tool()
def get_active_bank_accounts():
    """
    Get active bank accounts.
    
    Returns:
        List of active bank accounts
    """
    try:
        return client.account.get_active_bank_accounts()
    except Exception as e:
        return {"error": str(e)}

@mcp.tool()
def get_credit_cards():
    """
    Get credit cards.
    
    Returns:
        List of credit cards
    """
    try:
        return client.account.get_credit_cards()
    except Exception as e:
        return {"error": str(e)}

@mcp.tool()
def post_credit_card(card_data: Dict):
    """
    Post a credit card.
    
    Args:
        card_data: The credit card data
        
    Returns:
        Credit card GUID or error
    """
    try:
        return client.account.post_credit_card(card_data)
    except Exception as e:
        return {"error": str(e)}

@mcp.tool()
def get_customer_info():
    """
    Get customer information.
    
    Returns:
        Customer info
    """
    try:
        return client.account.get_customer_info()
    except Exception as e:
        return {"error": str(e)}

@mcp.tool()
def get_verified_bank_accounts():
    """
    Get verified bank accounts.
    
    Returns:
        List of verified bank accounts
    """
    try:
        return client.account.get_verified_bank_accounts()
    except Exception as e:
        return {"error": str(e)}

@mcp.tool()
def post_bank_account(bank_account_data: Dict):
    """
    Add a bank account.
    
    Args:
        bank_account_data: Bank account data
        
    Returns:
        Bank account GUID or error
    """
    try:
        return client.account.post_bank_account(bank_account_data)
    except Exception as e:
        return {"error": str(e)}

@mcp.tool()
def verify_bank_account(verification_data: Dict):
    """
    Verify a bank account.
    
    Args:
        verification_data: Bank account verification data
        
    Returns:
        Verification result
    """
    try:
        return client.account.verify_bank_account(verification_data)
    except Exception as e:
        return {"error": str(e)}

# ContentAPI Tools
@mcp.tool()
def get_article_resources(article_id: int):
    """
    Get article resources.
    
    Args:
        article_id: The ID of the article
        
    Returns:
        List of article resources
    """
    try:
        return client.content.get_article_resources(article_id)
    except Exception as e:
        return {"error": str(e)}

@mcp.tool()
def get_articles():
    """
    Get articles.
    
    Returns:
        List of articles
    """
    try:
        return client.content.get_articles()
    except Exception as e:
        return {"error": str(e)}

# CoreAPI Tools
@mcp.tool()
def get_open_cores():
    """
    Get open cores.
    
    Returns:
        List of open cores
    """
    try:
        return client.core.get_open_cores()
    except Exception as e:
        return {"error": str(e)}

# CustomerAPI Tools
@mcp.tool()
def get_users():
    """
    Get users.
    
    Returns:
        List of users
    """
    try:
        return client.customer.get_users()
    except Exception as e:
        return {"error": str(e)}

# VehicleAPI Tools
@mcp.tool()
def get_all_dtcs():
    """
    Get all Diagnostic Trouble Codes.
    
    Returns:
        List of DTCs
    """
    try:
        return client.vehicle.get_all_dtcs()
    except Exception as e:
        return {"error": str(e)}

@mcp.tool()
def get_drive_types_by_vhid(vhid: str):
    """
    Get drive types by vhid.
    
    Args:
        vhid: The vehicle ID
        
    Returns:
        List of drive types
    """
    try:
        return client.vehicle.get_drive_types_by_vhid(vhid)
    except Exception as e:
        return {"error": str(e)}

@mcp.tool()
def get_engines_by_vhid(vhid: str):
    """
    Get engines by vhid.
    
    Args:
        vhid: The vehicle ID
        
    Returns:
        List of engines
    """
    try:
        return client.vehicle.get_engines_by_vhid(vhid)
    except Exception as e:
        return {"error": str(e)}

@mcp.tool()
def get_makes_by_vhid(vhid: str):
    """
    Get makes by vhid.
    
    Args:
        vhid: The vehicle ID
        
    Returns:
        List of makes
    """
    try:
        return client.vehicle.get_makes_by_vhid(vhid)
    except Exception as e:
        return {"error": str(e)}

@mcp.tool()
def get_models_by_vhid(vhid: str):
    """
    Get models by vhid.
    
    Args:
        vhid: The vehicle ID
        
    Returns:
        List of models
    """
    try:
        return client.vehicle.get_models_by_vhid(vhid)
    except Exception as e:
        return {"error": str(e)}

@mcp.tool()
def get_submodels_by_vhid(vhid: str):
    """
    Get submodels by vhid.
    
    Args:
        vhid: The vehicle ID
        
    Returns:
        List of submodels
    """
    try:
        return client.vehicle.get_submodels_by_vhid(vhid)
    except Exception as e:
        return {"error": str(e)}

@mcp.tool()
def get_transmissions(tag_number: Optional[str] = None, transmission_mfr_code: Optional[str] = None):
    """
    Get transmission information.
    
    Args:
        tag_number: Optional tag number
        transmission_mfr_code: Optional transmission manufacturer code
        
    Returns:
        List of transmissions
    """
    try:
        return client.vehicle.get_transmissions(tag_number=tag_number, transmission_mfr_code=transmission_mfr_code)
    except Exception as e:
        return {"error": str(e)}

@mcp.tool()
def get_vehicle_by_vhid(vhid: str):
    """
    Get vehicle information by vhid.
    
    Args:
        vhid: The vehicle ID
        
    Returns:
        Vehicle information
    """
    try:
        return client.vehicle.get_vehicle_by_vhid(vhid)
    except Exception as e:
        return {"error": str(e)}

@mcp.tool()
def get_vehicles_by_vin(vin: str):
    """
    Get vehicle information by VIN.
    
    Args:
        vin: The vehicle identification number
        
    Returns:
        Vehicle information
    """
    try:
        return client.vehicle.get_vehicles_by_vin(vin)
    except Exception as e:
        return {"error": str(e)}

@mcp.tool()
def get_years(vhid: Optional[str] = None):
    """
    Get the years for a given vhid.
    
    Args:
        vhid: Optional vehicle ID
        
    Returns:
        List of years
    """
    try:
        return client.vehicle.get_years(vhid=vhid)
    except Exception as e:
        return {"error": str(e)}

@mcp.tool()
def get_year_make_model_vhid(year: int, make: str, model: str):
    """
    Get the vhid for a given year, make, and model.
    
    Args:
        year: The vehicle year
        make: The vehicle make
        model: The vehicle model
        
    Returns:
        Vehicle ID (vhid) information
    """
    try:
        return client.vehicle.get_year_make_model_vhid(year, make, model)
    except Exception as e:
        return {"error": str(e)}
    
if __name__ == "__main__":
    # Initialize and run the server
    mcp.run(transport='stdio')
