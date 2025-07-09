# 🩺 Diabetes‑Predictor (Flask + scikit‑learn)

A tiny web app that guesses if someone might have diabetes.  
You enter 8 health numbers → the model crunches them → you get **Yes / No**.

## What’s inside?

| Part | What I used |
|------|-------------|
| Data  | Pima Indians Diabetes CSV |
| Model | Random Forest (scikit‑learn) |
| Web   | Flask 🐍 |

I made it as I wanted to make something with ML+Web.

```bash
git clone https://github.com/<your‑user>/diabetes‑predictor.git
cd diabetes‑predictor
python -m venv venv && venv\Scripts\activate  # or source venv/bin/activate
pip install -r requirements.txt
python app.py
