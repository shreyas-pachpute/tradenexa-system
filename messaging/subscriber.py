import zmq

ctx = zmq.Context()
sub = ctx.socket(zmq.SUB)
sub.connect("tcp://localhost:5556")
sub.setsockopt_string(zmq.SUBSCRIBE, "TICK")

while True:
    topic, payload = sub.recv_string().split(maxsplit=1)
    timestamp, price = payload.split()
    # pass price to your agent logic…
