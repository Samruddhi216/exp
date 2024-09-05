import requests
import pandas as pd

# GitHub repository details
REPO_OWNER = 'Samruddhi216'
REPO_NAME = 'table'
GITHUB_TOKEN = 'EXPORT_TOKEN'

# GitHub API URL for pull requests
API_URL = f'https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}/pulls'

headers = {
    'Authorization': f'token {GITHUB_TOKEN}',
    'Accept': 'application/vnd.github.v3+json',
}

# Fetch pull requests from GitHub
response = requests.get(API_URL, headers=headers)
pull_requests = response.json()

# Extract pull request timestamps
data = []
for pr in pull_requests:
    data.append({
        'PR Number': pr.get('number'),
        'Title': pr.get('title'),
        'Created At': pr.get('created_at'),
        'Updated At': pr.get('updated_at'),
        'Closed At': pr.get('closed_at'),
        'Merged At': pr.get('merged_at')
    })

# Convert data to DataFrame
df = pd.DataFrame(data)

# Convert timestamps to ISO format if needed
for col in ['Created At', 'Updated At', 'Closed At', 'Merged At']:
    df[col] = pd.to_datetime(df[col]).dt.strftime('%Y-%m-%d %H:%M:%S')  # Format as needed

# Save DataFrame to CSV
df.to_csv('pull_requests.csv', index=False)
