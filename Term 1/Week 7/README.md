# Term 1 - Week 7: Computer Vision

---

## 1. Homework & workshop assignments -> [`homework/`](homework/)

**What was the assignment?**

**What did I hand in?**
_List the files, or link to them. Notebook exports, screenshots, scripts._

**What did I find difficult, and how did I solve it?**

### Checklist
- [ ] My workshop / homework files are in `homework/`
- [ ] Everything runs without errors, or I explained what does not and why

---


## 2. Hackathon prototype -> [`hackathon/`](hackathon/)

> Your tool and your SDG for this hackathon are announced at the **start of Friday's class**.
> Write them down here once you know them.

**Project title:**
BirdWatch NL-AI-Powered Bird Identification and Monitoring Assistant
**My pair partner:**
Domile Zukaite
**Tool we had to use:**
Roboflow - for training and using the custom bird-detection model.
**SDG we had to address:**
SDG 15 - Life on Land, particularly Target 15.1, which includes freshwater ecosystems, and Target 15.5, which addresses biodiversity loss.
**What problem does it solve, and for whom?**
BirdWatch NL addresses a practical problem for beginner birdwatchers taking photographs beside Dutch canals and in parks. Recognising birds and counting several individuals in one photograph can be difficult, particularly when birds are far away, partly hidden, or surrounded by reflections and other visual distractions. Keeping observations organised can also take extra effort.

The project is designed primarily for beginners who want help recognising selected bird groups and recording their observations. Its wider connection to SDG 15 is that understanding and recording local wildlife can support nature awareness. However, the application is an educational prototype, not a professional bird-monitoring system, and its actual usefulness for beginners still needs to be evaluated.

Research on Dutch bird populations shows why biodiversity observation matters: some bird groups have declined, although trends differ between species and habitats. BirdWatch NL does not claim to reverse those declines. Instead, it explores whether computer vision can make one small part of observing local birds easier.
**What did you build?**
We built a local web application using Python and Streamlit, connected to a custom object-detection model trained with Roboflow. Users can upload a bird photograph, detect and count birds from six broad groups—ducks, geese, swans, crows, pigeons, and seagulls—and review or correct the predicted counts.

Users can also enter the observation date, a general location, and optional notes, then save the record in a CSV file. The model recognises broad groups rather than exact bird species, and its predictions may be wrong.

**Link to the live thing (if any):**
Demo video: https://drive.google.com/file/d/1MWeiT3g1r1Km78b3tP1FshlhYvtiyuA6/view?usp=sharing
Roboflow workflow: https://app.roboflow.com/gumguard-ai/solutions/chat?workflowUrl=waterbird-monitoring-assi-vwaterbird-monitoring-assi-2-rfdetr-small-t1-logic
**How do I run it?**
Application status: The application runs locally; a publicly deployed website has not been confirmed.

During a successful end-to-end test on 29 October 2026, the AI detected one seagull in an uploaded photograph. The observation was reviewed and saved with a date and location, and it appeared in the observations table. CSV download was available. This demonstrates that the basic workflow worked in that test, but one successful prediction does not establish overall model accuracy.
How do I run it?

Install Python 3.12 and download or clone the GitHub repository.

Open a terminal in the project directory.

Install the required dependencies:

py -3.12 -m pip install streamlit pillow inference-sdk

Start the application:

py -3.12 -m streamlit run app.py

Open the local address printed in the terminal, usually http://localhost:8501.

Enter a valid Roboflow API key when requested. An internet connection is needed for cloud inference.

Upload a bird photograph, select Detect birds with AI, review the counts, enter the observation details, and save the record.

Security: Real API keys must not be committed to GitHub. The application saves the uploaded filename in the observation record, not a copy of the photograph.

**Who did what?**
Domile Zukaite:

Developed the BirdWatch NL web application using Python and Streamlit.

Worked with Roboflow to train and integrate the custom bird-detection model.

Connected the AI model to the application for automatic bird identification and counting.

Implemented the observation system, including manual count corrections, date and location inputs, and CSV storage.

Tested and troubleshot the application, from uploading a photograph to saving an observation.

Slyman Arnaot:

Collected bird photographs for the dataset used to train the AI model.

Created the hackathon presentation, explaining the problem, the proposed solution, and its connection to SDG 15.

Prepared the GitHub README documenting the project, its functionality, and its ethical considerations.

**Ethical reflection - what are the risks of your tool? Who could it harm?**
BirdWatch NL can misidentify birds, miss individuals, count reflections, or assign an unsupported bird to the wrong group. These mistakes could mislead beginners and create unreliable records, particularly if users treated the results as scientific monitoring data. The application warns users that AI predictions may be wrong and allows them to correct counts before saving. Further testing on unseen photographs is needed to measure detection and counting errors. Photographs may also contain identifiable people or reveal sensitive nesting locations, so users should avoid photographing people without permission and use general locations when recording observations. Because photos are sent to Roboflow for cloud inference, users should understand that the images leave their devices. API keys must remain private, and birds should never be disturbed to obtain photographs. The tool is intended for education and personal observation, not professional ecological surveys.
### Checklist
- [ ] Prototype code (or export / workflow file) is in `hackathon/`
- [ ] This week's slides are in `hackathon/`
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
The most important thing I learned is that training an AI model is only one part of building a useful computer-vision application. The model needs to be connected to something people can actually use, tested on unfamiliar images, and evaluated honestly. I also learned that the quality and variety of the training photographs matter, and that the model must be allowed to make mistakes without those mistakes automatically becoming trusted observations.
**Where does this connect to "AI for Good"?**
BirdWatch NL connects to AI for Good because it explores how computer vision can help people learn about local biodiversity and organise their observations. This supports the aims of SDG 15 by encouraging awareness of wildlife, but the app does not directly protect habitats or prove that biodiversity is improving. The project also demonstrates responsible AI: users can correct predictions, unsupported birds should not be mislabelled, personal information should be protected, and the model must be tested before its results are trusted. Its value depends not just on whether the AI works, but on whether it helps people responsibly and honestly.
_One concrete link to ethics, sustainability or social impact._
