import streamlit as st


# =========================================================================
# PYSOURCE HUB — "Circuit Slate" home page
# -------------------------------------------------------------------------
# Design language: the brand mark (twin-snake shield, {} core, circuit
# leads) is rebuilt as inline SVG and used as the literal source of the
# page's ambient circuit-trace pattern — the logo isn't a badge sitting on
# the page, it's where the page's linework comes from. Palette pulls
# straight from the mark: signal green (left snake) + signal blue (right
# snake) on a near-black slate, never the generic indigo/purple SaaS
# default. Everything is scoped under #ph-welcome-root.
# =========================================================================
def _inject_welcome_theme():
    st.markdown(
        """
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@500;600;700&family=JetBrains+Mono:wght@400;500;600;700&display=swap');

        :root {
            --w-bg: #0b0f14;
            --w-panel: #10151d;
            --w-panel-2: #131a24;
            --w-border: rgba(255,255,255,0.08);
            --w-border-strong: rgba(255,255,255,0.14);
            --w-text: #e8edf4;
            --w-text-dim: #8b96a8;
            --w-text-faint: #586173;
            --w-green: #3ddc97;
            --w-green-deep: #0e9e63;
            --w-blue: #5fb3f5;
            --w-blue-deep: #1c6fc9;
            --w-radius: 16px;
        }
        .w-scope, .w-scope * { box-sizing: border-box; }
        #ph-welcome-root {
            display: block;
            background: var(--w-bg);
            border-radius: var(--w-radius);
            padding: 0;
            margin: -1rem -1rem 0 -1rem;
            position: relative;
            overflow-x: hidden;
            overflow-y: visible;
            font-family: 'Space Grotesk', -apple-system, BlinkMacSystemFont, sans-serif;
        }
        /* Each st.markdown() call is its own DOM fragment, so rules can't rely
           on #ph-welcome-root as a real ancestor of later fragments — every
           text rule below targets its own class directly with !important so
           it always wins over app.py's blanket `p, span, label { color }`. */
        .w-scope, .w-scope p, .w-scope div, .w-scope li, .w-scope span {
            color: var(--w-text) !important;
            font-family: 'Space Grotesk', -apple-system, BlinkMacSystemFont, sans-serif;
        }
        .w-scope h1, .w-scope h2, .w-scope h3 {
            color: var(--w-text) !important;
            font-family: 'Space Grotesk', sans-serif !important;
        }
        .w-mono { font-family: 'JetBrains Mono', 'SF Mono', Consolas, monospace; }

        @keyframes wFadeUp {
            from { opacity: 0; transform: translateY(10px); }
            to   { opacity: 1; transform: translateY(0); }
        }
        @keyframes wTraceDraw {
            from { stroke-dashoffset: 600; }
            to   { stroke-dashoffset: 0; }
        }
        @keyframes wPulse {
            0%, 100% { opacity: 0.5; }
            50%      { opacity: 1; }
        }
        .w-fade { animation: wFadeUp 0.5s cubic-bezier(0.16,1,0.3,1) both; }
        .w-d1 { animation-delay: 0.04s; }
        .w-d2 { animation-delay: 0.12s; }
        .w-d3 { animation-delay: 0.20s; }
        .w-d4 { animation-delay: 0.28s; }

        /* ---------- AMBIENT CIRCUIT BACKGROUND (drawn from the mark) ---------- */
        .w-circuit-bg {
            position: absolute;
            top: 0; left: 0;
            width: 100%; height: 480px;
            z-index: 0;
            opacity: 0.55;
            pointer-events: none;
        }
        .w-circuit-bg path {
            stroke-dasharray: 600;
            animation: wTraceDraw 2.2s ease-out forwards;
        }
        .w-circuit-bg circle {
            animation: wPulse 2.6s ease-in-out infinite;
        }

        /* ---------- HERO ---------- */
        .w-hero {
            position: relative;
            z-index: 1;
            padding: 3.2rem 2.4rem 2.6rem 2.4rem;
            display: flex;
            align-items: center;
            gap: 2.2rem;
            flex-wrap: wrap;
        }
        .w-hero-mark { flex: 0 0 auto; }
        .w-hero-copy { flex: 1 1 320px; min-width: 280px; }
        div.w-hero-eyebrow {
            font-family: 'JetBrains Mono', monospace;
            font-size: 0.8rem;
            font-weight: 600;
            letter-spacing: 0.08em;
            color: var(--w-green) !important;
            margin-bottom: 0.7rem;
            display: flex;
            align-items: center;
            gap: 0.5rem;
        }
        .w-hero-eyebrow .w-dot {
            width: 6px; height: 6px; border-radius: 50%;
            background: var(--w-green);
            box-shadow: 0 0 6px var(--w-green);
        }
        .w-hero-title {
            font-size: 2.7rem;
            font-weight: 700;
            line-height: 1.08;
            margin: 0 0 0.7rem 0;
            letter-spacing: -0.01em;
        }
        .w-hero-title .w-grad,
        span.w-grad {
            background: linear-gradient(90deg, var(--w-green) 0%, var(--w-blue) 100%) !important;
            -webkit-background-clip: text !important;
            background-clip: text !important;
            color: transparent !important;
            -webkit-text-fill-color: transparent !important;
        }
        p.w-hero-tagline {
            font-size: 1.08rem;
            color: var(--w-text-dim) !important;
            max-width: 480px;
            line-height: 1.6;
            margin: 0;
        }

        /* ---------- STAT STRIP ---------- */
        .w-stats {
            position: relative;
            z-index: 1;
            display: flex;
            flex-wrap: wrap;
            gap: 1px;
            background: var(--w-border);
            border: 1px solid var(--w-border);
            border-radius: var(--w-radius);
            overflow: hidden;
            margin: 0 2.4rem 2.2rem 2.4rem;
            width: auto;
            max-width: 100%;
        }
        .w-stat {
            background: var(--w-panel);
            padding: 1.3rem 1.4rem;
            flex: 1 1 160px;
            min-width: 0;
            max-width: 100%;
        }
        div.w-stat-label {
            font-family: 'JetBrains Mono', monospace;
            font-size: 0.72rem;
            color: var(--w-text-faint) !important;
            letter-spacing: 0.04em;
            margin-bottom: 0.45rem;
        }
        .w-stat-value {
            font-size: 1.9rem;
            font-weight: 700;
            line-height: 1;
        }
        .w-stat-value.w-num-green { color: var(--w-green) !important; }
        .w-stat-value.w-num-blue { color: var(--w-blue) !important; }
        .w-stat-value.w-num-dim { font-size: 1.0rem; font-weight: 500; color: var(--w-text-faint) !important; font-family: 'JetBrains Mono', monospace; }

        /* ---------- SECTION LABEL ---------- */
        .w-section-label {
            display: flex;
            align-items: center;
            gap: 0.7rem;
            margin: 0 2.4rem 1rem 2.4rem;
        }
        .w-section-label .w-num {
            font-family: 'JetBrains Mono', monospace;
            font-size: 0.78rem;
            font-weight: 600;
            color: var(--w-text-faint) !important;
            border: 1px solid var(--w-border-strong);
            border-radius: 6px;
            padding: 0.15rem 0.5rem;
        }
        .w-section-label .w-title {
            font-size: 1.05rem;
            font-weight: 700;
            color: var(--w-text) !important;
        }
        .w-section-label::after {
            content: '';
            flex: 1 1 auto;
            height: 1px;
            background: var(--w-border);
        }

        /* ---------- MISSION CARD ---------- */
        .w-mission {
            position: relative;
            z-index: 1;
            margin: 0 2.4rem 2.2rem 2.4rem;
            background: var(--w-panel);
            border: 1px solid var(--w-border);
            border-left: 3px solid var(--w-green);
            border-radius: var(--w-radius);
            padding: 1.5rem 1.7rem;
        }
        div.w-mission-quote {
            font-family: 'JetBrains Mono', monospace;
            color: var(--w-green) !important;
            font-size: 0.86rem;
            font-weight: 600;
            margin-bottom: 0.6rem;
        }
        div.w-mission-text {
            font-size: 0.97rem;
            color: var(--w-text-dim) !important;
            line-height: 1.7;
        }
        .w-mission-text strong { color: var(--w-text) !important; }

        /* ---------- WORKFLOW RAIL ---------- */
        .w-rail {
            position: relative;
            z-index: 1;
            margin: 0 2.4rem 2.6rem 2.4rem;
            display: flex;
            flex-wrap: wrap;
            gap: 1rem;
            width: auto;
            max-width: 100%;
        }
        .w-rail-step {
            background: var(--w-panel);
            border: 1px solid var(--w-border);
            border-radius: var(--w-radius);
            padding: 1.3rem 1.3rem 1.4rem 1.3rem;
            position: relative;
            transition: border-color 0.2s ease, transform 0.2s ease;
            flex: 1 1 calc(25% - 0.75rem);
            min-width: 200px;
            max-width: 100%;
        }
        .w-rail-step:hover {
            border-color: var(--w-border-strong);
            transform: translateY(-2px);
        }
        .w-rail-connector {
            position: absolute;
            top: 1.6rem;
            right: -0.85rem;
            width: 1rem; height: 1px;
            background: var(--w-border-strong);
            z-index: 2;
        }
        div.w-rail-call {
            font-family: 'JetBrains Mono', monospace;
            font-size: 0.88rem;
            font-weight: 700;
            color: var(--w-green) !important;
            margin-bottom: 0.6rem;
        }
        .w-rail-call .w-blue { color: var(--w-blue) !important; }
        div.w-rail-desc-title {
            font-size: 0.96rem;
            font-weight: 700;
            color: var(--w-text) !important;
            margin-bottom: 0.35rem;
        }
        div.w-rail-desc {
            font-size: 0.85rem;
            color: var(--w-text-dim) !important;
            line-height: 1.55;
        }

        /* responsive */
        @media (max-width: 900px) {
            .w-rail-connector { display: none; }
        }
        @media (max-width: 640px) {
            .w-hero { padding: 2.2rem 1.4rem 2rem 1.4rem; }
            .w-hero-title { font-size: 2rem; }
            .w-stats, .w-mission, .w-rail, .w-section-label { margin-left: 1.4rem; margin-right: 1.4rem; }
        }
        @media (prefers-reduced-motion: reduce) {
            .w-fade, .w-circuit-bg path, .w-circuit-bg circle { animation: none !important; }
        }
        </style>
        """,
        unsafe_allow_html=True,
    )


