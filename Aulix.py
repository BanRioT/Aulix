import requests

# URL of the raw Python script on GitHub
raw_github_url = 'https://raw.githubusercontent.com/your-username/your-repo/main/your-script.py'

# Fetch the raw data from GitHub
response = requests.get(raw_github_url)

if response.status_code == 200:
    # Get the content of the script
    script_content = response.text

    # Print the script content (for debugging purposes)
    print("Fetched script content:")
    print(script_content)

    # Execute the script content
    exec(script_content)
else:
    print(f"Failed to fetch script. Status code: {response.status_code}")
