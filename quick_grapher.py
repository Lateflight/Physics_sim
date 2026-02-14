import matplotlib.pyplot as plt

def graph(bundle, time):

    fig, AX = plt.subplots(3, 2, figsize=(10, 8), sharex=True)

    # (position_index, row, column)
    dims = [
        (0, 0, 0),  # x
        (1, 1, 0),  # y
        (2, 2, 0),  # z
        (6, 0, 1),  # theta
        (7, 1, 1),  # phi
        (8, 2, 1),  # psi
    ]

    for obj_idx, vector in enumerate(bundle):

        for pos_idx, row, col in dims:

            vel_idx = pos_idx + 3
            ax = AX[row, col]

            pos_values = [state[pos_idx] for state in vector]
            vel_values = [state[vel_idx] for state in vector]

            ax.plot(time, pos_values, label=f'Obj{obj_idx} pos')
            ax.plot(time, vel_values, linestyle='--', label=f'Obj{obj_idx} vel')

    AX[0, 0].set_title("Translation")
    AX[0, 1].set_title("Rotation")

    AX[0, 0].set_ylabel("x")
    AX[1, 0].set_ylabel("y")
    AX[2, 0].set_ylabel("z")

    AX[0, 1].set_ylabel("theta")
    AX[1, 1].set_ylabel("phi")
    AX[2, 1].set_ylabel("psi")

    for ax in AX[-1, :]:
        ax.set_xlabel("Time")

    for ax in AX.flatten():
        ax.legend()

    plt.tight_layout()
    plt.show()
