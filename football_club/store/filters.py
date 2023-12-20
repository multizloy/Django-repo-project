import django_filters

from store.models import Item


# фильтры для товаров с названием и ценой 1 в 1 с поиском
""" class Product_Filter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr="iexact")

    class Meta:
        model = Item
        fields = [
            "price",
        ]
 """


# фильтры для товаров с областью поиска
class Product_Filter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr="iexact")
    # price = django_filters.NumberFilter()
    price__gt = django_filters.NumberFilter(field_name="price", lookup_expr="gt")
    price__lt = django_filters.NumberFilter(field_name="price", lookup_expr="lt")

    # category__name = django_filters.CharFilter(lookup_expr="icontains")

    class Meta:
        model = Item
        fields = ["Имя"]
        fields = {"price": ["lt", "gt"]}
