import streamlit as st
import os
import welcome

st.set_page_config(layout="wide", page_title="PySource Hub", page_icon="🚀")

CATALOG_DIR = "project_catalog"


def inject_custom_css():
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@500;600;700;800&family=JetBrains+Mono:wght@400;500;600;700&display=swap');

    :root {
        --ph-bg: #0b0f14; --ph-bg-el: #10151d; --ph-surface: #131a24;
        --ph-surface-hv: #161d28; --ph-border: rgba(255,255,255,0.08);
        --ph-border-st: rgba(255,255,255,0.16);
        --ph-green: #3ddc97; --ph-green-soft: rgba(61,220,151,0.12);
        --ph-blue: #5fb3f5; --ph-blue-soft: rgba(95,179,245,0.12);
        --ph-text: #e8edf4; --ph-text-sec: #8b96a8; --ph-text-dim: #586173;
        --ph-ok: #3ddc97; --ph-ok-soft: rgba(61,220,151,0.10);
        --ph-err: #f4615a; --ph-err-soft: rgba(244,97,90,0.10);
        --ph-info: #5fb3f5; --ph-info-soft: rgba(95,179,245,0.10);
        --ph-r: 14px; --ph-rs: 10px;
    }

    html,body,[class*="css"] { font-family:'Space Grotesk',-apple-system,sans-serif !important; }

    .stApp {
        background:
            radial-gradient(circle at 12% 0%,rgba(61,220,151,0.05) 0%,transparent 45%),
            radial-gradient(circle at 88% 8%,rgba(95,179,245,0.05) 0%,transparent 45%),
            var(--ph-bg) fixed;
        color: var(--ph-text);
    }

    #MainMenu { visibility:hidden; }
    footer { visibility:hidden; }
    header[data-testid="stHeader"] { background:transparent; }
    .block-container { padding-top:2rem !important; padding-bottom:3rem !important; max-width:1400px; }

    @keyframes fadeIn { from{opacity:0;transform:translateY(8px)} to{opacity:1;transform:translateY(0)} }
    .ph-fade { animation:fadeIn 0.5s cubic-bezier(0.16,1,0.3,1) both; }
    div[data-testid="stTabs"] { animation:fadeIn 0.5s cubic-bezier(0.16,1,0.3,1) both; }

    div[data-testid="stTabs"] button[role="tab"] {
        font-weight:600; font-size:0.95rem; color:var(--ph-text-sec);
        padding:0.6rem 1.1rem; border-radius:10px 10px 0 0; transition:all 0.2s ease;
    }
    div[data-testid="stTabs"] button[role="tab"]:hover { color:var(--ph-text); background:var(--ph-surface-hv); }
    div[data-testid="stTabs"] button[aria-selected="true"] {
        color:#fff !important; background:var(--ph-green-soft);
        border-bottom:2px solid var(--ph-green) !important;
    }
    div[data-testid="stTabs"] div[data-baseweb="tab-highlight"] { background-color:var(--ph-green) !important; }

    section[data-testid="stSidebar"] {
        background:linear-gradient(180deg,var(--ph-bg-el) 0%,var(--ph-bg) 100%);
        border-right:1px solid var(--ph-border);
    }
    section[data-testid="stSidebar"] div[data-baseweb="select"]>div {
        background:var(--ph-surface) !important; border:1px solid var(--ph-border-st) !important;
        border-radius:var(--ph-rs) !important; transition:border-color 0.2s ease;
    }
    section[data-testid="stSidebar"] div[data-baseweb="select"]>div:hover { border-color:var(--ph-green) !important; }

    h1,h2,h3,h4 { color:var(--ph-text) !important; font-weight:700 !important; font-family:'Space Grotesk',sans-serif !important; }

    .ph-glass-info,.ph-glass-ok,.ph-glass-err {
        display:flex; gap:0.8rem; align-items:flex-start;
        padding:1.1rem 1.3rem; border-radius:var(--ph-rs);
        margin-bottom:0.9rem; font-size:0.93rem; line-height:1.55;
        transition:transform 0.22s ease;
    }
    .ph-glass-info:hover,.ph-glass-ok:hover,.ph-glass-err:hover { transform:translateY(-2px); }
    .ph-glass-info  { background:var(--ph-info-soft);  border:1px solid rgba(95,179,245,0.28); color:#d6ecfd; }
    .ph-glass-ok    { background:var(--ph-ok-soft);    border:1px solid rgba(61,220,151,0.28);  color:#d8f7e8; }
    .ph-glass-err   { background:var(--ph-err-soft);   border:1px solid rgba(244,97,90,0.28);   color:#fdd9d6; }

    .ph-ws-hdr {
        padding:1.6rem 1.9rem; border-radius:var(--ph-r);
        background:var(--ph-surface); border:1px solid var(--ph-border);
        margin-bottom:1.4rem; position:relative; overflow:hidden;
    }
    .ph-ws-hdr::before {
        content:''; position:absolute; top:0; left:0; bottom:0; width:3px;
        background:linear-gradient(180deg,var(--ph-green),var(--ph-blue));
    }
    .ph-ws-title { font-size:1.5rem !important; font-weight:700 !important; margin:0 0 0.3rem 0 !important; }
    .ph-ws-tag {
        display:inline-block; font-family:'JetBrains Mono',monospace;
        font-size:0.78rem; color:var(--ph-green); background:var(--ph-green-soft);
        padding:0.2rem 0.6rem; border-radius:6px; margin-bottom:0.6rem;
    }
    .ph-ws-desc { color:var(--ph-text-sec); font-size:0.97rem; margin:0; }

    .ph-sec-lbl {
        font-size:0.95rem; font-weight:700; color:var(--ph-text);
        margin:1.6rem 0 0.7rem 0; display:flex; align-items:center; gap:0.6rem;
    }

    .ph-ide-bar {
        display:flex; align-items:center; gap:0.5rem;
        background:var(--ph-bg-el); border:1px solid var(--ph-border);
        border-bottom:none; border-radius:var(--ph-r) var(--ph-r) 0 0; padding:0.7rem 1rem;
    }
    .ph-dot-r{width:11px;height:11px;border-radius:50%;background:#f4615a;}
    .ph-dot-y{width:11px;height:11px;border-radius:50%;background:#f0b84e;}
    .ph-dot-g{width:11px;height:11px;border-radius:50%;background:#3ddc97;}
    .ph-ide-fn { margin-left:0.6rem; font-family:'JetBrains Mono',monospace; font-size:0.82rem; color:var(--ph-text-sec); }

    div[data-testid="stExpander"] {
        border:1px solid var(--ph-border) !important; border-top:none !important;
        border-radius:0 0 var(--ph-r) var(--ph-r) !important;
        background:var(--ph-bg-el) !important; margin-top:-1px;
    }
    div[data-testid="stExpander"] summary {
        font-family:'JetBrains Mono',monospace !important; font-size:0.85rem !important;
        color:var(--ph-text-sec) !important; padding:0.75rem 1.1rem !important;
    }
    div[data-testid="stExpander"] summary:hover { color:var(--ph-text) !important; }

    pre,code { font-family:'JetBrains Mono',monospace !important; }
    div[data-testid="stCode"] { border-radius:var(--ph-rs); border:1px solid var(--ph-border); }
    div[data-testid="stCode"] pre { background:#0c1018 !important; }

    .ph-chat-shell {
        background:var(--ph-surface); border:1px solid var(--ph-border);
        border-radius:var(--ph-r); padding:1.3rem 1.4rem 0.6rem 1.4rem; margin-bottom:0.9rem;
    }
    .ph-chat-hdr { display:flex; align-items:center; gap:0.6rem; margin-bottom:0.3rem; }
    .ph-chat-dot { width:8px;height:8px;border-radius:50%;background:var(--ph-ok); }
    .ph-chat-title { font-weight:700; font-size:1rem; color:var(--ph-text); }
    .ph-chat-cap { color:var(--ph-text-dim); font-size:0.84rem; margin:0 0 0.9rem 1.4rem; }

    div[data-testid="stChatMessage"] {
        background:var(--ph-bg-el) !important; border:1px solid var(--ph-border) !important;
        border-radius:var(--ph-rs) !important; margin-bottom:0.6rem !important;
    }
    div[data-testid="stChatInput"] textarea {
        background:var(--ph-bg-el) !important; border:1px solid var(--ph-border-st) !important;
        border-radius:var(--ph-rs) !important; color:var(--ph-text) !important;
    }

    .ph-links a {
        display:inline-block; font-size:0.88rem; font-weight:600; color:var(--ph-text) !important;
        background:var(--ph-surface-hv); border:1px solid var(--ph-border-st);
        padding:0.5rem 1rem; border-radius:999px; margin-right:0.6rem;
        text-decoration:none !important; transition:all 0.2s ease;
    }
    .ph-links a:hover { border-color:var(--ph-green); color:var(--ph-green) !important; transform:translateY(-2px); }

    p,span,label,.stMarkdown { color:var(--ph-text); }
    ::-webkit-scrollbar { width:8px; height:8px; }
    ::-webkit-scrollbar-track { background:var(--ph-bg); }
    ::-webkit-scrollbar-thumb { background:var(--ph-border-st); border-radius:4px; }
    </style>
    """, unsafe_allow_html=True)


def extract_project_number(filename):
    try:
        return int(filename.replace("project", "").replace(".py", ""))
    except ValueError:
        return float('inf')


def get_project_metadata(filepath):
    meta = {"title": os.path.basename(filepath), "description": "No description provided.",
            "limitations": [], "challenge": "No practice task declared.", "code": ""}
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            lines = f.readlines()
        meta["code"] = "".join(lines)
        for line in lines:
            if line.startswith("# TITLE:"):       meta["title"] = line.replace("# TITLE:", "").strip()
            elif line.startswith("# DESCRIPTION:"): meta["description"] = line.replace("# DESCRIPTION:", "").strip()
            elif line.startswith("# LIMITATIONS:"):
                meta["limitations"] = [x.strip() for x in line.replace("# LIMITATIONS:", "").split("|") if x.strip()]
            elif line.startswith("# CHALLENGE:"): meta["challenge"] = line.replace("# CHALLENGE:", "").strip()
    except Exception:
        pass
    return meta


def glass_card(kind, icon_html, text):
    cls = {"info": "ph-glass-info", "ok": "ph-glass-ok", "err": "ph-glass-err"}[kind]
    st.markdown(f'<div class="{cls} ph-fade"><span>{icon_html}</span><span>{text}</span></div>',
                unsafe_allow_html=True)


# =========================================================================
inject_custom_css()

if not os.path.exists(CATALOG_DIR):
    os.makedirs(CATALOG_DIR)

raw_files = sorted([f for f in os.listdir(CATALOG_DIR) if f.endswith(".py")], key=extract_project_number)

project_map = {}
for fn in raw_files:
    path = os.path.join(CATALOG_DIR, fn)
    meta = get_project_metadata(path)
    project_map[f"{fn.replace('.py','').upper()}: {meta['title']}"] = meta

# Tabs — no emojis
tab1, tab2 = st.tabs(["Hub Home Overview", "Project Workspace Dashboard"])

with tab1:
    welcome.render_welcome_page(project_map)

with tab2:
    if not raw_files:
        glass_card("info", "&#128205;", "No active repositories found in the catalog directory.")
    else:
        st.sidebar.markdown(
            '<div style="padding:0.4rem 0 1rem 0;font-size:1.05rem;font-weight:700;color:var(--ph-text);">Repository Selector</div>'
            '<div style="font-size:0.83rem;color:var(--ph-text-dim);margin-top:-0.7rem;margin-bottom:0.6rem;">Select a system build below</div>',
            unsafe_allow_html=True)
        selected = st.sidebar.selectbox("Workspace:", list(project_map.keys()), label_visibility="collapsed")

        cur  = project_map[selected]
        mtag = selected.split(':')[0]

        st.markdown(f"""
        <div class="ph-ws-hdr ph-fade">
            <div class="ph-ws-tag">{mtag}</div>
            <h2 class="ph-ws-title">{cur['title']}</h2>
            <p class="ph-ws-desc">{cur['description']}</p>
        </div>
        """, unsafe_allow_html=True)

        col_doc, col_ai = st.columns([2, 1], gap="large")

        with col_doc:
            st.markdown('<div class="ph-sec-lbl ph-fade">1 &middot; Code Blueprint</div>', unsafe_allow_html=True)
            st.markdown(f"""
            <div class="ph-ide-bar ph-fade">
                <div class="ph-dot-r"></div><div class="ph-dot-y"></div><div class="ph-dot-g"></div>
                <span class="ph-ide-fn">{mtag.lower()}.py</span>
            </div>
            """, unsafe_allow_html=True)
            with st.expander("Click to view operational code", expanded=True):
                st.code(cur['code'], language="python")

            st.markdown('<div class="ph-sec-lbl ph-fade">2 &middot; Known Limitations &amp; Flaws</div>', unsafe_allow_html=True)
            if cur['limitations']:
                for lim in cur['limitations']:
                    glass_card("err", "&#9888;", lim)
            else:
                glass_card("ok", "&#10003;", "No limitations documented for this module.")

            st.markdown('<div class="ph-sec-lbl ph-fade">3 &middot; Open-Source Practice Task</div>', unsafe_allow_html=True)
            glass_card("info", "&#128161;", f"<strong>Your Code Challenge:</strong> {cur['challenge']}")

            st.markdown("""
            <div class="ph-links" style="margin-top:1rem;">
                <a href="https://github.com/" target="_blank">Fork on GitHub</a>
                <a href="https://github.com/" target="_blank">Submit Pull Request</a>
            </div>
            """, unsafe_allow_html=True)

        with col_ai:
            st.markdown("""
            <div class="ph-chat-shell ph-fade">
                <div class="ph-chat-hdr"><div class="ph-chat-dot"></div><div class="ph-chat-title">AI Code Mentor</div></div>
                <div class="ph-chat-cap">Ask questions about code design constraints!</div>
            </div>
            """, unsafe_allow_html=True)

            if "chat_history" not in st.session_state:
                st.session_state.chat_history = [{"role": "assistant", "content": "Hey there! Let's analyze this project breakdown together."}]
            for msg in st.session_state.chat_history:
                with st.chat_message(msg["role"]):
                    st.write(msg["content"])

            if user_input := st.chat_input("Ask a logic design question...", key="ws_chat"):
                with st.chat_message("user"):
                    st.write(user_input)
                st.session_state.chat_history.append({"role": "user", "content": user_input})
                reply = "Awesome question! Notice how variables are routed through loops in this module. Try isolating that logic block!"
                with st.chat_message("assistant"):
                    st.write(reply)
                st.session_state.chat_history.append({"role": "assistant", "content": reply})