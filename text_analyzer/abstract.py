from abc import ABC, abstractmethod
from typing import List

from .structures import WordFrequencyStructure


__all__ = ['TextAnalyzerAbstract']


class TextAnalyzerAbstract(ABC):
    """
    Replacement approach for the IWordFrequency interface.

    Note that the ABC inheritance in combination with the @abstractmethod
    decorators makes it impossible to instantiate a subclass of this abstract
    without implementing the methods.
    """
    @abstractmethod
    def calculate_highest_frequency(self, input_string: str) -> int:
        """
        Returns the frequency of the most occurring word.
        :param input_string:
        :return: Integer
        """
        raise NotImplementedError(
            'Please implement calculate_highest_frequency on your extending '
            '{c_name}.'.format(c_name=self.__class__.__qualname__))

    @abstractmethod
    def calculate_frequency_for_word(self, input_string: str, word: str) \
            -> int:
        """
        Returns the frequency of the given "word" in "input_string".
        :param input_string:
        :param word:
        :return:
        """
        raise NotImplementedError(
            'Please implement calculate_frequency_for_word on your extending '
            '{c_name}.'.format(c_name=self.__class__.__qualname__))

    @abstractmethod
    def calculate_most_frequent_n_words(self, input_string: str, n: int) \
            -> List[WordFrequencyStructure]:
        """
        Returns a list of the n most frequently occurring words.
        :param input_string:
        :param n:
        :return:
        """
        raise NotImplementedError(
            'Please implement calculate_most_frequent_n_words on your '
            'extending {c_name}.'.format(c_name=self.__class__.__qualname__))
