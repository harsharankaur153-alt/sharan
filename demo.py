from env import WorkplaceEnv
from models import Action

env = WorkplaceEnv()
obs = env.reset()

actions = [
    Action(type="classify", email_id=3, content="spam"),
    Action(type="reply", email_id=1, content="Sorry for delay"),
    Action(type="schedule", email_id=2, content="Meeting scheduled"),
]

for act in actions:
    obs, reward, done, _ = env.step(act)
    print("Reward:", reward)