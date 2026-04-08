from models import Observation, Action, Email

class WorkplaceEnv:
    def __init__(self):
        self.reset()

    def reset(self):
        self.inbox = [
            Email(id=1, content="Urgent client complaint", status="pending", priority=5),
            Email(id=2, content="Meeting at 5pm", status="pending", priority=3),
            Email(id=3, content="Spam offer!!!", status="pending", priority=1),
        ]
        self.step_count = 0
        return self._get_obs()

    def _get_obs(self):
        return Observation(
            inbox=self.inbox,
            satisfaction=0.5,
            step_count=self.step_count
        )

    def step(self, action):
        reward = 0.0
        self.step_count += 1

        email = next((e for e in self.inbox if e.id == action.email_id), None)

        if not email:
            return self._get_obs(), -0.20, False, {}

        if action.type == "classify":
            if "spam" in email.content.lower():
                reward += 0.20

        elif action.type == "reply":
            if "sorry" in action.content.lower():
                reward += 0.40
                email.status = "resolved"

        elif action.type == "schedule":
            reward += 0.30
            email.status = "resolved"

        done = all(e.status == "resolved" for e in self.inbox)

        return self._get_obs(), round(reward, 2), done, {}