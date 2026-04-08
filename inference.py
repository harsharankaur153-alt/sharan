import os
from env import WorkplaceEnv

HF_TOKEN = os.getenv("HF_TOKEN", "dummy")

env = WorkplaceEnv()
obs = env.reset()

print("[START]")

actions = [
    {"type": "classify", "email_id": 3, "content": "spam"},
    {"type": "reply", "email_id": 1, "content": "Sorry"},
    {"type": "schedule", "email_id": 2, "content": "Meeting"}
]

step = 1
total = 0

for act in actions:
    obs, reward, done, _ = env.step(type("A", (), act))
    total += reward
    print(f"[STEP {step}] reward={reward:.2f}, done={str(done).lower()}")
    step += 1
success = total >= 0.80
print(f"[END] final_score={total:.2f}, success={str(success).lower()}")