import gymnasium as gym
from stable_baselines3 import PPO  # or SAC/DQN as appropriate

# 1. Register or point to your custom env
env = gym.make("TradingEnv-v0")          # use your env ID :contentReference[oaicite:8]{index=8}

# 2. Instantiate model
model = PPO("MlpPolicy", env, verbose=1)

# 3. Train & log
model.learn(total_timesteps=100_000)     # adjust as budget allows

# 4. Save trained policy
model.save("agents/ppo_trading_model")
