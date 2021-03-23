from django.test import TestCase

from unittest.mock import Mock, patch

from rest_framework import status

from .services import get_repository_info


class ViewTest(TestCase):
    
    def setUp(self):
        self.mock_repo_info = {
            "id": 1296269,
            "node_id": "MDEwOlJlcG9zaXRvcnkxMjk2MjY5",
            "name": "Hello-World",
            "full_name": "octocat/Hello-World",
            "description": "This your first repo!",
            "clone_url": "https://github.com/octocat/Hello-World.git",
            "forks_count": 9,
            "forks": 9,
            "stargazers_count": 80,
            "watchers_count": 80,
            "watchers": 80,
            "size": 108,
            "subscribers_count": 9999,
            "created_at": "2011-01-26T19:01:12Z",
            "language": "Python",
            "owner": {
                "login": "octocat",
                "id": 1,
                "node_id": "MDQ6VXNlcjE=",
                "avatar_url": "https://github.com/images/error/octocat_happy.gif",
                "gravatar_id": ""
            }
        }

    @patch('repository.services.requests.get')
    def test_getting_repo_info_and_status_200(self, mock_get):

        mock_response = Mock()
        mock_response.json.return_value = self.mock_repo_info
        mock_response.status_code = status.HTTP_200_OK

        mock_get.return_value = mock_response

        result_status, result = get_repository_info("octocat", "Hello-World")
        expected_response = {
            "id": 1296269,
            "node_id": "MDEwOlJlcG9zaXRvcnkxMjk2MjY5",
            "name": "Hello-World",
            "full_name": "octocat/Hello-World",
            "description": "This your first repo!",
            "clone_url": "https://github.com/octocat/Hello-World.git",
            "forks_count": 9,
            "forks": 9,
            "stargazers_count": 80,
            "watchers_count": 80,
            "watchers": 80,
            "size": 108,
            "subscribers_count": 9999,
            "created_at": "2011-01-26T19:01:12Z",
            "language": "Python",
            "owner": {
                "login": "octocat",
                "id": 1,
                "node_id": "MDQ6VXNlcjE=",
                "avatar_url": "https://github.com/images/error/octocat_happy.gif",
                "gravatar_id": ""
            }
        }
        self.assertEqual(result_status, status.HTTP_200_OK)
        self.assertEqual(result, expected_response)
        

    @patch('repository.services.requests.get')
    def test_getting_repo_for_non_exising_repo(self, mock_get):
        mock_response = Mock()
        expected_response = {
            "detail": "Not found.",
            "status_code": 404
        }
        mock_response.json.return_value = expected_response
        mock_response.status_code = status.HTTP_404_NOT_FOUND

        mock_get.return_value = mock_response

        result_status, result = get_repository_info("notexistingowner", "notexistingrepo")

        self.assertEqual(result, {
            "detail": "Not found.",
            "status_code": 404
        })
        self.assertEqual(result_status, status.HTTP_404_NOT_FOUND)


    @patch('repository.services.requests.get')
    def test_getting_filtered_repo_info(self, mock_get):
        mock_response = Mock()

        mock_response.json.return_value = self.mock_repo_info
        mock_response.status_code = status.HTTP_200_OK

        mock_get.return_value = mock_response

        client_response = self.client.get("/repository/{}/{}".format("octocat", "Hello-World"))

        expected_response = {
            "full_name": "octocat/Hello-World",
            "description": "This your first repo!",
            "clone_url": "https://github.com/octocat/Hello-World.git",
            "owner_id": '1',
            "language": "Python"
        }

        self.assertEqual(client_response.status_code, status.HTTP_200_OK)
        self.assertEqual(client_response.json(), expected_response)

    
    @patch('repository.services.requests.get')
    def test_service_unavailable(self, mock_get):
        mock_response = Mock()

        mock_response.json.return_value = {}
        mock_response.status_code = status.HTTP_503_SERVICE_UNAVAILABLE
        mock_get.return_value = mock_response
        
        client_response = self.client.get("/repository/{}/{}".format("user_name", "repository_name"))

        expected_response = {
            "detail": "service temporarily unavailable, try again later.",
            "status_code": 503
        }

        self.assertEqual(client_response.status_code, status.HTTP_503_SERVICE_UNAVAILABLE)
        self.assertEqual(client_response.json(), expected_response)