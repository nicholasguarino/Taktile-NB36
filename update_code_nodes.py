import requests
import os

API_URL = "https://eu-central-1.taktile-org.decide.taktile.com/run/api/v1/flows/patch-decision-graph/sandbox/decide"
API_KEY = os.getenv("TAKTILE_API_KEY")
FLOW_ID = "06457ab1-3367-43c3-9e6b-4dbaa88d1b1b" # Flow ID for the sandbox environment

if not API_KEY:
    raise ValueError("TAKTILE_API_KEY environment variable is not set in GitHub Actions Secrets")

headers = {
    "X-Api-Key": API_KEY,
    "Content-Type": "application/json",
    "Accept": "application/json"
}

# Dictionary mapping filenames to their corresponding node IDs
# These node IDs should match the nodes in your Taktile flow
NODE_MAPPING = {
    "Multiply.py": "affc68e2-f4e7-40b2-a8e4-4f08ac9cc123",  # Replace with actual node ID from your flow
    "Summarize.py": "affc68e2-f4e7-40b2-a8e4-4f08ac9cc643"  # Replace with actual node ID from your flow
}

def update_code_node(filename, node_id):
    try:
        # Read the source code from the file
        with open(f"CodeNodes/{filename}", "r") as code_file:
            code_content = code_file.read()
        
        # Prepare the payload for the patch request
        payload = {
            "flow_id": FLOW_ID,
            "node_id": node_id,
            "src_code": code_content
        }

        # Make the PATCH request to update the code node
        response = requests.post(
            API_URL,
            headers=headers,
            json=payload
        )

        if response.status_code == 200:
            print(f"Successfully updated {filename} -> {node_id}")
            return True
        else:
            print(f"Failed to update {filename}. Status: {response.status_code}")
            print(f"Response body: {response.text}")
            return False
            
    except FileNotFoundError:
        print(f"File not found: CodeNodes/{filename}")
        return False
    except Exception as e:
        print(f"Error updating {filename}: {str(e)}")
        return False

def main():
    success = True
    for filename, node_id in NODE_MAPPING.items():
        if not update_code_node(filename, node_id):
            success = False
    
    if not success:
        exit(1)  # Exit with error code if any updates failed

if __name__ == "__main__":
    main()