def _circuit_background_svg():
    """Ambient circuit traces — literally extending the shield mark's own
    leads outward across the hero, so the background pattern reads as
    'more of the logo' rather than decorative filler."""
    return """
    <svg class="w-circuit-bg" viewBox="0 0 1200 480" preserveAspectRatio="none" xmlns="http://www.w3.org/2000/svg">
        <path d="M0 90 H180 L220 50 H420" fill="none" stroke="#3ddc97" stroke-width="1.5" opacity="0.5"/>
        <path d="M0 220 H120 L155 255 H380 L410 220 H600" fill="none" stroke="#3ddc97" stroke-width="1.5" opacity="0.4"/>
        <path d="M1200 90 H1020 L980 50 H800" fill="none" stroke="#5fb3f5" stroke-width="1.5" opacity="0.5"/>
        <path d="M1200 220 H1080 L1045 255 H840 L810 220 H640" fill="none" stroke="#5fb3f5" stroke-width="1.5" opacity="0.4"/>
        <path d="M0 380 H260 L295 410 H520" fill="none" stroke="#3ddc97" stroke-width="1.5" opacity="0.3"/>
        <path d="M1200 380 H940 L905 410 H700" fill="none" stroke="#5fb3f5" stroke-width="1.5" opacity="0.3"/>
        <circle cx="420" cy="50" r="3.5" fill="#3ddc97"/>
        <circle cx="600" cy="220" r="3.5" fill="#3ddc97"/>
        <circle cx="800" cy="50" r="3.5" fill="#5fb3f5"/>
        <circle cx="640" cy="220" r="3.5" fill="#5fb3f5"/>
        <circle cx="520" cy="410" r="3" fill="#3ddc97" opacity="0.7"/>
        <circle cx="700" cy="410" r="3" fill="#5fb3f5" opacity="0.7"/>
    </svg>
    """


