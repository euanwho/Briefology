from .dictionary_analysis import Dictionary, WordList, Analyser

def analyse_dictionary(file_name):
    analyser = Analyser()
    dictionary = Dictionary(file_name)
    return dictionary.get_duplicates()