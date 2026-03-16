import pickle
from retrieval import retrieve_solution

## Loading classifier
model = pickle.load(open("model/model.pkl", "rb"))

## Loading vectorizer
vectorizer = pickle.load(open("model/vectorizer.pkl", "rb"))

def solve_ticket(ticket_text):
    ## Predicting category
    ticket_vec = vectorizer.transform([ticket_text])
    category = model.predict(ticket_vec)[0]
    classifier_confidence = model.predict_proba(ticket_vec).max()

    ## Retreiving the solution
    solution, similarity_score = retrieve_solution(ticket_text)

    ## Confidence decision
    if similarity_score < 0.55:
        solution = "Low confidence — escalate to human support"
    
    return {
        "category": category,
        "classifier_confidence": float(classifier_confidence),
        "similarity_score": similarity_score,
        "solution": solution
    }