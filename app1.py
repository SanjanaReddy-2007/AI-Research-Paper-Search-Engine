from search.search_engine import SearchEngine

engine = SearchEngine()

results = engine.search("machine learning healthcare")

for r in results:
    print(r["title"])