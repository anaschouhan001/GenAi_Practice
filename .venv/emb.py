from google import genai
import numpy as np 

client = genai.Client()
document= [
    "Refund requests are allowed within 7 days.",
    ["Python classes happen monday to friday "],
    ["Student get 3 interview opportunities ",]
]

question="Can I get my money back after 5 days."
document_vector= []

result = client.models.embed_content(
    model="gemini-embedding",
    contents=question
)
vector= result.embeddings[0].values
document_vector.append(vector)

question_result= client.models.embed_content(
    model="gemini-embedding-001",
    contents=question
    
)
question_vector = question_result.embeddings[0]. values
def cosine_similarity(a,b):
    a= np.array(a)
    b=np.array(b)
    
    return np.dot(a,b) / (
        np.linalg.norm(a) * np.linalg.norm(b)
)
    for document, vector in zip(documents,document_vector):
        score=cosine_similarity(
            question_vector,
            vector
        )
        
        print(round(score,3),document)