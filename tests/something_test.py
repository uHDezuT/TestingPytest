import requests

from configurations import SERVISE_URL
from src.baseclasses.response import Response
from src.schemas.post import POST_SCHEMA


def test_getting_posts():
	r = requests.get(url=SERVISE_URL)
	response = Response(r)
	response.assert_status_code(200).validate(POST_SCHEMA)

# [{'id': 1, 'title': 'Post 1'}, {'id': 2, 'title': 'Post 2'}, {'id': 3, 'title': 'Post 3'}]
