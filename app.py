import streamlit as st
import requests
import streamlit.components.v1 as components

# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="Language Translation Tool",
    page_icon="🌐",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ============================================================
# CUSTOM CSS — MIDNIGHT NAVY + ELECTRIC BLUE
# ============================================================

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

* {
    font-family: 'Inter', sans-serif;
}

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}

/* ============================================================
   MAIN BACKGROUND
   ============================================================ */

.stApp {
    background:
        radial-gradient(
            circle at 8% 8%,
            rgba(37, 99, 235, 0.22),
            transparent 24%
        ),
        radial-gradient(
            circle at 92% 20%,
            rgba(14, 165, 255, 0.14),
            transparent 25%
        ),
        radial-gradient(
            circle at 85% 88%,
            rgba(37, 99, 235, 0.16),
            transparent 27%
        ),
        linear-gradient(
            135deg,
            #020B24 0%,
            #071735 52%,
            #020B24 100%
        );

    color: #F8FAFC;
    min-height: 100vh;
}

/* ============================================================
   PAGE CONTAINER
   ============================================================ */

.block-container {
    max-width: 1250px;
    padding-top: 1.2rem !important;
    padding-bottom: 2.5rem !important;
}

/* ============================================================
   HIDE STREAMLIT DEFAULT ELEMENTS
   ============================================================ */

#MainMenu {
    visibility: hidden;
}

footer {
    visibility: hidden;
}

header {
    background: transparent !important;
}

/* ============================================================
   AMBIENT BLUE GLOW
   ============================================================ */

.stApp::before {
    content: "";
    position: fixed;
    width: 360px;
    height: 360px;
    left: -180px;
    top: 30%;
    border-radius: 50%;
    background: rgba(37, 99, 235, 0.18);
    filter: blur(110px);
    pointer-events: none;
    z-index: 0;
}

.stApp::after {
    content: "";
    position: fixed;
    width: 320px;
    height: 320px;
    right: -150px;
    bottom: 8%;
    border-radius: 50%;
    background: rgba(14, 165, 255, 0.14);
    filter: blur(105px);
    pointer-events: none;
    z-index: 0;
}

/* ============================================================
   HERO SECTION
   ============================================================ */

.hero-section {
    position: relative;
    text-align: center;
    padding: 12px 10px 30px 10px;
    overflow: hidden;
}

/* subtle dotted world-map-style background */

.hero-section::before {
    content: "";
    position: absolute;
    width: 900px;
    height: 250px;
    left: 50%;
    top: 0;
    transform: translateX(-50%);

    background-image:
        radial-gradient(
            circle,
            rgba(56, 189, 248, 0.55) 1px,
            transparent 1.4px
        );

    background-size: 8px 8px;

    opacity: 0.10;

    mask-image: linear-gradient(
        to bottom,
        black,
        transparent
    );

    -webkit-mask-image: linear-gradient(
        to bottom,
        black,
        transparent
    );

    pointer-events: none;
}

/* ============================================================
   GLOBE
   ============================================================ */

.globe-area {
    position: relative;
    width: 105px;
    height: 105px;
    margin: 0 auto 12px auto;
}

.globe {
    position: absolute;
    width: 78px;
    height: 78px;
    left: 13px;
    top: 13px;

    display: flex;
    align-items: center;
    justify-content: center;

    border-radius: 50%;

    font-size: 50px;

    background:
        radial-gradient(
            circle at 32% 28%,
            #8DDCFF 0%,
            #38BDF8 18%,
            #2563EB 55%,
            #102B70 100%
        );

    border: 2px solid rgba(56, 189, 248, 0.75);

    box-shadow:
        0 0 20px rgba(14, 165, 255, 0.65),
        0 0 55px rgba(37, 99, 235, 0.35),
        inset -10px -12px 20px rgba(0, 0, 0, 0.25);

    z-index: 2;
}

/* Globe orbit */

.globe-orbit {
    position: absolute;
    width: 112px;
    height: 38px;
    left: -3px;
    top: 34px;

    border: 2px solid rgba(56, 189, 248, 0.58);
    border-radius: 50%;

    transform: rotate(-18deg);

    box-shadow:
        0 0 10px rgba(14, 165, 255, 0.20);
}

