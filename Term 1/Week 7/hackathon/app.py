from pathlib import Path
from datetime import date, datetime
import csv
import io
import streamlit as st
from PIL import Image 
from inference_sdk import InferenceHTTPClient, InferenceConfiguration

st.set_page_config(page_title="BirdWatch NL | Local bird observations", page_icon=None, layout="wide")
BASE = Path(__file__).resolve().parent
PHOTOS = BASE / "photos"
DATA = BASE / "observations.csv"
SPECIES = ["Duck", "Goose", "Swan", "Crow", "Pigeon", "Seagull"]

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Libre+Baskerville:wght@400;700&display=swap');
html,body,[class*="css"],[data-testid="stApp"] {font-family:'DM Sans',sans-serif;}
.stApp {background:#f6f4ec;color:#193c30;}
.block-container {max-width:1100px;padding-top:1.6rem;padding-bottom:5rem;}
h1,h2,h3 {font-family:'Libre Baskerville',Georgia,serif!important;color:#193c30!important;letter-spacing:-.035em;}
h1 {font-size:clamp(2.5rem,5vw,4.6rem)!important;line-height:1.12!important;}
h2 {font-size:1.75rem!important;margin-top:1.5rem!important;}
p {line-height:1.7;}
[data-testid="stHeader"] {background:transparent;}
[data-testid="stFileUploader"] {background:#fff;border:1px solid #d8dfd1;border-radius:14px;padding:12px;}
div.stButton>button[kind="primary"],div.stDownloadButton>button {background:#245a43!important;color:#fff!important;border:0!important;border-radius:8px!important;padding:.7rem 1.2rem!important;}
div[data-testid="stMetric"] {background:#fff;border:1px solid #e0e4d9;padding:16px;border-radius:12px;}
.hero-note {font-size:.75rem;letter-spacing:.19em;text-transform:uppercase;font-weight:700;color:#6b7b61;margin-bottom:10px;}
.intro {font-size:1.12rem;max-width:650px;color:#4e6759;}
.divider {height:1px;background:#d7dfd3;margin:30px 0;}
.species-note {font-size:.86rem;color:#64796b;margin-top:4px;}
.small-note {color:#63766b;font-size:.9rem;}
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="hero-note">A community birdwatching project · The Netherlands</div>', unsafe_allow_html=True)
st.title("A closer look at the birds around us.")
st.markdown('<p class="intro">Meet BirdWatch NL — a place to photograph, identify and record the birds sharing our parks, ponds and neighbourhoods.</p>', unsafe_allow_html=True)

hero = PHOTOS / "ducks_in_park.jpg"
if hero.exists():
    st.image(str(hero), use_container_width=True)
    st.caption("Our own field photography · Mallard ducks in a local park")

st.markdown('<div class="divider"></div>', unsafe_allow_html=True)
st.markdown('<div class="hero-note">01 / Meet the birds</div>', unsafe_allow_html=True)
st.header("Who are we looking for?")
st.write("Our project follows five familiar bird groups found in Dutch parks, ponds and neighbourhoods. These photographs come from our own field collection.")

bird_cards = [
    ("Ducks", "mallard_on_water.jpg", "Look for ducks on ponds, canals and park lakes."),
    ("Geese", "geese.jpg", "Geese often graze beside lakes and open grassland."),
    ("Swans", "swan_on_lake.jpg", "Swans are large waterbirds with long necks."),
    ("Crows", "crow.jpg", "Crows are intelligent black birds often seen in trees and parks."),
    ("Pigeons", "pigeons.jpg", "Pigeons are familiar visitors to city streets and parks."),
("Seagulls", "seagull.jfif", "Seagulls are often seen around Dutch parks, lakes and waterways."),
]
for start in (0, 3):
    columns = st.columns(3)
    for column, (name, filename, description) in zip(columns, bird_cards[start:start + 3]):
        with column:
            photo = PHOTOS / filename
            if photo.exists():
                st.image(str(photo), use_container_width=True)
            st.subheader(name)
            st.markdown(f'<div class="species-note">{description}</div>', unsafe_allow_html=True)

st.markdown('<div class="divider"></div>',unsafe_allow_html=True)
st.markdown('<div class="hero-note">02 / Your observation</div>',unsafe_allow_html=True)
st.header("Record a bird sighting")
st.write("Upload a photo, check what you can see, and save your observation. Automatic Roboflow counting will be connected after our model is trained.")
uploaded=st.file_uploader("Choose a bird photograph",type=["jpg","jpeg","png"])
if uploaded: 
   st.write("AI bird detection is starting...")
    uploaded.seek(0)
    image_bytes = uploaded.getvalue()
    image_path = BASE / "bird_to_detect.jpg"
    image_path.write_bytes(image_bytes)
    st.write("Photo ready for AI analysis.")
    try:
        st.image(Image.open(uploaded),caption="Your observation photograph",use_container_width=True)
    except Exception:
        st.error("We couldn't open that photo. Please try a JPG or PNG.")

st.info("Manual review mode: these are counts you enter yourself, not AI predictions yet.")
counts={}
cols=st.columns(6)
for i,species in enumerate(SPECIES):
    with cols[i]:
        counts[species]=st.number_input(species,min_value=0,step=1,value=0,key="count_"+species)
total=sum(counts.values())
st.metric("Total birds observed",total)
st.caption("Waterbirds: ducks, geese and swans · Other birds: crows and pigeons")

st.markdown('<div class="divider"></div>',unsafe_allow_html=True)
st.markdown('<div class="hero-note">03 / Field notes</div>',unsafe_allow_html=True)
st.header("Save your sighting")
left,right=st.columns(2)
with left:
    observation_date=st.date_input("Date of observation",value=date.today())
with right:
    location=st.text_input("Location (e.g. park or town)")
notes=st.text_area("Notes (optional)",placeholder="Weather, habitat, anything interesting...")
if st.button("Save observation",type="primary"):
    if not location.strip():
        st.warning("Please enter a location before saving.")
    elif uploaded is None:
        st.warning("Please upload a bird photograph before saving.")
    else:
        DATA.parent.mkdir(parents=True,exist_ok=True)
        fields=["saved_at","observation_date","location","photo_filename"]+[s.lower() for s in SPECIES]+["total","notes"]
        row={"saved_at":datetime.now().isoformat(timespec="seconds"),"observation_date":str(observation_date),"location":location.strip(),"photo_filename":uploaded.name,"total":total,"notes":notes}
        row.update({s.lower():counts[s] for s in SPECIES})
        is_new=not DATA.exists()
        with DATA.open("a",newline="",encoding="utf-8") as f:
            writer=csv.DictWriter(f,fieldnames=fields)
            if is_new: writer.writeheader()
            writer.writerow(row)
        st.success("Observation saved to observations.csv in your app folder!")
        st.caption("The CSV records the photo filename, not a copy of the uploaded image. Keep your original photo.")

if DATA.exists():
    st.markdown("### Your saved observations")
    with DATA.open("r",encoding="utf-8",newline="") as f:
        content=f.read()
    st.download_button("Download observation records (CSV)",content,file_name="birdwatch_observations.csv",mime="text/csv")
    with DATA.open("r",encoding="utf-8",newline="") as f:
        rows=list(csv.DictReader(f))
    if rows:
        st.dataframe(list(reversed(rows[-20:])),use_container_width=True,hide_index=True)

st.markdown('<div class="divider"></div>',unsafe_allow_html=True)
st.markdown('<p class="small-note">BirdWatch NL · Student prototype supporting awareness of SDG 15: Life on Land. Photo observations are not official population surveys. Always verify bird counts.</p>',unsafe_allow_html=True)
