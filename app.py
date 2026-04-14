from rag_engine import VectorDB

# Initialize DB
db = VectorDB()

# Load resume
with open("resume_data.txt", "r") as f:
    resume = f.read()

# Split into chunks
chunks = resume.split(".")

# Store chunks
for chunk in chunks:
    if chunk.strip():
        db.add(chunk.strip())

print("\n🚀 AI Resume Analyzer Ready (type 'exit' to quit)\n")

while True:
    query = input("Ask about resume: ")

    if query.lower() == "exit":
        break

    result = db.search(query)

    print("Answer:", result, "\n")
