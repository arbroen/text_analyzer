from text_analyzer.analyzer import MinimalTextAnalyzer


m = MinimalTextAnalyzer()

r = m.calculate_frequency_for_word('wor, worrd, word, word.word', 'word')
b = m.calculate_highest_frequency('Somebody went kung fu fighting went fu')

print(r)
print(b)
