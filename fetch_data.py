import requests
import json

BASE_URL = "https://ca-seassessment-api-dev.happywater-190f264d.northcentralus.azurecontainerapps.io"

API_KEY = "sa_274d81a2d7da1ffd898ded4f2133807fc7a91acebd39d70c8dd5a42fdbfd9162"

headers = {
    "Authorization": f"Bearer {API_KEY}"
}

all_data = []

page = 1

while True:

    print(f"Fetching page {page}")

    response = requests.get(
        f"{BASE_URL}/api/v1/dataset?page={page}",
        headers=headers
    )

    data = response.json()

    print(data)

    all_data.extend(data["data"])

    if not data["has_more"]:
        break

    page += 1

print(f"Total records fetched: {len(all_data)}")

with open("all_data.json", "w") as f:
    json.dump(all_data, f, indent=2)

print("Done. Data saved in all_data.json")