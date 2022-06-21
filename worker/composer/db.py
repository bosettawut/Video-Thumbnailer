import redis
from rq import Queue
red = redis.Redis(host='redis', port=6379)
simple_app = Queue(connection=red)

def make_db(x,y):
  red.set(x,y)
  return "Set DataBase"

def generate_id():
  return "Id is Generated"