/* Small language bubbles */

.language-bubble {
    position: absolute;

    width: 30px;
    height: 30px;

    border-radius: 9px;

    display: flex;
    align-items: center;
    justify-content: center;

    color: white;
    font-size: 14px;
    font-weight: 700;

    background:
        linear-gradient(
            135deg,
            #2563EB,
            #0EA5FF
        );

    border: 1px solid rgba(56, 189, 248, 0.55);

    box-shadow:
        0 0 15px rgba(14, 165, 255, 0.30);

    z-index: 3;
}

.language-bubble.one {
    left: -8px;
    top: 4px;
}

.language-bubble.two {
    right: -5px;
    top: 28px;

    background:
        linear-gradient(
            135deg,
            #4F46E5,
            #8B5CF6
        );
}

.language-bubble.three {
    right: 4px;
    bottom: 0;

    background:
        linear-gradient(
            135deg,
            #0284C7,
            #06B6D4
        );
}

/* ============================================================
   HERO TITLE
   ============================================================ */

.hero-title {
    position: relative;

    margin: 0;

    font-size: clamp(
        2.2rem,
        4vw,
        3.7rem
    );

    font-weight: 800;

    letter-spacing: -1.5px;

    line-height: 1.1;
}

.hero-title .white {
    color: #F8FAFC;
}

.hero-title .blue {
    background:
        linear-gradient(
            90deg,
            #38BDF8,
            #0EA5FF,
            #60A5FA
        );

    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;

    background-clip: text;
}

.hero-subtitle {
    position: relative;

    margin-top: 12px;
    margin-bottom: 16px;

    color: #AFC1DF;

    font-size: 1rem;
    font-weight: 400;
}

.hero-underline {
    width: 110px;
    height: 4px;

    margin: auto;

    border-radius: 20px;

    background:
        linear-gradient(
            90deg,
            #2563EB,
            #0EA5FF,
            #38BDF8
        );

    box-shadow:
        0 0 16px rgba(14, 165, 255, 0.55);
}

/* ============================================================
   MAIN GLASS CARD
   ============================================================ */

.main-card {
    position: relative;

    background:
        linear-gradient(
            145deg,
            rgba(16, 31, 61, 0.96),
            rgba(7, 23, 53, 0.96)
        );

    border-radius: 24px;

    padding: 30px 34px;

    border: 1px solid rgba(37, 99, 235, 0.55);

    box-shadow:
        0 25px 70px rgba(0, 0, 0, 0.42),
        0 0 35px rgba(14, 165, 255, 0.10),
        inset 0 1px 0 rgba(255, 255, 255, 0.045);

    backdrop-filter: blur(18px);
    -webkit-backdrop-filter: blur(18px);
}

/* glowing top edge */

.main-card::before {
    content: "";

    position: absolute;

    top: -1px;
    left: 35px;

    width: 125px;
    height: 3px;

    border-radius: 20px;

    background:
        linear-gradient(
            90deg,
            #2563EB,
            #0EA5FF,
            #38BDF8
        );

    box-shadow:
        0 0 16px rgba(14, 165, 255, 0.70);
}

/* ============================================================
   SECTION HEADINGS
   ============================================================ */

.section-heading {
    display: flex;
    align-items: center;

    gap: 13px;

    color: #F8FAFC;

    font-size: 20px;
    font-weight: 700;

    margin-top: 2px;
    margin-bottom: 14px;
}

.section-icon {
    width: 42px;
    height: 42px;

    display: flex;
    align-items: center;
    justify-content: center;

    border-radius: 13px;

    color: white;

    font-size: 20px;

    background:
        linear-gradient(
            135deg,
            #2563EB,
            #0EA5FF
        );

    border: 1px solid rgba(56, 189, 248, 0.50);

    box-shadow:
        0 0 18px rgba(14, 165, 255, 0.22);
}

/* ============================================================
   TEXT AREA
   ============================================================ */

