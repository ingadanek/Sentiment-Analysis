import glob


def preprocess_review(review, PUNCTUATION):
    """ Returns a list of words. """

    for punct in PUNCTUATION:
        review = review.replace(punct, " ")

    return review.lower().replace('<br />',' ').split()


def count_words(path_pattern, PUNCTUATION):
    files = glob.glob(path_pattern)
    words_count = {}
    for file in files:
        with open(file, encoding = 'UTF-8') as stream:
            content = stream.read()
            words = preprocess_review(content, PUNCTUATION)
            for word in set(words):
                words_count[word] = words_count.get(word, 0) + 1
    return words_count


def compute_sentiment(words, positive_words, negative_words, debug=False):
    sentence_sentiment = 0
    for word in words:
        positive = positive_words.get(word, 0)
        negative = negative_words.get(word, 0)
        all_ = positive + negative
        if all_ != 0:
            word_sentiment = (positive - negative) / all_
        else:
            word_sentiment = 0.0
        if debug:
            print(word, word_sentiment)

        sentence_sentiment += word_sentiment
    sentence_sentiment /= len(words)
    return sentence_sentiment


def raport(sentence_sentiment):
    if sentence_sentiment > 0:
        label = 'positive,'
    else:
        label = 'negative,'
    print('--')
    print('This sentence is', label, 'sentiment =', sentence_sentiment )


def main():
    PATH_POS = 'M03/data/aclImdb/train/pos/*.txt'
    PATH_NEG = 'M03/data/aclImdb/train/neg/*.txt'

    PUNCTUATION = '<>,./?!'

    words_count_pos = count_words(PATH_POS, PUNCTUATION)
    words_count_neg = count_words(PATH_NEG, PUNCTUATION)

    sentence = input('Enter review: ') 
    words = preprocess_review(sentence, PUNCTUATION)

    sentence_sentiment = compute_sentiment(words, words_count_pos, words_count_neg, debug=True)
    print('--')
    raport(sentence_sentiment)

if __name__ == '__main__':
    main()