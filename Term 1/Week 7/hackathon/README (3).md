# BirdWatch NL — AI-Powered Bird Identification and Monitoring Assistant 

**Hackathon:** AI for Good — Hackathon 7: Eyes on Earth  
**Team:** Domile Zukaite/ Slyman Arnaot
**Required AI tool:** Roboflow  
**Application:** Python and Streamlit  
**SDG:** 15 — Life on Land, particularly Targets 15.1 (freshwater ecosystems) and 15.5 (biodiversity loss)

## What problem does it solve, and for whom?

BirdWatch NL addresses a small but practical problem for **beginner birdwatchers taking phone photos beside Dutch canals and in parks**: recognising which broad bird groups are visible, counting them, and keeping a dated, organised record. Birds photographed at a distance, partly hidden or against reflections can be difficult to recognise and count. The need is a **research-informed design hypothesis**, not yet validated through interviews or usability testing.

The wider environmental context matters, but bird trends are mixed. According to the *Compendium voor de Leefomgeving* (2026), among 184 Dutch breeding-bird species, 82 declined and 88 increased between 1990 and 2025. In a separate farmland-bird indicator, 21 of 27 characteristic species declined between 1990 and 2024. Sovon's structured waterbird counts involve almost 2,000 volunteers and professionals. These figures illustrate the importance of careful observation; they do **not** mean BirdWatch NL produces scientific monitoring data.

**Primary user:** a beginner who takes bird photos and wants a first AI suggestion plus an easy personal observation log. **Secondary users:** students, teachers, families and nature-education groups. **Not intended for:** professional survey teams, rare-species verification or official population estimates.

## What did you build?

We built a working local **Streamlit** web app connected to a **custom Roboflow object-detection workflow**. A user uploads a JPG/PNG bird photo, clicks **Detect birds with AI**, reviews and edits the predicted counts, enters a date, general location and optional notes, and saves an observation to a downloadable CSV file.

The model uses six **broad bird groups**, not exact species: **duck, goose, swan, crow, pigeon and seagull**. Unsupported birds, such as a Eurasian coot, should not be forced into one of those labels. The current app allows users to correct counts, but does not provide a full bounding-box editing interface.

**Why Roboflow is essential:** it supplies the automatic bird-detection predictions; without it, the app would only be a manual logging form. Streamlit handles the user interface and saves the reviewed record. Our project used a 300-image labelled dataset for the custom model; this does not by itself establish accuracy.

## Evidence that it works

- **Demo video:** https://drive.google.com/file/d/1MWeiT3g1r1Km78b3tP1FshlhYvtiyuA6/view?usp=sharing
- **Roboflow workflow:**https://app.roboflow.com/gumguard-ai/solutions/chat?workflowUrl=waterbird-monitoring-assi-vwaterbird-monitoring-assi-2-rfdetr-small-t1-logic

In a successful end-to-end local test on **29 October 2026**, the AI detected **one seagull** in an uploaded photo. The result was reviewed, saved with a date and location, and appeared in the observations table; CSV download was available. **One successful test is not evidence of overall accuracy.**

## How do I run it?

1. Install **Python 3.12** and download/clone this repository.
2. Open a terminal in the project directory.
3. Install dependencies:

   ```bash
   py -3.12 -m pip install streamlit pillow inference-sdk
   ```

4. Start the app:

   ```bash
   py -3.12 -m streamlit run app.py
   ```

5. Open the local URL printed in the terminal (usually `http://localhost:8501`).
6. Enter your own **Roboflow API key** in the app when requested. Internet access is needed for inference.
7. Upload a bird photo, run detection, review the counts, and save an observation.

**Security:** Never commit real API keys, secrets, personal photographs or private observation data. The CSV saves the uploaded **filename**, not a copy of the photo.

## Why this approach instead of an existing app?

**ObsIdentify** already suggests identifications from nature photos, and **Merlin/eBird Photo ID** already offers bird detection and identification. BirdWatch NL does **not** claim to invent bird recognition. Its narrower, testable idea is whether a custom six-group detector combined with an **editable count and simple personal CSV log** helps beginners. We have not yet shown that it is easier or faster than existing tools.

## Who did what?

- **Domile:** Developed the BirdWatch NL web application using Python and Streamlit.

Worked with Roboflow to train and integrate the custom bird detection model.

Connected the AI model to the application to enable automatic bird identification and counting.

Implemented the observation system, including manual count corrections, location and date inputs, and CSV storage.

Tested and troubleshot the application to ensure the complete process worked, from uploading a photograph to saving an observation.
- **Slyman:**
- Collected bird photographs for the dataset used to train the AI model.

Created the hackathon presentation, explaining the problem, solution, and connection to SDG 15.

Prepared the GitHub README documenting the project, its functionality, and ethical considerations.


## Ethical reflection

BirdWatch NL may misidentify birds, miss individuals, count reflections or assign unsupported birds to the wrong group. A plausible-looking prediction could mislead a beginner and contaminate a saved record, especially if it were mistaken for official monitoring data. **Already implemented:** the app warns that AI predictions may be wrong and lets users edit counts before saving. **Next steps:** evaluate unseen photos by group, measure false detections and counting errors, and clearly explain unsupported categories (including coots). Photos may accidentally contain identifiable people or sensitive nesting locations; users should avoid photographing people without permission, use general locations, and never publish precise nest sites. Uploaded photos are sent to Roboflow for cloud inference, so users should understand that the image leaves their device. API keys must remain private. Wildlife should not be disturbed to obtain photographs, and training images must be self-collected or used with permission.

## Limitations and next tests

The six labels are broad groups, not species-level identifications. No comprehensive test-set metrics or beginner usability results have yet been documented. We would next test unseen images across distances, angles, backgrounds and group sizes; report precision/recall by group and counting error; and run a small **3–5-person beginner usability study**, comparing time, accuracy, corrections and confidence with and without BirdWatch NL. A personal photo log is **not** equivalent to a standardised Sovon survey or a measured SDG impact.

## Desk research and references

The accompanying **BirdWatch NL Desk Research** explains the problem, SDG 15 connection, intended users, existing solutions, risks and proposed evaluation. Key references:

- Compendium voor de Leefomgeving (2026a). [Fauna van het agrarisch gebied, 1990–2024](https://www.clo.nl/indicatoren/nl158010-fauna-van-het-agrarisch-gebied-1990-2024).
- Compendium voor de Leefomgeving (2026b). [Trend van broedvogels, 1990–2025](https://www.clo.nl/indicatoren/nl138121-trend-van-broedvogels-1990-2025).
- Sovon (n.d.). [Waterbird counts](https://www.sovon.nl/tellen/telprojecten/watervogeltelling).
- Sovon (2024). [State of Birds in the Netherlands](https://stats.sovon.nl/static/publicaties/Vogelbalans-2024_EN_LR.pdf).
- United Nations (n.d.). [Goal 15](https://sdgs.un.org/goals/goal15).
- eBird Support (2025). [Merlin Photo ID](https://support.ebird.org/en/support/solutions/articles/48001271537-merlin-photo-id-in-manage-media).
- Observation International (2026). *ObsIdentify* mobile application.

