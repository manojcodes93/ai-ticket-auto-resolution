import pickle
from retrieval import retrieve_solution
from llm_generator import generate_response

# Load classifier
model = pickle.load(open("model/model.pkl", "rb"))

# Load vectorizer
vectorizer = pickle.load(open("model/vectorizer.pkl", "rb"))

def solve_ticket(ticket_text):
    try:
        # Classification
        ticket_vec = vectorizer.transform([ticket_text])
        category = model.predict(ticket_vec)[0]
        classifier_confidence = model.predict_proba(ticket_vec).max()

        # Retrieval
        solutions = retrieve_solution(ticket_text)

        if not solutions:
            return {
                "category": category,
                "confidence": f"{round(classifier_confidence * 100, 2)}%",
                "response": "No solution found. Please contact support."
            }

        best_solution = solutions[0]

        # Decide whether to call LLM
        if classifier_confidence > 0.7:
            # High confidence → no LLM
            return {
                "category": category,
                "confidence": f"{round(classifier_confidence * 100, 2)}%",
                "response": best_solution
            }

        # Use Hugging Face LLM (fallback)
        llm_response = generate_response(ticket_text, solutions)

        return {
            "category": category,
            "confidence": f"{round(classifier_confidence * 100, 2)}%",
            "response": llm_response
        }

    except Exception as e:
        return {
            "error": str(e)
        }