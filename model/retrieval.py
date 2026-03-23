import pickle
from sentence_transformers import SentenceTransformer, util

# Load embeddings
with open("model/embeddings.pkl", "rb") as f:
    data = pickle.load(f)

tickets = data["tickets"]
answers = data["answers"]
ticket_embeddings = data["embeddings"]


## Loading the model
model = SentenceTransformer("all-MiniLM-L6-v2")

print("Embeddings loaded successfully")

def retrieve_solution(user_ticket):

    ## Encoding the user ticket
    query_embedding = model.encode(user_ticket, convert_to_tensor = True)

    ## Computing the similarity
    scores = util.cos_sim(query_embedding, ticket_embeddings)

    # getting top 3 similar tickets
    top_k = 3
    top_results = scores[0].topk(k=top_k)

    solutions = []
    similarity_scores = []

    for idx, score in zip(top_results.indices, top_results.values):
        solutions.append(answers[idx.item()])
        similarity_scores.append(score.item())

    return solutions, similarity_scores