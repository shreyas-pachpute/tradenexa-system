import zmq

ctx = zmq.Context()
router = ctx.socket(zmq.ROUTER)
router.bind("tcp://*:5557")             # receive orders from agents
dealer = ctx.socket(zmq.DEALER)
dealer.bind("tcp://*:5558")             # send orders to execution

zmq.proxy(router, dealer)               # brokerless routing :contentReference[oaicite:11]{index=11}
