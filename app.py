import streamlit as st
import os
import welcome  # Import our new welcome file cleanly

# Set layout configurations for a clean wide-screen dashboard layout
st.set_page_config(layout="wide", page_title="PySource Hub", page_icon="🚀")

CATALOG_DIR = "project_catalog"


# =========================================================================
# THEME / CSS INJECTION — "Circuit Slate"
# -------------------------------------------------------------------------
# App-wide palette pulled from the brand mark (twin-snake shield): signal
# green + signal blue on near-black slate. Replaces the prior generic
# indigo SaaS look so every tab, the sidebar, the workspace, and the chat
# panel share one identity with the home page.
# =========================================================================
def inject_custom_css():
    st.markdown(
        """
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@500;600;700;800&family=JetBrains+Mono:wght@400;500;600;700&display=swap');

        :root {
            --ph-bg: #0b0f14;
            --ph-bg-elevated: #10151d;
            --ph-surface: #131a24;
            --ph-surface-hover: #161d28;
            --ph-border: rgba(255, 255, 255, 0.08);
            --ph-border-strong: rgba(255, 255, 255, 0.16);
            --ph-green: #3ddc97;
            --ph-green-deep: #0e9e63;
            --ph-green-soft: rgba(61, 220, 151, 0.12);
            --ph-blue: #5fb3f5;
            --ph-blue-deep: #1c6fc9;
            --ph-blue-soft: rgba(95, 179, 245, 0.12);
            --ph-text-primary: #e8edf4;
            --ph-text-secondary: #8b96a8;
            --ph-text-dim: #586173;
            --ph-success: #3ddc97;
            --ph-success-soft: rgba(61, 220, 151, 0.10);
            --ph-error: #f4615a;
            --ph-error-soft: rgba(244, 97, 90, 0.10);
            --ph-info: #5fb3f5;
            --ph-info-soft: rgba(95, 179, 245, 0.10);
            --ph-radius: 14px;
            --ph-radius-sm: 10px;
        }

        /* ---------- GLOBAL BASE ---------- */
        html, body, [class*="css"] {
            font-family: 'Space Grotesk', -apple-system, BlinkMacSystemFont, sans-serif !important;
        }

        .stApp {
            background:
                radial-gradient(circle at 12% 0%, rgba(61,220,151,0.05) 0%, transparent 45%),
                radial-gradient(circle at 88% 8%, rgba(95,179,245,0.05) 0%, transparent 45%),
                var(--ph-bg) fixed;
            color: var(--ph-text-primary);
        }

        /* Hide default Streamlit chrome for a cleaner feel */
        #MainMenu { visibility: hidden; }
        footer { visibility: hidden; }
        header[data-testid="stHeader"] { background: transparent; }

        .block-container {
            padding-top: 2.2rem !important;
            padding-bottom: 3rem !important;
            max-width: 1400px;
        }

        /* ---------- FADE-IN ANIMATION ---------- */
        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(10px); }
            to   { opacity: 1; transform: translateY(0); }
        }
        .ph-fade-in {
            animation: fadeIn 0.55s cubic-bezier(0.16, 1, 0.3, 1) both;
        }
        .ph-delay-1 { animation-delay: 0.06s; }
        .ph-delay-2 { animation-delay: 0.14s; }
        .ph-delay-3 { animation-delay: 0.22s; }

        div[data-testid="stVerticalBlock"],
        div[data-testid="stTabs"] {
            animation: fadeIn 0.5s cubic-bezier(0.16, 1, 0.3, 1) both;
        }

        /* ---------- TABS ---------- */
        div[data-testid="stTabs"] button[role="tab"] {
            font-weight: 600;
            font-size: 0.95rem;
            color: var(--ph-text-secondary);
            padding: 0.6rem 1.1rem;
            border-radius: 10px 10px 0 0;
            transition: all 0.2s ease;
        }
        div[data-testid="stTabs"] button[role="tab"]:hover {
            color: var(--ph-text-primary);
            background: var(--ph-surface-hover);
        }
        div[data-testid="stTabs"] button[aria-selected="true"] {
            color: #ffffff !important;
            background: var(--ph-green-soft);
            border-bottom: 2px solid var(--ph-green) !important;
        }
        div[data-testid="stTabs"] div[data-baseweb="tab-highlight"] {
            background-color: var(--ph-green) !important;
        }

        /* ---------- SIDEBAR ---------- */
        section[data-testid="stSidebar"] {
            background: linear-gradient(180deg, var(--ph-bg-elevated) 0%, var(--ph-bg) 100%);
            border-right: 1px solid var(--ph-border);
        }
        section[data-testid="stSidebar"] .stSelectbox label {
            color: var(--ph-text-secondary) !important;
            font-weight: 600;
            font-size: 0.82rem;
            letter-spacing: 0.03em;
            text-transform: uppercase;
        }
        section[data-testid="stSidebar"] div[data-baseweb="select"] > div {
            background: var(--ph-surface) !important;
            border: 1px solid var(--ph-border-strong) !important;
            border-radius: var(--ph-radius-sm) !important;
            transition: border-color 0.2s ease;
        }
        section[data-testid="stSidebar"] div[data-baseweb="select"] > div:hover {
            border-color: var(--ph-green) !important;
        }

        /* ---------- HEADERS ---------- */
        h1, h2, h3, h4 {
            color: var(--ph-text-primary) !important;
            font-weight: 700 !important;
            font-family: 'Space Grotesk', sans-serif !important;
        }

        /* ---------- GENERIC CARD ---------- */
        .ph-card {
            background: var(--ph-surface);
            border: 1px solid var(--ph-border);
            border-radius: var(--ph-radius);
            padding: 1.6rem 1.8rem;
            margin-bottom: 1.2rem;
            transition: transform 0.25s ease, border-color 0.25s ease, box-shadow 0.25s ease;
        }
        .ph-card:hover {
            transform: translateY(-2px);
            border-color: var(--ph-border-strong);
            box-shadow: 0 12px 28px -8px rgba(0,0,0,0.5);
        }
        .ph-card-eyebrow {
            font-family: 'JetBrains Mono', monospace;
            font-size: 0.74rem;
            font-weight: 700;
            letter-spacing: 0.06em;
            color: var(--ph-green);
            margin-bottom: 0.6rem;
        }
        .ph-card-title {
            margin: 0 0 0.8rem 0 !important;
            font-size: 1.25rem !important;
        }
        .ph-card-text {
            color: var(--ph-text-secondary);
            line-height: 1.65;
            font-size: 0.96rem;
            margin-bottom: 0.7rem;
        }
        .ph-section-label {
            font-size: 0.95rem;
            font-weight: 700;
            color: var(--ph-text-primary);
            margin: 1.6rem 0 0.7rem 0;
            display: flex;
            align-items: center;
            gap: 0.6rem;
        }

        /* ---------- GLASSMORPHISM INFO / SUCCESS / ERROR ---------- */
        .ph-glass-info, .ph-glass-success, .ph-glass-error {
            display: flex;
            gap: 0.8rem;
            align-items: flex-start;
            padding: 1.1rem 1.3rem;
            border-radius: var(--ph-radius-sm);
            backdrop-filter: blur(12px);
            -webkit-backdrop-filter: blur(12px);
            margin-bottom: 0.9rem;
            font-size: 0.93rem;
            line-height: 1.55;
            transition: transform 0.22s ease, box-shadow 0.22s ease;
        }
        .ph-glass-info:hover, .ph-glass-success:hover, .ph-glass-error:hover {
            transform: translateY(-2px);
        }
        .ph-glass-icon { font-size: 1.1rem; line-height: 1.4; }

        .ph-glass-info {
            background: var(--ph-info-soft);
            border: 1px solid rgba(95, 179, 245, 0.28);
            color: #d6ecfd;
        }
        .ph-glass-info:hover { box-shadow: 0 10px 24px -8px rgba(95, 179, 245, 0.25); }

        .ph-glass-success {
            background: var(--ph-success-soft);
            border: 1px solid rgba(61, 220, 151, 0.28);
            color: #d8f7e8;
        }
        .ph-glass-success:hover { box-shadow: 0 10px 24px -8px rgba(61, 220, 151, 0.25); }

        .ph-glass-error {
            background: var(--ph-error-soft);
            border: 1px solid rgba(244, 97, 90, 0.28);
            color: #fdd9d6;
        }
        .ph-glass-error:hover { box-shadow: 0 10px 24px -8px rgba(244, 97, 90, 0.25); }

        /* ---------- WORKSPACE HEADER ---------- */
        .ph-workspace-header {
            padding: 1.6rem 1.9rem;
            border-radius: var(--ph-radius);
            background: var(--ph-surface);
            border: 1px solid var(--ph-border);
            margin-bottom: 1.4rem;
            position: relative;
            overflow: hidden;
        }
        .ph-workspace-header::before {
            content: '';
            position: absolute;
            top: 0; left: 0; bottom: 0;
            width: 3px;
            background: linear-gradient(180deg, var(--ph-green), var(--ph-blue));
        }
        .ph-workspace-title {
            font-size: 1.5rem !important;
            font-weight: 700 !important;
            margin: 0 0 0.3rem 0 !important;
        }
        .ph-workspace-tag {
            display: inline-block;
            font-family: 'JetBrains Mono', monospace;
            font-size: 0.78rem;
            color: var(--ph-green);
            background: var(--ph-green-soft);
            padding: 0.2rem 0.6rem;
            border-radius: 6px;
            margin-bottom: 0.6rem;
        }
        .ph-workspace-desc {
            color: var(--ph-text-secondary);
            font-size: 0.97rem;
            margin: 0;
        }

        /* ---------- IDE-STYLE CODE PANEL ---------- */
        .ph-ide-topbar {
            display: flex;
            align-items: center;
            gap: 0.5rem;
            background: var(--ph-bg-elevated);
            border: 1px solid var(--ph-border);
            border-bottom: none;
            border-radius: var(--ph-radius) var(--ph-radius) 0 0;
            padding: 0.7rem 1rem;
        }
        .ph-ide-dot { width: 11px; height: 11px; border-radius: 50%; }
        .ph-ide-dot.red { background: #f4615a; }
        .ph-ide-dot.yellow { background: #f0b84e; }
        .ph-ide-dot.green { background: #3ddc97; }
        .ph-ide-filename {
            margin-left: 0.6rem;
            font-family: 'JetBrains Mono', monospace;
            font-size: 0.82rem;
            color: var(--ph-text-secondary);
        }

        div[data-testid="stExpander"] {
            border: 1px solid var(--ph-border) !important;
            border-top: none !important;
            border-radius: 0 0 var(--ph-radius) var(--ph-radius) !important;
            background: var(--ph-bg-elevated) !important;
            margin-top: -1px;
        }
        div[data-testid="stExpander"] summary {
            font-family: 'JetBrains Mono', monospace !important;
            font-size: 0.85rem !important;
            color: var(--ph-text-secondary) !important;
            padding: 0.75rem 1.1rem !important;
        }
        div[data-testid="stExpander"] summary:hover {
            color: var(--ph-text-primary) !important;
        }

        pre, code {
            font-family: 'JetBrains Mono', monospace !important;
        }
        div[data-testid="stCode"] {
            border-radius: var(--ph-radius-sm);
            border: 1px solid var(--ph-border);
        }
        div[data-testid="stCode"] pre {
            background: #0c1018 !important;
        }
        div[data-testid="stCode"] pre code {
            background: transparent !important;
        }

        /* ---------- AI MENTOR CHAT PANEL ---------- */
        .ph-chat-shell {
            background: var(--ph-surface);
            border: 1px solid var(--ph-border);
            border-radius: var(--ph-radius);
            padding: 1.3rem 1.4rem 0.6rem 1.4rem;
            margin-bottom: 0.9rem;
        }
        .ph-chat-header {
            display: flex;
            align-items: center;
            gap: 0.6rem;
            margin-bottom: 0.3rem;
        }
        .ph-chat-status-dot {
            width: 8px; height: 8px; border-radius: 50%;
            background: var(--ph-success);
            box-shadow: 0 0 8px var(--ph-success);
        }
        .ph-chat-title {
            font-weight: 700;
            font-size: 1rem;
            color: var(--ph-text-primary);
        }
        .ph-chat-caption {
            color: var(--ph-text-dim);
            font-size: 0.84rem;
            margin: 0 0 0.9rem 1.4rem;
        }

        div[data-testid="stChatMessage"] {
            background: var(--ph-bg-elevated) !important;
            border: 1px solid var(--ph-border) !important;
            border-radius: var(--ph-radius-sm) !important;
            margin-bottom: 0.6rem !important;
            transition: transform 0.2s ease;
        }
        div[data-testid="stChatMessage"]:hover {
            transform: translateY(-1px);
        }

        div[data-testid="stChatInput"] textarea {
            background: var(--ph-bg-elevated) !important;
            border: 1px solid var(--ph-border-strong) !important;
            border-radius: var(--ph-radius-sm) !important;
            color: var(--ph-text-primary) !important;
        }
        div[data-testid="stChatInput"] {
            border-top: 1px solid var(--ph-border) !important;
        }

        /* ---------- BUTTONS / LINKS ---------- */
        .ph-link-row { margin-top: 1rem; }
        .ph-link-row a {
            display: inline-block;
            font-size: 0.88rem;
            font-weight: 600;
            color: var(--ph-text-primary) !important;
            background: var(--ph-surface-hover);
            border: 1px solid var(--ph-border-strong);
            padding: 0.5rem 1rem;
            border-radius: 999px;
            margin-right: 0.6rem;
            text-decoration: none !important;
            transition: all 0.2s ease;
        }
        .ph-link-row a:hover {
            border-color: var(--ph-green);
            color: var(--ph-green) !important;
            transform: translateY(-2px);
        }

        /* Misc text fallbacks */
        p, span, label, .stMarkdown { color: var(--ph-text-primary); }
        ::-webkit-scrollbar { width: 8px; height: 8px; }
        ::-webkit-scrollbar-track { background: var(--ph-bg); }
        ::-webkit-scrollbar-thumb { background: var(--ph-border-strong); border-radius: 4px; }
        </style>
        """,
        unsafe_allow_html=True,
    )


