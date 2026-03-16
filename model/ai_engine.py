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
    best_score = similarity_score[0]

    # convert to percentage
    classifier_confidence_pct = round(classifier_confidence * 100, 2)
    similarity_score_pct = round(best_score * 100, 2)

    ## Confidence decision
    if best_score < 0.55:
        return {
            "category": category,
            "confidence": f"{classifier_confidence_pct}%",
            "message": "Low confidence — escalate to human support"
        }
    
    return {
        "category": category,
        "confidence": f"{classifier_confidence_pct}%",
        "suggested_solutions": solution
    }