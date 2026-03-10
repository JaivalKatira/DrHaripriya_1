import streamlit as st
import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# ── Page config ──────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Dr. Haripriya Katira | Prosthodontist",
    page_icon="🦷",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ── Custom CSS ────────────────────────────────────────────────────────────────
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=DM+Serif+Display:ital@0;1&family=DM+Sans:ital,opsz,wght@0,9..40,300;0,9..40,400;0,9..40,500;0,9..40,600;1,9..40,300&display=swap');

    :root {
        --ink:       #0f1117;
        --paper:     #faf9f6;
        --accent:    #1a6b5a;
        --accent2:   #e8f4f1;
        --muted:     #6b7280;
        --border:    #e4e2dc;
        --card:      #ffffff;
        --radius:    14px;
        --shadow:    0 4px 24px rgba(0,0,0,.07);
    }

    html, body, [class*="css"] {
        font-family: 'DM Sans', sans-serif;
        background-color: var(--paper) !important;
        color: var(--ink);
    }

    #MainMenu, footer, header { visibility: hidden; }
    .block-container { padding: 2.5rem 3rem 4rem !important; max-width: 1100px; }

    .hero {
        background: linear-gradient(135deg, var(--accent) 0%, #0d4a3c 100%);
        border-radius: var(--radius);
        padding: 2.8rem 3rem;
        margin-bottom: 2.5rem;
        color: #fff;
        position: relative;
        overflow: hidden;
    }
    .hero::before {
        content: "";
        position: absolute;
        width: 320px; height: 320px;
        border-radius: 50%;
        background: rgba(255,255,255,.05);
        top: -80px; right: -60px;
    }
    .hero h1 {
        font-family: 'DM Serif Display', serif;
        font-size: 2.6rem;
        line-height: 1.15;
        margin: 0 0 .5rem;
        color: #fff !important;
    }
    .hero p {
        font-size: 1.05rem;
        color: rgba(255,255,255,.82);
        margin: 0;
        font-weight: 300;
        letter-spacing: .01em;
    }
    .badge {
        display: inline-block;
        background: rgba(255,255,255,.15);
        border: 1px solid rgba(255,255,255,.3);
        color: #fff;
        border-radius: 99px;
        padding: .25rem .8rem;
        font-size: .78rem;
        margin: .9rem .3rem 0 0;
        font-weight: 500;
        letter-spacing: .03em;
        text-transform: uppercase;
    }

    .card {
        background: var(--card);
        border: 1px solid var(--border);
        border-radius: var(--radius);
        padding: 2rem 2rem 2.2rem;
        box-shadow: var(--shadow);
        height: 100%;
    }
    .card h2 {
        font-family: 'DM Serif Display', serif;
        font-size: 1.5rem;
        color: var(--ink);
        margin: 0 0 1rem;
        padding-bottom: .6rem;
        border-bottom: 2px solid var(--accent2);
    }
    .card p { font-size: .97rem; line-height: 1.75; color: #374151; }

    .img-wrap { display: flex; justify-content: center; margin-bottom: 1.2rem; }
    .img-wrap img {
        width: 130px !important;
        height: 130px !important;
        border-radius: 50% !important;
        object-fit: cover;
        border: 3px solid var(--accent2);
        box-shadow: 0 0 0 5px var(--accent2);
    }

    .soc-btn {
        display: flex;
        align-items: center;
        gap: .65rem;
        width: 100%;
        padding: .78rem 1.2rem;
        border-radius: 10px;
        border: 1.5px solid var(--border);
        background: var(--card);
        color: var(--ink);
        font-size: .95rem;
        font-weight: 500;
        text-decoration: none !important;
        margin-bottom: .75rem;
        transition: all .18s ease;
        box-shadow: 0 1px 4px rgba(0,0,0,.04);
        cursor: pointer;
    }
    .soc-btn:hover {
        border-color: var(--accent);
        background: var(--accent2);
        color: var(--accent);
        transform: translateX(3px);
    }
    .soc-icon { font-size: 1.15rem; }

    .stats-row { display: flex; gap: 1rem; margin-top: 1.4rem; flex-wrap: wrap; }
    .stat-chip {
        background: var(--accent2);
        border-radius: 10px;
        padding: .6rem 1.1rem;
        text-align: center;
        flex: 1; min-width: 80px;
    }
    .stat-chip .num { font-family:'DM Serif Display',serif; font-size:1.5rem; color:var(--accent); display:block; }
    .stat-chip .lbl { font-size:.72rem; text-transform:uppercase; letter-spacing:.06em; color:var(--muted); font-weight:600; }

    .skills { display: flex; flex-wrap: wrap; gap: .5rem; margin-top: 1rem; }
    .skill-pill {
        background: #f3f4f6;
        border: 1px solid var(--border);
        border-radius: 99px;
        padding: .28rem .85rem;
        font-size: .8rem;
        font-weight: 500;
        color: #374151;
    }

    .form-card {
        background: var(--card);
        border: 1px solid var(--border);
        border-radius: var(--radius);
        padding: 2.4rem 2.6rem;
        box-shadow: var(--shadow);
        margin-top: 2.2rem;
    }
    .form-card h2 { font-family:'DM Serif Display',serif; font-size:1.7rem; margin:0 0 .4rem; }
    .form-card .sub { color:var(--muted); font-size:.92rem; margin:0 0 1.8rem; }

    div[data-testid="stTextInput"] input,
    div[data-testid="stTextArea"] textarea {
        border-radius: 8px !important;
        border-color: var(--border) !important;
        font-family: 'DM Sans', sans-serif !important;
        font-size: .92rem !important;
    }
    div[data-testid="stTextInput"] input:focus,
    div[data-testid="stTextArea"] textarea:focus {
        border-color: var(--accent) !important;
        box-shadow: 0 0 0 3px rgba(26,107,90,.12) !important;
    }
    div[data-testid="stFormSubmitButton"] button {
        background: var(--accent) !important;
        color: #fff !important;
        border: none !important;
        border-radius: 8px !important;
        padding: .65rem 2rem !important;
        font-size: .95rem !important;
        font-weight: 600 !important;
        transition: background .18s;
    }
    div[data-testid="stFormSubmitButton"] button:hover { background: #155748 !important; }

    .divider { border: none; border-top: 1px solid var(--border); margin: 2rem 0; }
    </style>
    """,
    unsafe_allow_html=True,
)


# ── Email helper ──────────────────────────────────────────────────────────────
def send_email(name: str, email: str, message: str) -> bool:
    """
    Sends an enquiry email via Gmail SMTP (SSL, port 465).

    Credentials live in  .streamlit/secrets.toml  (NEVER commit that file to Git):
        SENDER_EMAIL = "jaival.katira@gmail.com"   ← Gmail that SENDS the email
        APP_PASSWORD = "xxxx xxxx xxxx xxxx"        ← 16-char Gmail App Password

    The email is delivered to Dr. Haripriya's inbox: haripriya5498@gmail.com
    """
    try:
        sender   = st.secrets["SENDER_EMAIL"]   # jaival.katira@gmail.com
        app_pwd  = st.secrets["APP_PASSWORD"]   # Gmail App Password
        receiver = "drharipriyakatira@gmail.com"    # ← Dr. Haripriya receives here

        msg = MIMEMultipart("alternative")
        msg["Subject"]  = f"New Patient Enquiry from {name}"
        msg["From"]     = sender
        msg["To"]       = receiver
        msg["Reply-To"] = email    # clicking Reply sends directly back to patient

        html_body = f"""
        <html><body style="font-family:Arial,sans-serif;color:#111;">
        <h2 style="color:#1a6b5a;">🦷 New Patient Enquiry</h2>
        <table style="border-collapse:collapse;width:100%;max-width:500px;">
          <tr><td style="padding:8px 12px;background:#f3f4f6;font-weight:600;width:120px;">Name</td>
              <td style="padding:8px 12px;">{name}</td></tr>
          <tr><td style="padding:8px 12px;background:#f3f4f6;font-weight:600;">Email</td>
              <td style="padding:8px 12px;"><a href="mailto:{email}">{email}</a></td></tr>
          <tr><td style="padding:8px 12px;background:#f3f4f6;font-weight:600;vertical-align:top;">Message</td>
              <td style="padding:8px 12px;">{message}</td></tr>
        </table>
        <p style="color:#6b7280;font-size:12px;margin-top:20px;">
            Sent via Dr. Haripriya Katira's portfolio website.
        </p>
        </body></html>
        """

        msg.attach(MIMEText(html_body, "html"))

        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login(sender, app_pwd)
            server.sendmail(sender, receiver, msg.as_string())
        return True

    except Exception as exc:
        st.exception(exc)   # shows full traceback while testing; comment out in production
        return False


# ═══════════════════════════════════════════════════════════════════════════════
#  HERO STRIP
# ═══════════════════════════════════════════════════════════════════════════════
st.markdown(
    """
    <div class="hero">
        <h1>Dr. Haripriya Katira</h1>
        <p>MDS Prosthodontist · Smile Architect · Dental Specialist</p>
        <span class="badge">🦷 Prosthodontics</span>
        <span class="badge">😁 Smile Design</span>
        <span class="badge">👑 Implantology</span>
        <span class="badge">✨ Aesthetic Dentistry</span>
    </div>
    """,
    unsafe_allow_html=True,
)

# ═══════════════════════════════════════════════════════════════════════════════
#  TWO-COLUMN MAIN SECTION
# ═══════════════════════════════════════════════════════════════════════════════
col_about, col_connect = st.columns([3, 2], gap="large")

# ── About Me ──────────────────────────────────────────────────────────────────
with col_about:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown('<h2>About Me</h2>', unsafe_allow_html=True)

    # ┌──────────────────────────────────────────────────────────────────────────┐
    # │  📸  HOW TO ADD YOUR PROFILE PHOTO FROM YOUR DEVICE                     │
    # │                                                                          │
    # │  Step 1 — Copy your photo into the same folder as app.py                │
    # │           e.g.  my_project/                                              │
    # │                     app.py                                               │
    # │                     profile.jpg    ← put your photo here                │
    # │                                                                          │
    # │  Step 2 — Replace the st.image(...) line below with:                    │
    # │           st.image("profile.jpg", width=130)                            │
    # │                                                                          │
    # │  If your photo is inside a sub-folder (e.g. assets/):                  │
    # │           st.image("assets/profile.jpg", width=130)                     │
    # │                                                                          │
    # │  Absolute path (Windows example, not ideal for deployment):             │
    # │           st.image(r"C:\Users\Jaival\Pictures\haripriya.jpg", width=130)│
    # │                                                                          │
    # │  Supported formats: JPG · JPEG · PNG · WEBP                             │
    # │  Best crop: square or portrait (renders as a circle on-screen)          │
    # └──────────────────────────────────────────────────────────────────────────┘
    st.markdown('<div class="img-wrap">', unsafe_allow_html=True)
    st.image(
        # ↓↓↓ REPLACE THIS URL with your image path, e.g. "profile.jpg" ↓↓↓
        "profile_DrHaripriya_1.jpeg",
        width=130,
    )
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown(
        """
        <p>
        Welcome! I'm <strong>Dr. Haripriya Katira</strong>, an <strong>MDS Prosthodontist</strong>
        dedicated to restoring smiles and transforming lives through the art and science of
        modern dentistry. With a post-graduate specialisation in Prosthodontics, I bring a
        meticulous, patient-first approach to every treatment — from a simple crown to a
        full smile makeover.
        </p>
        <p>
        My clinical expertise spans <strong>dental implants, complete &amp; partial dentures,
        fixed prostheses, smile design, and full-mouth rehabilitation</strong>. I believe that
        a confident smile is not a luxury — it is a cornerstone of well-being — and I strive
        to make high-quality, aesthetic dentistry accessible to every patient.
        </p>
        <p>
        Outside the clinic, I am passionate about patient education and staying current with
        the latest advances in digital dentistry and CAD/CAM technology, ensuring every
        patient receives care that is both evidence-based and beautifully crafted.
        </p>
        """,
        unsafe_allow_html=True,
    )

    # Stats — feel free to update these numbers
    st.markdown(
        """
        <div class="stats-row">
          <div class="stat-chip"><span class="num">MDS</span><span class="lbl">Qualification</span></div>
          <div class="stat-chip"><span class="num">500+</span><span class="lbl">Smiles Restored</span></div>
          <div class="stat-chip"><span class="num">5★</span><span class="lbl">Patient Rating</span></div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # Speciality pills
    specialities = [
        "Dental Implants", "Smile Design", "Dentures", "Crowns & Bridges",
        "Full-Mouth Rehab", "Veneers", "Occlusal Therapy", "CAD/CAM Prosthetics",
    ]
    pills_html = '<div class="skills">' + "".join(
        f'<span class="skill-pill">{s}</span>' for s in specialities
    ) + "</div>"
    st.markdown(pills_html, unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)


# ── Connect ───────────────────────────────────────────────────────────────────
with col_connect:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown('<h2>Connect With Me</h2>', unsafe_allow_html=True)
    st.markdown(
        '<p style="color:#6b7280;font-size:.9rem;margin-bottom:1.4rem;">'
        "Book a consultation or reach out — I'd love to help you smile with confidence.</p>",
        unsafe_allow_html=True,
    )

    socials = [
        {
            "label": "LinkedIn",
            "icon": "💼",
            "url": "https://www.linkedin.com/in/dr-haripriya-katira-39763939b?utm_source=share_via&utm_content=profile&utm_medium=member_ios",
            "sub": "Professional profile",
        },
        {
            "label": "Instagram",
            "icon": "📸",
            "url": "https://www.instagram.com/dr.smilearchitect?igsh=MW9vbGkycHgxZW85aw==",
            "sub": "@dr.smilearchitect",
        },
        {
            "label": "WhatsApp",
            "icon": "💬",
            # wa.me format: country code (91 for India) + number without spaces or +
            "url": "https://wa.me/919769528954",
            "sub": "+91 97695 28954",
        },
    ]

    for s in socials:
        st.markdown(
            f"""
            <a href="{s['url']}" target="_blank" rel="noopener noreferrer" class="soc-btn">
                <span class="soc-icon">{s['icon']}</span>
                <span>
                    <strong>{s['label']}</strong><br>
                    <span style="font-size:.78rem;color:#6b7280;font-weight:400">{s['sub']}</span>
                </span>
                <span style="margin-left:auto;color:#9ca3af;font-size:.85rem">↗</span>
            </a>
            """,
            unsafe_allow_html=True,
        )

    st.markdown("<hr class='divider'>", unsafe_allow_html=True)

    # ┌──────────────────────────────────────────────────────────────────────────┐
    # │  🏥  HOW TO ADD A CLINIC LOGO OR BANNER IMAGE                           │
    # │                                                                          │
    # │  Place clinic_logo.png (or any image) next to app.py, then uncomment:  │
    # │      st.image("clinic_logo.png", use_container_width=True)              │
    # └──────────────────────────────────────────────────────────────────────────┘
    # st.image("clinic_logo.png", use_container_width=True)   # ← uncomment & set path

    st.markdown(
        """
        <p style="font-size:.85rem;color:#6b7280;text-align:center;">
            📍 Available for in-clinic &amp; tele-consultations<br>
            ⏱ Usually replies within 24 hours
        </p>
        """,
        unsafe_allow_html=True,
    )
    st.markdown('</div>', unsafe_allow_html=True)


# ═══════════════════════════════════════════════════════════════════════════════
#  ENQUIRE NOW FORM
# ═══════════════════════════════════════════════════════════════════════════════
st.markdown(
    """
    <div class="form-card">
        <h2>Enquire Now</h2>
        <p class="sub">Have a question or want to book a consultation? Fill in the form and Dr. Haripriya will get back to you shortly.</p>
    </div>
    """,
    unsafe_allow_html=True,
)

with st.form("enquiry_form", clear_on_submit=True):
    f_col1, f_col2 = st.columns(2, gap="medium")

    with f_col1:
        name_input = st.text_input(
            "Your Name *",
            placeholder="Rahul Sharma",
            help="Full name so the doctor knows who she is speaking with.",
        )
    with f_col2:
        email_input = st.text_input(
            "Email Address *",
            placeholder="rahul@example.com",
            help="A reply will be sent to this address.",
        )

    msg_input = st.text_area(
        "Message *",
        placeholder="Hi Dr. Haripriya, I'd like to enquire about dental implants / smile design…",
        height=150,
        help="Describe your concern or question in as much detail as you like.",
    )

    submitted = st.form_submit_button("🦷  Send Enquiry", use_container_width=False)

if submitted:
    if not name_input.strip():
        st.error("Please enter your name.")
    elif "@" not in email_input or "." not in email_input:
        st.error("Please enter a valid email address.")
    elif len(msg_input.strip()) < 10:
        st.error("Message is too short — please write at least a sentence.")
    else:
        with st.spinner("Sending your enquiry…"):
            success = send_email(name_input.strip(), email_input.strip(), msg_input.strip())

        if success:
            st.success(
                f"🎉 Thank you, **{name_input.strip()}**! Your enquiry has been sent successfully. "
                "Dr. Haripriya will be in touch within 24 hours."
            )
        else:
            st.error(
                "⚠️ Something went wrong while sending your message. "
                "Please reach out directly via WhatsApp or Instagram."
            )

# ── Footer ────────────────────────────────────────────────────────────────────
st.markdown("<hr class='divider'>", unsafe_allow_html=True)
st.markdown(
    "<p style='text-align:center;color:#9ca3af;font-size:.8rem;'>"
    "© 2025 Dr. Haripriya Katira · MDS Prosthodontist · Built with Streamlit</p>",
    unsafe_allow_html=True,

)
