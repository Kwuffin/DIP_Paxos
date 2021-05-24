from Computer import Computer
from System import DisSystem
from Message import Message
from Network import Network


def give_inputs():
    """
    Lets the user give inputs to the simulation
    :return: List of inputs
    """
    print("Give inputs\n"
          "'0 END' will end the input session.")
    end = False
    input_list = []
    while not end:
        user_input = input("")
        input_list.append(user_input)

        if user_input == "0 END":
            end = True

    inputs_list = []
    for str in input_list:
        inputs_list.append(str.split(" "))

    # Converts strings to integers where necessary
    for line in inputs_list:
        for i in range(len(line)):
            try:
                line[i] = int(line[i])
            except ValueError:
                line[i] = line[i]
                continue

    return inputs_list


def create_events(inputs):
    """
    Interprets the user inputs and turns them into events.
    :param inputs: Creates events
    :return:
    """
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
    """
    Creates our Distributed System and starts the simulation
    :param inputs: The inputs given by the user.
    :return: None
    """
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
