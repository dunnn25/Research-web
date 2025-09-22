import os.path
from whoosh.index import create_in, open_dir
from whoosh.fields import *

index_dir = "indexdir"

# Check if the directory exists and contains an index
if not os.path.exists(index_dir) :
    os.makedirs(index_dir, exist_ok=True)
    schema = Schema(title=TEXT(stored=True), path=ID(stored=True), content=TEXT)
    ix = create_in(index_dir, schema)
    writer = ix.writer()
    writer.add_document(title="First document", path="/a",
                        content="This is the first document we've added!")
    writer.add_document(title="Second document", path="/b",
                        content="The second one is even more interesting!")
    writer.commit()
else:
    ix = open_dir(index_dir)

# Now you can proceed with the search
from whoosh.qparser import QueryParser
with ix.searcher() as searcher:
    query = QueryParser("content", ix.schema).parse("first")
    results = searcher.search(query)
    print("Number of results:", len(results))
    print(results[0]["title"])