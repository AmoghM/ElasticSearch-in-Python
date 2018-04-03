from elasticsearch import Elasticsearch
es = Elasticsearch()

print es.indices.create(index="first_index",ignore=400)

print es.indices.exists(index="first_index")

print es.indices.delete(index="first_index", ignore=[400,404])

print es.indices.exists(index="first_index")
