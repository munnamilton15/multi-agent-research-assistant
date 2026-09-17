from ddgs import DDGS

results = DDGS().text(
    "Generative AI software development",
    max_results=5
)

for result in results:
    print("\nTITLE:", result.get("title"))
    print("URL:", result.get("href"))
    print("DESCRIPTION:", result.get("body"))

