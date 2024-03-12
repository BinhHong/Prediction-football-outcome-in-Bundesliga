<p align="center">

<img src="https://img.shields.io/badge/made%20by-Binh%20Hong%20Ngoc-green">
<a href="https://www.linkedin.com/in/binhhongngoc/">
  <img src="https://img.shields.io/badge/-LinkedIn-blue?style=flat&logo=linkedin&logoColor=white" alt="LinkedIn Profile">
</a>
</p>

<h1 align="center"> Prediction football outcome in Bundesliga </h1>

<h3> TABLE OF CONTENTS </h3>
<ol>
    <li><a href="#intro">Introduction</a></li>
    <li><a href="#scraping">Data scraping</a></li>
    <li><a href="#preprocessing">Data preprocessing</a></li>
    <li><a href="#models">Machine Learning models</a></li>
    <li><a href="#results">Results and evaluation</a> </li>
    <li><a href="#acknowledgement">Acknowledgement</a></li>
</ol>

<h2 id="intro">Introduction</h2>

The 2022/2023 Bundesliga season has come to an end with dramatic results, where the title was only decided by the last match and the goal difference, and the last slot for Champions League was determined during the last 9 minutes of the final day. Beside of that, a huge number of over 13.1 million fans watching matches was a significant improvement compared to the previous years impacted by Covid 19 restrictions, which explains the exciting atmosphere all over the stadiums. In the season 2023/2024 up to now there is a big surprise that Leverkusen is 10 points ahead of Bayer Munich, which promises a uprising. In addition to this, most of the matches so far have ended with a high number of goals, especially the fact that the teams played more aggressively and offensively, making the current season so exciting.

In this project, the prediction of the next match between two teams is carried out, based on their previous performance. The outcome is stated as the probability that a team will win, draw or lose. Furthermore, in order to grasp a picture of the fact the teams are putting more effort on attack than on defence, a probability that both teams scoring is also considered.

<h2 id="scraping">Data scraping</h2>

The dataset is scraped from the website https://fbref.com/, using the libraries requests and BeautifulSoup. The detailed statistics of all matches from season 2019/2020 to season 2023/2024 are then saved to dataframe.

<h2 id="preprocessing">Data preprocessing</h2>
A careful data preparation has been carried out, among them
<ul>
    <li> data cleaning: remove duplicates, spot missing values and impute on some stats: shot on target %, save % ...</li>
    <li> outliers: an analysis of the outliers has been made. A correction has been performed to some values in several rows that appeared to be incorrect due to wrong calculation </li>
    <li> feature engineering: LabelEncoder has been used, to add additional significant columns to the dataset. Moreover, the average performance of the last k=4 games has been calculated. Lastly, we have considered correlation matrix and picked the most significant features for the models </li>
</ul>

<h2 id="models">Machine Learning models</h2>

The following models have been used in the project:
<ul>
    <li> Logistic Regression </li>
    <li> Random Forest </li>
    <li> Support vector machine </li>
</ul>
 
<h2 id="results">Results and evaluation</h2>
Models | Accuracy | BLEU-1 | BLEU-2
--- | --- | --- | ---
Vgg 16 with Lstm | 0.5125 | 0.540437 | 0.316454
Resnet 50 with Lstm | 0.5522 | 0.538153 | 0.321559
InceptionV3 with Lstm | 0.5012 | 0.545291 | 0.323035
<h2 id="acknowledgement">Acknowledgement</h2>
