# Term 1 - Week 6: Language Models

---

## 1. Homework & workshop assignments -> [`homework/`](homework/)

**What was the assignment?**
We worked with language models and looked at three ideas: word embeddings, RNNs/LSTMs, and transformers. The notebook helped us see how words can be represented as numbers, how a model can remember information in a sequence, and how a transformer uses context. For the individual task, we had to test a sentiment model on feedback examples, compare its predictions with our own labels, and think about mistakes and possible harm.

**What did I hand in?**
 Week6_Workshop_Student.ipynb 

**What did I find difficult, and how did I solve it?**
At first, embeddings, LSTMs and transformers sounded like similar things, so it was hard to understand what each one actually does. The examples helped me see the difference: embeddings turn words into numbers, an LSTM reads things in order and can keep useful information, and a transformer uses context from different parts of the text. I also learned that a sentiment prediction can be wrong, so it should be checked against human judgement.
### Checklist
- [x] My workshop / homework files are in `homework/`
- [x] Everything runs without errors, or I explained what does not and why

---


## 2. Hackathon prototype -> [`hackathon/`](hackathon/)

> Your tool and your SDG for this hackathon are announced at the **start of Friday's class**.
> Write them down here once you know them.

**Project title:**
Rail Pulse - Understanding Passenger Reactions to Railway Disruptions
**My pair partner:**
Akif Olgun
**Tool we had to use:**
A pretrained sentiment model from Hugging Face, running locally in Python with the transformers library. The collector uses cardiffnlp/twitter-xlm-roberta-base-sentiment.
**SDG we had to address:**
SDG 9 - Industry, Innovation and Infrastructure. Our project is related to reliable and resilient transport infrastructure, but it does not measure the UN's official SDG indicators or find the technical cause of railway problems.
**What problem does it solve, and for whom?**
The intended user is a passenger-communications or service-quality analyst at NS or ProRail. When train services are disrupted, this person may want to understand what passengers are saying online. Reading every post by hand takes time, so Rail Pulse aims to show the overall sentiment and let the analyst check the posts behind a change in the chart.

**What did you build?**
We made a Python prototype that listens to public posts on Bluesky, filters for posts that might be related to Dutch railways, runs a pretrained sentiment model and saves the results in an SQLite database. A second notebook reads the database and shows sentiment counts and trends. A third notebook prepares a sample for human labelling and comparison between models.

**Link to the live thing (if any):**
_Deployed URL, workflow export, video demo - whatever proves it works._

**How do I run it?**
1. Open the project folder in Jupyter and use the project's Python environment.
2. Run 01_live_collector_corrected.ipynb from top to bottom. Wait for the model to load and check the collector status.
3. Keep the computer awake and connected to the internet while the collector runs.
4. Open 02_dashboard.ipynb from the same project folder to view the charts and inspect the saved posts.
5. After enough real posts have been collected, open 03_evaluation.ipynb, label 50 posts yourself, and compare the models.
**Who did what?**
Akif mainly worked on the technical implementation and notebooks. I mainly worked on the desk research, the user and problem definition, the SDG connection, and thinking about the limitations and ethical risks. We discussed the results and what still needed to be checked.
**Ethical reflection - what are the risks of your tool? Who could it harm?**
The people who post online are not the same as all Dutch train passengers. Some passengers never post, and the people who do post may have stronger opinions. The model can misunderstand Dutch wording, sarcasm or a factual service announcement, so a label is not always right. A rise in negative posts also does not prove what caused a disruption. We should show the number of posts, check the original messages, collect only what is needed and follow the platform's rules. The dashboard should help a person investigate a concern, not make decisions automatically or blame staff.
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
I learned that a language model does not understand text in the same way a person does. It finds patterns in numbers and uses them to make a prediction. The model can be useful, but the result still needs to be checked, especially when the text is sarcastic, unclear or in a language the model handles less well.
**Where does this connect to "AI for Good"?**
Rail Pulse could help a railway communications team notice when public reactions change and look more closely at what passengers are saying. This might help them decide whether clearer information is needed during a disruption. But the tool could also misrepresent people if the data are biased or the model is wrong, so a human should review the posts before taking action.
