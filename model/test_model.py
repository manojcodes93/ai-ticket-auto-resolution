import pickle

model = pickle.load(open("model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

ticket = ["vpn not connecting"]

ticket_vector = vectorizer.transform(ticket)

prediction = model.predict(ticket_vector)

print("Prediction:", prediction[0])