import re

from typing import List
from collections import Counter

from .abstract import TextAnalyzerAbstract
from .structures import WordFrequencyStructure


__all__ = ['MinimalTextAnalyzer']


class MinimalTextAnalyzer(TextAnalyzerAbstract):
    """
    We have the great standard library "collections" do all the work for us.
    Because why not?
    """
    @staticmethod
    def _word_counter(input_string: str) -> Counter:
        """
        The delimiters are defined ambiguously, hence let's fallback to a regex
        word splitter. Return the results as a Counter object.
        :param input_string:
        :return:
        """
        # @todo sorting
        return Counter(re.findall(pattern='\w+', string=input_string.lower()))

    def calculate_highest_frequency(self, input_string: str) -> int:
        """
        Returns the frequency of the most occurring word.
        :param input_string:
        :return: Integer
        """
        counted = \
            self._word_counter(input_string=input_string).most_common(n=1)

        if len(counted):
            return counted[0][1]

        return 0

    def calculate_frequency_for_word(self, input_string: str, word: str) \
            -> int:
        """
        Returns the frequency of the given "word" in "input_string".
        :param input_string:
        :param word:
        :return:
        """
        return self._word_counter(input_string=input_string)[word.lower()]

    def calculate_most_frequent_n_words(self, input_string: str, n: int) \
            -> List[WordFrequencyStructure]:
        """
        Returns a list of the n most frequently occurring words.
        :param input_string:
        :param n:
        :return:
        """
        return self._word_counter(input_string=input_string).most_common(n=n)


class MaximalTextAnalyzer(TextAnalyzerAbstract):
    """
    Let's assume "collections" broke. We don't know exactly what a separator
    character is, so approach that definition as not an alphabetical letter.
    """
    _letters = [
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
        'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    def _insert_into_sorted_list(self, current, word):

        return word

    def _parse_words(self, input_string: str):
        """
        A string is an iterable. Let's parse through it.

        :param input_string:
        :return:
        """
        _current_word = ''
        parsed_words = []

        for character in input_string.lower():
            if character in self._letters:
                _current_word += character
            elif len(_current_word):
                # @todo insert into sorted list
                # parsed_words = self._insert_into_sorted_list(parsed, word)
                if _current_word in parsed_words.keys():
                    parsed_words[_current_word] = parsed_words[_current_word] + 1
                else:
                    parsed_words[_current_word] = 1

                _current_word = ''

        # What if it does not end with a separator?
        if _current_word:
            if _current_word in parsed_words.keys():
                parsed_words[_current_word] = parsed_words[_current_word] + 1
            else:
                parsed_words[_current_word] = 1

        return parsed_words

    def calculate_highest_frequency(self, input_string: str) -> int:
        """
        Returns the frequency of the most occurring word.
        :param input_string:
        :return: Integer
        """
        parsed_words = self._parse_words(input_string=input_string)

        return

    def calculate_frequency_for_word(self, input_string: str, word: str) \
            -> int:
        """
        Returns the frequency of the given "word" in "input_string".
        :param input_string:
        :param word:
        :return:
        """
        return 0

    def calculate_most_frequent_n_words(self, input_string: str, n: int) \
            -> List[WordFrequencyStructure]:
        """
        Returns a list of the n most frequently occurring words.
        :param input_string:
        :param n:
        :return:
        """
        return 1
