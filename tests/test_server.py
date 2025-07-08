"""Tests for the MCP server functionality"""

import pytest
import asyncio
from unittest.mock import Mock, patch, AsyncMock
from uuid import UUID
from mcp.server.fastmcp import FastMCP
import sys
import os

# Add the parent directory to the path to import server
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class TestMCPServer:
    """Test class for MCP server tools"""
    
    @pytest.fixture
    def mock_client(self):
        """Create a mock TransendAPIClient"""
        mock_client = Mock()
        
        # Mock branch API
        mock_client.branch = Mock()
        mock_client.branch.get_all_branches = Mock(return_value=[{"id": 1, "name": "Branch 1"}])
        mock_client.branch.get_branch_by_number = Mock(return_value={"id": 1, "number": "001"})
        
        # Mock product API
        mock_client.product = Mock()
        mock_client.product.get_all_sort_types = Mock(return_value=[{"id": 1, "name": "Sort Type 1"}])
        mock_client.product.get_all_tags = Mock(return_value=[{"id": 1, "name": "Tag 1"}])
        mock_client.product.get_availability_by_item_id = Mock(return_value={"available": True})
        mock_client.product.get_available_quantity = Mock(return_value={"quantity": 10})
        mock_client.product.get_brands = Mock(return_value=[{"id": 1, "name": "Brand 1"}])
        mock_client.product.get_categories = Mock(return_value=[{"id": 1, "name": "Category 1"}])
        
        # Mock account API
        mock_client.account = Mock()
        mock_client.account.delete_bank_account = Mock()
        mock_client.account.update_credit_card_default = Mock()
        mock_client.account.delete_credit_card = Mock()
        mock_client.account.get_active_bank_accounts = Mock(return_value=[{"id": 1, "active": True}])
        mock_client.account.get_credit_cards = Mock(return_value=[{"id": 1, "last_four": "1234"}])
        mock_client.account.post_credit_card = Mock(return_value={"guid": "test-guid"})
        mock_client.account.get_customer_info = Mock(return_value={"id": 1, "name": "Test Customer"})
        mock_client.account.get_verified_bank_accounts = Mock(return_value=[{"id": 1, "verified": True}])
        mock_client.account.post_bank_account = Mock(return_value={"guid": "bank-guid"})
        mock_client.account.verify_bank_account = Mock(return_value={"verified": True})
        
        # Mock content API
        mock_client.content = Mock()
        mock_client.content.get_article_resources = Mock(return_value=[{"id": 1, "title": "Resource 1"}])
        mock_client.content.get_articles = Mock(return_value=[{"id": 1, "title": "Article 1"}])
        
        # Mock core API
        mock_client.core = Mock()
        mock_client.core.get_open_cores = Mock(return_value=[{"id": 1, "status": "open"}])
        
        # Mock customer API
        mock_client.customer = Mock()
        mock_client.customer.get_users = Mock(return_value=[{"id": 1, "username": "testuser"}])
        
        # Mock vehicle API
        mock_client.vehicle = Mock()
        mock_client.vehicle.get_all_dtcs = Mock(return_value=[{"code": "P0001", "description": "Test DTC"}])
        mock_client.vehicle.get_drive_types_by_vhid = Mock(return_value=[{"id": 1, "type": "FWD"}])
        mock_client.vehicle.get_engines_by_vhid = Mock(return_value=[{"id": 1, "type": "V6"}])
        mock_client.vehicle.get_makes_by_vhid = Mock(return_value=[{"id": 1, "name": "Toyota"}])
        mock_client.vehicle.get_models_by_vhid = Mock(return_value=[{"id": 1, "name": "Camry"}])
        mock_client.vehicle.get_submodels_by_vhid = Mock(return_value=[{"id": 1, "name": "LE"}])
        mock_client.vehicle.get_transmissions = Mock(return_value=[{"id": 1, "type": "Automatic"}])
        mock_client.vehicle.get_vehicle_by_vhid = Mock(return_value={"id": 1, "year": 2020})
        mock_client.vehicle.get_vehicles_by_vin = Mock(return_value=[{"id": 1, "vin": "TEST123"}])
        mock_client.vehicle.get_years = Mock(return_value=[2020, 2021, 2022])
        mock_client.vehicle.get_year_make_model_vhid = Mock(return_value={"vhid": "test-vhid"})
        
        return mock_client

    @patch('server.client')
    def test_get_all_branches_success(self, mock_client_instance, mock_client):
        """Test successful branch retrieval"""
        mock_client_instance.branch.get_all_branches.return_value = [{"id": 1, "name": "Branch 1"}]
        
        from server import get_all_branches
        result = get_all_branches()
        
        assert result == [{"id": 1, "name": "Branch 1"}]
        mock_client_instance.branch.get_all_branches.assert_called_once_with(active=None)

    @patch('server.client')
    def test_get_all_branches_with_active_filter(self, mock_client_instance, mock_client):
        """Test branch retrieval with active filter"""
        mock_client_instance.branch.get_all_branches.return_value = [{"id": 1, "name": "Active Branch"}]
        
        from server import get_all_branches
        result = get_all_branches(active=True)
        
        assert result == [{"id": 1, "name": "Active Branch"}]
        mock_client_instance.branch.get_all_branches.assert_called_once_with(active=True)

    @patch('server.client')
    def test_get_all_branches_error(self, mock_client_instance, mock_client):
        """Test branch retrieval error handling"""
        mock_client_instance.branch.get_all_branches.side_effect = Exception("API Error")
        
        from server import get_all_branches
        result = get_all_branches()
        
        assert result == {"error": "API Error"}

    @patch('server.client')
    def test_get_branch_by_number_success(self, mock_client_instance, mock_client):
        """Test successful branch retrieval by number"""
        mock_client_instance.branch.get_branch_by_number.return_value = {"id": 1, "number": "001"}
        
        from server import get_branch_by_number
        result = get_branch_by_number("001")
        
        assert result == {"id": 1, "number": "001"}
        mock_client_instance.branch.get_branch_by_number.assert_called_once_with("001")

    @patch('server.client')
    def test_get_all_sort_types_success(self, mock_client_instance, mock_client):
        """Test successful sort types retrieval"""
        mock_client_instance.product.get_all_sort_types.return_value = [{"id": 1, "name": "Sort Type 1"}]
        
        from server import get_all_sort_types
        result = get_all_sort_types()
        
        assert result == [{"id": 1, "name": "Sort Type 1"}]
        mock_client_instance.product.get_all_sort_types.assert_called_once()

    @patch('server.client')
    def test_get_all_tags_success(self, mock_client_instance, mock_client):
        """Test successful tags retrieval"""
        mock_client_instance.product.get_all_tags.return_value = [{"id": 1, "name": "Tag 1"}]
        
        from server import get_all_tags
        result = get_all_tags()
        
        assert result == [{"id": 1, "name": "Tag 1"}]
        mock_client_instance.product.get_all_tags.assert_called_once()

    @patch('server.client')
    def test_get_availability_by_item_id_success(self, mock_client_instance, mock_client):
        """Test successful availability retrieval"""
        mock_client_instance.product.get_availability_by_item_id.return_value = {"available": True}
        
        from server import get_availability_by_item_id
        result = get_availability_by_item_id("item123")
        
        assert result == {"available": True}
        mock_client_instance.product.get_availability_by_item_id.assert_called_once_with("item123")

    @patch('server.client')
    def test_get_available_quantity_success(self, mock_client_instance, mock_client):
        """Test successful quantity retrieval"""
        mock_client_instance.product.get_available_quantity.return_value = {"quantity": 10}
        
        from server import get_available_quantity
        result = get_available_quantity("item123", "001", "type1")
        
        assert result == {"quantity": 10}
        mock_client_instance.product.get_available_quantity.assert_called_once_with("item123", "001", "type1")

    @patch('server.client')
    def test_delete_bank_account_success(self, mock_client_instance, mock_client):
        """Test successful bank account deletion"""
        from server import delete_bank_account
        result = delete_bank_account(123)
        
        assert result == {"success": True}
        mock_client_instance.account.delete_bank_account.assert_called_once_with(123)

    @patch('server.client')
    def test_delete_bank_account_error(self, mock_client_instance, mock_client):
        """Test bank account deletion error handling"""
        mock_client_instance.account.delete_bank_account.side_effect = Exception("Delete Error")
        
        from server import delete_bank_account
        result = delete_bank_account(123)
        
        assert result == {"error": "Delete Error"}

    @patch('server.client')
    def test_update_credit_card_default_success(self, mock_client_instance, mock_client):
        """Test successful credit card default update"""
        from server import update_credit_card_default
        result = update_credit_card_default("550e8400-e29b-41d4-a716-446655440000")
        
        assert result == {"success": True}
        mock_client_instance.account.update_credit_card_default.assert_called_once()

    @patch('server.client')
    def test_delete_credit_card_success(self, mock_client_instance, mock_client):
        """Test successful credit card deletion"""
        from server import delete_credit_card
        result = delete_credit_card("550e8400-e29b-41d4-a716-446655440000")
        
        assert result == {"success": True}
        mock_client_instance.account.delete_credit_card.assert_called_once()

    @patch('server.client')
    def test_get_vehicles_by_vin_success(self, mock_client_instance, mock_client):
        """Test successful vehicle retrieval by VIN"""
        mock_client_instance.vehicle.get_vehicles_by_vin.return_value = [{"id": 1, "vin": "TEST123"}]
        
        from server import get_vehicles_by_vin
        result = get_vehicles_by_vin("TEST123")
        
        assert result == [{"id": 1, "vin": "TEST123"}]
        mock_client_instance.vehicle.get_vehicles_by_vin.assert_called_once_with("TEST123")

    @patch('server.client')
    def test_get_year_make_model_vhid_success(self, mock_client_instance, mock_client):
        """Test successful vhid retrieval by year/make/model"""
        mock_client_instance.vehicle.get_year_make_model_vhid.return_value = {"vhid": "test-vhid"}
        
        from server import get_year_make_model_vhid
        result = get_year_make_model_vhid(2020, "Toyota", "Camry")
        
        assert result == {"vhid": "test-vhid"}
        mock_client_instance.vehicle.get_year_make_model_vhid.assert_called_once_with(2020, "Toyota", "Camry")

    @patch('server.client')
    def test_get_customer_info_success(self, mock_client_instance, mock_client):
        """Test successful customer info retrieval"""
        mock_client_instance.account.get_customer_info.return_value = {"id": 1, "name": "Test Customer"}
        
        from server import get_customer_info
        result = get_customer_info()
        
        assert result == {"id": 1, "name": "Test Customer"}
        mock_client_instance.account.get_customer_info.assert_called_once()

    @patch('server.client')
    def test_get_articles_success(self, mock_client_instance, mock_client):
        """Test successful articles retrieval"""
        mock_client_instance.content.get_articles.return_value = [{"id": 1, "title": "Article 1"}]
        
        from server import get_articles
        result = get_articles()
        
        assert result == [{"id": 1, "title": "Article 1"}]
        mock_client_instance.content.get_articles.assert_called_once()

    @patch('server.client')
    def test_get_open_cores_success(self, mock_client_instance, mock_client):
        """Test successful open cores retrieval"""
        mock_client_instance.core.get_open_cores.return_value = [{"id": 1, "status": "open"}]
        
        from server import get_open_cores
        result = get_open_cores()
        
        assert result == [{"id": 1, "status": "open"}]
        mock_client_instance.core.get_open_cores.assert_called_once()

    @patch('server.client')
    def test_get_users_success(self, mock_client_instance, mock_client):
        """Test successful users retrieval"""
        mock_client_instance.customer.get_users.return_value = [{"id": 1, "username": "testuser"}]
        
        from server import get_users
        result = get_users()
        
        assert result == [{"id": 1, "username": "testuser"}]
        mock_client_instance.customer.get_users.assert_called_once()
