# from elasticsearch_dsl import DocType, Index
# from blog.models import Post

# posts = Index('post')


# @posts.doc_type
# class PostDocument(DocType):
#     class Meta:
#         model = Post

#         fields = [
#             'id',
#             'title',
#             'author',
#             'body',
#         ]

from elasticsearch_dsl.connections import connections
# Create a connection to ElasticSearch
connections.create_connection()
from elasticsearch_dsl import DocType, Index
from blog.models import Post

post = Index('post')

# reference elasticsearch doc for default settings here
post.settings(
    number_of_shards=1,
    number_of_replicas=0
)


@post.doc_type
class PostDocument(DocType):
    class Meta:
        model = Post

        fields = [
            'id',
            'title',
            'author',
            'body',
        ]
