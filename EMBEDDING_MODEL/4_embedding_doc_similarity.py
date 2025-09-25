from langchain_openai import OpenAIEmbeddings
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from dotenv import load_dotenv
load_dotenv()


embedding = OpenAIEmbeddings(model = "text-embedding-3-large",dimensions=300)

documents = [
    "Delhi is the capital of India",
    "London is the Capital of England",
    "Paris is the capital of France",
    "Lucknow is the capital of Uttar Pradesh",
    "Dehradun is the capital of Uttrakhand",
]
query = "tell me about Dehradun"

doc_embeddings = embedding.embed_documents(documents)
query_embedding = embedding.embed_query(query)

similarity_vectors = cosine_similarity([query_embedding],doc_embeddings)[0]
index,score = sorted(list(enumerate(similarity_vectors)),key=lambda x:x[1],reverse=True)[0]

print(documents[index])
