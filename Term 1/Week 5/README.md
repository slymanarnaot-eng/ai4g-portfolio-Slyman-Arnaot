# Term 1 - Week 5: Machine Learning Basics

---

## 1. Homework & workshop assignments -> [`homework/`](homework/)

**What was the assignment?**
We practiced the basics of machine learning and worked with Python, classification, evaluation metrics, and model concepts such as confusion matrices, precision, recall, and F1 score.

**What did I hand in?**
homework/Week5_Workshop_Student.ipynb

**What did I find difficult, and how did I solve it?**
At first I was mainly confused about what the model was actually learning and why we needed separate training and test data. The confusion matrix also took me a little time because I had to look at it from the actual result and predicted result at the same time. I solved this by going through the workflow step by step and running the notebook again from the beginning instead of changing things randomly. Seeing the training and test scores next to each other also made overfitting much easier to understand.
### Checklist
- [x] My workshop / homework files are in `homework/`
- [x] Everything runs without errors, or I explained what does not and why

---


## 2. Hackathon prototype -> [`hackathon/`](hackathon/)

> Your tool and your SDG for this hackathon are announced at the **start of Friday's class**.
> Write them down here once you know them.

**Project title:**
 Predicting Credit Card Default
**My pair partner:**
Rayna Jong and Lili Tárnok
**Tool we had to use:**
Scikit-learn
**SDG we had to address:**
SDG 8 - Decent Work and Economic Growth
**What problem does it solve, and for whom?**
The project predicts whether a credit-card client is likely to default on their payment next month. The main user is a credit-risk analyst at a bank or credit-card provider. The prediction can help the analyst identify clients who may need further risk assessment.

**What did you build?**

We built a machine-learning classification project using the UCI Default of Credit Card Clients dataset. We trained and tuned three models: K-Nearest Neighbours, Logistic Regression, and Random Forest.
Because missing a real defaulter is an important risk, we used recall on the default class as our main metric. Random Forest performed best overall, with a test recall of 0.362 and an F1 score of 0.466.


**Link to the live thing (if any):**
There is no deployed live application. The working prototype is the Jupyter notebook in the `hackathon/` folder.

**How do I run it?**
Open the Jupyter notebook in Google Colab and run the cells from top to bottom. The notebook downloads the UCI dataset, preprocesses the data, trains and tunes the three models, evaluates them on the held-out test set, performs error analysis, and makes a prediction for a new example.

**Who did what?**
I did most of the desk research and worked on choosing and understanding the dataset. I also helped shape the problem, looked at the classification approach, and worked on the technical part of the model comparison. Lili Tárnok mainly helped with brainstorming, discussing the idea. Rayna Jong prepared the presentation. We discussed the decisions together.

**Ethical reflection - what are the risks of your tool? Who could it harm?**
The model could harm clients if its predictions are treated as final decisions about their credit. A false negative could cause a bank to underestimate a client's risk, while a false positive could cause unnecessary risk-management actions for a client who would not default. The dataset also contains sensitive demographic information such as sex, age, education, and marital status. In addition, the data comes from Taiwanese clients from 2005, so the model may not represent customers in other countries or today's customers. For these reasons, the model should only be used as decision support, with human review and monitoring of subgroup performance.


### Checklist
- [x] Prototype code (or export / workflow file) is in `hackathon/`
- [x] This week's slides are in `hackathon/`
- [x] The prototype actually runs, and I wrote down how to run it
- [x] Ethical reflection written above

---

## 3. Presentation -> [`presentation/`](presentation/)

*Only fill this in for the week your group was selected to present. You need at least **one** of these across the whole term.*

- [ ] My group presented in this week
- [ ] Slides are in `presentation/`
- [ ] Proof of the live demo is in `presentation/` (recording, screenshots, or link)

**How did it go? What would I do differently next time?**

---

## 4. Reflection

**What is the most important thing I learned this week?**
The most important thing I learned was how to build and evaluate a classification model properly. I learned why we should split the data before preprocessing, use pipelines to avoid data leakage, tune models using cross-validation, and evaluate the final models on a separate test set. I also learned that accuracy can be misleading when the classes are imbalanced, so choosing the right metric is important.

**Where does this connect to "AI for Good"?**
This connects to AI for Good because the project applies machine learning to a real financial problem while considering its impact on people. Predicting credit-card default can support better risk management, but the model can also create unfair or harmful outcomes if it is used without human oversight. This is why we considered false positives, false negatives, subgroup performance, fairness, and the limitations of the dataset.
