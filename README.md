# exoplanet-classification

# a. Problem statement

The NASA Kepler mission has produced a large dataset of exoplanet candidates, including confirmed planets, false positives, and candidates awaiting validation. The challenge is to classify these objects accurately using machine learning techniques. Traditional statistical methods struggle with the complexity and imbalance of the dataset, making it necessary to apply modern classification algorithms.

This project aims to implement six machine learning models — Logistic Regression, Decision Tree, K-Nearest Neighbor, Naive Bayes, Random Forest, and XGBoost — to classify exoplanet candidates. Each model is evaluated using multiple metrics (Accuracy, AUC Score, Precision, Recall, F1 Score, and Matthews Correlation Coefficient) to determine their effectiveness. The ultimate goal is to identify the most reliable model for predicting exoplanet status, thereby supporting astrophysical research and improving automated classification pipelines.


# b. Dataset description:

The dataset used in this project comes from NASA’s Kepler Mission, which was designed to detect Earth-like planets orbiting other stars. Kepler monitored the brightness of over 150,000 stars to identify periodic dips in light intensity, known as transits, which indicate the presence of orbiting planets.

The dataset includes Kepler Objects of Interest (KOIs), which are classified into three categories:

Confirmed planets – validated exoplanets with reliable orbital parameters.

False positives – signals caused by other astrophysical phenomena (e.g., binary stars, instrumental noise).

Candidates – potential planets awaiting further confirmation.

Key features in the dataset include:

Orbital parameters (period, semi-major axis, eccentricity)

Planetary characteristics (radius, equilibrium temperature)

Stellar properties (host star radius, effective temperature, metallicity)

Disposition label (CONFIRMED, FALSE POSITIVE, CANDIDATE)

This dataset is publicly available through the NASA Exoplanet Archive and has been widely used in astrophysics and machine learning research to benchmark classification models.

# c. Models Used

Model	Type / Approach
Logistic Regression	Linear model
Decision Tree	Non-linear tree-based
K-Nearest Neighbor	Distance-based
Naive Bayes (Gaussian)	Probabilistic
Random Forest	Ensemble (Bagging)
XGBoost	Ensemble (Boosting)


# Models Used

|---------------------------|----------------------------|
| Model                     | Type / Approach            |
|---------------------------|----------------------------|
| Logistic Regression       | Linear model               |
| Decision Tree             | Non-linear tree-based      |
| K-Nearest Neighbor        | Distance-based             |
| Naive Bayes (Gaussian)    | Probabilistic              |
| Random Forest             | Ensemble (Bagging)         |
| XGBoost                   | Ensemble (Boosting)        |
|--------------------------------------------------------|

# Make a Comparison Table with the evaluation metrics calculated for all the 6 models as below:

| ML Model Name       | Accuracy | AUC Score | Precision | Recall | F1 Score |   MCC   |
|---------------------|----------|-----------|-----------|--------|----------|---------|
| Logistic Regression | 0.7998   | 0.9611    | 0.8012    | 0.7216 | 0.6715   | 0.7126  |
| Decision Tree       | 0.8991   | 0.9067    | 0.8609    | 0.8587 | 0.8597   | 0.8347  |
| KNN                 | 0.7491   | 0.7754    | 0.4905    | 0.6564 | 0.5457   | 0.6543  |
| Naive Bayes         | 0.3215   | 0.5548    | 0.5033    | 0.3919 | 0.3167   | 0.1025  |
| Random Forest       | 0.9117   | 0.9765    | 0.8862    | 0.8757 | 0.8805   | 0.8547  |
| XGBoost             | 0.9237   | 0.9821    | 0.8959    | 0.8935 | 0.8943   | 0.8752  |


# Observations on the performance of each model on the chosen dataset

| ML Model Name        | Observation about model performance |
|-----------------------|-------------------------------------|
| Logistic Regression   | Achieved decent accuracy (~0.80) and high AUC (~0.96), but recall was lower, indicating difficulty in correctly identifying all positive cases. |
| Decision Tree         | Strong overall performance (~0.90 accuracy) with balanced precision and recall. Slightly prone to overfitting but interpretable. |
| K-Nearest Neighbor    | Moderate accuracy (~0.75) but poor precision (~0.49). Struggled with class imbalance and feature scaling, leading to biased predictions. |
| Naive Bayes           | Weak performance (accuracy ~0.32, MCC ~0.10). Assumption of feature independence did not hold well for this dataset, resulting in misclassifications. |
| Random Forest (Ensemble) | High accuracy (~0.91) and strong balance across metrics. Robust against overfitting and handled dataset complexity effectively. |
| XGBoost (Ensemble)    | Best overall performer (~0.92 accuracy, MCC ~0.88). Achieved the highest precision, recall, and F1, making it the most reliable model for this dataset. |