textarea {
    border-radius: 17px !important;

    border: 1px solid rgba(37, 99, 235, 0.52) !important;

    background:
        linear-gradient(
            145deg,
            #111F3B,
            #0C1933
        ) !important;

    color: #F8FAFC !important;

    font-size: 17px !important;

    line-height: 1.6 !important;

    padding: 17px !important;

    box-shadow:
        inset 0 1px 0 rgba(255,255,255,0.03),
        0 8px 24px rgba(0,0,0,0.18);
}

textarea:focus {
    border-color: #0EA5FF !important;

    box-shadow:
        0 0 0 1px rgba(14,165,255,0.30),
        0 0 22px rgba(14,165,255,0.14) !important;
}

textarea::placeholder {
    color: #7185A8 !important;
}

/* ============================================================
   LANGUAGE LABELS
   ============================================================ */

.language-label {
    font-size: 12px;

    color: #AFC1DF;

    font-weight: 600;

    text-transform: uppercase;

    letter-spacing: 1px;

    margin-bottom: 7px;
}

/* ============================================================
   SELECT BOXES
   ============================================================ */

div[data-baseweb="select"] > div {
    border-radius: 15px !important;

    border: 1px solid rgba(37, 99, 235, 0.52) !important;

    background:
        linear-gradient(
            145deg,
            #111F3B,
            #0C1933
        ) !important;

    min-height: 56px !important;

    box-shadow:
        inset 0 1px 0 rgba(255,255,255,0.03),
        0 6px 20px rgba(0,0,0,0.16);
}

div[data-baseweb="select"] > div:hover {
    border-color: #0EA5FF !important;

    box-shadow:
        0 0 18px rgba(14,165,255,0.16);
}

div[data-baseweb="select"] span {
    color: #F8FAFC !important;
}

div[data-baseweb="select"] svg {
    fill: #AFC1DF !important;
}

/* ============================================================
   LANGUAGE ARROW
   ============================================================ */

.language-arrow {
    height: 100%;

    min-height: 70px;

    display: flex;

    align-items: center;

    justify-content: center;
}

.arrow-circle {
    width: 52px;
    height: 52px;

    border-radius: 50%;

    display: flex;

    align-items: center;

    justify-content: center;

    color: #FFFFFF;

    font-size: 25px;

    font-weight: 700;

    background:
        linear-gradient(
            135deg,
            #2563EB,
            #0EA5FF
        );

    border: 2px solid rgba(56, 189, 248, 0.65);

    box-shadow:
        0 0 18px rgba(14, 165, 255, 0.40),
        0 0 35px rgba(37, 99, 235, 0.20);

    transition: all 0.25s ease;
}

.arrow-circle:hover {
    transform: scale(1.07);

    box-shadow:
        0 0 25px rgba(14, 165, 255, 0.60);
}

/* ============================================================
   TRANSLATE BUTTON
   ============================================================ */

div.stButton > button {
    width: 100%;

    height: 58px;

    border-radius: 15px !important;

    border: 1px solid rgba(56, 189, 248, 0.55) !important;

    color: #FFFFFF !important;

    font-size: 18px !important;

    font-weight: 700 !important;

    background:
        linear-gradient(
            90deg,
            #2563EB 0%,
            #0EA5FF 50%,
            #2563EB 100%
        ) !important;

    box-shadow:
        0 9px 30px rgba(14, 165, 255, 0.28),
        inset 0 1px 0 rgba(255,255,255,0.18);

    transition:
        transform 0.2s ease,
        box-shadow 0.2s ease !important;
}

div.stButton > button:hover {
    transform: translateY(-2px);

    box-shadow:
        0 13px 38px rgba(14, 165, 255, 0.42),
        0 0 20px rgba(37, 99, 235, 0.20) !important;
}

div.stButton > button:active {
    transform: translateY(0);
}

/* ============================================================
   RESULT HEADING
   ============================================================ */

.result-heading {
    display: flex;

    align-items: center;

    gap: 13px;

    color: #F8FAFC;

    font-size: 20px;

    font-weight: 700;

    margin-top: 28px;

    margin-bottom: 12px;
}

