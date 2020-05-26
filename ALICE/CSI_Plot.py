import matplotlib.pyplot as plt
import numpy as np


def draw_complex_plots(data):
    """
    Plots all the CSI complex numbers on real/imaginary axis
    Each color represents a different numpy array
    :param data: list of numpy arrays containing CSI complex numbers
    :return:
    """
    fig = plt.figure()
    ax1 = fig.add_subplot(111)  # 111 is to create only one subplot that fills screen

    # Turn on grid-lines and set axis labels
    ax1.set_axisbelow(True)
    ax1.yaxis.grid(color="gray", linestyle="dashed")
    ax1.xaxis.grid(color="gray", linestyle="dashed")
    ax1.set_ylabel("imag")
    ax1.set_xlabel("real")

    # Plot each numpy array on the same subplot
    for i in range(0, len(data)):
        ax1.scatter(
            x=[x.real for x in data[i]], y=[x.imag for x in data[i]], label=str(i)
        )

    plt.legend(loc="lower left")

    # set real and imaginary axis limits (MAX should not go above 512)
    plt.xlim(-500, 500)
    plt.ylim(-500, 500)
    plt.show()


def draw_four_stem_plots(data):
    """
    Plot Stem plots of standardized CSI data when there are four sets
    :param data: four sets of CSI data
    :return:
    """
    mags = []
    for i in range(0, 4):
        mag = []
        for j in range(0, len(data[i])):
            mag.append(20 * np.log10(np.abs(data[i][j])))
        mags.append(mag)

    space = range(0, len(data[i]))
    fig = plt.figure()
    ax1 = fig.add_subplot(221)
    ax1.yaxis.grid(color="gray", linestyle="dashed")
    ax1.xaxis.grid(color="gray", linestyle="dashed")
    ax1.set_xlabel("")  # TODO figure out what X axis label is
    ax1.set_ylabel("dB")
    ax1.stem(space, mags[0], use_line_collection=True)

    ax1 = fig.add_subplot(222)
    ax1.yaxis.grid(color="gray", linestyle="dashed")
    ax1.xaxis.grid(color="gray", linestyle="dashed")
    ax1.set_xlabel("")  # TODO figure out what X axis label is
    ax1.set_ylabel("dB")
    ax1.stem(space, mags[1], use_line_collection=True)

    ax1 = fig.add_subplot(223)
    ax1.yaxis.grid(color="gray", linestyle="dashed")
    ax1.xaxis.grid(color="gray", linestyle="dashed")
    ax1.set_xlabel("")  # TODO figure out what X axis label is
    ax1.set_ylabel("dB")
    ax1.stem(space, mags[2], use_line_collection=True)

    ax1 = fig.add_subplot(224)
    ax1.yaxis.grid(color="gray", linestyle="dashed")
    ax1.xaxis.grid(color="gray", linestyle="dashed")
    ax1.set_xlabel("")  # TODO figure out what X axis label is
    ax1.set_ylabel("dB")
    ax1.stem(space, mags[3], use_line_collection=True)
    plt.show()


def draw_two_stem_plots(data):
    """
        Plot Stem plots of standardized CSI data when there are two sets
        :param data: two sets of CSI data
        :return:
        """
    mags = []
    for i in range(0, 2):
        mag = []
        for j in range(0, len(data[i])):
            mag.append(20 * np.log10(np.abs(data[i][j])))
        mags.append(mag)

    space = np.linspace(
        -1 * len(data[0]) / 2 * 0.3125, (len(data[0]) / 2 - 1) * 0.3125, len(data[0])
    )
    fig = plt.figure()
    ax1 = fig.add_subplot(211)
    ax1.yaxis.grid(color="gray", linestyle="dashed")
    ax1.xaxis.grid(color="gray", linestyle="dashed")
    ax1.set_xlabel("")  # TODO figure out what X axis label is
    ax1.set_ylabel("dB")
    ax1.stem(space, mags[0], use_line_collection=True)

    ax1 = fig.add_subplot(212)
    ax1.yaxis.grid(color="gray", linestyle="dashed")
    ax1.xaxis.grid(color="gray", linestyle="dashed")
    ax1.set_xlabel("")  # TODO figure out what X axis label is
    ax1.set_ylabel("dB")
    ax1.stem(space, mags[1], use_line_collection=True)
    plt.show()


def draw_stem_plots(info, num_tones):
    """
    Draw stem plot of given data
    :param info: numpy array of complex numbers
    :return:
    """
    mag = []
    for i in range(0, num_tones):
        mag.append(20 * np.log10(np.abs(info[i])))

    space = np.linspace(
        -1 * num_tones / 2 * 0.3125, (num_tones / 2 - 1) * 0.3125, num_tones
    )

    fig = plt.figure()
    ax1 = fig.add_subplot(111)  # 111 is to create only one subplot that fills screen

    # Turn on grid-lines and set axis labels
    ax1.set_axisbelow(True)
    ax1.yaxis.grid(color="gray", linestyle="dashed")
    ax1.xaxis.grid(color="gray", linestyle="dashed")
    ax1.set_xlabel("")  # TODO figure out what X axis label is
    ax1.set_ylabel("dB")
    ax1.stem(space, mag, use_line_collection=True)

    plt.show()