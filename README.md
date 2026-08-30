# Shamva Innovators

A single Streamlit app that collects student projects from the Shamva Innovators summer program. Visitors open one site, then browse each student’s work from the home gallery or the sidebar.

## Run the app

Python 3.13 or newer is recommended. A local `.venv` may already exist in this folder.

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
streamlit run app.py
```

Then open [http://localhost:8501](http://localhost:8501).

Delma Mandeya’s “Ask Me Anything” box uses OpenAI if you set `OPENAI_API_KEY` in a `.env` file. Without a key, that page still loads and the question box falls back to a static message.

## How to use it

- Home (`/`) is a gallery of every student project.
- The sidebar switches from one project to another.
- You can also go straight to a student by URL, for example `/christine` or `/delma-kaduya`.

## Student projects

| Student | Project | Path |
| --- | --- | --- |
| Christine | Student Resource Platform | `/christine` |
| Crispen | Science quiz game | `/crispen` |
| Daizy | Shamva water schedule | `/daizy` |
| Delma Kaduya | Patient assistant | `/delma-kaduya` |
| Delma Mandeya | Teen pregnancy education hub | `/delma-mandeya` |
| Elisiya | AfyaBot chronic disease assessment | `/elisiya` |
| Kush | Mentors information | `/kush` |
| Nokutenda | Student attendance | `/nokutenda` |
| Nokutenda Kuzanga | Waste awareness | `/nokutenda-kuzanga` |
| Collen | School report system | `/collen` |
| Loveness | Drug abuse awareness | `/loveness` |
| Samaz | Men's anonymous forum | `/samaz` |

## What’s in this repo

- `app.py` — Streamlit hub that registers every page
- `gallery.py` — home gallery
- `students/` — the runnable Streamlit page for each student
- `originals/` — the files students originally submitted, kept as-is
- `requirements.txt` — Python dependencies
