import Computer


class Network:
    def __init__(self, comps):
        self.computers = comps
        self.queue = []

    def queue_message(self, message):
        self.queue.append(message)

    def extract_message(self):
        if self.queue:

            for message in self.queue:

                if not message.src.failed and not message.dst.failed:
                    self.queue.remove(message)
                    return message

