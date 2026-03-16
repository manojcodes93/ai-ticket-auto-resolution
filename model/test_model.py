from retrieval import retrieve_solution

ticket = "How do I bake a chocolate cake in the oven?"

solution, score = retrieve_solution(ticket)

print("\nUser Ticket:")
print(ticket)

print("\nSuggested Solution:")
print(solution)

print("\nSimilarity Score:", score)