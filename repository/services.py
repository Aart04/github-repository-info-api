import requests
from github import settings

def get_repository_info(owner, repository_name):
    url =      url = 'https://api.github.com/repos/{}/{}'.format(owner, repository_name)
    headers = {'Accept': 'application/vnd.github.v3+json', 
               'Authorization': 'token ' + settings.GITHUB_KEY}

    response = requests.get(url=url, headers=headers)
    response_json = response.json
    response_status = response.status_code
    
    return response_status, response_json