"""Shared test fixtures and configuration for pytest"""

import pytest
import os
from unittest.mock import Mock, AsyncMock
from uuid import UUID


@pytest.fixture
def mock_env_vars():
    """Mock environment variables for testing"""
    return {
        'TRANSEND_API_KEY': 'test_api_key_12345',
        'TRANSEND_API_TOKEN': 'test_api_token_67890'
    }


@pytest.fixture
def mock_transend_client():
    """Create a comprehensive mock of TransendAPIClient"""
    mock_client = Mock()
    
    # Branch API
    mock_client.branch = Mock()
    mock_client.branch.get_all_branches = Mock(return_value=[
        {"id": 1, "name": "Test Branch", "active": True}
    ])
    mock_client.branch.get_branch_by_number = Mock(return_value={
        "id": 1, "number": "001", "name": "Test Branch"
    })
    
    # Product API
    mock_client.product = Mock()
    mock_client.product.get_all_sort_types = Mock(return_value=[
        {"id": 1, "name": "Sort Type 1"}
    ])
    mock_client.product.get_all_tags = Mock(return_value=[
        {"id": 1, "name": "Tag 1"}
    ])
    mock_client.product.get_availability_by_item_id = Mock(return_value={
        "item_id": "test123", "available": True, "quantity": 10
    })
    mock_client.product.get_available_quantity = Mock(return_value={
        "quantity": 5, "reserved": 2, "available": 3
    })
    mock_client.product.get_brands = Mock(return_value=[
        {"id": 1, "name": "Test Brand"}
    ])
    mock_client.product.get_categories = Mock(return_value=[
        {"id": 1, "name": "Test Category"}
    ])
    
    # Account API
    mock_client.account = Mock()
    mock_client.account.delete_bank_account = Mock()
    mock_client.account.update_credit_card_default = Mock()
    mock_client.account.delete_credit_card = Mock()
    mock_client.account.get_active_bank_accounts = Mock(return_value=[
        {"id": 1, "account_number": "****1234", "active": True}
    ])
    mock_client.account.get_credit_cards = Mock(return_value=[
        {"id": 1, "last_four": "1234", "brand": "Visa"}
    ])
    mock_client.account.post_credit_card = Mock(return_value={
        "guid": "550e8400-e29b-41d4-a716-446655440000"
    })
    mock_client.account.get_customer_info = Mock(return_value={
        "id": 1, "name": "Test Customer", "email": "test@example.com"
    })
    mock_client.account.get_verified_bank_accounts = Mock(return_value=[
        {"id": 1, "account_number": "****5678", "verified": True}
    ])
    mock_client.account.post_bank_account = Mock(return_value={
        "guid": "bank-guid-123"
    })
    mock_client.account.verify_bank_account = Mock(return_value={
        "verified": True, "status": "success"
    })
    
    # Content API
    mock_client.content = Mock()
    mock_client.content.get_article_resources = Mock(return_value=[
        {"id": 1, "title": "Test Resource", "type": "pdf"}
    ])
    mock_client.content.get_articles = Mock(return_value=[
        {"id": 1, "title": "Test Article", "published": True}
    ])
    
    # Core API
    mock_client.core = Mock()
    mock_client.core.get_open_cores = Mock(return_value=[
        {"id": 1, "core_number": "CORE001", "status": "open"}
    ])
    
    # Customer API
    mock_client.customer = Mock()
    mock_client.customer.get_users = Mock(return_value=[
        {"id": 1, "username": "testuser", "active": True}
    ])
    
    # Vehicle API
    mock_client.vehicle = Mock()
    mock_client.vehicle.get_all_dtcs = Mock(return_value=[
        {"code": "P0001", "description": "Test DTC", "severity": "low"}
    ])
    mock_client.vehicle.get_drive_types_by_vhid = Mock(return_value=[
        {"id": 1, "type": "FWD", "description": "Front Wheel Drive"}
    ])
    mock_client.vehicle.get_engines_by_vhid = Mock(return_value=[
        {"id": 1, "type": "V6", "displacement": "3.5L"}
    ])
    mock_client.vehicle.get_makes_by_vhid = Mock(return_value=[
        {"id": 1, "name": "Toyota", "country": "Japan"}
    ])
    mock_client.vehicle.get_models_by_vhid = Mock(return_value=[
        {"id": 1, "name": "Camry", "make": "Toyota"}
    ])
    mock_client.vehicle.get_submodels_by_vhid = Mock(return_value=[
        {"id": 1, "name": "LE", "trim_level": "base"}
    ])
    mock_client.vehicle.get_transmissions = Mock(return_value=[
        {"id": 1, "type": "Automatic", "speeds": 8}
    ])
    mock_client.vehicle.get_vehicle_by_vhid = Mock(return_value={
        "id": 1, "year": 2020, "make": "Toyota", "model": "Camry"
    })
    mock_client.vehicle.get_vehicles_by_vin = Mock(return_value=[
        {"id": 1, "vin": "TEST123456789", "year": 2020}
    ])
    mock_client.vehicle.get_years = Mock(return_value=[2020, 2021, 2022, 2023])
    mock_client.vehicle.get_year_make_model_vhid = Mock(return_value={
        "vhid": "test_vhid_12345"
    })
    
    return mock_client


