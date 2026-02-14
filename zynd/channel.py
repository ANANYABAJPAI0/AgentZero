class ZyndChannel:
    def __init__(self):
        self.logs = []

    def send(self, sender_id, receiver_agent, payload):
        log = f"{sender_id} → {receiver_agent.agent_id}"
        print(f"[ZYND] {log}")
        self.logs.append(log)
        return receiver_agent.receive(payload)
