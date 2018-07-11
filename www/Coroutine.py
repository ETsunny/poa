def consumer():
    r = ''
    print('consumer start')
    while True:
        n = yield r
        print('n=>>', n)
        if not n:
            print('consumer,return')
            return
        print('[CONSUMER] Consuming %s...' % n)
        r = '200 OK'


def produce(c):
    print('produce start')
    c.send(None)
    n = 0
    while n < 5:
        n = n + 1
        print('[PRODUCER] Producing %s...' % n)
        r = c.send(n)
        print('[PRODUCER] Consumer return: %s' % r)
    c.close()


c = consumer()
produce(c)
