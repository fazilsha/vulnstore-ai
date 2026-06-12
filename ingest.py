import json
import chromadb

from sentence_transformers import SentenceTransformer

client = chromadb.PersistentClient(path="./chroma_db")

collection = client.get_or_create_collection(
    name="products"
)

model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)

with open("data/products.json", "r") as f:
    products = json.load(f)

for product in products:

    text = f"""
    Name: {product['name']}
    Category: {product['category']}
    Price: {product['price']}
    Description: {product['description']}
    """

    embedding = model.encode(text).tolist()

    collection.add(
        ids=[str(product["id"])],
        documents=[text],
        embeddings=[embedding]
    )

print("Products loaded successfully")