@pytest.fixture
def mock_anthropic_client():
    """Create a mock Anthropic client"""
    mock_anthropic = Mock()
    
    # Default text response
    mock_content = Mock()
    mock_content.type = 'text'
    mock_content.text = 'Test response from Anthropic'
    
    mock_response = Mock()
    mock_response.content = [mock_content]
    mock_anthropic.messages.create.return_value = mock_response
    
    return mock_anthropic


@pytest.fixture
def mock_mcp_session():
    """Create a mock MCP ClientSession"""
    mock_session = AsyncMock()
    mock_session.initialize = AsyncMock()
    mock_session.list_tools = AsyncMock()
    mock_session.call_tool = AsyncMock()
    
    # Mock tools response
    mock_tool = Mock()
    mock_tool.name = "test_tool"
    mock_tool.description = "Test tool description"
    mock_tool.inputSchema = {
        "type": "object",
        "properties": {
            "param": {
                "type": "string",
                "description": "Test parameter"
            }
        }
    }
    
    mock_tools_response = Mock()
    mock_tools_response.tools = [mock_tool]
    mock_session.list_tools.return_value = mock_tools_response
    
    # Mock tool call response
    mock_tool_result = Mock()
    mock_tool_result.content = [{"result": "success", "data": "test_data"}]
    mock_session.call_tool.return_value = mock_tool_result
    
    return mock_session


@pytest.fixture
def sample_tool_schemas():
    """Sample tool schemas for testing"""
    return [
        {
            "name": "get_all_branches",
            "description": "Get all branches from the Transend API.",
            "input_schema": {
                "type": "object",
                "properties": {
                    "active": {
                        "type": "boolean",
                        "description": "Optional flag to filter branches by active status"
                    }
                }
            }
        },
        {
            "name": "get_vehicles_by_vin",
            "description": "Get vehicle information by VIN.",
            "input_schema": {
                "type": "object",
                "properties": {
                    "vin": {
                        "type": "string",
                        "description": "The vehicle identification number"
                    }
                },
                "required": ["vin"]
            }
        }
    ]


@pytest.fixture
def sample_api_responses():
    """Sample API responses for testing"""
    return {
        "branches": [
            {"id": 1, "name": "Main Branch", "active": True, "location": "Downtown"},
            {"id": 2, "name": "North Branch", "active": True, "location": "North Side"},
            {"id": 3, "name": "Closed Branch", "active": False, "location": "Old Town"}
        ],
        "vehicles": [
            {
                "id": 1,
                "vin": "1HGBH41JXMN109186",
                "year": 2021,
                "make": "Honda",
                "model": "Civic",
                "trim": "LX"
            }
        ],
        "customer_info": {
            "id": 12345,
            "name": "John Doe",
            "email": "john.doe@example.com",
            "phone": "+1-555-0123",
            "address": {
                "street": "123 Main St",
                "city": "Anytown",
                "state": "CA",
                "zip": "12345"
            }
        }
    }


@pytest.fixture(autouse=True)
def clean_environment():
    """Clean up environment variables after each test"""
    original_env = os.environ.copy()
    yield
    # Restore original environment
    os.environ.clear()
    os.environ.update(original_env)


# Pytest configuration for async tests
pytest_plugins = ('pytest_asyncio',)
