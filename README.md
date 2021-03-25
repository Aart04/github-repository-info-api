# github-repo-info
Simple REST API for getting informations about repository from [GitHub API](https://docs.github.com/en/rest/reference/repos). This app was made with Django and Django REST framework.

## Setting up
1. Change file .env.production to .env and fill in SECRET_KEY with random string of 50 characters. 
2. Fill GITHUB_KEY with Your personal token ([instruction](https://docs.github.com/en/github/authenticating-to-github/creating-a-personal-access-token))
3. Save changes made in .env file.
4. Run `docker-compose build`.
5. Run `docker-compose up`.
6. Django server should be running on 0.0.0.0/8000.


## API endpoints
To get informations about repository make request on:
http://0.0.0.0:8000/repository/{owner}/{repository_name}