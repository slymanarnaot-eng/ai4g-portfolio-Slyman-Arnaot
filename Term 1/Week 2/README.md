# Term 1 - Week 2: Loops & Functions

---

## 1. Homework & workshop assignments -> [`homework/`](homework/)

**What was the assignment?**
Exercises practicing Python loops, functions, and data structures from Week 2 lectures.

**What did I hand in?**
Notebook exports and Python scripts in `homework/`.

**What did I find difficult, and how did I solve it?**
Structuring nested loops and properly passing arguments into helper functions. Solved by breaking down functions into single-purpose logic blocks and testing each part step-by-step.

### Checklist
- [x] My workshop / homework files are in `homework/`
- [x] Everything runs without errors, or I explained what does not and why

---


## 2. Hackathon prototype -> [`hackathon/`](hackathon/)

> Your tool and your SDG for this hackathon are announced at the **start of Friday's class**.
> Write them down here once you know them.

**My pair partner:**
Bart Bruggeling 
**Tool we had to use:**
n8n
**SDG we had to address:**
SDG 3 health and well-being
**What problem does it solve, and for whom?**
_Name a real, specific user. "Everyone" is not a user._
People with diabetes type 1 and type 2, it is a blood sugar measurement reminder and it helps with advise and observation. This to prevent other diabetes related illnesses. 
**What did you build?**
_Two or three sentences. What can a user actually do with it?_
Get a notification to measure their blood sugar. And a small data bank with the previous measurements.
**Link to the live thing (if any):**
https://glucoflow-web-interf-usvo.bolt.host/

https://drive.google.com/file/d/1IN25rPuz_70JJRTqfjwMEOj5Tiqb_1Ru/view?usp=sharing

https://slyman.app.n8n.cloud/workflow/JiNPTdTtny1ovd3G

**How do I run it?**
1. Open the GlucoFlow web application.
2. Login using the prototype sign-in screen.
3. Fill in patient vitals: Patient ID (e.g., `P001`), Glucose (mg/dL), Heart Rate (BPM), Symptom, and Physical Activity.
4. Click **Analyze Health Status**.
5. To test an urgent escalation: Enter a glucose reading above `250 mg/dL` (e.g., `300 mg/dL`). The UI will display an **URGENT** badge and confirmation modal, and dispatch a live Telegram notification.
**Who did what?**
_Be honest about the split of work between you and your partner._
We did 50/50. We both brainstormed and came up with the idea. I made the readme, helped with the bolt webpage and made the powerpoint slides. Slyman made the n8n nodes, bolt webpage and made the powerpoint the  We had good communication with what needed to be done and worked in our own strengths.
**Ethical reflection - what are the risks of your tool? Who could it harm?**
_Every hackathon requires this. One honest paragraph beats three vague ones._
The data of the measurements are vulnerable, also the link with a medical information could be a risk. The AI can give the wrong medical information. And people who can not afford technology or internet can not use this tool.


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
The live demo executed smoothly, showing the real-time POST request passing through n8n to Gemini and successfully triggering the Telegram emergency alert in under 3 seconds.

---

## 4. Reflection

**What is the most important thing I learned this week?**
How to build real-time web application frontends connected directly to backend automation engines (n8n) using webhooks, JSON payloads, and structured AI classification prompts.

**Where does this connect to "AI for Good"?**
GlucoFlow directly supports UN SDG 3 (Target 3.4) by reducing premature non-communicable disease risks through automated early detection while supporting patient mental health and reducing daily monitoring distress through empathetic UI design.