# =========================================================================
# DATA / FILE LOGIC — unchanged from original
# =========================================================================
def extract_project_number(filename):
    try:
        num_str = filename.replace("project", "").replace(".py", "")
        return int(num_str)
    except ValueError:
        return float('inf')


def get_project_metadata(filepath):
    metadata = {"title": os.path.basename(filepath), "description": "No description layout provided.", "limitations": [], "challenge": "No community practice task declared.", "code": ""}
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            lines = f.readlines()
        metadata["code"] = "".join(lines)
        for line in lines:
            if line.startswith("# TITLE:"): metadata["title"] = line.replace("# TITLE:", "").strip()
            elif line.startswith("# DESCRIPTION:"): metadata["description"] = line.replace("# DESCRIPTION:", "").strip()
            elif line.startswith("# LIMITATIONS:"):
                raw_limits = line.replace("# LIMITATIONS:", "").strip()
                metadata["limitations"] = [bit.strip() for bit in raw_limits.split("|") if bit.strip()]
            elif line.startswith("# CHALLENGE:"): metadata["challenge"] = line.replace("# CHALLENGE:", "").strip()
    except Exception:
        pass
    return metadata


# =========================================================================
# UI HELPER RENDERERS (custom glassmorphism replacements for st.error/st.info)
# =========================================================================
def render_limitation_card(text):
    st.markdown(
        f"""
        <div class="ph-glass-error ph-fade-in">
            <span class="ph-glass-icon">⚠️</span>
            <span>{text}</span>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_no_limitations_card():
    st.markdown(
        """
        <div class="ph-glass-success ph-fade-in">
            <span class="ph-glass-icon">✅</span>
            <span>No limitations documented for this module code.</span>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_challenge_card(text):
    st.markdown(
        f"""
        <div class="ph-glass-info ph-fade-in">
            <span class="ph-glass-icon">💡</span>
            <span><strong>Your Code Challenge:</strong> {text}</span>
        </div>
        """,
        unsafe_allow_html=True,
    )


# =========================================================================
# APP BOOTSTRAP
# =========================================================================
inject_custom_css()

if not os.path.exists(CATALOG_DIR):
    os.makedirs(CATALOG_DIR)

raw_files = [f for f in os.listdir(CATALOG_DIR) if f.endswith(".py")]
all_files = sorted(raw_files, key=extract_project_number)

# Build project map from directory files
project_map = {}
for filename in all_files:
    path = os.path.join(CATALOG_DIR, filename)
    meta = get_project_metadata(path)
    display_label = f"{filename.replace('.py','').upper()}: {meta['title']}"
    project_map[display_label] = meta

# --- CREATE CLEAN NAVIGATION TABS AT THE TOP OF THE PAGE ---
tab1, tab2 = st.tabs(["🏠  Hub Home Overview", "💻  Project Workspace Dashboard"])

with tab1:
    # Render our isolated front page function cleanly!
    welcome.render_welcome_page(project_map)

with tab2:
    if not all_files:
        st.markdown(
            """
            <div class="ph-glass-info ph-fade-in">
                <span class="ph-glass-icon">📭</span>
                <span>No active repositories found in the catalog directory.</span>
            </div>
            """,
            unsafe_allow_html=True,
        )
    else:
        # Move the selector cleanly into the sidebar only when browsing code workspace
        st.sidebar.markdown(
            """
            <div style="padding: 0.4rem 0 1rem 0;">
                <div style="font-size:1.05rem; font-weight:700; color:var(--ph-text-primary);">
                    📁 Repository Selector
                </div>
                <div style="font-size:0.83rem; color:var(--ph-text-dim); margin-top:0.2rem;">
                    Select a system build below
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )
        selected_project_key = st.sidebar.selectbox(
            "Choose active workspace file:",
            list(project_map.keys()),
            label_visibility="collapsed",
        )

        current_project = project_map[selected_project_key]
        module_tag = selected_project_key.split(':')[0]

        # --- WORKSPACE HEADER ---
        st.markdown(
            f"""
            <div class="ph-workspace-header ph-fade-in">
                <div class="ph-workspace-tag">📂 {module_tag}</div>
                <h2 class="ph-workspace-title">{current_project['title']}</h2>
                <p class="ph-workspace-desc">{current_project['description']}</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

        col_doc, col_ai = st.columns([2, 1], gap="large")

        with col_doc:
            st.markdown('<div class="ph-section-label ph-fade-in">1 · Code Blueprint</div>', unsafe_allow_html=True)

            # IDE-style fake "window" topbar sitting on top of the expander
            st.markdown(
                f"""
                <div class="ph-ide-topbar ph-fade-in">
                    <div class="ph-ide-dot red"></div>
                    <div class="ph-ide-dot yellow"></div>
                    <div class="ph-ide-dot green"></div>
                    <span class="ph-ide-filename">{module_tag.lower()}.py</span>
                </div>
                """,
                unsafe_allow_html=True,
            )
            with st.expander("🔍  Click to view clean operational code", expanded=True):
                st.code(current_project['code'], language="python")

            st.markdown('<div class="ph-section-label ph-fade-in">2 · Known Limitations &amp; Flaws</div>', unsafe_allow_html=True)
            if current_project['limitations']:
                for limitation in current_project['limitations']:
                    render_limitation_card(limitation)
            else:
                render_no_limitations_card()

            st.markdown('<div class="ph-section-label ph-fade-in">3 · Open-Source Practice Task</div>', unsafe_allow_html=True)
            render_challenge_card(current_project['challenge'])

            st.markdown(
                """
                <div class="ph-link-row">
                    <a href="https://github.com/" target="_blank">✨ Fork on GitHub</a>
                    <a href="https://github.com/" target="_blank">🚀 Submit Pull Request</a>
                </div>
                """,
                unsafe_allow_html=True,
            )

        with col_ai:
            st.markdown(
                """
                <div class="ph-chat-shell ph-fade-in">
                    <div class="ph-chat-header">
                        <div class="ph-chat-status-dot"></div>
                        <div class="ph-chat-title">🤖 AI Code Mentor</div>
                    </div>
                    <div class="ph-chat-caption">Ask questions about code design constraints!</div>
                </div>
                """,
                unsafe_allow_html=True,
            )

            if "chat_history" not in st.session_state:
                st.session_state.chat_history = [{"role": "assistant", "content": "Hey there! Let's analyze this project breakdown together."}]
            for msg in st.session_state.chat_history:
                with st.chat_message(msg["role"]):
                    st.write(msg["content"])

            if user_input := st.chat_input("Ask a logic design question...", key="workspace_chat"):
                with st.chat_message("user"):
                    st.write(user_input)
                st.session_state.chat_history.append({"role": "user", "content": user_input})

                feedback = f"Awesome logic question. Looking at your current selected code snippet, notice how variables are routed through loops. Try isolating that logic block!"
                with st.chat_message("assistant"):
                    st.write(feedback)
                st.session_state.chat_history.append({"role": "assistant", "content": feedback})