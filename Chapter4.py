from elasticsearch import Elasticsearch
es = Elasticsearch("http://localhost:9200")
doc1 = {"sentence" : "Today is a sunny day."}
doc2 = {"sentence" : "Today is a bright-sunny day"}


res = es.search(index="english", body={ "from": 0, "size": 0, "query": { "bool": { "must_not": { "match": { "sentence": "bright" } }, "should": { "match": { "sentence": "sunny" } } } } })

print res
#{u'hits': {u'hits': [], u'total': 1, u'max_score': 0.0}, u'_shards': {u'successful': 5, u'failed': 0, u'skipped': 0, u'total': 5}, u'took': 16, u'timed_out': False}

res = es.search(index="english", body={ "from": 0, "size": 1, "query": { "bool": { "must_not": { "match": { "sentence": "bright" } }, "should": { "match": { "sentence": "sunny" } } } } })

print res
#{u'hits': {u'hits': [{u'_score': 0.2876821, u'_type': u'sentences', u'_id': u'1', u'_source': {u'sentence': u'Today is a sunny day.'}, u'_index': u'english'}], u'total': 1, u'max_score': 0.2876821}, u'_shards': {u'successful': 5, u'failed': 0, u'skipped': 0, u'total': 5}, u'took': 8, u'timed_out': False}
