import chromadb

from llm import generate_answer

from sentence_transformers import SentenceTransformer

client = chromadb.PersistentClient(
    path="./chroma_db"
)

collection = client.get_collection(
    "products"
)

model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)


def search_products(query):

    query_embedding = model.encode(
        query
    ).tolist()

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=3
    )

    return results["documents"][0]


def ask_rag(question):

    documents = search_products(question)

    context = "\n".join(documents)

    answer = generate_answer(
        question,
        context
    )

    return answer