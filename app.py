import streamlit as st

# ----------------------------------------------------------------------------
# PAGE CONFIG
# ----------------------------------------------------------------------------
st.set_page_config(
    layout="wide",
    page_title="practice-lab",
    page_icon=None,
)

# ----------------------------------------------------------------------------
# DATA
# ----------------------------------------------------------------------------
projects_data = {
    "caesar-cipher": {
        "title": "caesar-cipher",
        "tagline": "Shift-based text encoder/decoder",
        "language": "Python",
        "lines": 9,
        "commit": "fix: stub out shift logic before case handling",
        "commit_hash": "a3f29c1",
        "topics": ["strings", "loops", "modulo"],
        "description": "Encodes and decodes messages by shifting letters along the alphabet by a fixed key.",
        "concepts": "String indexing, loop-based traversal, and wrap-around arithmetic using modulo.",
        "limitations": [
            {"label": "case-handling", "kind": "bug", "detail": "Capital letters are skipped or break the index lookup entirely."},
            {"label": "input-safety", "kind": "bug", "detail": "Spaces, punctuation, and digits crash the index calculation."},
            {"label": "weak-crypto", "kind": "design", "detail": "Breakable in minutes with basic letter-frequency analysis."},
        ],
        "challenge": "Rewrite the loop so it handles upper- and lowercase letters and passes spaces through untouched.",
        "code": """alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar_cipher(text, shift, direction):
    cipher_text = ""
    for letter in text:
        # Fails on uppercase letters or spaces
        shifted_position = (alphabets.index(letter) + shift) % 26
        cipher_text += alphabets[shifted_position]
    return cipher_text""",
    },
    "secret-auction": {
        "title": "secret-auction",
        "tagline": "Blind bidding console",
        "language": "Python",
        "lines": 11,
        "commit": "feat: store bids in a dict keyed by bidder name",
        "commit_hash": "9e7d014",
        "topics": ["dictionaries", "io", "while-loops"],
        "description": "Lets multiple bidders enter sealed offers, then reveals the highest bid.",
        "concepts": "Dictionary key-value storage, input loops, and max-value lookup.",
        "limitations": [
            {"label": "no-persistence", "kind": "design", "detail": "Bids live only in memory — closing the program erases the ledger."},
            {"label": "tie-handling", "kind": "bug", "detail": "Equal top bids resolve silently to whichever was entered first."},
        ],
        "challenge": "Detect duplicate top bids and prompt only those bidders to re-bid.",
        "code": """bid_records = {}

while True:
    name = input("Enter name: ").strip().lower()
    if name == 'exit':
        break
    bid = int(input("Enter bid: $"))
    bid_records[name] = bid

# Ties resolve to the first match only
winner = max(bid_records, key=bid_records.get)
print(f"Winner is {winner} with ${bid_records[winner]}")""",
    },
    "smart-calculator": {
        "title": "smart-calculator",
        "tagline": "Command-line arithmetic loop",
        "language": "Python",
        "lines": 9,
        "commit": "refactor: split add/divide into standalone functions",
        "commit_hash": "5b18a06",
        "topics": ["functions", "control-flow", "cli"],
        "description": "Runs a continuous terminal calculator for basic arithmetic operations.",
        "concepts": "Function calls, conditional branching, and a persistent input loop.",
        "limitations": [
            {"label": "type-safety", "kind": "bug", "detail": "Non-numeric input crashes the program on conversion."},
            {"label": "div-by-zero", "kind": "bug", "detail": "No guard exists before the divide operation runs."},
        ],
        "challenge": "Wrap input parsing and division in error handling so bad input warns instead of crashing.",
        "code": """def add(a, b): return a + b
def divide(a, b): return a / b  # No zero-division guard

while True:
    choice = int(input("1-Add, 2-Divide, 3-Exit: "))
    if choice == 3: break
    n1 = float(input("Num 1: "))
    n2 = float(input("Num 2: "))  # Crashes on non-numeric input
    print(add(n1, n2) if choice == 1 else divide(n1, n2))""",
    },
}

ALL_FILES = list(projects_data.keys())

# ----------------------------------------------------------------------------
# THEME
# ----------------------------------------------------------------------------
if "theme" not in st.session_state:
    st.session_state.theme = "light"

if "page" not in st.session_state:
    st.session_state.page = "home"

