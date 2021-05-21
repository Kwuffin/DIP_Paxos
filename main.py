from Computer import Computer
from System import DisSystem
from Message import Message
from Network import Network


def queue_message(network, message):
    network.queue.append(message)


def extract_message(network):
    if network.queue:

        for message in network.queue:

            if not message.src.failed and not message.dst.failed:
                network.queue.remove(message)
                return message


def deliver_message(computer, message):

    if message.type == "PROPOSE":
        pass

    elif message.type == "PREPARE":
        pass

    elif message.type == "PROMISE":
        pass

    elif message.type == "ACCEPT":
        pass

    elif message.type == "ACCEPTED":
        pass

    elif message.type == "REJECTED":
        pass


def give_inputs():
    print("Give inputs\n"
          "'0 END' will end the input session.")
    end = False
    input_list = []
    while not end:
        user_input = input("")
        input_list.append(user_input)

        if user_input == "0 END":
            end = True

    tuple_list = []
    for str in input_list:
        tuple_list.append(str.split(" "))

    return tuple_list



# bijv 1:
start1 = (1, 3, 15)
second1 = (0, 'PROPOSE', 1, 42)
end1 = (0, 'END')


test1 = [('1', '3', '15'), ('0', 'PROPOSE', '1', '42'), ('0', 'END')]


def simulation(n_p, n_a, tmax, E):
    # np, na , maxticks = inputs[0]

    P = set()  # Proposers
    A = set()  # Acceptors
    N = Network()  # queue

    for i in range(n_p):
        P.add(Computer(f"P{i+1}"))
    for i in range(n_a):
        A.add(Computer(f"A{i+1}"))
    # p1 = Computer()
    # p2 = Computer()
    #
    # a1 = Computer()
    # a2 = Computer()
    # a3 = Computer()
    for t in range(tmax):
        if N.queue.len() == 0 or E.len() == 0:
            return
        e = E[0] if t == E[0][0] else None
        if e is not None:
            E.remove(e)
            (t, F, R, pi_c, pi_v) = e

            # Fail computers
            for computer in F:
                if "P" in computer:  # If the computer is a proposer
                    for proposer in P:
                        if proposer.name == computer:
                            proposer.failed = True
                else:
                    for acceptor in A:
                        if acceptor.name == computer:
                            acceptor.failed = True

            # Repair computers
            for computer in R:
                if "P" in computer:  # If the computer is a proposer
                    for proposer in P:
                        if proposer.name == computer:
                            proposer.failed = False
                else:
                    for acceptor in A:
                        if acceptor.name == computer:
                            acceptor.failed = False

            if pi_v is not None and pi_c is not None:
                m = Message(None, pi_c, "PROPOSE", pi_v)
                deliver_message(pi_c, m)
        else:
            m = extract_message(N)
            if m is not None:
                deliver_message(m.dst, m)


# bijv 2:
start2 = (2, 3, 50)
second2 = (0, 'PROPOSE', 1, 42)
third2 = (8, 'FAIL', 'PROPOSER', 1)
fourth2 = (11, 'PROPOSE', 2, 37)
fifth2 = (26, 'RECOVER', 'PROPOSER', 1)
end2 = (0, 'END')
test2 = [(2, 3, 50), (0, 'PROPOSE', 1, 42),(8, 'FAIL', 'PROPOSER', 1),(11, 'PROPOSE', 2, 37),(26, 'RECOVER', 'PROPOSER', 1)]
test3 = [(2, 3, 50), (0, 'PROPOSE', 1, 42),(8, 'FAIL', 'PROPOSER', 1),(11, 'PROPOSE', 2, 37),(26, 'RECOVER', 'PROPOSER', 1), (0, 'END')]


def create_events(inputs):
    """Converts given inputs into events"""
    event_lst = []
    for event in inputs:
        tick = int(event[0])
        F = []
        R = []
        msg_P = None
        msg_V = None

        if event[1] == "PROPOSE":
            msg_P = int(event[2])
            msg_V = event[3]

        elif event[1] == "FAIL":
            if event[2] == "PROPOSER":
                F.append('P'+str(event[3]))

            else:
                F.append('A'+str(event[3]))

        elif event[1] == "RECOVER":
            if event[2] == "PROPOSER":
                R.append('P'+str(event[3]))

            else:
                R.append('A'+str(event[3]))

        event_lst.append((tick, F, R, msg_P, msg_V))

    return event_lst


def start_sim(inputs):
    start = inputs[0]
    n_p = start[0]
    n_a = start[1]
    tmax = start[2]
    events = inputs[1:]
    E = create_events(events)

    simulation(n_p, n_a, tmax, E)


if __name__ == '__main__':
    # events = give_inputs()
    # start_sim(events)
    print(create_events(test2[1:]))
