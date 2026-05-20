import json
import hashlib
import base64

with open("all_data.json", "r") as f:
    all_data = json.load(f)

combined_bytes = b""

for item in all_data:
    combined_bytes += base64.b64decode(item)

hash_value = hashlib.sha256(combined_bytes).hexdigest()

print(hash_value)