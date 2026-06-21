def total_revenue(purchases):
    """
    Рассчитывает общую выручку
    """
    total = 0

    for purchase in purchases:
        total += purchase['price'] * purchase['quantity']

    return total

def items_by_category(purchases):
    """
    Возвращает словарь, где ключ — категория, а значение — список уникальных товаров в этой категории
    """
    category_items = {}
    for purchase in purchases:
        category = purchase['category']
        item = purchase['item']
        # Если нет категории в словаре, добавляем её
        if category not in category_items:
            category_items[category] = []
        # Если нет товара в списке категорий
        if item not in category_items[category]:
            category_items[category].append(item)
    
    return category_items

def expensive_purchases(purchases, min_price):
    """
    Возвращает список покупок, где цена товара больше или равна min_price
    """
    result = []
    for purchase in purchases:
        if purchase['price'] >= min_price:
            result.append(purchase)
    
    return result

def average_price_by_category(purchases):
    """
    Рассчитывает среднюю цену товаров по каждой категории
    """
    category_prices = {}
    category_counts = {}
    
    for purchase in purchases:
        category = purchase['category']
        price = purchase['price']
        if category not in category_prices:
            category_prices[category] = 0
            category_counts[category] = 0
        category_prices[category] += price
        category_counts[category] += 1
    
    average_prices = {}
    for category in category_prices:
        average_prices[category] = category_prices[category] / category_counts[category]
    
    return average_prices

def most_frequent_category(purchases):
    """
    Находит и возвращает категорию, в которой куплено больше всего единиц товаров
    """
    category_quantities = {}
    
    for purchase in purchases:
        category = purchase['category']
        quantity = purchase['quantity']
        if category not in category_quantities:
            category_quantities[category] = 0
        category_quantities[category] += quantity
    
    max_category = None
    max_quantity = -1
    for category, quantity in category_quantities.items():
        if quantity > max_quantity:
            max_quantity = quantity
            max_category = category
    
    return max_category


# main
purchases = [
    {"item": "apple", "category": "fruit", "price": 1.2, "quantity": 10},
    {"item": "banana", "category": "fruit", "price": 0.5, "quantity": 5},
    {"item": "milk", "category": "dairy", "price": 1.5, "quantity": 2},
    {"item": "bread", "category": "bakery", "price": 2.0, "quantity": 3},
]

# Общая выручка
revenue = total_revenue(purchases)
print(f"Общая выручка: {revenue}")

# Товары по категориям
categories = items_by_category(purchases)
print(f"Товары по категориям: {categories}")

# Покупки дороже заданной цены
min_price = 1.0
expensive = expensive_purchases(purchases, min_price)
print(f"Покупки дороже {min_price}: {expensive}")

# Средняя цена по категориям
avg_prices = average_price_by_category(purchases)
print(f"Средняя цена по категориям: {avg_prices}")

# Категория с наибольшим количеством проданных товаров
most_frequent = most_frequent_category(purchases)
print(f"Категория с наибольшим количеством проданных товаров: {most_frequent}")