from django.db import models

class Client(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=100)
    address = models.TextField()
    registration_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()
    added_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name

class Order(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    order_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.client} - {self.total_amount}"

# Создание клиента
def create_client(name, email, phone_number, address):
    client = Client(name=name, email=email, phone_number=phone_number, address=address)
    client.save()
    return client

# Получение всех клиентов
def get_all_clients():
    return Client.objects.all()

# Получение клиента по ID
def get_client_by_id(client_id):
    return Client.objects.get(id=client_id)

# Обновление информации о клиенте
def update_client(client_id, name, email, phone_number, address):
    client = get_client_by_id(client_id)
    client.name = name
    client.email = email
    client.phone_number = phone_number
    client.address = address
    client.save()

# Удаление клиента
def delete_client(client_id):
    client = get_client_by_id(client_id)
    client.delete()

# Создание товара
def create_product(name, description, price, quantity):
    product = Product(name=name, description=description, price=price, quantity=quantity)
    product.save()
    return product

# Получение всех товаров
def get_all_products():
    return Product.objects.all()

# Получение товара по ID
def get_product_by_id(product_id):
    return Product.objects.get(id=product_id)

# Обновление информации о товаре
def update_product(product_id, name, description, price, quantity):
    product = get_product_by_id(product_id)
    product.name = name
    product.description = description
    product.price = price
    product.quantity = quantity
    product.save()

# Удаление товара
def delete_product(product_id):
    product = get_product_by_id(product_id)
    product.delete()

# Создание заказа
def create_order(client, products, total_amount):
    order = Order(client=client, total_amount=total_amount)
    order.save()
    order.products.set(products)
    return order

# Получение всех заказов
def get_all_orders():
    return Order.objects.all()

# Получение заказа по ID
def get_order_by_id(order_id):
    return Order.objects.get(id=order_id)

# Обновление информации о заказе
def update_order(order_id, client, products, total_amount):
    order = get_order_by_id(order_id)
    order.client = client
    order.total_amount = total_amount
    order.save()
    order.products.set(products)

# Удаление заказа
def delete_order(order_id):
    order = get_order_by_id(order_id)
    order.delete()