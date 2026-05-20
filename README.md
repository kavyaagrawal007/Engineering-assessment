I successfully completed dataset retrieval, integrity verification, RSA key retrieval, and decryption of all records.
Analysis performed on the decrypted telemetry dataset included:
endpoint frequency analysis
HTTP method distribution
status code anomaly analysis
latency and request size ordering
unique tuple extraction
chronological sequence analysis
endpoint/user-segment correlation
modulo and positional extraction attempts
Key findings:
The dataset is highly normalized and appears intentionally synthetic.
The strongest statistical anomaly observed was the combination:

PATCH + 401 (17 occurrences).
Auth-related endpoints (login/refresh/users) clustered heavily around anomalous records.
Status code 429 showed notable association with the "partner" user segment.
Endpoint coverage was balanced across analytics, billing, notifications, orders, products, search, users, webhooks, and auth endpoints.
Multiple deterministic extraction attempts suggest Layer 3 is encoded through a specific intended filtering/extraction rule rather than obvious plaintext hidden directly in records.
All retrieval, decryption, and analysis scripts are included in the repository submission.
 