THEMES = {
    "light": {
        "canvas": "#FFFFFF",
        "canvas-inset": "#F6F8FA",
        "canvas-raised": "#FFFFFF",
        "border": "#D1D9E0",
        "border-muted": "#E7EBEF",
        "text": "#1F2328",
        "text-muted": "#59636E",
        "text-faint": "#818B98",
        "accent": "#0969DA",
        "accent-soft": "#DDF1FF",
        "bug": "#CF222E",
        "bug-soft": "#FFEBE9",
        "design": "#9A6700",
        "design-soft": "#FFF8C5",
        "good": "#1A7F37",
        "good-soft": "#DAFBE1",
        "purple": "#8250DF",
        "purple-soft": "#FBEFFF",
        "sidebar": "#F6F8FA",
        "topbar": "#24292F",
        "topbar-text": "#FFFFFF",
        "shadow": "rgba(31,35,40,0.06)",
        "shadow-strong": "rgba(31,35,40,0.12)",
        "lang-py": "#3572A5",
    },
    "dark": {
        "canvas": "#0D1117",
        "canvas-inset": "#161B22",
        "canvas-raised": "#161B22",
        "border": "#30363D",
        "border-muted": "#21262D",
        "text": "#E6EDF3",
        "text-muted": "#9198A1",
        "text-faint": "#6E7681",
        "accent": "#4493F8",
        "accent-soft": "#0C2D6B",
        "bug": "#F85149",
        "bug-soft": "#3D1418",
        "design": "#D29922",
        "design-soft": "#3B2D04",
        "good": "#3FB950",
        "good-soft": "#0F2A1A",
        "purple": "#A371F7",
        "purple-soft": "#2B1D40",
        "sidebar": "#0D1117",
        "topbar": "#010409",
        "topbar-text": "#E6EDF3",
        "shadow": "rgba(0,0,0,0.35)",
        "shadow-strong": "rgba(0,0,0,0.55)",
        "lang-py": "#3572A5",
    },
}

t = THEMES[st.session_state.theme]

