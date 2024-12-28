from sqlalchemy import Column, Integer, String, Float, ForeignKey, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

Base = declarative_base()

# Модель Category
class Category(Base):
    __tablename__ = 'categories'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

    # Связь с продуктами
    products = relationship("Product", back_populates="category", cascade="all, delete-orphan")

# Модель Product
class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    price = Column(Float, nullable=False)
    category_id = Column(Integer, ForeignKey('categories.id'))

    # Обратная связь с категорией
    category = relationship("Category", back_populates="products")

    
# Подключение к базе данных и настройка сессии
engine = create_engine('sqlite:///example.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

# CRUD-операции
# 1. Создание категорий и продуктов
def create_category_and_products():
    category1 = Category(name="Electronics")
    category2 = Category(name="Clothing")

    product1 = Product(name="Smartphone", price=699.99, category=category1)
    product2 = Product(name="Laptop", price=999.99, category=category1)
    product3 = Product(name="T-shirt", price=19.99, category=category2)

    session.add_all([category1, category2, product1, product2, product3])
    session.commit()

# 2. Чтение продуктов по категориям
def read_products_by_category(category_name):
    category = session.query(Category).filter_by(name=category_name).first()
    if category:
        for product in category.products:
            print(f"Product: {product.name}, Price: {product.price}")
    else:
        print("Category not found.")

# 3. Обновление категории у продукта
def update_product_category(product_name, new_category_name):
    product = session.query(Product).filter_by(name=product_name).first()
    new_category = session.query(Category).filter_by(name=new_category_name).first()

    if product and new_category:
        product.category = new_category
        session.commit()
        print(f"Product '{product.name}' moved to category '{new_category.name}'.")
    else:
        print("Product or category not found.")

# 4. Удаление категории и связанных продуктов
def delete_category_and_products(category_name):
    category = session.query(Category).filter_by(name=category_name).first()
    if category:
        session.delete(category)
        session.commit()
        print(f"Category '{category_name}' and its products were deleted.")
    else:
        print("Category not found.")

# Пример использования
if __name__ == "__main__":
    create_category_and_products()

    print("\nProducts in Electronics:")
    read_products_by_category("Electronics")

    print("\nUpdating category for T-shirt:")
    update_product_category("T-shirt", "Electronics")

    print("\nDeleting category Clothing:")
    delete_category_and_products("Clothing")
