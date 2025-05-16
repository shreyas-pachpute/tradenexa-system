import zmq, time, pandas as pd

ctx = zmq.Context()
pub = ctx.socket(zmq.PUB)
pub.bind("tcp://*:5556")

# Load or simulate ticks
df = pd.read_csv("data/market.csv")
for _, row in df.iterrows():
    topic = "TICK"
    msg = f"{row.timestamp} {row.price}"
    pub.send_string(f"{topic} {msg}")  # PUB/SUB pattern :contentReference[oaicite:10]{index=10}
    time.sleep(0.001)