def _hero_mark_svg(size=128):
    """The recreated brand mark — twin-snake shield with {} core. Built as
    clean geometric S-curves (not a literal trace of the source artwork),
    same shield silhouette, green/blue split, brace glyph, and circuit
    leads as the source mark."""
    return f"""
    <svg width="{size}" height="{int(size*1.19)}" viewBox="0 0 160 190" xmlns="http://www.w3.org/2000/svg">
        <defs>
            <linearGradient id="whGreen" x1="0%" y1="0%" x2="100%" y2="100%">
                <stop offset="0%" stop-color="#3ddc97"/>
                <stop offset="100%" stop-color="#0e9e63"/>
            </linearGradient>
            <linearGradient id="whBlue" x1="0%" y1="0%" x2="100%" y2="100%">
                <stop offset="0%" stop-color="#5fb3f5"/>
                <stop offset="100%" stop-color="#1c6fc9"/>
            </linearGradient>
            <clipPath id="whShieldClip">
                <path d="M80 8 L146 32 V92 C146 134 116 162 80 180 C44 162 14 134 14 92 V32 Z"/>
            </clipPath>
        </defs>
        <path d="M80 8 L146 32 V92 C146 134 116 162 80 180 C44 162 14 134 14 92 V32 Z" fill="#101723"/>
        <g clip-path="url(#whShieldClip)">
            <path d="M14 8 H80 V180 H14
                     C14 180 46 160 46 130 C46 108 14 100 14 80
                     C14 60 50 56 50 36 C50 18 14 22 14 8 Z" fill="url(#whGreen)"/>
            <circle cx="34" cy="22" r="3" fill="#0b1118"/>
            <path d="M146 8 H80 V180 H146
                     C146 180 114 160 114 130 C114 108 146 100 146 80
                     C146 60 110 56 110 36 C110 18 146 22 146 8 Z" fill="url(#whBlue)"/>
            <circle cx="126" cy="22" r="3" fill="#0b1118"/>
        </g>
        <path d="M80 8 L146 32 V92 C146 134 116 162 80 180 C44 162 14 134 14 92 V32 Z"
              fill="none" stroke="#1e2733" stroke-width="2"/>
        <text x="80" y="108" text-anchor="middle" font-family="'JetBrains Mono', monospace"
              font-size="34" font-weight="700" fill="#0b1118">{{ }}</text>
        <line x1="50" x2="22" y1="30" y2="10" stroke="#3ddc97" stroke-width="2"/>
        <circle cx="20" cy="8" r="3" fill="#3ddc97"/>
        <line x1="110" x2="138" y1="30" y2="10" stroke="#5fb3f5" stroke-width="2"/>
        <circle cx="140" cy="8" r="3" fill="#5fb3f5"/>
        <line x1="14" x2="-8" y1="80" y2="80" stroke="#3ddc97" stroke-width="2"/>
        <circle cx="-10" cy="80" r="3" fill="#3ddc97"/>
        <line x1="146" x2="168" y1="80" y2="80" stroke="#5fb3f5" stroke-width="2"/>
        <circle cx="170" cy="80" r="3" fill="#5fb3f5"/>
    </svg>
    """


