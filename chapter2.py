from elasticsearch import Elasticsearch
es = Elasticsearch("http://localhost:9200")

#documents to insert in the elasticsearch index "cities"
doc1 = {"city":"New Delhi", "country":"India"}
doc2 = {"city":"London", "country":"England"}
doc3 = {"city":"Los Angeles", "country":"USA"}

#Inserting doc1 in id=1
es.index(index="cities", doc_type="places", id=1, body=doc1)
#{u'_type': u'places', u'_seq_no': 15, u'_shards': {u'successful': 1, u'failed': 0, u'total': 2}, u'_index': u'cities', u'_version': 16, u'_primary_term': 1, u'result': u'updated', u'_id': u'1'}

#Inserting doc2 in id=2
es.index(index="cities", doc_type="places", id=2, body=doc2)
#{u'_type': u'places', u'_seq_no': 12, u'_shards': {u'successful': 1, u'failed': 0, u'total': 2}, u'_index': u'cities', u'_version': 13, u'_primary_term': 1, u'result': u'updated', u'_id': u'2'}

#Inserting doc3 in id=3
es.index(index="cities", doc_type="places", id=3, body=doc3)
#{u'_type': u'places', u'_seq_no': 10, u'_shards': {u'successful': 1, u'failed': 0, u'total': 2}, u'_index': u'cities', u'_version': 11, u'_primary_term': 1, u'result': u'updated', u'_id': u'3'}

#retrieve data for id=2
res = es.get(index="cities", doc_type="places", id=2)

print res
#{u'_type': u'places', u'_source': {u'city': u'London', u'country': u'England'}, u'_index': u'cities', u'_version': 13, u'found': True, u'_id': u'2'}

print res['_source']
#{u'city': u'London', u'country': u'England'}
