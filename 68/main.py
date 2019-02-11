# coding: utf-8
import json
import pymongo
from pymongo import MongoClient

# MongoDBのデータベースtestdbにコレクションartistにアクセス
client = MongoClient()
db = client.testdb
collection = db.artist

# 検索
results = collection.find({'tags.value': 'dance'})

# ソート
results.sort('rating.count', pymongo.DESCENDING)

# 10件表示
for doc in results.limit(10):

	if 'rating' in doc:
		rating = doc['rating']['count']
	else:
		rating = '(none)'		# ratingがないドキュメントもあるので

	print('{}(id:{})\t{}'.format(doc['name'], doc['id'], rating))
