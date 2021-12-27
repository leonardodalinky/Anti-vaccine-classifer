import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import SnowballStemmer, WordNetLemmatizer
from nltk.corpus import wordnet
from typing import List, Dict, Any, Optional, Union


def preprocess_sentence(sentence: str) -> List[str]:
    tokens = _tokenize(sentence)
    return _lemmatize_words(tokens)


def _tokenize(text: str) -> List[str]:
    return word_tokenize(text)


def _lemmatize_words(tokens: List[str]) -> List[str]:
    """
    lemmatize the word and turn them into lowercase

    :param tokens:
    :return:
    """
    def get_wordnet_pos(treebank_tag: str):
        if treebank_tag.startswith('J'):
            return wordnet.ADJ
        elif treebank_tag.startswith('V'):
            return wordnet.VERB
        elif treebank_tag.startswith('N'):
            return wordnet.NOUN
        elif treebank_tag.startswith('R'):
            return wordnet.ADV
        else:
            return wordnet.NOUN
    # to lowercase
    token_poss = nltk.pos_tag(tokens)
    lemmatizer = WordNetLemmatizer()
    ret = list()
    for idx, token_pos in enumerate(token_poss):
        token, pos = token_pos
        ret.append(lemmatizer.lemmatize(token, get_wordnet_pos(pos)).lower())
    return ret