# ----------------------------------------------------------------------------
# STYLE
# ----------------------------------------------------------------------------
st.markdown(
    f"""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500;600&display=swap');

        html, body, [class*="css"] {{
            font-family: 'Inter', -apple-system, sans-serif;
        }}

        .stApp {{
            background-color: {t['canvas']} !important;
        }}

        [data-testid="stHeader"] {{
            background-color: {t['canvas']} !important;
        }}

        [data-testid="stSidebar"] {{
            background-color: {t['sidebar']} !important;
            border-right: 1px solid {t['border']};
        }}

        [data-testid="stMainBlockContainer"] {{
            padding-top: 1.4rem;
            max-width: 1280px;
        }}

        h1, h2, h3, h4, p, span, div, label {{
            color: {t['text']};
        }}

        /* ================= TOP BAR ================= */
        .topbar {{
            background: {t['topbar']};
            color: {t['topbar-text']};
            padding: 0.7rem 1.2rem;
            display: flex;
            align-items: center;
            gap: 0.6rem;
            font-size: 0.92rem;
            font-weight: 600;
            border-radius: 8px;
            margin-bottom: 1.1rem;
            box-shadow: 0 1px 0 {t['shadow']};
        }}

        .topbar .mark {{
            width: 22px;
            height: 22px;
            border-radius: 6px;
            background: linear-gradient(135deg, {t['accent']}, {t['purple']});
            display: inline-block;
        }}

        .topbar .crumb-sep {{ color: {t['text-faint']}; font-weight: 400; }}
        .topbar .crumb-light {{ color: {t['topbar-text']}; opacity: 0.6; font-weight: 400; }}

        /* ================= REPO HEADER ================= */
        .repo-header {{
            border: 1px solid {t['border']};
            border-radius: 10px;
            padding: 1.1rem 1.3rem;
            margin-bottom: 1rem;
            background: {t['canvas-raised']};
            box-shadow: 0 1px 2px {t['shadow']}, 0 6px 16px {t['shadow']};
            display: flex;
            justify-content: space-between;
            align-items: flex-start;
            gap: 1rem;
        }}

        .repo-name {{
            font-size: 1.45rem;
            font-weight: 600;
            color: {t['text']};
            display: flex;
            align-items: center;
            gap: 0.5rem;
        }}

        .repo-name .owner {{ color: {t['text-muted']}; font-weight: 400; }}

        .visibility-pill {{
            font-size: 0.68rem;
            font-weight: 600;
            border: 1px solid {t['border']};
            border-radius: 999px;
            padding: 0.08rem 0.55rem;
            color: {t['text-muted']};
        }}

        .repo-tagline {{
            color: {t['text-muted']};
            font-size: 0.9rem;
            margin-top: 0.3rem;
        }}

        .topic-row {{
            margin-top: 0.7rem;
            display: flex;
            gap: 0.4rem;
            flex-wrap: wrap;
        }}

        .topic-pill {{
            font-size: 0.72rem;
            font-weight: 500;
            background: {t['accent-soft']};
            color: {t['accent']};
            border-radius: 999px;
            padding: 0.12rem 0.65rem;
        }}

        .stat-pills {{
            display: flex;
            gap: 0.5rem;
            flex-shrink: 0;
        }}

        .stat-pill {{
            border: 1px solid {t['border']};
            border-radius: 6px;
            padding: 0.32rem 0.7rem;
            font-size: 0.78rem;
            font-weight: 600;
            color: {t['text']};
            background: {t['canvas-inset']};
            text-align: center;
            box-shadow: 0 1px 0 {t['shadow']};
        }}

        .stat-pill .num {{ display: block; font-size: 0.95rem; }}
        .stat-pill .lbl {{ display: block; font-size: 0.65rem; color: {t['text-muted']}; font-weight: 500; margin-top: 0.1rem; }}

        /* ================= TAB STRIP ================= */
        .tab-strip {{
            display: flex;
            gap: 1.5rem;
            border-bottom: 1px solid {t['border']};
            margin-bottom: 1.1rem;
            font-size: 0.88rem;
        }}

        .tab-item {{
            padding-bottom: 0.65rem;
            color: {t['text-muted']};
            font-weight: 500;
        }}

        .tab-item.active {{
            color: {t['text']};
            border-bottom: 2px solid {t['accent']};
            font-weight: 600;
        }}

        .tab-item .count {{
            background: {t['canvas-inset']};
            border-radius: 999px;
            padding: 0.04rem 0.45rem;
            font-size: 0.72rem;
            margin-left: 0.3rem;
            color: {t['text-muted']};
        }}

        /* ================= COMMIT BAR ================= */
        .commit-bar {{
            display: flex;
            align-items: center;
            gap: 0.6rem;
            background: {t['canvas-inset']};
            border: 1px solid {t['border']};
            border-bottom: none;
            border-radius: 10px 10px 0 0;
            padding: 0.65rem 1rem;
            font-size: 0.82rem;
            box-shadow: inset 0 1px 0 {t['shadow']};
        }}

        .commit-avatar {{
            width: 20px;
            height: 20px;
            border-radius: 50%;
            background: linear-gradient(135deg, {t['purple']}, {t['accent']});
            flex-shrink: 0;
        }}

        .commit-msg {{ color: {t['text']}; font-weight: 600; flex: 1; }}
        .commit-hash {{
            font-family: 'JetBrains Mono', monospace;
            color: {t['text-muted']};
            background: {t['canvas']};
            border: 1px solid {t['border']};
            border-radius: 5px;
            padding: 0.08rem 0.4rem;
            font-size: 0.74rem;
        }}

        /* ================= FILE TREE TABLE ================= */
        .file-table {{
            border: 1px solid {t['border']};
            border-top: none;
            border-radius: 0 0 10px 10px;
            overflow: hidden;
            margin-bottom: 1.5rem;
            box-shadow: 0 1px 2px {t['shadow']}, 0 8px 18px {t['shadow']};
        }}

        .file-row {{
            display: flex;
            align-items: center;
            gap: 0.6rem;
            padding: 0.55rem 1rem;
            border-bottom: 1px solid {t['border-muted']};
            font-size: 0.85rem;
            background: {t['canvas']};
        }}

        .file-row:last-child {{ border-bottom: none; }}
        .file-row .ficon {{ width: 16px; height: 16px; flex-shrink: 0; color: {t['lang-py']}; }}
        .file-row .fname {{ color: {t['accent']}; font-weight: 500; flex: 1; }}
        .file-row .fmsg {{ color: {t['text-muted']}; flex: 2; }}
        .file-row .ftime {{ color: {t['text-faint']}; font-size: 0.78rem; white-space: nowrap; }}

        /* ================= FILE PANE (code viewer) ================= */
        .file-pane-head {{
            background: {t['canvas-inset']};
            border: 1px solid {t['border']};
            border-bottom: none;
            border-radius: 10px 10px 0 0;
            padding: 0.6rem 1rem;
            font-family: 'JetBrains Mono', monospace;
            font-size: 0.82rem;
            color: {t['text-muted']};
            display: flex;
            justify-content: space-between;
            align-items: center;
        }}

        .file-pane-head .fname {{ color: {t['text']}; font-weight: 600; }}

        .file-pane-wrap {{
            border: 1px solid {t['border']};
            border-top: none;
            border-radius: 0 0 10px 10px;
            overflow: hidden;
            margin-bottom: 1.5rem;
            box-shadow: 0 1px 2px {t['shadow']}, 0 8px 18px {t['shadow']};
        }}

        .file-pane-wrap [data-testid="stCodeBlock"] {{
            border-radius: 0 !important;
            margin: 0 !important;
        }}

        /* ================= SECTION HEAD ================= */
        .sec-head {{
            font-size: 0.78rem;
            font-weight: 600;
            text-transform: uppercase;
            letter-spacing: 0.04em;
            color: {t['text-muted']};
            margin: 1.6rem 0 0.7rem 0;
            display: flex;
            align-items: center;
            gap: 0.5rem;
        }}

        .sec-head::after {{ content: ''; flex: 1; height: 1px; background: {t['border-muted']}; }}

        /* ================= ISSUE ROWS ================= */
        .flaw-row {{
            display: flex;
            align-items: center;
            gap: 0.7rem;
            padding: 0.65rem 0.9rem;
            border: 1px solid {t['border']};
            border-radius: 8px;
            margin-bottom: 0.5rem;
            background: {t['canvas-raised']};
            box-shadow: 0 1px 2px {t['shadow']};
        }}

        .chip {{
            font-family: 'JetBrains Mono', monospace;
            font-size: 0.72rem;
            font-weight: 600;
            padding: 0.15rem 0.6rem;
            border-radius: 999px;
            white-space: nowrap;
        }}

        .chip-bug {{ background: {t['bug-soft']}; color: {t['bug']}; }}
        .chip-design {{ background: {t['design-soft']}; color: {t['design']}; }}
        .flaw-detail {{ font-size: 0.88rem; color: {t['text']}; }}

        /* ================= TASK CARD ================= */
        .task-card {{
            border: 1px solid {t['accent']};
            border-radius: 8px;
            padding: 1rem 1.2rem;
            background: {t['accent-soft']};
            box-shadow: 0 1px 2px {t['shadow']};
        }}

        .task-label {{
            font-family: 'JetBrains Mono', monospace;
            font-size: 0.72rem;
            font-weight: 700;
            text-transform: uppercase;
            letter-spacing: 0.05em;
            color: {t['accent']};
            display: block;
            margin-bottom: 0.4rem;
        }}

        .task-card p {{ color: {t['text']}; font-size: 0.92rem; margin: 0; }}

        /* ================= BUTTONS ================= */
        .btn-row {{ display: flex; gap: 0.6rem; margin-top: 1.2rem; }}

        .btn {{
            border: 1px solid {t['border']};
            border-radius: 6px;
            padding: 0.45rem 0.95rem;
            font-size: 0.85rem;
            font-weight: 500;
            color: {t['text']};
            text-decoration: none;
            background: {t['canvas-inset']};
            box-shadow: 0 1px 0 {t['shadow']};
        }}

        .btn-primary {{ background: {t['good']}; border-color: {t['good']}; color: #FFFFFF; }}

        /* ================= ABOUT PANEL (right rail) ================= */
        .about-panel {{
            border: 1px solid {t['border']};
            border-radius: 10px;
            padding: 1rem 1.1rem;
            background: {t['canvas-raised']};
            box-shadow: 0 1px 2px {t['shadow']}, 0 6px 16px {t['shadow']};
            margin-bottom: 1.1rem;
        }}

        .about-title {{
            font-size: 0.95rem;
            font-weight: 600;
            margin-bottom: 0.5rem;
        }}

        .about-row {{
            display: flex;
            justify-content: space-between;
            font-size: 0.83rem;
            color: {t['text-muted']};
            padding: 0.35rem 0;
            border-bottom: 1px solid {t['border-muted']};
        }}

        .about-row:last-child {{ border-bottom: none; }}
        .about-row .val {{ color: {t['text']}; font-weight: 500; }}

        .lang-bar {{
            display: flex;
            height: 7px;
            border-radius: 999px;
            overflow: hidden;
            margin: 0.6rem 0 0.4rem 0;
        }}

        .lang-seg-py {{ background: {t['lang-py']}; }}
        .lang-seg-md {{ background: {t['accent']}; }}

        .lang-legend {{
            display: flex;
            gap: 0.9rem;
            font-size: 0.78rem;
            color: {t['text-muted']};
            flex-wrap: wrap;
        }}

        .lang-dot {{ width: 8px; height: 8px; border-radius: 50%; display: inline-block; margin-right: 0.3rem; }}

        /* ================= MENTOR PANEL ================= */
        .panel {{
            border: 1px solid {t['border']};
            border-radius: 10px;
            padding: 0.9rem 1rem;
            background: {t['canvas-raised']};
            box-shadow: 0 1px 2px {t['shadow']}, 0 6px 16px {t['shadow']};
            margin-bottom: 0.9rem;
        }}

        .panel-title {{ font-size: 0.95rem; font-weight: 600; color: {t['text']}; }}
        .panel-sub {{ font-size: 0.82rem; color: {t['text-muted']}; margin-top: 0.15rem; }}

        /* ================= HOME / LANDING PAGE ================= */
        .hero {{
            border: 1px solid {t['border']};
            border-radius: 12px;
            padding: 2.6rem 2.4rem;
            margin-bottom: 1.4rem;
            background: linear-gradient(165deg, {t['canvas-raised']} 0%, {t['canvas-inset']} 100%);
            box-shadow: 0 1px 2px {t['shadow']}, 0 10px 24px {t['shadow']};
        }}

        .hero-kicker {{
            font-family: 'JetBrains Mono', monospace;
            font-size: 0.78rem;
            font-weight: 600;
            letter-spacing: 0.06em;
            text-transform: uppercase;
            color: {t['accent']};
            margin-bottom: 0.8rem;
            display: flex;
            align-items: center;
            gap: 0.5rem;
        }}

        .hero-kicker .mark {{
            width: 10px;
            height: 10px;
            border-radius: 3px;
            background: linear-gradient(135deg, {t['accent']}, {t['purple']});
            display: inline-block;
        }}

        .hero-title {{
            font-size: 2.5rem;
            font-weight: 700;
            line-height: 1.12;
            margin-bottom: 0.8rem;
            color: {t['text']};
            letter-spacing: -0.01em;
        }}

        .hero-title .accent-word {{ color: {t['accent']}; }}

        .hero-sub {{
            font-size: 1.05rem;
            color: {t['text-muted']};
            max-width: 640px;
            line-height: 1.55;
            margin-bottom: 1.5rem;
        }}

        .hero-stats {{
            display: flex;
            gap: 1.8rem;
            margin-top: 1.6rem;
            padding-top: 1.4rem;
            border-top: 1px solid {t['border-muted']};
        }}

        .hero-stat .num {{
            font-size: 1.4rem;
            font-weight: 700;
            color: {t['text']};
            font-family: 'JetBrains Mono', monospace;
        }}

        .hero-stat .lbl {{
            font-size: 0.78rem;
            color: {t['text-muted']};
            margin-top: 0.1rem;
        }}

        .how-card {{
            border: 1px solid {t['border']};
            border-radius: 10px;
            padding: 1.3rem 1.3rem;
            background: {t['canvas-raised']};
            box-shadow: 0 1px 2px {t['shadow']};
            height: 100%;
        }}

        .how-step {{
            font-family: 'JetBrains Mono', monospace;
            font-size: 0.72rem;
            font-weight: 700;
            color: {t['accent']};
            background: {t['accent-soft']};
            border-radius: 999px;
            width: 26px;
            height: 26px;
            display: flex;
            align-items: center;
            justify-content: center;
            margin-bottom: 0.7rem;
        }}

        .how-title {{
            font-size: 1rem;
            font-weight: 600;
            margin-bottom: 0.4rem;
            color: {t['text']};
        }}

        .how-body {{
            font-size: 0.86rem;
            color: {t['text-muted']};
            line-height: 1.5;
        }}

        .preview-card {{
            border: 1px solid {t['border']};
            border-radius: 10px;
            padding: 1.1rem 1.2rem;
            background: {t['canvas-raised']};
            box-shadow: 0 1px 2px {t['shadow']};
            height: 100%;
        }}

        .preview-card .pname {{
            font-weight: 600;
            color: {t['accent']};
            font-size: 0.95rem;
            margin-bottom: 0.25rem;
        }}

        .preview-card .ptag {{
            font-size: 0.82rem;
            color: {t['text-muted']};
            margin-bottom: 0.7rem;
        }}

        .preview-card .pmeta {{
            display: flex;
            gap: 0.7rem;
            font-size: 0.74rem;
            color: {t['text-faint']};
        }}

        .preview-card .pmeta .bugcount {{ color: {t['bug']}; font-weight: 600; }}

        /* ================= STREAMLIT OVERRIDES ================= */
        [data-testid="stExpander"] {{
            border: 1px solid {t['border']} !important;
            background: {t['canvas']} !important;
            border-radius: 8px !important;
        }}

        .stCodeBlock {{ border: none !important; }}

        .stChatMessage {{
            background: {t['canvas-inset']} !important;
            border: 1px solid {t['border']} !important;
            border-radius: 8px !important;
        }}

        [data-testid="stCaptionContainer"] {{ color: {t['text-muted']} !important; }}
        ::placeholder {{ color: {t['text-faint']} !important; }}
        hr {{ border-color: {t['border-muted']} !important; }}
    </style>
    """,
    unsafe_allow_html=True,
)

