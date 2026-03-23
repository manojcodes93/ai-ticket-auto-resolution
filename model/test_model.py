from retrieval import retrieve_solution

ticket = "VPN connection failing when logging in"

solution, score = retrieve_solution(ticket)

print("\nUser Ticket:")
print(ticket)

print("\nSuggested Solution:")
print(solution)

print("\nSimilarity Score:", score)