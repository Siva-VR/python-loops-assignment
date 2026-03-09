#Task 1 — Build a JSON Structure
import json

# Create a Python dictionary
user_profile = {
    "name": "siva",
    "age": 25,
    "email": "siva@gmail.com",
    "is_active": True,
    "skills": ["Python", "Data Analysis", "Machine Learning"]
}

# Convert dictionary to JSON string with indentation
json_string = json.dumps(user_profile, indent=4)

# Print the JSON
print("Task 1 Output:")
print(json_string)

#Task 2 — Parse an API Responseimport json

# Mock API response JSON string
api_response = '{"status": "success", "data": {"user_id": 101, "username": "alex99", "score": 87.5}}'

# Parse JSON string
parsed_data = json.loads(api_response)

# Extract username and score
username = parsed_data["data"]["username"]
score = parsed_data["data"]["score"]

# Print results
print("\nTask 2 Output:")
print("Username:", username)
print("Score:", score)
print(f"User {username} scored {score} points")


#Task 3 — Handle Nested JSON


import json

# Nested JSON string
nested_json = '''
{
  "name": "Priya",
  "address": {
    "city": "Bengaluru",
    "state": "Karnataka",
    "zip": "560001"
  }
}
'''

# Parse JSON
data = json.loads(nested_json)

# Extract city and zip
city = data["address"]["city"]
zip_code = data["address"]["zip"]

print("\nTask 3 Output:")
print("City:", city)
print("Zip Code:", zip_code)

# Add country to address
data["address"]["country"] = "India"

# Print updated JSON
updated_json = json.dumps(data, indent=4)
print("\nUpdated JSON:")
print(updated_json)