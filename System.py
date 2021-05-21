from Computer import Computer
from Message import Message
from Network import Network
from main import *


class DisSystem:
    def __init__(self):
        self.P = set()      # Proposers
        self.A = set()      # Acceptors
        self.N = Network()  # queue
        self.total_computers = None       # Computers
        self.n = 0

    def deliver_message(self, computer, message):
        if message.type == "PROPOSE":
            computer.value = message.value
            for acceptor in self.A:
                m = Message(computer, acceptor, "PREPARE", None, self.n)
                queue_message(self.N, m)

        elif message.type == "PREPARE":
            m = Message(computer, message.src, "PROMISE", computer.value, self.n)
            queue_message(self.N, m)    # TODO: create functie for prior



        elif message.type == "PROMISE":
            if message.src.value is None:
                val = computer.value
            else:
                val = message.src.value
            m = Message(computer, message.src, "ACCEPT", val, self.n)
            message.src.value = computer.value
            message.src.prior = self.n
            queue_message(self.N, m)

        elif message.type == "ACCEPT":
            if computer.prior is not None:
                for acceptor in self.A:
                    m = Message()

        elif message.type == "ACCEPTED":
            pass

        elif message.type == "REJECTED":
            pass

    def simulation(self, n_p, n_a, tmax, E):
        # np, na , maxticks = inputs[0]

        self.total_computers = n_a + 1  # Acceptors + the proposer
        for i in range(n_p):
            self.P.add(Computer(f"P{i + 1}", tot_comps=self.total_computers))
        for i in range(n_a):
            self.A.add(Computer(f"A{i + 1}", tot_comps=self.total_computers))
        self.total_computers = len(self.A) + 1
        # p1 = Computer()
        # p2 = Computer()
        #
        # a1 = Computer()
        # a2 = Computer()
        # a3 = Computer()
        for t in range(tmax):
            if self.N.queue.len() == 0 or E.len() == 0:
                return
            e = E[0] if t == E[0][0] else None
            if e is not None:
                E.remove(e)
                (t, F, R, pi_c, pi_v) = e

                # Fail computers
                for computer in F:
                    if "P" in computer:  # If the computer is a proposer
                        for proposer in self.P:
                            if proposer.name == computer:
                                proposer.failed = True
                    else:
                        for acceptor in self.A:
                            if acceptor.name == computer:
                                acceptor.failed = True

                # Repair computers
                for computer in R:
                    if "P" in computer:  # If the computer is a proposer
                        for proposer in self.P:
                            if proposer.name == computer:
                                proposer.failed = False
                    else:
                        for acceptor in self.A:
                            if acceptor.name == computer:
                                acceptor.failed = False

                if pi_v is not None and pi_c is not None:
                    self.n += 1
                    m = Message(None, pi_c, "PROPOSE", pi_v, self.n)
                    deliver_message(pi_c, m)
            else:
                m = extract_message(self.N)
                if m is not None:
                    deliver_message(m.dst, m)
