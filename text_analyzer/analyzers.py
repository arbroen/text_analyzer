import re

from typing import List, Tuple, Dict
from collections import Counter

from .abstract import TextAnalyzerAbstract
from .structures import WordFrequencyStructure


__all__ = ['MinimalTextAnalyzer', 'MaximalTextAnalyzer']


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
        return Counter(re.findall(pattern='\w+', string=input_string.lower()))

    def _sorted_counter(self, input_string: str) \
            -> List[Tuple[str, int]]:
        """
        Applies secondary sorting to the results of the Counter class. Which is
        impossible to sort directly since it subclasses Dict.
        :param input_string:
        :return:
        """
        _counter = self._word_counter(input_string=input_string)

        return sorted(_counter.most_common(), key=lambda x: (-x[1], x[0]))

    def _typed_sorted_result(self, input_string: str) \
            -> List[WordFrequencyStructure]:
        """
        Apply the class WordFrequencyStructure over the results (formality).
        :return:
        """
        sorted_results = self._sorted_counter(input_string=input_string)

        return list(map(lambda x: WordFrequencyStructure(*x), sorted_results))

    def calculate_highest_frequency(self, input_string: str) -> int:
        """
        Returns the frequency of the most occurring word.
        :param input_string:
        :return: Integer
        """
        results = \
            self._typed_sorted_result(input_string=input_string)

        if len(results):
            return results[0].frequency

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
        results = \
            self._typed_sorted_result(input_string=input_string)

        return results[:n]


class MaximalTextAnalyzer(MinimalTextAnalyzer):
    """
    Let's assume "collections" broke. We don't know exactly what a separator
    character is, so approach that definition as not an alphabetical letter.

    ! Note, with the exception off the convenient constructor
    collections.namedtuple :: WordFrequencyStructure

    ! Note, it (partially) uses MinimalTextAnalyzer's implementations of the
    TextAnalyzerAbstract abstract methods and _typed_sorted_result. Yes, I am
    that lazy.
    """
    _letters = [
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
        'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    @staticmethod
    def _insert_into_dict(words_dict: Dict[str, int], key: str) \
            -> Dict[str, int]:
        """
        Prevents duplication of this logical part.
        :param words_dict:
        :param key:
        :return:
        """
        if key in words_dict.keys():
            words_dict[key] = words_dict[key] + 1
        else:
            words_dict[key] = 1

        return words_dict

    @staticmethod
    def _word_counter(input_string: str) -> Dict[str, int]:
        """
        A string is an iterable. Let's parse through it.

        :param input_string:
        :return:
        """
        # @todo Create a data type that can counts keys as they are added
        _current_word = ''
        parsed_words = {}

        for character in input_string.lower():
            if character in MaximalTextAnalyzer._letters:
                _current_word += character
            elif len(_current_word):
                parsed_words = MaximalTextAnalyzer._insert_into_dict(
                    words_dict=parsed_words, key=_current_word)

                _current_word = ''

        # What if it does not end with a separator?
        if _current_word:
            parsed_words = MaximalTextAnalyzer._insert_into_dict(
                words_dict=parsed_words, key=_current_word)

        return parsed_words

    def _sorted_counter(self, input_string: str) \
            -> List[Tuple[str, int]]:
        """
        Applies secondary sorting to the results of the Counter class. Which is
        impossible to sort directly since it subclasses Dict.

        Note: A possible warning can be thrown due to missing mypy stubs.

        :param input_string:
        :return:
        """
        _counter = self._word_counter(input_string=input_string)

        return sorted(_counter.items(), key=lambda x: (-x[1], x[0]))

    def calculate_frequency_for_word(self, input_string: str, word: str) \
            -> int:
        """
        Returns the frequency of the given "word" in "input_string".

        We have to account for the fact that a Counter defaults to 0 when
        they key does not exist.

        :param input_string:
        :param word:
        :return:
        """
        results = self._word_counter(input_string=input_string)
        word = word.lower()

        if word in results.keys():
            return results[word]

        return 0
