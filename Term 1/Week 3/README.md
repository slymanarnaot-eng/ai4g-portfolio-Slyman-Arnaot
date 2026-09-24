# Term 1 - Week 3: Lists & Dictionaries

---

## 1. Homework & workshop assignments -> [`homework/`](homework/)

**What was the assignment?**
The workshop focused on Python Lists & Dictionaries and using them to organise and work with information.
**What did I hand in?**
Workshop / homework files are in homework/.

Notebook exports, Desk research, screenshots, and scripts are included where applicable.

**What did I find difficult, and how did I solve it?**
I found it difficult at first to understand how lists and dictionaries store information and how to access individual values. I solved this by practising the examples from the workshop and testing small pieces of Python code step by step.

### Checklist
- [x] My workshop / homework files are in `homework/`
- [x] Everything runs without errors, or I explained what does not and why

---


## 2. Hackathon prototype -> [`hackathon/`](hackathon/)

> Your tool and your SDG for this hackathon are announced at the **start of Friday's class**.
> Write them down here once you know them.

**Project title:**
Healthcare Easy - Translate, Explain, Simplify
**My pair partner:**
Sandra Wandel
**Tool we had to use:**
Python + Gemini API
The prototype is a Python terminal application that sends a healthcare message to Gemini and receives a structured explanation.
**SDG we had to address:**
SDG 10 - Reduced Inequalities
**What problem does it solve, and for whom?**
Healthcare information can be difficult to understand when people face language barriers or complicated medical terminology.

Our target users are people in the Netherlands who receive healthcare information in a language or level of medical language that they do not easily understand.

Healthcare Easy is designed to help the user understand a healthcare message in their requested language. It does more than direct translation: it translates, explains, and simplifies the information.

**What did you build?**
We built a working Python MVP that lets users select the original and target language, paste a healthcare message, and receive a structured explanation from Gemini. It provides a simple explanation, clear actions, important information, unclear or missing details, and a full explanation in the requested language. It also includes a safety note and privacy guidance to remind users not to share unnecessary sensitive information.

**Link to the live thing (if any):**
_Deployed URL, workflow export, video demo - whatever proves it works._

**How do I run it?**
Open Anaconda Prompt and run:

cd C:\Users\Desktop\Downloads\healthcare-easy
python terminal_app.py

The project uses the GEMINI_API_KEY environment variable. The API key is not stored in the Python file.

**Who did what?**
Slyman:
Did the desk research
Developed the Python prototype.
Worked on the Gemini API integration.
Designed the structured healthcare explanation.
Added language selection and multilingual output.
Added safety and privacy instructions.
Tested different source/target language combinations.
Prepared the demo and presentation.
Sandra:
Did the desk research
Prepared the presentation.
**Ethical reflection - what are the risks of your tool? Who could it harm?**
Because incorrect healthcare information can cause harm, Healthcare Easy treats the original message as the source of truth and avoids diagnosing, prescribing, changing important details, or guessing missing information. It also includes a safety note and privacy guidance, reminding users not to share unnecessary sensitive information.

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
The live demo showed the main flow: selecting the languages, entering a healthcare message, and receiving a structured explanation. It also showed that the prototype goes beyond translation by explaining the message, identifying actions, highlighting important information, and pointing out unclear details. Next time, I would keep the introduction shorter and focus more on the actual user experience.
---

## 4. Reflection

**What is the most important thing I learned this week?**
I learned how to connect an AI model programmatically using an API key and integrate it with an interface that I can design in Python. I also learned that building an AI prototype is not only about making it work technically, but also about designing clear instructions, structured outputs, safety rules, and a good user experience.
**Where does this connect to "AI for Good"?**
Healthcare Easy connects to SDG 10 - Reduced Inequalities because it focuses on making healthcare information easier to understand for people who experience language or terminology barriers.

The project also showed me the importance of responsible AI in a sensitive area such as healthcare. The prototype includes safety and privacy considerations and avoids presenting itself as a replacement for professional medical support.
