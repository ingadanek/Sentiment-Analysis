# Sentiment Analysis

Using Python and its packages to analyse a dataset of 50,000 film reviews so they can automatically determine the sentiment of new comments and reviews.

All of the positive and negative comments are in the subfolders called 'pos' and 'neg' respectively.

Positive comments are those with rating of minimum 7 out of 10.
Negative comments are those with rating of maximum 6 out of 10.

Each review is located in a separate file.

Program asks a user to enter a review to then calculate its sentiment.


First, each word's sentiment is calculated using the following equation:

 (positive-negative)/all_

positive - the number of positive reviews in which the given word appeared,
negative - the number of positive reviews in which the given word appeared,
all_ - the number of all the reviews in which the given word appeared

For example, if a certain word appears in 5 positive reviews and 5 negative reviews, then its sentiment equals (5-5)/10 = 0.0. 
If that word appears in 9 positive reviews and 1 negative review, then its sentiment equals (9-1)/10 = +0.8.

Having calculated each word's sentiment, the program then proceeds to calculating the sentiment of the whole review. In order to do that, the mean value of each word's sentiment is calculated.

The whole review is considered to be:
positive when its sentiment is > 0,
negative when its sentiment is < 0

## Code and Resources Used
**Python Version:** `3.10.6`

**Modules:** `glob` 
