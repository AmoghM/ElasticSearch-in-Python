from elasticsearch import Elasticsearch
es = Elasticsearch("http://localhost:9200")

doc1 = {"sentence" : "Today is a sunny day."}
doc2 = {"sentence" : "Today is a bright-sunny day"}

es.index(index="english", doc_type="sentences", id=1, body=doc1)
#{u'_type': u'sentences', u'_seq_no': 1, u'_shards': {u'successful': 1, u'failed': 0, u'total': 2}, u'_index': u'english', u'_version': 2, u'_primary_term': 1, u'result': u'updated', u'_id': u'1'}

es.index(index="english", doc_type="sentences", id=2, body=doc2)
#{u'_type': u'sentences', u'_seq_no': 2, u'_shards': {u'successful': 1, u'failed': 0, u'total': 2}, u'_index': u'english', u'_version': 3, u'_primary_term': 1, u'result': u'updated', u'_id': u'2'}

res = es.search(index="english", body={"from":0,"size":0,"query":{"match":{"sentence":"SUNNY"}}})
print res
#{u'hits': {u'hits': [], u'total': 2, u'max_score': 0.0}, u'_shards': {u'successful': 5, u'failed': 0, u'skipped': 0, u'total': 5}, u'took': 1, u'timed_out': False}

res = es.search(index="english", body={"from":0,"size":2,"query":{"match":{"sentence":"SUNNY"}}})
print res
#{u'hits': {u'hits': [{u'_score': 0.2876821, u'_type': u'sentences', u'_id': u'2', u'_source': {u'sentence': u'Today is a bright-sunny day'}, u'_index': u'english'}, {u'_score': 0.2876821, u'_type': u'sentences', u'_id': u'1', u'_source': {u'sentence': u'Today is a sunny day.'}, u'_index': u'english'}], u'total': 2, u'max_score': 0.2876821}, u'_shards': {u'successful': 5, u'failed': 0, u'skipped': 0, u'total': 5}, u'took': 2, u'timed_out': False}

res = es.search(index="english", body={"from":0,"size":0,"query":{"match_phrase":{"sentence":"SUNNY"}}})
print res
#{u'hits': {u'hits': [], u'total': 2, u'max_score': 0.0}, u'_shards': {u'successful': 5, u'failed': 0, u'skipped': 0, u'total': 5}, u'took': 1, u'timed_out': False}

res = es.search(index="english", body={"from":0,"size":0,"query":{"match_phrase":{"sentence":"bright SUNNY"}}})
print res
#{u'hits': {u'hits': [], u'total': 1, u'max_score': 0.0}, u'_shards': {u'successful': 5, u'failed': 0, u'skipped': 0, u'total': 5}, u'took': 1, u'timed_out': False}

res = es.search(index="english", body={"from":0,"size":0,"query":{"term":{"sentence":"bright SUNNY"}}})
print res
#{u'hits': {u'hits': [], u'total': 0, u'max_score': 0.0}, u'_shards': {u'successful': 5, u'failed': 0, u'skipped': 0, u'total': 5}, u'took': 2, u'timed_out': False}