.result-icon {
    width: 42px;
    height: 42px;

    border-radius: 50%;

    display: flex;

    align-items: center;

    justify-content: center;

    background:
        linear-gradient(
            135deg,
            #22C55E,
            #16A34A
        );

    border: 1px solid rgba(74, 222, 128, 0.55);

    color: white;

    font-size: 21px;

    box-shadow:
        0 0 18px rgba(34,197,94,0.30);
}

/* ============================================================
   FOOTER
   ============================================================ */

.footer {
    text-align: center;

    color: #647A9F;

    font-size: 13px;

    margin-top: 24px;

    padding-top: 16px;
}

.footer-highlight {
    color: #38BDF8;
}

/* ============================================================
   MOBILE
   ============================================================ */

@media (max-width: 768px) {

    .block-container {
        padding-left: 1rem !important;
        padding-right: 1rem !important;
    }

    .main-card {
        padding: 22px 18px;
        border-radius: 20px;
    }

    .hero-title {
        font-size: 2.1rem;
    }

    .hero-subtitle {
        font-size: 0.9rem;
    }

    .arrow-circle {
        width: 46px;
        height: 46px;
        font-size: 22px;
    }

    .section-heading {
        font-size: 18px;
    }

    .translated-text {
        font-size: 1rem;
    }
}

</style>
""", unsafe_allow_html=True)


# ============================================================
# HEADER
# ============================================================

st.html("""
<div class="hero-section">

    <div class="globe-area">

        <div class="globe-orbit"></div>

        <div class="globe">
            🌐
        </div>

        <div class="language-bubble one">
            A
        </div>

        <div class="language-bubble two">
            文
        </div>

        <div class="language-bubble three">
            अ
        </div>

    </div>

    <div class="hero-title">
        <span class="white">Language </span>
        <span class="blue">Translation Tool</span>
    </div>

    <div class="hero-subtitle">
        Translate text quickly and easily between multiple languages.
    </div>

    <div class="hero-underline"></div>

</div>
""")


# ============================================================
# MAIN CARD
# ============================================================

st.markdown(
    '<div class="main-card">',
    unsafe_allow_html=True
)


# ============================================================
# ENTER TEXT
# ============================================================

st.markdown("""
<div class="section-heading">
    <div class="section-icon">✎</div>
    <div>Enter Text</div>
</div>
""", unsafe_allow_html=True)

text = st.text_area(
    "Text to translate",
    placeholder="Type or paste the text you want to translate...",
    height=155,
    label_visibility="collapsed"
)


# ============================================================
# LANGUAGES
# ============================================================

languages = {
    "English": "en",
    "French": "fr",
    "German": "de",
    "Hindi": "hi",
    "Italian": "it",
    "Japanese": "ja",
    "Korean": "ko",
    "Portuguese": "pt",
    "Russian": "ru",
    "Spanish": "es",
    "Arabic": "ar",
    "Bengali": "bn",
    "Chinese": "zh",
    "Dutch": "nl",
    "Greek": "el",
    "Indonesian": "id",
    "Persian": "fa",
    "Polish": "pl",
    "Romanian": "ro",
    "Swedish": "sv",
    "Thai": "th",
    "Turkish": "tr",
    "Ukrainian": "uk",
    "Urdu": "ur",
    "Vietnamese": "vi"
}

st.markdown("""
<div class="section-heading" style="margin-top: 28px;">
    <div class="section-icon">文</div>
    <div>Select Languages</div>
