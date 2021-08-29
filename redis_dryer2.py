def dryer():
    import redis
    import os
    import time

    conn = redis.Redis(host='localhost', port=6379)
    pid = os.getpid()
    timeout = 20
    print('Dryer process %s is starting' % pid)

    while True:
        msg = conn.blpop('dishes', timeout)
        if not msg:
            break
        val = msg[1].decode('utf-8')
        if val == 'quit':
            break
        print('%s: drided %s' % (pid, val))
        time.sleep(0.1)
    print('Dryer proces %s is done' % pid)

import multiprocessing
DRYERS = 3
for num in range(DRYERS):
    p = multiprocessing.Process(target=dryer)
    p.start()