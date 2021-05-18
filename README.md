# Send Email By Using Celery

* Mail Queue provides an easy and simple way to send email. Each email is saved and queued up either in real time or with Celery.

## Description of the code

# Server Setup
* pip3 install django-mail-queue
* pip3 install django-celery
* pip3 install redis
	
	
# About Celery: 
* Celery, a powerful asynchronous job queue used for running tasks in the background. 
* Add celery.py file in main Django project and create tasks
* Task is responsible to send email or any other job


 
# About Redis:
   * Redis is also requiered : "Redis is an open source (BSD licensed), in-memory data structure store, used as a database, cache, 
   * and message broker. Redis provides data structures such as strings, hashes, lists, sets, sorted sets with range queries, b
   * itmaps, hyperloglogs, geospatial indexes, and streams. Redis has built-in replication, Lua scripting, 
   * LRU eviction, transactions, and different levels of on-disk persistence, and provides high availability via 
   * Redis Sentinel and automatic partitioning with Redis Cluster.
     