</div>
""", unsafe_allow_html=True)


# ============================================================
# LANGUAGE SELECTION
# ============================================================

col1, arrow_col, col2 = st.columns(
    [5, 1, 5],
    gap="medium"
)

with col1:

    st.markdown(
        '<div class="language-label">Source Language</div>',
        unsafe_allow_html=True
    )

    source_language = st.selectbox(
        "Source Language",
        list(languages.keys()),
        label_visibility="collapsed"
    )

with arrow_col:

    st.markdown("""
    <div class="language-arrow">
        <div class="arrow-circle">→</div>
    </div>
    """, unsafe_allow_html=True)

with col2:

    st.markdown(
        '<div class="language-label">Target Language</div>',
        unsafe_allow_html=True
    )

    target_language = st.selectbox(
        "Target Language",
        list(languages.keys()),
        index=3,
        label_visibility="collapsed"
    )


# ============================================================
# TRANSLATE BUTTON
# ============================================================

st.markdown("<br>", unsafe_allow_html=True)

translate_clicked = st.button(
    "🌐  Translate",
    type="primary",
    use_container_width=True
)


# ============================================================
# TRANSLATION
# ============================================================

if translate_clicked:

    if not text.strip():

        st.warning(
            "⚠️ Please enter some text to translate."
        )

    elif source_language == target_language:

        st.info(
            "ℹ️ Please select different source and target languages."
        )

    else:

        try:

            response = requests.post(
                "http://127.0.0.1:5000/translate",
                data={
                    "q": text,
                    "source": languages[source_language],
                    "target": languages[target_language],
                    "format": "text"
                },
                timeout=15
            )

            if response.status_code == 200:

                result = response.json()
                translated_text = result["translatedText"]

                # --------------------------------------------
                # RESULT HEADING
                # --------------------------------------------

                st.markdown("""
                <div class="result-heading">
                    <div class="result-icon">✓</div>
                    <div>Translated Text</div>
                </div>
                """, unsafe_allow_html=True)

                # --------------------------------------------
                # ESCAPE TRANSLATED TEXT
                # --------------------------------------------

                escaped_text = (
                    translated_text
                    .replace("&", "&amp;")
                    .replace("<", "&lt;")
                    .replace(">", "&gt;")
                    .replace('"', "&quot;")
                    .replace("'", "&#39;")
                    .replace("\n", "<br>")
                )

                # --------------------------------------------
                # RESULT BOX
                # --------------------------------------------

                html_code = f"""
                <div style="
                    background: linear-gradient(
                        135deg,
                        #063B37,
                        #07332F
                    );
                    border: 1px solid #22C55E;
                    border-radius: 16px;
                    padding: 20px 20px 20px 24px;
                    min-height: 85px;
                    display: flex;
                    align-items: center;
                    justify-content: space-between;
                    gap: 20px;
                    box-sizing: border-box;
                    box-shadow:
                        0 0 20px rgba(34,197,94,0.08);
                ">

                    <div style="
                        color: #F8FAFC;
                        font-size: 22px;
                        font-weight: 600;
                        line-height: 1.5;
                        word-break: break-word;
                        flex: 1;
                    ">
                        {escaped_text}
                    </div>

                    <button
                        onclick="copyTranslation()"
                        style="
                            background: #0A4A43;
                            color: #F8FAFC;
                            border: 1px solid #22C55E;
                            border-radius: 11px;
                            padding: 10px 17px;
                            font-size: 15px;
                            font-weight: 600;
                            cursor: pointer;
                            white-space: nowrap;
                        "
                    >
                        📋 Copy
                    </button>

                    <script>
                        function copyTranslation() {{

                            const text = {translated_text!r};

                            navigator.clipboard.writeText(text)
                            .then(function() {{

                                const buttons =
                                    document.querySelectorAll(
                                        "button"
                                    );

                                const button =
                                    buttons[buttons.length - 1];

                                button.innerHTML = "✓ Copied";

                                setTimeout(function() {{
                                    button.innerHTML = "📋 Copy";
                                }}, 1500);

                            }});

                        }}
                    </script>

                </div>
                """

                components.html(
                    html_code,
                    height=125
                )

            else:

                st.error(
                    f"❌ Translation failed. "
                    f"Server returned status code "
                    f"{response.status_code}."
                )

        except requests.exceptions.RequestException:

            st.error(
                "❌ Unable to connect to the translation service. "
                "Please make sure LibreTranslate is running."
            )


# ============================================================
# CLOSE CARD
# ============================================================

st.markdown(
    "</div>",
    unsafe_allow_html=True
)


# ============================================================
# FOOTER
# ============================================================

st.html("""
<div class="footer">
    Built with <span class="footer-highlight">♥</span>
    using Python • Streamlit • LibreTranslate
</div>
""")
