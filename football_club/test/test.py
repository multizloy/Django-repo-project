import unittest
from django import views
from django.http import HttpRequest
from cart import views


class TestItemListView(unittest.TestCase):
    def test_item_list_view_status_code(self):
        # Arrange
        request = HttpRequest()

        # Act
        response = views.Cart_List(request)

        # Assert
        self.assertEqual(response.status_code, 200)

    def test_item_list_view_returns_template(self):
        # Arrange
        request = HttpRequest()

        # Act
        response = views.Cart_List(request)

        # Assert
        self.assertTemplateUsed(response, "store/item_list.html")


from cart.views import add_cart_summary, delete_cart_summary
from unittest.mock import patch

from cart.views import add_cart_summary, delete_cart_summary
from unittest.mock import patch


class TestCartViews(unittest.TestCase):
    @patch("cart.views.Cart")
    @patch("cart.views.get_object_or_404")
    @patch("cart.views.Item")
    @patch("cart.views.request")
    def test_add_cart_summary(
        self, mock_request, mock_Item, mock_get_object, mock_Cart
    ):
        mock_request.POST.get.return_value = "post"
        mock_Item.id = 1
        mock_Cart.return_value.add.return_value = None
        mock_Cart.return_value.__len__.return_value = 5

        response = add_cart_summary(mock_request)

        self.assertEqual(response.content, b'{"qty": 5}')

    @patch("cart.views.Cart")
    @patch("cart.views.request")
    def test_delete_cart_summary(self, mock_request, mock_Cart):
        mock_request.POST.get.return_value = "post"
        mock_Cart.return_value.delete.return_value = None

        response = delete_cart_summary(mock_request)

        self.assertEqual(response.template_name, "cart/cart_list.html")