# ----------------------------------------------------------------------------
# SIDEBAR — file tree + theme toggle
# ----------------------------------------------------------------------------
with st.sidebar:
    st.markdown(
        '<div style="font-size:0.95rem;font-weight:700;margin-bottom:0.2rem;">practice-lab</div>'
        '<div style="font-size:0.78rem;color:%s;margin-bottom:1rem;">Public repository</div>' % t["text-muted"],
        unsafe_allow_html=True,
    )

    nav_choice = st.radio(
        "Navigate",
        ["Home", "Browse projects"],
        label_visibility="collapsed",
        index=0 if st.session_state.page == "home" else 1,
    )
    new_page = "home" if nav_choice == "Home" else "repo"
    if new_page != st.session_state.page:
        st.session_state.page = new_page
        st.rerun()

    st.markdown("---")

    st.markdown(
        '<div style="font-size:0.72rem;font-weight:600;text-transform:uppercase;'
        'letter-spacing:0.05em;color:%s;margin-bottom:0.5rem;">Files</div>' % t["text-faint"],
        unsafe_allow_html=True,
    )

    selected_option = st.radio(
        "Files",
        ALL_FILES,
        label_visibility="collapsed",
        format_func=lambda x: f"{x}.py",
    )
    if st.session_state.page == "home" and selected_option:
        pass  # selection still tracked; switching to Browse will show it

    st.markdown("---")
    theme_choice = st.radio("Theme", ["light", "dark"], index=0 if st.session_state.theme == "light" else 1, horizontal=True)
    if theme_choice != st.session_state.theme:
        st.session_state.theme = theme_choice
        st.rerun()

