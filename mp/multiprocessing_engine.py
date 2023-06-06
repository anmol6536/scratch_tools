from multiprocessing import Pool, cpu_count
from itertools import repeat
from enum import Enum, auto
from typing import Callable, Iterable, Optional, Union, Generator


class MultiProcessingFunction(Enum):
    STARMAP = auto()
    IMAP_UNORDERED = auto()


class MultiProcessing(object):
    """
    This class is used to perform mp operations.
    """
    THREADS = cpu_count()
    method: MultiProcessingFunction = MultiProcessingFunction.STARMAP
    function: Callable = None
    arguments: Optional[Iterable] = None
    results = None

    def __init__(self,
                 method: MultiProcessingFunction = None) -> None:
        """
        This function is used to initialize the class.
        :param method: Method to be used for mp
        """
        if method is not None:
            self.method = method

    @staticmethod
    def __multiprocessing_input_formatter(primary_arg, *args) -> zip:
        """
        This function is used to format the input for the mp.Pool.starmap function.
        :param primary_arg: Iterable object
        :param args: Arguments that must be repeated
        :return: zip object with the same length as primary_arg
        """
        counter = len(primary_arg)
        secondary_args = []
        for arg in args:
            secondary_args.append(repeat(arg, counter))
        compiled_args = zip(primary_arg, *secondary_args)
        return compiled_args

    def __call__(self, __func, __primary_arg, *args) -> Union[Generator, Iterable]:
        """
        This function is used to call the mp function.
        :param __func: Function to be called
        :param __primary_arg: Iterable object
        :param args: Arguments that must be repeated
        :return: None
        """
        self.arguments = self.__multiprocessing_input_formatter(__primary_arg, *args)
        self.function = __func
        return self.run()

    def run(self) -> Union[Generator, Iterable]:
        """
        This function is used to run the mp function.
        :return: Iterable object with response
        """
        with Pool() as pool:
            if self.method == MultiProcessingFunction.STARMAP:
                return pool.starmap(self.function, self.arguments)
            elif self.method == MultiProcessingFunction.IMAP_UNORDERED:
                return pool.imap_unordered(self.function, self.arguments)
            else:
                raise ValueError('Method not recognized')

    def __repr__(self) -> str:
        """
        This function is used to represent the class.
        :return:
        """
        return f'{self.__class__.__name__}({self.method})'

    def __del__(self):
        """
        This function is used to delete the class.
        :return:
        """
        del self
