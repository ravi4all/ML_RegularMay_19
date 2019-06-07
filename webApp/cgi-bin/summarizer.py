import re
import string
import copy
import pandas as pd
import numpy as np
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.corpus.reader.wordnet import NOUN, VERB, ADJ, ADV
from nltk.corpus import brown, stopwords
from nltk.cluster.util import cosine_distance
from operator import itemgetter


def textProcessing(dataset):
    tokens = []
    sentencesTokenize = sent_tokenize(dataset)
    for item in sentencesTokenize:
        tokens.append(word_tokenize(item.lower()))
    sentences = copy.deepcopy(tokens)

    englishStopwords = stopwords.words('english')
    punctuations = list(string.punctuation)

    for i in range(len(tokens)):
        tokens[i] = ' '.join(tokens[i])
        tokens[i] = re.sub(r"i'm", "i am", tokens[i])
        tokens[i] = re.sub(r"n't", "not", tokens[i])
        tokens[i] = re.sub(r"n 't", "not", tokens[i])
        tokens[i] = re.sub(r"n' t", "not", tokens[i])
        tokens[i] = re.sub(r"he's", "he is", tokens[i])
        tokens[i] = re.sub(r"she's", "she is", tokens[i])
        tokens[i] = re.sub(r"that's", "that is", tokens[i])
        tokens[i] = re.sub(r"what's", "what is", tokens[i])
        tokens[i] = re.sub(r"where's", "where is", tokens[i])
        tokens[i] = re.sub(r"\'ll", " will", tokens[i])
        tokens[i] = re.sub(r"\'ve", " have", tokens[i])
        tokens[i] = re.sub(r"\'re", " are", tokens[i])
        tokens[i] = re.sub(r"\'d", " would", tokens[i])
        tokens[i] = re.sub(r"won't", "will not", tokens[i])
        tokens[i] = re.sub(r"can't", "cannot", tokens[i])
        tokens[i] = re.sub(r"don't", "do not", tokens[i])

        tokens[i] = "".join(ch for ch in tokens[i] if ch not in punctuations)

    Tokens = []
    for item in tokens:
        Tokens.append(word_tokenize(item.lower()))

    for i in range(len(Tokens)):
        Tokens[i] = [value for value in Tokens[i] if value not in englishStopwords]

    pos_tags = {
        NOUN: ['NN', 'NNS', 'NNP', 'NNPS', 'PRP', 'PRP$', 'WP', 'WP$'],
        VERB: ['VB', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ'],
        ADJ: ['JJ', 'JJR', 'JJS'],
        ADV: ['RB', 'RBR', 'RBS', 'WRB']
    }

    tagged_words = []
    for token in Tokens:
        tagged_words.append(nltk.pos_tag(token))

    pos_word = []
    pos_words = []

    for i in range(len(tagged_words)):
        pos_word = []
        for j in range(len(tagged_words[i])):

            flag = False
            #         pos_words.append([])
            for key, value in pos_tags.items():
                if tagged_words[i][j][1] in value:
                    pos_word.append((tagged_words[i][j], key))
                    flag = True
                    break
        if not flag:
            pos_word.append((tagged_words[i][j], NOUN))
        pos_words.append(pos_word)

    normalized_words = []
    lem = WordNetLemmatizer()
    for i in range(len(pos_words)):
        normalized_words.append([lem.lemmatize(w[0], pos=p) for w, p in pos_words[i]])

    return normalized_words, sentences

def pagerank(M, eps=1.0e-8, d=0.85):
    N = M.shape[1]
    v = np.random.rand(N, 1)
    v = v / np.linalg.norm(v, 1)
    last_v = np.ones((N, 1), dtype=np.float32) * np.inf
    M_hat = (d * M) + (((1 - d) / N) * np.ones((N, N), dtype=np.float32))

    while np.linalg.norm(v - last_v, 2) > eps:
        last_v = v
        v = np.matmul(M_hat, v)
    return v


def sentence_similarity(sent1, sent2):
    all_words = list(set(sent1 + sent2))

    vector1 = [0] * len(all_words)
    vector2 = [0] * len(all_words)

    for w in sent1:
        vector1[all_words.index(w)] += 1

    for w in sent2:
        vector2[all_words.index(w)] += 1

    return 1 - cosine_distance(vector1, vector2)


def build_similarity_matrix(sentences):
    S = np.zeros((len(sentences), len(sentences)))
    for i in range(len(sentences)):
        for j in range(len(sentences)):
            if i == j:
                continue
            else:
                S[i][j] = sentence_similarity(sentences[i], sentences[j])

    for i in range(len(S)):
        S[i] /= S[i].sum()
    return S


def predict(dataset):
    normalized_words, sentences = textProcessing(dataset)
    S = build_similarity_matrix(normalized_words)

    sentence_ranks = pagerank(S)
    ranked_sentence_indexes = [item[0] for item in sorted(enumerate(sentence_ranks), key=lambda item: -item[1])]

    selected_sentences = sorted(ranked_sentence_indexes[:5])
    summary = itemgetter(*selected_sentences)(sentences)
    len(summary)
    finalSummary = []
    for sent in summary:
        # print(' '.join(sent))
        finalSummary.append(' '.join(sent))

    summarizedText = ' '.join(finalSummary)
    return summarizedText
