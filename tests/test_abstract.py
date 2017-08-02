import pytest

from text_analyzer.abstract import TextAnalyzerAbstract


class TestAbstract(object):
    def test_raises(self):
        with pytest.raises(TypeError):
            TextAnalyzerAbstract()
