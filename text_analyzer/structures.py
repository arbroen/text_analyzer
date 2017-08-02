from collections import namedtuple


__all__ = ['WordFrequencyStructure', 'WordCounter']


WordFrequencyStructure = namedtuple(
    typename='WordFrequencyStructure', field_names=['word', 'frequency'])
