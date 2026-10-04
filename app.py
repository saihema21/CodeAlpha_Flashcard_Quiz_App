import streamlit as st

# =========================================================
# PAGE CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="FlashLearn | Flashcard Quiz",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =========================================================
# CUSTOM CSS
# =========================================================

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}

.block-container {
    max-width: 1250px;
    padding-top: 2rem;
    padding-bottom: 2rem;
}

/* Header */

.hero {
    padding: 30px 35px;
    border-radius: 24px;
    background: linear-gradient(135deg, #111827, #374151);
    color: white;
    margin-bottom: 25px;
}

.hero-title {
    font-size: 38px;
    font-weight: 800;
    margin-bottom: 5px;
}

.hero-subtitle {
    font-size: 16px;
    color: #d1d5db;
}

/* Statistics */

.stat-card {
    padding: 22px;
    border-radius: 18px;
    background: #ffffff;
    border: 1px solid #e5e7eb;
    box-shadow: 0 4px 15px rgba(0,0,0,0.05);
}

.stat-title {
    font-size: 14px;
    color: #6b7280;
    font-weight: 600;
}

.stat-value {
    font-size: 30px;
    font-weight: 800;
    margin-top: 5px;
}

/* Flashcard */

.flashcard {
    background: linear-gradient(145deg, #ffffff, #f8fafc);
    border: 1px solid #e2e8f0;
    border-radius: 26px;
    padding: 55px 45px;
    min-height: 330px;
    display: flex;
    flex-direction: column;
    justify-content: center;
    text-align: center;
    box-shadow: 0 12px 35px rgba(15,23,42,0.08);
    margin: 20px 0;
}

.card-label {
    font-size: 13px;
    font-weight: 700;
    color: #6b7280;
    text-transform: uppercase;
    letter-spacing: 1px;
    margin-bottom: 20px;
}

.card-question {
    font-size: 31px;
    font-weight: 800;
    color: #111827;
    line-height: 1.3;
}

.card-answer {
    font-size: 20px;
    color: #374151;
    line-height: 1.7;
    margin-top: 20px;
}

.answer-box {
    margin-top: 25px;
    padding: 18px;
    border-radius: 14px;
    background: #f1f5f9;
}

/* Section */

.section-title {
    font-size: 24px;
    font-weight: 800;
    color: #111827;
    margin-top: 30px;
}

/* Sidebar */

[data-testid="stSidebar"] {
    border-right: 1px solid #e5e7eb;
}

.sidebar-title {
    font-size: 23px;
    font-weight: 800;
}

/* Buttons */

.stButton > button {
    border-radius: 12px;
    min-height: 45px;
    font-weight: 600;
}

/* Footer */

.footer {
    text-align: center;
    padding: 25px;
    color: #6b7280;
    font-size: 13px;
}

</style>
""", unsafe_allow_html=True)


# =========================================================
# SESSION STATE
# =========================================================

if "flashcards" not in st.session_state:

    st.session_state.flashcards = [

        {
            "question": "What is Artificial Intelligence?",
            "answer": "Artificial Intelligence is the simulation of human intelligence in machines."
        },

        {
            "question": "What does ML stand for?",
            "answer": "ML stands for Machine Learning."
        },

        {
            "question": "What is Deep Learning?",
            "answer": "Deep Learning is a subset of Machine Learning that uses artificial neural networks with multiple layers to learn complex patterns from large amounts of data."
        },

        {
            "question": "What is Python?",
            "answer": "Python is a high-level, interpreted programming language widely used in web development, data science, automation and AI."
        },

        {
            "question": "What does API stand for?",
            "answer": "API stands for Application Programming Interface. It allows different software applications to communicate with each other."
        }

    ]


if "current_card" not in st.session_state:
    st.session_state.current_card = 0


if "show_answer" not in st.session_state:
    st.session_state.show_answer = False


# =========================================================
# SIDEBAR
# =========================================================

with st.sidebar:

    st.markdown(
        '<div class="sidebar-title">🧠 FlashLearn</div>',
        unsafe_allow_html=True
    )

    st.caption("Smart learning through interactive flashcards")

    st.divider()

    st.subheader("➕ Create Flashcard")

    new_question = st.text_input(
        "Question",
        placeholder="Enter your question..."
    )

    new_answer = st.text_area(
        "Answer",
        placeholder="Enter the answer..."
    )

    if st.button(
        "➕ Add Flashcard",
        use_container_width=True
    ):

        if new_question.strip() and new_answer.strip():

            st.session_state.flashcards.append(
                {
                    "question": new_question.strip(),
                    "answer": new_answer.strip()
                }
            )

            st.success("Flashcard added successfully!")

            st.rerun()

        else:

            st.warning("Please enter both fields.")

    st.divider()

    st.subheader("📊 Study Statistics")

    st.metric(
        "Total Flashcards",
        len(st.session_state.flashcards)
    )

    st.metric(
        "Current Card",
        st.session_state.current_card + 1
    )


# =========================================================
# HERO HEADER
# =========================================================

st.markdown("""
<div class="hero">

<div class="hero-title">
🧠 FlashLearn
</div>

<div class="hero-subtitle">
Interactive Flashcard Quiz Platform • Learn smarter, one card at a time.
</div>

</div>
""", unsafe_allow_html=True)


# =========================================================
# TOP STATISTICS
# =========================================================

total = len(st.session_state.flashcards)

current = st.session_state.current_card

if total > 0:

    card_number = current + 1

else:

    card_number = 0


c1, c2, c3 = st.columns(3)


with c1:

    st.markdown(
        f"""
        <div class="stat-card">
        <div class="stat-title">TOTAL CARDS</div>
        <div class="stat-value">{total}</div>
        </div>
        """,
        unsafe_allow_html=True
    )


with c2:

    st.markdown(
        f"""
        <div class="stat-card">
        <div class="stat-title">CURRENT CARD</div>
        <div class="stat-value">{card_number}</div>
        </div>
        """,
        unsafe_allow_html=True
    )


with c3:

    percentage = int((card_number / total) * 100) if total else 0

    st.markdown(
        f"""
        <div class="stat-card">
        <div class="stat-title">STUDY PROGRESS</div>
        <div class="stat-value">{percentage}%</div>
        </div>
        """,
        unsafe_allow_html=True
    )


# =========================================================
# STUDY AREA
# =========================================================

st.markdown(
    '<div class="section-title">📚 Study Mode</div>',
    unsafe_allow_html=True
)


if total == 0:

    st.info(
        "Your flashcard collection is empty. "
        "Use the sidebar to create your first card."
    )

else:

    card = st.session_state.flashcards[current]

    # Progress
    st.progress(card_number / total)

    st.caption(
        f"Card {card_number} of {total}"
    )

    # -----------------------------------------
    # CARD
    # -----------------------------------------

    if st.session_state.show_answer:

        st.markdown(
            f"""
            <div class="flashcard">

                <div class="card-label">
                    QUESTION
                </div>

                <div class="card-question">
                    {card["question"]}
                </div>

                <div class="answer-box">

                    <div class="card-label">
                        ANSWER
                    </div>

                    <div class="card-answer">
                        {card["answer"]}
                    </div>

                </div>

            </div>
            """,
            unsafe_allow_html=True
        )

    else:

        st.markdown(
            f"""
            <div class="flashcard">

                <div class="card-label">
                    QUESTION
                </div>

                <div class="card-question">
                    {card["question"]}
                </div>

                <div class="answer-box">

                    <div class="card-answer">
                        🔒 Answer hidden
                    </div>

                    <div style="color:#6b7280;">
                        Click "Show Answer" below to reveal it.
                    </div>

                </div>

            </div>
            """,
            unsafe_allow_html=True
        )


    # =====================================================
    # NAVIGATION
    # =====================================================

    col1, col2, col3 = st.columns([1, 1.3, 1])


    with col1:

        if st.button(
            "⬅️ Previous",
            use_container_width=True
        ):

            st.session_state.current_card = (
                current - 1
            ) % total

            st.session_state.show_answer = False

            st.rerun()


    with col2:

        if st.button(
            "👁️ Show Answer",
            use_container_width=True
        ):

            st.session_state.show_answer = True

            st.rerun()


    with col3:

        if st.button(
            "Next ➡️",
            use_container_width=True
        ):

            st.session_state.current_card = (
                current + 1
            ) % total

            st.session_state.show_answer = False

            st.rerun()


# =========================================================
# MANAGE FLASHCARDS
# =========================================================

st.divider()

st.markdown(
    '<div class="section-title">✏️ Manage Flashcards</div>',
    unsafe_allow_html=True
)

st.caption(
    "Customize your study deck by editing or removing flashcards."
)


for index, card in enumerate(
    st.session_state.flashcards
):

    with st.expander(
        f"📌 Card {index + 1} — {card['question']}"
    ):

        edited_question = st.text_input(
            "Question",
            value=card["question"],
            key=f"edit_question_{index}"
        )

        edited_answer = st.text_area(
            "Answer",
            value=card["answer"],
            key=f"edit_answer_{index}"
        )

        col1, col2 = st.columns(2)

        with col1:

            if st.button(
                "💾 Save Changes",
                key=f"save_{index}",
                use_container_width=True
            ):

                st.session_state.flashcards[index] = {
                    "question": edited_question,
                    "answer": edited_answer
                }

                st.success("Flashcard updated!")

                st.rerun()


        with col2:

            if st.button(
                "🗑️ Delete Card",
                key=f"delete_{index}",
                use_container_width=True
            ):

                st.session_state.flashcards.pop(index)

                st.session_state.current_card = 0

                st.session_state.show_answer = False

                st.rerun()


# =========================================================
# FOOTER
# =========================================================

st.markdown("""
<div class="footer">

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<br>

<b>FlashLearn</b> • Flashcard Quiz Application

<br>

Built for <b>CodeAlpha App Development Internship</b>

<br><br>

Learn • Practice • Improve

</div>
""", unsafe_allow_html=True)