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
# CUSTOM CSS
# ============================================================

st.markdown("""
<style>

.stApp {
    background:
        radial-gradient(
            circle at 5% 5%,
            rgba(123, 72, 255, 0.22),
            transparent 20%
        ),
        radial-gradient(
            circle at 95% 95%,
            rgba(210, 80, 255, 0.20),
            transparent 22%
        ),
        linear-gradient(
            135deg,
            #f4f7ff 0%,
            #eef0ff 45%,
            #f8f2ff 100%
        );
}

.block-container {
    max-width: 1350px;
    padding-top: 2rem;
    padding-bottom: 2rem;
}

/* Main application card */

.main-card {
    background: rgba(255, 255, 255, 0.94);
    border-radius: 28px;
    padding: 40px 45px;
    box-shadow:
        0 20px 60px rgba(58, 70, 140, 0.15),
        0 4px 15px rgba(58, 70, 140, 0.07);
    border: 1px solid rgba(255, 255, 255, 0.9);
}

/* Section headings */

.section-heading {
    display: flex;
    align-items: center;
    gap: 15px;
    color: #172b75;
    font-size: 25px;
    font-weight: 750;
    margin-top: 5px;
    margin-bottom: 15px;
}

.section-icon {
    width: 48px;
    height: 48px;
    display: flex;
    align-items: center;
    justify-content: center;
    border-radius: 50%;
    color: white;
    font-size: 24px;
    background: linear-gradient(
        135deg,
        #7c3aed,
        #3b82f6
    );
    box-shadow:
        0 7px 18px rgba(100, 70, 220, 0.28);
}

/* Text area */

textarea {
    border-radius: 16px !important;
    border: 2px solid #d6ddff !important;
    background: #ffffff !important;
    font-size: 18px !important;
}

textarea:focus {
    border-color: #7655e8 !important;
    box-shadow:
        0 0 0 2px rgba(118, 85, 232, 0.12) !important;
}

/* Language labels */

.language-label {
    font-size: 16px;
    color: #172b75;
    font-weight: 600;
    margin-bottom: 6px;
}

/* Select boxes */

div[data-baseweb="select"] > div {
    border-radius: 16px !important;
    border: 2px solid #d6ddff !important;
    background: #ffffff !important;
    min-height: 58px;
}

/* Arrow */

.language-arrow {
    height: 100%;
    min-height: 70px;
    display: flex;
    align-items: center;
    justify-content: center;
}

.arrow-circle {
    width: 50px;
    height: 50px;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    color: white;
    font-size: 27px;
    font-weight: bold;
    background: linear-gradient(
        135deg,
        #8b5cf6,
        #3b82f6
    );
    box-shadow:
        0 8px 20px rgba(90, 80, 220, 0.28);
}

/* Translate button */

div.stButton > button {
    width: 100%;
    height: 62px;
    border-radius: 18px;
    border: none;
    color: white !important;
    font-size: 21px;
    font-weight: 700;
    background: linear-gradient(
        90deg,
        #8b35df 0%,
        #5c4ce8 45%,
        #087df2 100%
    );
    box-shadow:
        0 10px 25px rgba(76, 82, 220, 0.30);
    transition: all 0.2s ease;
}

div.stButton > button:hover {
    transform: translateY(-2px);
    box-shadow:
        0 14px 30px rgba(76, 82, 220, 0.38);
}

/* Result heading */

.result-heading {
    display: flex;
    align-items: center;
    gap: 14px;
    color: #164e63;
    font-size: 25px;
    font-weight: 750;
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
    background: linear-gradient(
        135deg,
        #42b857,
        #16833b
    );
    color: white;
    font-size: 23px;
}

/* Footer */

.footer {
    text-align: center;
    color: #4c5b8a;
    font-size: 15px;
    margin-top: 25px;
    padding-top: 20px;
    border-top: 1px solid rgba(100, 120, 180, 0.18);
}

</style>
""", unsafe_allow_html=True)

# ============================================================
# HEADER
# ============================================================

st.html("""
<div style="
    text-align: center;
    padding: 25px 10px 35px 10px;
">

    <div style="
        font-size: 58px;
        margin-bottom: 8px;
    ">
        🌐
    </div>

    <div style="
        font-size: 48px;
        font-weight: 800;
        letter-spacing: -1px;
        background: linear-gradient(
            90deg,
            #172b75,
            #7424d9,
            #172b75
        );
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    ">
        Language Translation Tool
    </div>

    <div style="
        font-size: 19px;
        color: #4d5a82;
        margin-top: 10px;
    ">
        Translate text quickly and easily between multiple languages.
    </div>

    <div style="
        width: 100px;
        height: 4px;
        margin: 18px auto 0 auto;
        border-radius: 10px;
        background: linear-gradient(
            90deg,
            #7424d9,
            #3284ff
        );
    ">
    </div>

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
                        #effbea,
                        #e7f8e8
                    );
                    border: 2px solid #b9e2bd;
                    border-left: 7px solid #249447;
                    border-radius: 16px;
                    padding: 20px 20px 20px 24px;
                    min-height: 85px;
                    display: flex;
                    align-items: center;
                    justify-content: space-between;
                    gap: 20px;
                    box-sizing: border-box;
                ">

                    <div style="
                        color: #176b39;
                        font-size: 23px;
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
                            background: white;
                            color: #176b39;
                            border: 2px solid #54a96b;
                            border-radius: 12px;
                            padding: 11px 18px;
                            font-size: 16px;
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
<div style="
    text-align: center;
    color: #4c5b8a;
    font-size: 15px;
    margin-top: 25px;
    padding-top: 20px;
">
    Built with ❤️ using Python • Streamlit • LibreTranslate
</div>
""")
