from text_analyzer.analyzers import MinimalTextAnalyzer, MaximalTextAnalyzer


class AnalyzerTestMixin(object):
    """
    Since we're using an TextAnalyzerAbstract class to ensure some methods,
    the following test can be generalized.
    """
    _analyzer = None
    _text = \
        "Lorem ipsum dolor sit amet, consectetuer adipiscing elit. " \
        "Aenean commodo ligula eget dolor. Aenean massa. Cum sociis " \
        "natoque penatibus et magnis dis parturient montes, nascetur " \
        "ridiculus mus. Donec quam felis, ultricies nec, pellentesque " \
        "eu, pretium quis, sem. Nulla consequat massa quis enim. Donec " \
        "pede justo, fringilla vel, aliquet nec, vulputate eget, arcu. " \
        "In enim justo, rhoncus ut, imperdiet a, venenatis vitae, justo." \
        " Nullam dictum felis eu pede mollis pretium. Integer tincidunt." \
        " Cras dapibus. Vivamus elementum semper nisi. Aenean vulputate" \
        " eleifend tellus. Aenean leo ligula, porttitor eu, consequat" \
        " vitae, eleifend ac, enim. Aliquam lorem ante, dapibus in, " \
        "viverra quis, feugiat a, tellus. Phasellus viverra nulla ut " \
        "metus varius laoreet. Quisque rutrum. Aenean imperdiet. " \
        "Etiam ultricies nisi vel augue. Curabitur ullamcorper " \
        "ultricies nisi. Nam eget dui."

    def test_calculate_highest_frequency(self):
        """
        Easiest test, lets double check for empty and whitespace.
        :return:
        """
        result = \
            self._analyzer.calculate_highest_frequency(input_string=self._text)

        assert result == 5

        # Edge cases
        result = \
            self._analyzer.calculate_highest_frequency(input_string="")

        assert result == 0

        result = \
            self._analyzer.calculate_highest_frequency(input_string="    ")

        assert result == 0

    def test_calculate_frequency_for_word(self):
        """
        Enim does not occur with a capital, however, we still expect the result
        to be three, since we're case insensitive.
        :return:
        """
        result = self._analyzer.calculate_frequency_for_word(
            input_string=self._text, word="enim")

        assert result == 3

        result = self._analyzer.calculate_frequency_for_word(
            input_string=self._text, word="Enim")

        assert result == 3

        # Edge cases, empty word, empty input
        result = self._analyzer.calculate_frequency_for_word(
            input_string=self._text, word="")

        assert result == 0

        result = self._analyzer.calculate_frequency_for_word(
            input_string="", word="")

        assert result == 0

        result = self._analyzer.calculate_frequency_for_word(
            input_string="", word="Enum")

        assert result == 0

    def test_calculate_most_frequent_n_words(self):
        result = self._analyzer.calculate_most_frequent_n_words(
            input_string=self._text, n=3)

        assert len(result) == 3

        result = self._analyzer.calculate_most_frequent_n_words(
            input_string=self._text, n=5)

        assert len(result) == 5

        # Edge cases
        result = self._analyzer.calculate_most_frequent_n_words(
            input_string="", n=5)

        assert len(result) == 0

        result = self._analyzer.calculate_most_frequent_n_words(
            input_string=self._text, n=0)

        assert len(result) == 0


class TestMinimumAnalyzer(AnalyzerTestMixin):
    def setup(self):
        self._analyzer = MinimalTextAnalyzer()


class TestMaximumAnalyzer(AnalyzerTestMixin):
    def setup(self):
        self._analyzer = MaximalTextAnalyzer()
