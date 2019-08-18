from elasticsearch_dsl.connections import connections
from elasticsearch_dsl import Text, Document, Search
from elasticsearch.helpers import bulk
from elasticsearch import Elasticsearch
from blog import models

connections.create_connection(hosts=["localhost"])


class BlogPostIndex(Document):
    title = Text()
    author = Text()
    body = Text()

    class Index:
        name = 'post-index'


def bulk_indexing():
    BlogPostIndex.init()
    es = Elasticsearch()
    bulk(
        client=es,
        actions=(
            b.indexing()
            for b in models.Post.objects.all().iterator()
            )
        )


def search(title):
    s = Search().filter('match', title=title)
    response = s.execute()
    return response
