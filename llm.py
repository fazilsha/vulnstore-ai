from ollama import chat

MODEL = "llama3"


def generate_answer(question, context):

    prompt = f"""
You are an ecommerce assistant.

Only answer using the provided context.

Context:
{context}

Question:
{question}
"""

    response = chat(
        model=MODEL,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response["message"]["content"]