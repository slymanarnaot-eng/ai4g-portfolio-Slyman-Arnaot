**Project title:** BirdWatch NL – AI-Powered Bird Monitoring Assistant
**Team:** Domile Zukaite/ Slyman Arnaot
**Tool we had to use:** Roboflow
**SDG we had to address:** SDG 15 – Life on Land
**What problem does it solve, and for whom?**
Monitoring local bird species can be challenging for people who are interested in nature but lack the experience to identify different birds accurately. Beginners may also struggle to keep organised records of the species they encounter.
BirdWatch NL is designed primarily for beginner birdwatchers, local nature enthusiasts and students observing birds in parks and urban green spaces in the Netherlands.
The project supports SDG 15 (Life on Land) by encouraging biodiversity awareness and making it easier to document local bird observations. It is not intended to replace professional ecological surveys.
**What did you build?**
We developed BirdWatch NL, an interactive web application built with Python and Streamlit and connected to an AI model trained using Roboflow.
Users can upload photographs of birds, and the AI automatically identifies and counts birds from six categories: ducks, geese, swans, crows, pigeons and seagulls. Users can review and correct the predictions, enter an observation date and location, add notes, and save their sightings. Observations are stored in a CSV file that can be downloaded for future reference.
**Link to the live thing (if any)**
Demo video: https://drive.google.com/file/d/1MWeiT3g1r1Km78b3tP1FshlhYvtiyuA6/view?usp=sharing
**Roboflow workflow:** [Insert workflow link if publicly shareable]
The prototype has been tested locally. In one successful test, the AI identified one seagull in an uploaded photograph, and the observation was saved successfully.
The application currently runs locally rather than on a publicly deployed website.
**How do I run it?**
Download or clone this GitHub repository.
Install Python 3.12.
Open a terminal in the project folder.
Install the required dependencies:
py -3.12 -m pip install streamlit pillow inference-sdk
Start the application:
py -3.12 -m streamlit run app.py
Open the local address shown in the terminal, usually http://localhost:8501.
Enter a valid Roboflow API key when prompted.
Upload a bird photograph and select Detect birds with AI.
Review the results, enter the observation details and select Save observation.
**Important: The application requires an internet connection for Roboflow AI inference. API keys should not be uploaded to GitHub.**
**Who did what?**
Domiles contribution: [Describe your actual responsibilities, such as developing the Streamlit website, integrating the Roboflow workflow, testing the AI predictions, and preparing documentation.]
Slymans contribution: [Describe your partner's actual responsibilities, such as image collection, annotation, model training, testing, research, or presentation preparation.]
Collaboration: [Explain briefly which parts you worked on together.]
**Ethical reflection** – what are the risks of your tool? Who could it harm?
One important ethical risk of BirdWatch NL is inaccurate AI identification. If the model incorrectly identifies a species or counts the wrong number of birds, users could save misleading observations. This could become particularly problematic if someone used the collected data for biodiversity research without verifying its accuracy. To reduce this risk, the application clearly warns users that AI predictions may be wrong and allows them to manually correct the counts before saving. Another concern is privacy: photographs uploaded for analysis are sent to Roboflow's cloud service, and location information could potentially reveal sensitive wildlife habitats or nesting sites. Users should avoid entering precise locations of vulnerable species, and future versions should provide clearer privacy guidance. The model may also perform less reliably on unfamiliar species, poor-quality photographs or crowded scenes. Therefore, BirdWatch NL is presented as an educational and observational tool rather than a scientifically validated monitoring system.
Current limitations and future improvements
The working prototype currently supports six bird categories. Although we successfully tested the complete process from photo upload to saved observation, we have not yet established its overall detection accuracy across different environments.
Future improvements could include a larger and more diverse training dataset, more supported species, systematic accuracy testing, better privacy guidance and public deployment of the application.
