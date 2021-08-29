import redis
conn = redis.Redis()

topic = ['maine coon', 'persian']
sub = conn.pubsub()
sub.subscribe(topic)
for msg in sub.listen():
    if msg['type'] == 'message':
        cat = msg['channel']
        hat = msg['data']
        print('Subscribe: %s wears a %s' % (cat, hat))
