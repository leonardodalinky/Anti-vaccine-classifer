# Anti-vaccine Classifier

A tweet classifier to distinguish each tweet as "anti-vaccine" or "others", based on XGBoost. All the data come from [avax-tweets-dataset](https://github.com/gmuric/avax-tweets-dataset) and [COVID19_Tweets_Dataset](https://github.com/lopezbec/COVID19_Tweets_Dataset).

This project is the final project of my ML course.

In this project, I go through the entire process of data collecting, data preprocessing, feature selection and model training by myself.

## File structure

```
.
├── avax-tweet-ids  // raw anti-vaxx tweet ids
│   ├── 2021_01
│   └── 2021_02
├── avax-tweets     // generated
├── avax-tweets-clean   // generated
├── covid19-tweet-ids   // raw covid19 tweet ids
│   └── 2021_01_05_22_Summary_Sentiment.txt
├── covid19-tweets  // generated
├── covid19-tweets-clean    // generated
├── data_collect.ipynb  // data collecting and cleaning
├── main.ipynb  // preprocessing & training
├── models  // generated for saving models
├── preprocess.py   // utils for preprocessing
├── requirements.txt
└── text_clean.py   // utils for data cleaning
```

## Requirements
```bash
pip install -r requirements.txt
```

## Datasets

At the beginning, we shall collect some data using a Twitter scraper tool called [stweet](https://github.com/markowanga/stweet), **which could get tweet without Twitter Developer Account**.

All the data come from [avax-tweets-dataset streaming-ids](https://github.com/gmuric/avax-tweets-dataset/tree/main/streaming-tweetids) and [COVID19_Tweets_Dataset Summary_Sentiment](https://github.com/lopezbec/COVID19_Tweets_Dataset/tree/main/Summary_Sentiment).

Create directory `avax-tweet-ids` and `covid19-tweet-ids`, then put some data from corresponding datasets like this:
```
├── avax-tweet-ids
│   ├── 2020-10
│   ├── 2020-11
│   ├── 2020-12
│   ├── 2021-01
│   ├── 2021-02
│   ├── 2021-03
│   ├── 2021-04
│   ├── 2021-05
│   ├── 2021-06
│   ├── 2021-07
│   ├── 2021-08
│   ├── 2021-09
│   ├── 2021-10
│   └── 2021-11
├── covid19-tweet-ids
│   ├── 2021_01
│   ├── 2021_02
│   ├── 2021_03
│   ├── 2021_04
│   ├── 2021_05
│   ├── 2021_06
│   ├── 2021_07
│   ├── 2021_08
│   ├── 2021_09
│   ├── 2021_10
│   └── 2021_11
├── ... ...
```

Then run the notebook `data_collect.ipynb` and follow the instructions.

## Preprocessing & Training

Run the notebook `main.ipynb` and follow the steps to train the full model.

## Analysis

```
Accuracy: 89.8%, Precision: 88.7%, Recall: 94.1%, F1 score: 91.3%
```

Amazing!

## License

MIT.
