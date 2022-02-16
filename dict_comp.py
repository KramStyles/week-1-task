
def dict_comp(stop, step):
    """
    This function takes in two integer values 'stop' and 'step' and returns a
    dictionary generated using python comprehension
    :param stop: Int provided by user
    :param step: Int provided by user
    :return: bigArray : Dictionary of python comprehension
    """

    try:
        array = [num for num in range(1, stop + 1)]
        big_array = {f"item-{index}": array[(index-1)*step:(index * step)] for index in range(1, int(stop/step) + 1)}
        return big_array                    
    except Exception as err:
        print("An error occurred: ", str(err))




