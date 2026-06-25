import streamlit as st
import streamlit.components.v1 as components


# =========================================================================
# PYSOURCE HUB — Welcome page with working light/dark toggle + starfield
# The toggle is a real st.button that flips st.session_state["ph_theme"].
# The starfield is inside components.html() so its <script> actually runs.
# =========================================================================

def _get_theme():
    if "ph_theme" not in st.session_state:
        st.session_state["ph_theme"] = "dark"
    return st.session_state["ph_theme"]


def _inject_base_css(theme):
    if theme == "dark":
        bg        = "#0b0f14"
        panel     = "#10151d"
        border    = "rgba(255,255,255,0.08)"
        border_st = "rgba(255,255,255,0.16)"
        text      = "#e8edf4"
        text_dim  = "#8b96a8"
        text_faint= "#586173"
        green     = "#3ddc97"
        blue      = "#5fb3f5"
        circuit_opacity = "0.55"
    else:
        bg        = "#f4f6f9"
        panel     = "#ffffff"
        border    = "rgba(0,0,0,0.08)"
        border_st = "rgba(0,0,0,0.16)"
        text      = "#111827"
        text_dim  = "#4b5563"
        text_faint= "#9ca3af"
        green     = "#0b8c55"
        blue      = "#1560b0"
        circuit_opacity = "0.12"

    st.markdown(f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@500;600;700&family=JetBrains+Mono:wght@400;500;700&display=swap');
    #ph-root {{
        background: {bg};
        border-radius: 16px;
        padding: 0;
        margin: -1rem -1rem 0 -1rem;
        position: relative;
        overflow: hidden;
        font-family: 'Space Grotesk', sans-serif;
        transition: background 0.3s ease;
    }}
    .ph-text, .ph-text p, .ph-text div, .ph-text span, .ph-text li {{
        color: {text} !important;
        font-family: 'Space Grotesk', sans-serif;
    }}
    .ph-text h1, .ph-text h2 {{ color: {text} !important; }}
    .ph-mono {{ font-family: 'JetBrains Mono', monospace; }}

    @keyframes phFade {{
        from {{ opacity: 0; transform: translateY(8px); }}
        to   {{ opacity: 1; transform: translateY(0); }}
    }}
    .ph-fade {{ animation: phFade 0.5s cubic-bezier(0.16,1,0.3,1) both; }}
    .ph-d1 {{ animation-delay: 0.05s; }}
    .ph-d2 {{ animation-delay: 0.12s; }}
    .ph-d3 {{ animation-delay: 0.20s; }}
    .ph-d4 {{ animation-delay: 0.28s; }}

    .ph-circuit {{
        position: absolute; top: 0; left: 0;
        width: 100%; height: 460px;
        z-index: 0; pointer-events: none;
        opacity: {circuit_opacity};
    }}
    .ph-circuit path {{ stroke-dasharray: 600; animation: phTrace 2s ease-out forwards; }}
    .ph-circuit circle {{ animation: phPulse 2.6s ease-in-out infinite; }}
    @keyframes phTrace {{ from {{ stroke-dashoffset: 600; }} to {{ stroke-dashoffset: 0; }} }}
    @keyframes phPulse {{ 0%,100% {{ opacity:0.5; }} 50% {{ opacity:1; }} }}

    .ph-hero {{
        position: relative; z-index: 1;
        padding: 3rem 2.4rem 2.4rem 2.4rem;
        display: flex; align-items: center; gap: 2rem; flex-wrap: wrap;
    }}
    .ph-eyebrow {{
        font-family: 'JetBrains Mono', monospace;
        font-size: 0.78rem; font-weight: 700; letter-spacing: 0.08em;
        color: {green} !important; margin-bottom: 0.6rem;
        display: flex; align-items: center; gap: 0.5rem;
    }}
    .ph-dot {{
        width:6px; height:6px; border-radius:50%;
        background:{green}; display:inline-block;
    }}
    .ph-title {{
        font-size: 2.6rem; font-weight: 700; line-height: 1.1;
        margin: 0 0 0.6rem 0; color: {text} !important;
    }}
    .ph-grad {{
        background: linear-gradient(90deg, {green} 0%, {blue} 100%);
        -webkit-background-clip: text; background-clip: text;
        color: transparent !important; -webkit-text-fill-color: transparent !important;
    }}
    .ph-tagline {{
        font-size: 1.05rem; color: {text_dim} !important;
        max-width: 480px; line-height: 1.6; margin: 0;
    }}

    .ph-stats {{
        position: relative; z-index: 1;
        display: flex; flex-wrap: wrap; gap: 1px;
        background: {border}; border: 1px solid {border};
        border-radius: 16px; overflow: hidden;
        margin: 0 2.4rem 2rem 2.4rem;
    }}
    .ph-stat {{
        background: {panel}; padding: 1.2rem 1.4rem;
        flex: 1 1 150px; min-width: 0;
    }}
    .ph-stat-label {{
        font-family: 'JetBrains Mono', monospace;
        font-size: 0.7rem; color: {text_faint} !important;
        letter-spacing: 0.04em; margin-bottom: 0.4rem;
    }}
    .ph-stat-val-g {{ font-size: 1.8rem; font-weight: 700; color: {green} !important; }}
    .ph-stat-val-b {{ font-size: 1.8rem; font-weight: 700; color: {blue} !important; }}
    .ph-stat-val-d {{ font-size: 0.95rem; font-weight: 500; color: {text_faint} !important; font-family:'JetBrains Mono',monospace; }}

    .ph-sec {{
        display: flex; align-items: center; gap: 0.7rem;
        margin: 0 2.4rem 0.9rem 2.4rem;
    }}
    .ph-sec-num {{
        font-family: 'JetBrains Mono', monospace; font-size: 0.75rem; font-weight: 600;
        color: {text_faint} !important; border: 1px solid {border_st};
        border-radius: 6px; padding: 0.14rem 0.45rem;
    }}
    .ph-sec-title {{ font-size: 1rem; font-weight: 700; color: {text} !important; }}
    .ph-sec::after {{ content:''; flex:1; height:1px; background:{border}; }}

    .ph-mission {{
        position: relative; z-index: 1;
        margin: 0 2.4rem 2rem 2.4rem;
        background: {panel}; border: 1px solid {border};
        border-left: 3px solid {green}; border-radius: 0 16px 16px 0;
        padding: 1.4rem 1.6rem;
    }}
    .ph-mission-q {{
        font-family: 'JetBrains Mono', monospace;
        font-size: 0.84rem; font-weight: 600;
        color: {green} !important; margin-bottom: 0.5rem;
    }}
    .ph-mission-t {{ font-size: 0.96rem; color: {text_dim} !important; line-height: 1.7; }}
    .ph-mission-t strong {{ color: {text} !important; }}

    .ph-rail {{
        position: relative; z-index: 1;
        margin: 0 2.4rem 2.4rem 2.4rem;
        display: flex; flex-wrap: wrap; gap: 0.9rem;
    }}
    .ph-step {{
        background: {panel}; border: 1px solid {border};
        border-radius: 16px; padding: 1.2rem;
        flex: 1 1 calc(25% - 0.7rem); min-width: 190px;
        position: relative;
        transition: border-color 0.2s ease, transform 0.2s ease;
    }}
    .ph-step:hover {{ border-color: {border_st}; transform: translateY(-2px); }}
    .ph-step-conn {{
        position: absolute; top: 1.5rem; right: -0.8rem;
        width: 0.9rem; height: 1px; background: {border_st}; z-index: 2;
    }}
    .ph-call {{
        font-family: 'JetBrains Mono', monospace;
        font-size: 0.85rem; font-weight: 700;
        color: {green} !important; margin-bottom: 0.5rem;
    }}
    .ph-call-b {{ color: {blue} !important; }}
    .ph-step-title {{ font-size: 0.93rem; font-weight: 700; color: {text} !important; margin-bottom: 0.3rem; }}
    .ph-step-desc {{ font-size: 0.83rem; color: {text_dim} !important; line-height: 1.5; }}

    @media (max-width: 900px) {{ .ph-step-conn {{ display:none; }} }}
    @media (max-width: 640px) {{
        .ph-hero {{ padding: 2rem 1.4rem; }}
        .ph-title {{ font-size: 2rem; }}
        .ph-stats,.ph-mission,.ph-rail,.ph-sec {{ margin-left:1.4rem; margin-right:1.4rem; }}
    }}
    </style>
    """, unsafe_allow_html=True)


def _circuit_svg():
    return """
    <svg class="ph-circuit" viewBox="0 0 1200 460" preserveAspectRatio="none" xmlns="http://www.w3.org/2000/svg">
        <path d="M0 90 H180 L220 50 H420" fill="none" stroke="#3ddc97" stroke-width="1.5"/>
        <path d="M0 220 H120 L155 255 H380 L410 220 H600" fill="none" stroke="#3ddc97" stroke-width="1.3"/>
        <path d="M1200 90 H1020 L980 50 H800" fill="none" stroke="#5fb3f5" stroke-width="1.5"/>
        <path d="M1200 220 H1080 L1045 255 H840 L810 220 H640" fill="none" stroke="#5fb3f5" stroke-width="1.3"/>
        <path d="M0 370 H260 L295 400 H520" fill="none" stroke="#3ddc97" stroke-width="1.2"/>
        <path d="M1200 370 H940 L905 400 H700" fill="none" stroke="#5fb3f5" stroke-width="1.2"/>
        <circle cx="420" cy="50" r="3.5" fill="#3ddc97"/>
        <circle cx="600" cy="220" r="3.5" fill="#3ddc97"/>
        <circle cx="800" cy="50" r="3.5" fill="#5fb3f5"/>
        <circle cx="640" cy="220" r="3.5" fill="#5fb3f5"/>
        <circle cx="520" cy="400" r="3" fill="#3ddc97" opacity="0.7"/>
        <circle cx="700" cy="400" r="3" fill="#5fb3f5" opacity="0.7"/>
    </svg>
    """


def _shield_svg(size=116):
    h = int(size * 1.19)
    return f"""<svg width="{size}" height="{h}" viewBox="0 0 160 190" xmlns="http://www.w3.org/2000/svg">
        <defs>
            <linearGradient id="sg" x1="0%" y1="0%" x2="100%" y2="100%">
                <stop offset="0%" stop-color="#3ddc97"/><stop offset="100%" stop-color="#0e9e63"/>
            </linearGradient>
            <linearGradient id="sb" x1="0%" y1="0%" x2="100%" y2="100%">
                <stop offset="0%" stop-color="#5fb3f5"/><stop offset="100%" stop-color="#1c6fc9"/>
            </linearGradient>
            <clipPath id="sc"><path d="M80 8 L146 32 V92 C146 134 116 162 80 180 C44 162 14 134 14 92 V32 Z"/></clipPath>
        </defs>
        <path d="M80 8 L146 32 V92 C146 134 116 162 80 180 C44 162 14 134 14 92 V32 Z" fill="#101723"/>
        <g clip-path="url(#sc)">
            <path d="M14 8 H80 V180 H14 C14 180 46 160 46 130 C46 108 14 100 14 80 C14 60 50 56 50 36 C50 18 14 22 14 8 Z" fill="url(#sg)"/>
            <path d="M146 8 H80 V180 H146 C146 180 114 160 114 130 C114 108 146 100 146 80 C146 60 110 56 110 36 C110 18 146 22 146 8 Z" fill="url(#sb)"/>
        </g>
        <path d="M80 8 L146 32 V92 C146 134 116 162 80 180 C44 162 14 134 14 92 V32 Z" fill="none" stroke="#1e2733" stroke-width="2"/>
        <text x="80" y="108" text-anchor="middle" font-family="JetBrains Mono,monospace" font-size="32" font-weight="700" fill="#0b1118">{{  }}</text>
        <line x1="50" x2="22" y1="30" y2="10" stroke="#3ddc97" stroke-width="2"/>
        <circle cx="20" cy="8" r="3" fill="#3ddc97"/>
        <line x1="110" x2="138" y1="30" y2="10" stroke="#5fb3f5" stroke-width="2"/>
        <circle cx="140" cy="8" r="3" fill="#5fb3f5"/>
        <line x1="14" x2="-6" y1="80" y2="80" stroke="#3ddc97" stroke-width="2"/>
        <circle cx="-8" cy="80" r="3" fill="#3ddc97"/>
        <line x1="146" x2="166" y1="80" y2="80" stroke="#5fb3f5" stroke-width="2"/>
        <circle cx="168" cy="80" r="3" fill="#5fb3f5"/>
    </svg>"""


def _starfield_component(theme):
    """Delivered via components.html so the <script> actually executes."""
    if theme == "light":
        components.html("<div style='height:0'></div>", height=0)
        return

    html = """
    <style>
    body { margin:0; padding:0; background:transparent; overflow:hidden; }
    canvas { position:fixed; top:0; left:0; width:100%; height:100%; pointer-events:none; }
    </style>
    <canvas id="sc"></canvas>
    <script>
    var c = document.getElementById('sc');
    var ctx = c.getContext('2d');
    var W, H, stars = [], raf;

    function resize() {
        W = window.innerWidth; H = window.innerHeight;
        c.width = W; c.height = H;
    }
    function mkStars() {
        stars = [];
        var shapes = ['dot','dot','dot','plus','diamond'];
        var colors = ['#e8edf4','#e8edf4','#3ddc97','#5fb3f5'];
        for (var i = 0; i < 200; i++) {
            stars.push({
                x: Math.random()*W, y: Math.random()*H,
                r: Math.random()*1.6+0.3,
                phase: Math.random()*Math.PI*2,
                spd: Math.random()*0.7+0.2,
                shape: shapes[Math.floor(Math.random()*shapes.length)],
                col: colors[Math.floor(Math.random()*colors.length)]
            });
        }
    }
    function draw(ts) {
        ctx.clearRect(0,0,W,H);
        var t = ts*0.001;
        for (var i=0;i<stars.length;i++) {
            var s=stars[i];
            var a = 0.1 + 0.9*(0.5+0.5*Math.sin(t*s.spd+s.phase));
            ctx.globalAlpha=a; ctx.fillStyle=s.col; ctx.strokeStyle=s.col; ctx.lineWidth=0.9;
            if(s.shape==='plus'){
                var sz=s.r*2.6;
                ctx.beginPath();
                ctx.moveTo(s.x-sz,s.y); ctx.lineTo(s.x+sz,s.y);
                ctx.moveTo(s.x,s.y-sz); ctx.lineTo(s.x,s.y+sz);
                ctx.stroke();
            } else if(s.shape==='diamond'){
                var d=s.r*2.4;
                ctx.beginPath();
                ctx.moveTo(s.x,s.y-d); ctx.lineTo(s.x+d*0.6,s.y);
                ctx.lineTo(s.x,s.y+d); ctx.lineTo(s.x-d*0.6,s.y);
                ctx.closePath(); ctx.fill();
            } else {
                ctx.beginPath(); ctx.arc(s.x,s.y,s.r,0,Math.PI*2); ctx.fill();
            }
        }
        ctx.globalAlpha=1;
        raf=requestAnimationFrame(draw);
    }
    resize(); mkStars(); raf=requestAnimationFrame(draw);
    window.addEventListener('resize',function(){ resize(); mkStars(); });
    </script>
    """
    components.html(html, height=0, scrolling=False)


def render_welcome_page(project_map):
    theme = _get_theme()

    total_repos = len(project_map)
    patches_merged = sum(1 for m in project_map.values() if not m.get("limitations"))
    open_challenges = sum(len(m.get("limitations",[])) for m in project_map.values())

    _inject_base_css(theme)

    # ---------- THEME TOGGLE (real Streamlit button) ----------
    icon   = "☀ LIGHT MODE" if theme == "dark" else "☽ DARK MODE"
    label  = f"Switch to {icon}"
    col_spacer, col_btn = st.columns([6, 1])
    with col_btn:
        if st.button(label, key="ph_theme_toggle", use_container_width=True):
            st.session_state["ph_theme"] = "light" if theme == "dark" else "dark"
            st.rerun()

    # Starfield lives in its own iframe via components.html
    _starfield_component(theme)

    # ---------- ROOT WRAPPER ----------
    st.markdown('<div id="ph-root">', unsafe_allow_html=True)
    st.markdown(_circuit_svg(), unsafe_allow_html=True)

    # ---------- HERO ----------
    st.markdown(f"""
    <div class="ph-hero ph-text ph-fade ph-d1">
        <div>{_shield_svg(110)}</div>
        <div>
            <div class="ph-eyebrow"><span class="ph-dot"></span>OPEN-SOURCE &middot; PYTHON &middot; LIVE CODE</div>
            <div class="ph-title">Py<span class="ph-grad">Source</span> Hub</div>
            <p class="ph-tagline">Read real, working code. Find what's broken. Patch it live.</p>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # ---------- STATS ----------
    st.markdown(f"""
    <div class="ph-stats ph-fade ph-d2">
        <div class="ph-stat">
            <div class="ph-stat-label ph-mono">ACTIVE_REPOS</div>
            <div class="ph-stat-val-g">{total_repos}</div>
        </div>
        <div class="ph-stat">
            <div class="ph-stat-label ph-mono">PATCHES_MERGED</div>
            <div class="ph-stat-val-b">{patches_merged}</div>
        </div>
        <div class="ph-stat">
            <div class="ph-stat-label ph-mono">OPEN_CHALLENGES</div>
            <div class="ph-stat-val-g">{open_challenges}</div>
        </div>
        <div class="ph-stat">
            <div class="ph-stat-label ph-mono">COMMUNITY_PRS</div>
            <div class="ph-stat-val-d">pending API</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # ---------- MISSION ----------
    st.markdown(
        '<div class="ph-sec ph-fade ph-d3">'
        '<span class="ph-sec-num ph-mono">01</span>'
        '<span class="ph-sec-title">Core mission</span></div>',
        unsafe_allow_html=True)
    st.markdown(f"""
    <div class="ph-mission ph-fade ph-d3">
        <div class="ph-mission-q ph-mono">"Read-first, patch-second."</div>
        <div class="ph-mission-t">
            Traditional platforms focus on competitive coding inside isolated browser sandboxes.
            PySource Hub bridges the gap between classroom syntax and professional development
            &mdash; students study working blueprints, discover documented limitations, and submit
            upgrades using real-world Git-Flow workflows.
        </div>
    </div>
    """, unsafe_allow_html=True)

    # ---------- WORKFLOW ----------
    st.markdown(
        '<div class="ph-sec ph-fade ph-d4">'
        '<span class="ph-sec-num ph-mono">02</span>'
        '<span class="ph-sec-title">Contribution workflow</span></div>',
        unsafe_allow_html=True)
    st.markdown("""
    <div class="ph-rail ph-fade ph-d4">
        <div class="ph-step">
            <div class="ph-step-conn"></div>
            <div class="ph-call ph-mono">git_clone<span class="ph-call-b">()</span></div>
            <div class="ph-step-title">Select a repository</div>
            <div class="ph-step-desc">Pick a project from the sidebar index dropdown.</div>
        </div>
        <div class="ph-step">
            <div class="ph-step-conn"></div>
            <div class="ph-call ph-mono">audit<span class="ph-call-b">(limitations)</span></div>
            <div class="ph-step-title">Audit flaws</div>
            <div class="ph-step-desc">Analyze the documented bugs or architectural limitations.</div>
        </div>
        <div class="ph-step">
            <div class="ph-step-conn"></div>
            <div class="ph-call ph-mono">fork<span class="ph-call-b">().patch(bug)</span></div>
            <div class="ph-step-title">Fork &amp; code</div>
            <div class="ph-step-desc">Fork the repository and patch the limitation locally.</div>
        </div>
        <div class="ph-step">
            <div class="ph-call ph-mono">git_push<span class="ph-call-b">() &rarr; PR</span></div>
            <div class="ph-step-title">Pull request</div>
            <div class="ph-step-desc">Submit your PR. Once merged, your logic replaces the blueprint live.</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)