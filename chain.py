from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

def create_chain():
    """Create a stateless chatbot chain (no conversation history)."""
    llm = ChatOllama(model="deepseek-r1:1.5b")

    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are a helpful assistant. Help the user to the best of your ability. Be concise."),
        ("human", "{input}")
    ])

    chain = prompt | llm | StrOutputParser()
    return chain

def get_response(user_input: str) -> str:
    """Get a response from the chatbot for a single user message (stateless)."""
    chain = create_chain()
    response = chain.invoke({"input": user_input})
    return response
