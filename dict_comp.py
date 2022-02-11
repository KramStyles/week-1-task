def dict_comp(stop, step):
    """
    This function takes in two integer values 'stop' and 'step' and returns a
    dictionary generated using python comprehension
    :param stop: Int provided by user
    :param step: Int provided by user
    :return: bigArray : Dictionary of python comprehension
    """
    counter = 1
    bigArray = {}
    array = []
    for num in range(1, stop + 1):
        if len(array) < step:
            array.append(num)
        if len(array) == step:
            bigArray[f"item_{counter}"] = array
            array = []
            counter += 1

    return bigArray


if __name__ == '__main__':
    print(dict_comp(10, 4))
