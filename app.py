from flask import Flask

app = Flask(__name__)

# Ürün listesi
products = [
    {'id': 1, 'name': 'Telefon'},
    {'id': 2, 'name': 'Laptop'},
    {'id': 3, 'name': 'Kulaklık'}
]

# Sepet
cart = []

# Anasayfa route'u (eksikti)
@app.route('/')
def home():
    return 'Telefon | Laptop | Kulaklık'  # veya HTML dön

# Ürün ekleme route'u
@app.route('/add/<int:product_id>')
def add_to_cart(product_id):
    product = next((p for p in products if p['id'] == product_id), None)
    if product:
        cart.append(product)
        return f"{product['name']} sepete eklendi!"
    return "Ürün bulunamadı."
