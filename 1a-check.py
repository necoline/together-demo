
import os
from together import Together

client = Together(api_key=os.environ.get("TOGETHER_API_KEY"))
dataset = "MathInstruct-207k"

# Upload your formatted data and get back the file ID
response = client.files.upload(file=f"Formatted{dataset}.jsonl")
fileId = response.model_dump()["id"]

# Verify that the file was uploaded successfully
file_metadata = client.files.retrieve(fileId)
print(file_metadata)