current_project = projects_data[selected_option]
other_files = [f for f in ALL_FILES if f != selected_option]

if st.session_state.page == "home":
    total_files = len(ALL_FILES)
    total_issues_home = sum(len(p["limitations"]) for p in projects_data.values())
    total_lines_home = sum(p["lines"] for p in projects_data.values())

    st.markdown(
        f"""
        <div class="hero">
            <div class="hero-kicker"><span class="mark"></span>practice-lab</div>
            <div class="hero-title">Read real code.<br>Find what's <span class="accent-word">broken</span>.<br>Fix it yourself.</div>
            <div class="hero-sub">
                A small collection of working Python scripts, each shipped with a deliberate flaw —
                a crash waiting to happen, a missing edge case, a design shortcut. Open a file, read
                it the way you'd read a teammate's pull request, and find the break point before you
                read the answer.
            </div>
            <div class="hero-stats">
                <div class="hero-stat"><div class="num">{total_files}</div><div class="lbl">projects</div></div>
                <div class="hero-stat"><div class="num">{total_issues_home}</div><div class="lbl">open issues</div></div>
                <div class="hero-stat"><div class="num">{total_lines_home}</div><div class="lbl">lines of code</div></div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown('<div class="sec-head">How it works</div>', unsafe_allow_html=True)
    how1, how2, how3 = st.columns(3, gap="medium")
    with how1:
        st.markdown(
            """
            <div class="how-card">
                <div class="how-step">1</div>
                <div class="how-title">Open a project</div>
                <div class="how-body">Pick any file from the repository. Each one runs fine on the happy path — that's the point.</div>
            </div>
            """,
            unsafe_allow_html=True,
        )
    with how2:
        st.markdown(
            """
            <div class="how-card">
                <div class="how-step">2</div>
                <div class="how-title">Read the issues</div>
                <div class="how-body">Every project lists its known flaws as labeled issues, same as you'd see on a real repository.</div>
            </div>
            """,
            unsafe_allow_html=True,
        )
    with how3:
        st.markdown(
            """
            <div class="how-card">
                <div class="how-step">3</div>
                <div class="how-title">Fix it</div>
                <div class="how-body">Rewrite the broken part yourself, or ask the mentor panel for a nudge if you get stuck.</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.markdown('<div class="sec-head">Projects in this repository</div>', unsafe_allow_html=True)
    pcols = st.columns(len(ALL_FILES), gap="medium")
    for i, fname in enumerate(ALL_FILES):
        p = projects_data[fname]
        with pcols[i]:
            st.markdown(
                f"""
                <div class="preview-card">
                    <div class="pname">{fname}.py</div>
                    <div class="ptag">{p['tagline']}</div>
                    <div class="pmeta">
                        <span>{p['lines']} lines</span>
                        <span class="bugcount">{len(p['limitations'])} issues</span>
                    </div>
                </div>
                """,
                unsafe_allow_html=True,
            )

    st.markdown("<div style='height:1.6rem;'></div>", unsafe_allow_html=True)
    if st.button("Browse all projects →", type="primary"):
        st.session_state.page = "repo"
        st.rerun()

else:
    # ----------------------------------------------------------------------------
    # TOP BAR
    # ----------------------------------------------------------------------------
    st.markdown(
        f"""
        <div class="topbar">
            <span class="mark"></span>
            <span class="crumb-light">practice-lab</span>
            <span class="crumb-sep">/</span>
            <span>{current_project['title']}</span>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # ----------------------------------------------------------------------------
    # REPO HEADER
    # ----------------------------------------------------------------------------
    total_issues = sum(len(p["limitations"]) for p in projects_data.values())
    st.markdown(
        f"""
        <div class="repo-header">
            <div>
                <div class="repo-name">
                    <span class="owner">practice-lab /</span> {current_project['title']}
                    <span class="visibility-pill">Public</span>
                </div>
                <div class="repo-tagline">{current_project['tagline']}</div>
                <div class="topic-row">
                    {''.join(f'<span class="topic-pill">{tag}</span>' for tag in current_project['topics'])}
                </div>
            </div>
            <div class="stat-pills">
                <div class="stat-pill"><span class="num">{len(ALL_FILES)}</span><span class="lbl">files</span></div>
                <div class="stat-pill"><span class="num">{len(current_project['limitations'])}</span><span class="lbl">issues</span></div>
                <div class="stat-pill"><span class="num">{current_project['lines']}</span><span class="lbl">lines</span></div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        f"""
        <div class="tab-strip">
            <div class="tab-item active">Code</div>
            <div class="tab-item">Issues <span class="count">{total_issues}</span></div>
            <div class="tab-item">Pull requests</div>
            <div class="tab-item">Insights</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    col_doc, col_ai = st.columns([2, 1], gap="large")

    # ----------------------------------------------------------------------------
    # MAIN COLUMN
    # ----------------------------------------------------------------------------
    with col_doc:
        # ---- commit bar + file listing (the part that made the page feel GitHub-y) ----
        st.markdown(
            f"""
            <div class="commit-bar">
                <span class="commit-avatar"></span>
                <span class="commit-msg">{current_project['commit']}</span>
                <span class="commit-hash">{current_project['commit_hash']}</span>
            </div>
            """,
            unsafe_allow_html=True,
        )

        rows = ""
        for f in ALL_FILES:
            p = projects_data[f]
            active = " style='background:%s;'" % t["canvas-inset"] if f == selected_option else ""
            rows += f"""
            <div class="file-row"{active}>
                <svg class="ficon" viewBox="0 0 16 16" fill="currentColor"><path d="M2 2.5A1.5 1.5 0 0 1 3.5 1h5.086a1.5 1.5 0 0 1 1.06.44l2.914 2.914a1.5 1.5 0 0 1 .44 1.06V13.5A1.5 1.5 0 0 1 11.5 15h-8A1.5 1.5 0 0 1 2 13.5z"/></svg>
                <span class="fname">{f}.py</span>
                <span class="fmsg">{p['commit']}</span>
                <span class="ftime">{p['commit_hash']}</span>
            </div>"""
        st.markdown(f'<div class="file-table">{rows}</div>', unsafe_allow_html=True)

        st.write(current_project["description"])

        # ---- code pane ----
        st.markdown(
            f"""
            <div class="file-pane-head">
                <span class="fname">{current_project['title']}.py</span>
                <span>{current_project['lines']} lines</span>
            </div>
            """,
            unsafe_allow_html=True,
        )
        st.markdown('<div class="file-pane-wrap">', unsafe_allow_html=True)
        st.code(current_project["code"], language="python", line_numbers=True)
        st.markdown('</div>', unsafe_allow_html=True)

        st.markdown('<div class="sec-head">Concepts in play</div>', unsafe_allow_html=True)
        st.write(current_project["concepts"])

        st.markdown(
            f'<div class="sec-head">Open issues · {len(current_project["limitations"])}</div>',
            unsafe_allow_html=True,
        )
        for f in current_project["limitations"]:
            chip_class = "chip-bug" if f["kind"] == "bug" else "chip-design"
            st.markdown(
                f"""
                <div class="flaw-row">
                    <span class="chip {chip_class}">{f['label']}</span>
                    <span class="flaw-detail">{f['detail']}</span>
                </div>
                """,
                unsafe_allow_html=True,
            )

        st.markdown('<div class="sec-head">Task</div>', unsafe_allow_html=True)
        st.markdown(
            f"""
            <div class="task-card">
                <span class="task-label">Fix required</span>
                <p>{current_project['challenge']}</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

        st.markdown(
            """
            <div class="btn-row">
                <a class="btn btn-primary" href="https://github.com/" target="_blank">Fork</a>
                <a class="btn" href="https://github.com/" target="_blank">Open pull request</a>
            </div>
            """,
            unsafe_allow_html=True,
        )

    # ----------------------------------------------------------------------------
    # RIGHT RAIL — About panel + Mentor
    # ----------------------------------------------------------------------------
    with col_ai:
        st.markdown(
            f"""
            <div class="about-panel">
                <div class="about-title">About</div>
                <div style="font-size:0.85rem;color:{t['text-muted']};margin-bottom:0.7rem;">
                    A library of small, intentionally flawed Python scripts for practicing real debugging and review.
                </div>
                <div class="about-row"><span>Files</span><span class="val">{len(ALL_FILES)}</span></div>
                <div class="about-row"><span>Open issues</span><span class="val">{total_issues}</span></div>
                <div class="about-row"><span>Default branch</span><span class="val">main</span></div>
                <div class="lang-bar">
                    <div class="lang-seg-py" style="width:88%;"></div>
                    <div class="lang-seg-md" style="width:12%;"></div>
                </div>
                <div class="lang-legend">
                    <span><span class="lang-dot" style="background:{t['lang-py']};"></span>Python 88.0%</span>
                    <span><span class="lang-dot" style="background:{t['accent']};"></span>Markdown 12.0%</span>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

        st.markdown(
            """
            <div class="panel">
                <div class="panel-title">Mentor</div>
                <div class="panel-sub">Ask for a hint on the issue you're stuck on.</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

        if "chat_history" not in st.session_state or st.session_state.get("chat_project") != selected_option:
            st.session_state.chat_history = [
                {
                    "role": "assistant",
                    "content": f"Looking at **{current_project['title']}** — what part of the fix are you stuck on?",
                }
            ]
            st.session_state.chat_project = selected_option

        for msg in st.session_state.chat_history:
            with st.chat_message(msg["role"]):
                st.write(msg["content"])

        if user_input := st.chat_input("Describe the issue you're hitting"):
            with st.chat_message("user"):
                st.write(user_input)
            st.session_state.chat_history.append({"role": "user", "content": user_input})

            mock_ai_feedback = (
                f"For **{current_project['title']}**, start by adding a guard condition before the "
                "operation that's failing — check the input or value before it reaches the line that breaks. "
                "Try it, then trace through one failing case by hand."
            )

            with st.chat_message("assistant"):
                st.write(mock_ai_feedback)
            st.session_state.chat_history.append({"role": "assistant", "content": mock_ai_feedback})