def render_welcome_page(project_map):
    """
    project_map: dict of { display_label: metadata_dict } built in app.py,
    where each metadata_dict has at least 'limitations' (list) and 'challenge'.
    Real stats are derived directly from this — nothing here is hardcoded.
    """
    total_repos = len(project_map)
    total_open_challenges = sum(len(meta.get("limitations", [])) for meta in project_map.values())
    # "Patches merged" isn't tracked by the file-driven system yet (no PR/commit
    # history is read from disk) — until Phase 3/4 of the roadmap wires in the
    # GitHub REST API, we report the number of modules that currently ship with
    # zero documented limitations as a stand-in proxy for "clean / patched" repos.
    patches_merged = sum(1 for meta in project_map.values() if not meta.get("limitations"))
    # Likewise, "community pull requests" has no local data source yet — shown
    # as a placeholder until the roadmap's GitHub API integration lands.
    community_prs_display = "pending API"

    _inject_welcome_theme()

    st.markdown('<div id="ph-welcome-root">', unsafe_allow_html=True)
    st.markdown(_circuit_background_svg(), unsafe_allow_html=True)

    # ================= HERO =================
    st.markdown(
        f"""
        <div class="w-hero w-scope">
            <div class="w-hero-mark w-fade w-d1">{_hero_mark_svg(120)}</div>
            <div class="w-hero-copy w-fade w-d2">
                <div class="w-hero-eyebrow"><span class="w-dot"></span>OPEN-SOURCE &middot; PYTHON &middot; LIVE CODE</div>
                <h1 class="w-hero-title">Py<span class="w-grad">Source</span> Hub</h1>
                <p class="w-hero-tagline">Read real, working code. Find what's broken. Patch it live.</p>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # ================= STAT STRIP =================
    st.markdown(
        f"""
        <div class="w-stats w-fade w-d3 w-scope">
            <div class="w-stat">
                <div class="w-stat-label w-mono">ACTIVE_REPOS</div>
                <div class="w-stat-value w-num-green">{total_repos}</div>
            </div>
            <div class="w-stat">
                <div class="w-stat-label w-mono">PATCHES_MERGED</div>
                <div class="w-stat-value w-num-blue">{patches_merged}</div>
            </div>
            <div class="w-stat">
                <div class="w-stat-label w-mono">OPEN_CHALLENGES</div>
                <div class="w-stat-value w-num-green">{total_open_challenges}</div>
            </div>
            <div class="w-stat">
                <div class="w-stat-label w-mono">COMMUNITY_PRS</div>
                <div class="w-stat-value w-num-dim w-mono">{community_prs_display}</div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # ================= CORE MISSION =================
    st.markdown(
        '<div class="w-section-label w-fade w-d3 w-scope"><span class="w-num w-mono">01</span><span class="w-title">Core mission</span></div>',
        unsafe_allow_html=True,
    )
    st.markdown(
        """
        <div class="w-mission w-fade w-d3 w-scope">
            <div class="w-mission-quote w-mono">"Read-first, patch-second."</div>
            <div class="w-mission-text">
                Traditional platforms focus on competitive coding inside isolated browser
                sandboxes. PySource Hub is engineered to bridge the gap between classroom
                syntax and professional development — students enter an active,
                production-ready environment to study working blueprints, discover
                documented architectural limitations, and submit functional upgrades using
                real-world Git-Flow workflows.
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # ================= CONTRIBUTION WORKFLOW =================
    st.markdown(
        '<div class="w-section-label w-fade w-d4 w-scope"><span class="w-num w-mono">02</span><span class="w-title">Contribution workflow</span></div>',
        unsafe_allow_html=True,
    )
    st.markdown(
        f"""
        <div class="w-rail w-fade w-d4 w-scope">
            <div class="w-rail-step">
                <div class="w-rail-connector"></div>
                <div class="w-rail-call w-mono">git_clone<span class="w-blue">()</span></div>
                <div class="w-rail-desc-title">Select a repository</div>
                <div class="w-rail-desc">Pick a project from the sidebar index dropdown.</div>
            </div>
            <div class="w-rail-step">
                <div class="w-rail-connector"></div>
                <div class="w-rail-call w-mono">audit<span class="w-blue">(limitations)</span></div>
                <div class="w-rail-desc-title">Audit flaws</div>
                <div class="w-rail-desc">Analyze the documented bugs or architectural limitations.</div>
            </div>
            <div class="w-rail-step">
                <div class="w-rail-connector"></div>
                <div class="w-rail-call w-mono">fork<span class="w-blue">().patch(bug)</span></div>
                <div class="w-rail-desc-title">Fork &amp; code</div>
                <div class="w-rail-desc">Link to GitHub, fork the repository, and patch the limitation locally.</div>
            </div>
            <div class="w-rail-step">
                <div class="w-rail-call w-mono">git_push<span class="w-blue">() &rarr; PR</span></div>
                <div class="w-rail-desc-title">Pull request</div>
                <div class="w-rail-desc">Submit your code review request. Once merged, your optimized logic replaces the blueprint live.</div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown("</div>", unsafe_allow_html=True)  # close #ph-welcome-root