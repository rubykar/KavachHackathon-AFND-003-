# KavachHackathon-AFND-003-
## Fake News Detector
<img width="1438" alt="Screenshot 2023-04-04 at 5 31 34 PM" src="https://user-images.githubusercontent.com/94167646/229860113-885c4b1b-148e-46fd-8e74-f99c344cb983.png">


We're making this project for Kavach Hackathon.
The project aims to detect fake news articles using machine learning techniques. The goal is to build a model that can accurately classify news articles as either real or fake.

## SetUp

To get started with this project, you will need to have Python 3 installed on your computer. You will also need to install the following packages:

  -  pandas
  -  numpy
  -  scikit-learn
  -  nltk
  -  matplotlib

You can install these packages using pip:

```
pip install pandas numpy scikit-learn nltk matplotlib
```

## Data
We're using IFND dataset to train our model.
This dataset is a collection of news articles from various sources. The dataset includes both real and fake news articles.
You can find this dataset on [KAGGLE](https://www.kaggle.com/datasets/sonalgarg174/ifnd-dataset).

## Preprocessing
Before training the model, the text data needs to be preprocessed.
The following steps are performed:

- Lowercasing: All text is converted to lowercase.
- Tokenization: The text is split into individual words.
- Stopword removal: Common words like "the" and "and" are removed.
- Stemming: Words are reduced to their stem form (e.g. "running" becomes "run").

## Training
The model is trained using a logistic regression classifier and KNN classifier. The training data is split into a training set and a validation set using a 80/20 split. The model is trained on the training set and evaluated on the validation set.

## Evaluation
The model is evaluated using the accuracy and F1 score, which is a weighted average of precision and recall. The F1 score and accuracy ranges from 0 to 1, with 1 being the best possible score.
The lr_model.pkl we used got an accuracy of 0.91 which made it rank above DecisionTree classifier which had the accuracy of 0.89 and NB classifier which had the accuracy of 0.90.

## Usage
We haven't launched our project on a public domain and we are not planning to do it in near future too.
But, you can still use our trained model to make predictions with the help of lr_model.pkl, knn_model.pkl and tfidf_model.pkl.

You can use it with the following Python code:-
```
tfidf_vectorizer = pickle.load(open('tfidf.pkl', 'rb'))
pickled_model = pickle.load(open('lr_model.pkl', 'rb'))
knn_model = pickle.load(open('knn_model.pkl', 'rb'))
```
You can also find the possible real version of the fake news using the knn_model.pkl. It gives you the 5 closest real versions of the fake news provided to it.

## Conclusion
This project demonstrates how machine learning can be used to detect fake news articles. While the model is not perfect, it shows promise and can be improved with more data and better preprocessing techniques.

## Contributors
Huge Thanks to the fellow contributors for making this possible!

[Ruby kar](https://github.com/rubykar)
[Prerna Budhwar](https://github.com/prernabr)
[Sneha Barman](https://github.com/SnehaBarman7121)
[Kundan Singh](https://github.com/kundan1209)
