def dict_comp(stop, step):
    """
    This function takes in two integer values 'stop' and 'step' and returns a
    dictionary generated using python comprehension
    :param stop: Int provided by user
    :param step: Int provided by user
    :return: bigArray : Dictionary of python comprehension
    """
    if type(stop) != int or type(step) != int:
        return "Only integers allowed"
    else:
        counter = 1
        big_array = {}
        array = []
        for num in range(1, stop + 1):
            if len(array) < step:
                array.append(num)
            if len(array) == step:
                big_array[f"item-{counter}"] = array
                array = []
                counter += 1

        return big_array

