from langchain_groq import ChatGroq

def get_response(context, ats, missing, query, api_key):

    llm = ChatGroq(
        model="llama-3.1-8b-instant",
        groq_api_key=api_key,
        temperature=0
    )

    prompt = f"""
You are an ATS assistant.

STRICT RULES:
- Use ATS Score and Missing Skills strictly
- If missing skills list is empty, explain why
- Be clear and helpful

Context:
{context}

ATS Score: {ats}
Missing Skills: {missing}

Question:
{query}
"""

    response = llm.invoke(prompt)

    return response.content