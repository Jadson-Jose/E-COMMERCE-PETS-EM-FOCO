import pytest
from product.models import Product

@pytest.mark.django_db
def test_create_product():
    product = Product.objects.create(
        name="Ração Premium",
        description="Ração para cães adultos 15kg",
        price=199.90,
        stock=50
    )
    
    assert product.name == "Ração Premium"
    assert product.stock == 50
    
@pytest.mark.django_db
def test_product_str():
    product = Product.objects.create(
        name="Brinquedo para gatos",
        description="Brinquedo interativo",
        price=29.90,
        stock=100
    )
    assert str(product) == "Brinquedo para gatos"

@pytest.mark.django_db
def test_product_description():
    product = Product.objects.create(
        name="Brinquedo para gatos",
        description="Brinquedo interativo",
        price=29.90,
        stock=100
    )
    assert product.description == "Brinquedo interativo"
    
@pytest.mark.django_db
def test_update_product_stock():
    product = Product.objects.create(
        name="Areia para gatos",
        description="Areia higiênica",
        price=49.99,
        stock=30
    )
    product.stock += 20
    product.save()
    
@pytest.mark.django_db
def test_delete_product():
    product = Product.objects.create(
        name="Coleira para cacharro",
        description="Coleira azul",
        price=59.99,
        stock=10
    )
    product_id = product.id
    product.delete()
    
    with pytest.raises(Product.DoesNotExist):
        Product.objects.get(id=product_id)