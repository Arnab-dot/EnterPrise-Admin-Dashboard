import streamlit as st
import requests
from datetime import datetime, date
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import json
import time

# Configuration
API_BASE_URL = "http://localhost:8000/api"

# Page config
st.set_page_config(
    page_title="Enterprise Admin Dashboard",
    page_icon=" ",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Professional Corporate CSS with Animations
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');

/* Global Variables */
:root {
    --primary-blue: #1f4e79;
    --secondary-blue: #2e5c8a;
    --accent-blue: #4a90e2;
    --light-blue: #e8f4ff;
    --dark-gray: #2c3e50;
    --medium-gray: #7f8c8d;
    --light-gray: #ecf0f1;
    --success-green: #27ae60;
    --warning-orange: #f39c12;
    --danger-red: #e74c3c;
    --white: #ffffff;
    --text-primary: #2c3e50;
    --text-secondary: #7f8c8d;
}

/* Keyframe Animations */
@keyframes fadeInUp {
    0% { opacity: 0; transform: translateY(30px); }
    100% { opacity: 1; transform: translateY(0); }
}

@keyframes fadeInLeft {
    0% { opacity: 0; transform: translateX(-30px); }
    100% { opacity: 1; transform: translateX(0); }
}

@keyframes fadeInRight {
    0% { opacity: 0; transform: translateX(30px); }
    100% { opacity: 1; transform: translateX(0); }
}

@keyframes slideDown {
    0% { opacity: 0; transform: translateY(-20px); }
    100% { opacity: 1; transform: translateY(0); }
}

@keyframes pulse {
    0% { transform: scale(1); }
    50% { transform: scale(1.05); }
    100% { transform: scale(1); }
}

@keyframes shimmer {
    0% { background-position: -200px 0; }
    100% { background-position: calc(200px + 100%) 0; }
}

@keyframes bounce {
    0%, 20%, 53%, 80%, 100% {
        animation-timing-function: cubic-bezier(0.215, 0.610, 0.355, 1.000);
        transform: translate3d(0,0,0);
    }
    40%, 43% {
        animation-timing-function: cubic-bezier(0.755, 0.050, 0.855, 0.060);
        transform: translate3d(0, -30px, 0);
    }
    70% {
        animation-timing-function: cubic-bezier(0.755, 0.050, 0.855, 0.060);
        transform: translate3d(0, -15px, 0);
    }
    90% { transform: translate3d(0,-4px,0); }
}

@keyframes spin {
    0% { transform: rotate(0deg); }
    100% { transform: rotate(360deg); }
}

@keyframes glow {
    0% { box-shadow: 0 0 5px var(--accent-blue); }
    50% { box-shadow: 0 0 20px var(--accent-blue), 0 0 30px var(--accent-blue); }
    100% { box-shadow: 0 0 5px var(--accent-blue); }
}

/* Hide Streamlit branding */
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}

/* Main container styling */
.main .block-container {
    padding-top: 2rem;
    padding-left: 2rem;
    padding-right: 2rem;
    max-width: 100%;
    animation: fadeInUp 0.8s ease-out;
}

/* Custom font for entire app */
html, body, [class*="css"], .stApp {
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
    color: var(--text-primary);
}

/* Header styling with animation */
.main-header {
    background: linear-gradient(135deg, var(--primary-blue) 0%, var(--secondary-blue) 100%);
    padding: 2rem;
    border-radius: 12px;
    margin-bottom: 2rem;
    box-shadow: 0 4px 20px rgba(31, 78, 121, 0.15);
    animation: slideDown 0.6s ease-out;
    position: relative;
    overflow: hidden;
}

.main-header::before {
    content: '';
    position: absolute;
    top: 0;
    left: -100%;
    width: 100%;
    height: 100%;
    background: linear-gradient(90deg, transparent, rgba(255,255,255,0.1), transparent);
    animation: shimmer 3s infinite;
}

.main-header h1 {
    color: var(--white);
    font-size: 2.5rem;
    font-weight: 700;
    margin: 0;
    text-shadow: 0 2px 4px rgba(0,0,0,0.1);
    animation: fadeInLeft 0.8s ease-out 0.2s both;
}

.main-header .subtitle {
    color: rgba(255, 255, 255, 0.9);
    font-size: 1.1rem;
    font-weight: 400;
    margin-top: 0.5rem;
    animation: fadeInLeft 0.8s ease-out 0.4s both;
}

/* Sidebar styling */
.css-1d391kg {
    background: linear-gradient(180deg, var(--primary-blue) 0%, var(--secondary-blue) 100%);
    animation: fadeInLeft 0.6s ease-out;
}

.css-1d391kg .css-17eq0hr {
    color: var(--white);
}

/* Fixed sidebar button alignment */
.css-1d391kg .stButton {
    display: flex !important;
    justify-content: center !important;
    align-items: center !important;
    width: 100% !important;
}

.css-1d391kg .stButton > div {
    width: 100% !important;
    display: flex !important;
    justify-content: center !important;
}

/* Card styling with animations */
.metric-card {
    background: var(--white);
    padding: 1.5rem;
    border-radius: 12px;
    border: 1px solid #e1e8ed;
    box-shadow: 0 2px 12px rgba(0, 0, 0, 0.08);
    transition: all 0.4s cubic-bezier(0.23, 1, 0.32, 1);
    margin-bottom: 1rem;
    animation: fadeInUp 0.6s ease-out;
    position: relative;
    overflow: hidden;
}

.metric-card::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    height: 3px;
    background: linear-gradient(90deg, var(--accent-blue), var(--primary-blue));
    transform: scaleX(0);
    transform-origin: left;
    transition: transform 0.3s ease;
}

.metric-card:hover {
    transform: translateY(-8px) scale(1.02);
    box-shadow: 0 8px 25px rgba(0, 0, 0, 0.15);
    animation: glow 2s infinite;
}

.metric-card:hover::before {
    transform: scaleX(1);
}

.metric-value {
    font-size: 2.5rem;
    font-weight: 700;
    color: var(--primary-blue);
    margin: 0;
    line-height: 1;
    transition: all 0.3s ease;
}

.metric-card:hover .metric-value {
    animation: bounce 1s ease-in-out;
}

.metric-label {
    font-size: 0.9rem;
    color: var(--text-secondary);
    font-weight: 500;
    text-transform: uppercase;
    letter-spacing: 0.5px;
    margin-bottom: 0.5rem;
    transition: color 0.3s ease;
}

.metric-card:hover .metric-label {
    color: var(--accent-blue);
}

/* Button styling with enhanced animations */
.stButton > button {
    background: linear-gradient(135deg, var(--accent-blue) 0%, var(--primary-blue) 100%) !important;
    color: var(--white) !important;
    border: none !important;
    border-radius: 8px !important;
    padding: 0.6rem 1.5rem !important;
    font-weight: 600 !important;
    font-size: 0.95rem !important;
    transition: all 0.4s cubic-bezier(0.23, 1, 0.32, 1) !important;
    box-shadow: 0 2px 8px rgba(74, 144, 226, 0.3) !important;
    position: relative !important;
    overflow: hidden !important;
    width: 100% !important;
    display: block !important;
}

.stButton > button:hover {
    transform: translateY(-2px) scale(1.05) !important;
    box-shadow: 0 8px 20px rgba(74, 144, 226, 0.4) !important;
    animation: pulse 2s infinite !important;
}

/* Success button */
.success-button > button {
    background: linear-gradient(135deg, var(--success-green) 0%, #219a52 100%) !important;
    box-shadow: 0 2px 8px rgba(39, 174, 96, 0.3) !important;
}

/* Danger button */
.danger-button > button {
    background: linear-gradient(135deg, var(--danger-red) 0%, #c0392b 100%) !important;
    box-shadow: 0 2px 8px rgba(231, 76, 60, 0.3) !important;
}

/* Update button styling */
.update-button > button {
    background: linear-gradient(135deg, var(--warning-orange) 0%, #e67e22 100%) !important;
    box-shadow: 0 2px 8px rgba(243, 156, 18, 0.3) !important;
}

/* Input styling with animations */
.stTextInput > div > div > input,
.stSelectbox > div > div > select,
.stDateInput > div > div > input,
.stNumberInput > div > div > input {
    border: 2px solid #e1e8ed !important;
    border-radius: 8px !important;
    padding: 0.75rem !important;
    font-size: 0.95rem !important;
    transition: all 0.3s cubic-bezier(0.23, 1, 0.32, 1) !important;
}

.stTextInput > div > div > input:focus,
.stSelectbox > div > div > select:focus,
.stDateInput > div > div > input:focus,
.stNumberInput > div > div > input:focus {
    border-color: var(--accent-blue) !important;
    box-shadow: 0 0 0 3px rgba(74, 144, 226, 0.1) !important;
    transform: translateY(-2px) !important;
}

/* Status badges with animations */
.status-badge {
    padding: 0.3rem 0.8rem;
    border-radius: 20px;
    font-size: 0.8rem;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 0.5px;
    transition: all 0.3s ease;
    animation: fadeInRight 0.5s ease-out;
    position: relative;
    overflow: hidden;
    display: inline-block;
}

.status-paid {
    background: rgba(39, 174, 96, 0.1);
    color: var(--success-green);
    border: 1px solid rgba(39, 174, 96, 0.2);
}

.status-sent {
    background: rgba(74, 144, 226, 0.1);
    color: var(--accent-blue);
    border: 1px solid rgba(74, 144, 226, 0.2);
}

.status-draft {
    background: rgba(127, 140, 141, 0.1);
    color: var(--medium-gray);
    border: 1px solid rgba(127, 140, 141, 0.2);
}

.status-overdue {
    background: rgba(231, 76, 60, 0.1);
    color: var(--danger-red);
    border: 1px solid rgba(231, 76, 60, 0.2);
}

/* Invoice row styling */
.invoice-row {
    background: var(--white);
    border-radius: 8px;
    padding: 1rem;
    margin-bottom: 0.5rem;
    box-shadow: 0 1px 4px rgba(0, 0, 0, 0.1);
    transition: all 0.3s ease;
    animation: fadeInUp 0.5s ease-out;
}

.invoice-row:hover {
    box-shadow: 0 3px 12px rgba(0, 0, 0, 0.15);
    transform: translateY(-2px);
}

/* Login form styling */
.login-container {
    background: var(--white);
    padding: 3rem;
    border-radius: 16px;
    box-shadow: 0 8px 32px rgba(0, 0, 0, 0.12);
    border: 1px solid #e1e8ed;
    max-width: 450px;
    margin: 2rem auto;
    animation: fadeInUp 0.8s ease-out;
}

.login-header {
    text-align: center;
    margin-bottom: 2rem;
}

.login-header h1 {
    color: var(--primary-blue);
    font-size: 2rem;
    font-weight: 700;
    margin-bottom: 0.5rem;
}

.login-header p {
    color: var(--text-secondary);
    font-size: 1rem;
}

/* Charts and visualizations */
.chart-container {
    background: var(--white);
    padding: 1.5rem;
    border-radius: 12px;
    box-shadow: 0 2px 12px rgba(0, 0, 0, 0.08);
    margin-bottom: 1.5rem;
    animation: fadeInUp 0.6s ease-out;
    transition: all 0.3s ease;
}

.chart-container:hover {
    transform: translateY(-5px);
    box-shadow: 0 8px 25px rgba(0, 0, 0, 0.12);
}

.chart-title {
    font-size: 1.25rem;
    font-weight: 600;
    color: var(--text-primary);
    margin-bottom: 1rem;
}

/* Page transition */
.page-transition {
    animation: fadeInUp 0.5s ease-out;
}

/* Responsive design */
@media (max-width: 768px) {
    .main .block-container {
        padding-left: 1rem;
        padding-right: 1rem;
    }

    .main-header {
        padding: 1.5rem;
    }

    .main-header h1 {
        font-size: 2rem;
    }
}

</style>
""", unsafe_allow_html=True)

# Session state initialization
if 'access_token' not in st.session_state:
    st.session_state.access_token = None
if 'refresh_token' not in st.session_state:
    st.session_state.refresh_token = None
if 'user_email' not in st.session_state:
    st.session_state.user_email = None
if 'user_role' not in st.session_state:
    st.session_state.user_role = None
if 'data_refresh_trigger' not in st.session_state:
    st.session_state.data_refresh_trigger = 0
if 'last_update' not in st.session_state:
    st.session_state.last_update = time.time()


# API Helper Functions
def refresh_access_token():
    """Refresh the access token using the refresh token"""
    if not st.session_state.refresh_token:
        return False
    try:
        response = requests.post(
            f"{API_BASE_URL}/users/token/refresh/",
            json={"refresh": st.session_state.refresh_token},
            timeout=10
        )
        if response.status_code == 200:
            data = response.json()
            st.session_state.access_token = data.get('access')
            return True
        else:
            st.session_state.access_token = None
            st.session_state.refresh_token = None
            return False
    except Exception as e:
        print(f"Token refresh error: {str(e)}")
        return False


def get_headers():
    if st.session_state.access_token:
        return {
            "Authorization": f"Bearer {st.session_state.access_token}",
            "Content-Type": "application/json"
        }
    return {"Content-Type": "application/json"}


def make_authenticated_request(method, url, **kwargs):
    """Make an authenticated request with automatic token refresh"""
    if 'headers' not in kwargs:
        kwargs['headers'] = get_headers()
    if 'timeout' not in kwargs:
        kwargs['timeout'] = 10

    try:
        response = requests.request(method, url, **kwargs)

        # If token expired, try to refresh and retry once
        if response.status_code == 401:
            try:
                error_data = response.json()
                if error_data.get('code') == 'token_not_valid':
                    if refresh_access_token():
                        kwargs['headers'] = get_headers()
                        response = requests.request(method, url, **kwargs)
                    else:
                        st.error("Session expired. Please login again.")
                        st.session_state.access_token = None
                        st.session_state.refresh_token = None
                        st.rerun()
            except:
                pass

        return response
    except requests.exceptions.ConnectionError:
        st.error("Cannot connect to server. Make sure Django is running on http://localhost:8000")
        return None
    except requests.exceptions.Timeout:
        st.error("Request timed out. Please try again.")
        return None
    except Exception as e:
        st.error(f"Request error: {str(e)}")
        return None


def login(email, password):
    try:
        response = requests.post(
            f"{API_BASE_URL}/users/token/",
            json={"email": email, "password": password},
            timeout=10
        )
        if response.status_code == 200:
            data = response.json()
            st.session_state.access_token = data.get('access')
            st.session_state.refresh_token = data.get('refresh')
            st.session_state.user_email = email
            return True, "Login successful!"
        else:
            return False, "Invalid credentials"
    except requests.exceptions.ConnectionError:
        return False, "Cannot connect to server. Make sure Django is running."
    except Exception as e:
        return False, f"Error: {str(e)}"


def register_user(email, password, role):
    try:
        response = requests.post(
            f"{API_BASE_URL}/users/register-user/",
            json={"email": email, "password": password, "role": role},
            timeout=10
        )
        if response.status_code == 201:
            return True, "User registered successfully!"
        else:
            try:
                error_msg = response.json()
                return False, str(error_msg)
            except:
                return False, f"Status code: {response.status_code}"
    except requests.exceptions.ConnectionError:
        return False, "Cannot connect to server. Make sure Django is running."
    except Exception as e:
        return False, f"Error: {str(e)}"


def force_refresh_data():
    """Force refresh all cached data"""
    st.session_state.data_refresh_trigger = int(time.time())
    st.session_state.last_update = time.time()


def get_clients():
    """Get clients with forced refresh capability"""
    try:
        response = make_authenticated_request('GET', f"{API_BASE_URL}/clients/")
        if response and response.status_code == 200:
            data = response.json()
            if isinstance(data, dict) and 'results' in data:
                return data.get('results', [])
            elif isinstance(data, list):
                return data
            return []
        return []
    except Exception as e:
        st.error(f"Error fetching clients: {str(e)}")
        return []


def create_client(data):
    try:
        # Ensure data is properly formatted
        if 'dob' in data:
            if isinstance(data['dob'], date):
                data['dob'] = data['dob'].strftime('%Y-%m-%d')
            elif not isinstance(data['dob'], str):
                data['dob'] = str(data['dob'])

        response = make_authenticated_request('POST', f"{API_BASE_URL}/clients/", json=data)
        if response and response.status_code == 201:
            # Force refresh data
            force_refresh_data()
            return True, response.json()
        elif response:
            try:
                error_data = response.json()
                return False, error_data
            except:
                return False, f"Status code: {response.status_code}, Response: {response.text}"
        else:
            return False, "No response from server"
    except Exception as e:
        return False, str(e)


def delete_client(client_id):
    try:
        response = make_authenticated_request('DELETE', f"{API_BASE_URL}/clients/{client_id}/")
        if response and response.status_code == 204:
            # Force refresh data
            force_refresh_data()
            return True
        return False
    except:
        return False


def get_invoices():
    """Get invoices with forced refresh capability"""
    try:
        response = make_authenticated_request('GET', f"{API_BASE_URL}/invoice/")
        if response and response.status_code == 200:
            data = response.json()
            if isinstance(data, dict) and 'results' in data:
                return data.get('results', [])
            elif isinstance(data, list):
                return data
            return []
        return []
    except Exception as e:
        st.error(f"Error fetching invoices: {str(e)}")
        return []


def create_invoice(data):
    try:
        response = make_authenticated_request('POST', f"{API_BASE_URL}/invoice/", json=data)
        if response and response.status_code == 201:
            # Force refresh data
            force_refresh_data()
            return True, response.json()
        elif response:
            try:
                error_data = response.json()
                return False, error_data
            except:
                return False, f"Status code: {response.status_code}"
        return False, "No response"
    except Exception as e:
        return False, str(e)


def update_invoice_status(invoice_id, status):
    """Update invoice status with proper error handling"""
    try:
        url = f"{API_BASE_URL}/invoice/{invoice_id}/"

        response = make_authenticated_request('PATCH', url, json={"status": status})

        if response:
            if response.status_code == 200:
                # Force refresh data immediately
                force_refresh_data()
                return True, response.json()
            else:
                try:
                    error_data = response.json()
                    return False, error_data
                except:
                    return False, f"Status code: {response.status_code}, Response: {response.text}"
        else:
            return False, "No response from server"
    except Exception as e:
        return False, str(e)


def delete_invoice(invoice_id):
    try:
        response = make_authenticated_request('DELETE', f"{API_BASE_URL}/invoice/{invoice_id}/")
        if response and response.status_code == 204:
            # Force refresh data
            force_refresh_data()
            return True
        return False
    except:
        return False


# Authentication Page
def auth_page():
    st.markdown("""
    <div class="main-header">
        <h1>Enterprise Admin Dashboard</h1>
        <p class="subtitle">Secure access to your business management system</p>
    </div>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1, 2, 1])

    with col2:
        st.markdown('<div class="login-container">', unsafe_allow_html=True)

        tab1, tab2 = st.tabs(["Login", "Register"])

        with tab1:
            st.markdown("""
            <div class="login-header">
                <h1>Welcome Back</h1>
                <p>Please sign in to your account</p>
            </div>
            """, unsafe_allow_html=True)

            with st.form("login_form"):
                email = st.text_input("Email Address", placeholder="Enter your email")
                password = st.text_input("Password", type="password", placeholder="Enter your password")

                col1, col2, col3 = st.columns([1, 2, 1])
                with col2:
                    login_clicked = st.form_submit_button("Sign In", use_container_width=True)

                if login_clicked:
                    if email and password:
                        with st.spinner("Authenticating..."):
                            success, message = login(email, password)
                        if success:
                            st.success("✓ " + message)
                            st.rerun()
                        else:
                            st.error("✗ " + message)
                    else:
                        st.warning("Please fill in all fields")

        with tab2:
            st.markdown("""
            <div class="login-header">
                <h1>Create Account</h1>
                <p>Register a new user account</p>
            </div>
            """, unsafe_allow_html=True)

            with st.form("register_form"):
                reg_email = st.text_input("Email Address", placeholder="Enter email address")
                reg_password = st.text_input("Password", type="password", placeholder="Create a password")
                role = st.selectbox("Role", ["admin", "staff", "viewer"])

                col1, col2, col3 = st.columns([1, 2, 1])
                with col2:
                    register_clicked = st.form_submit_button("Create Account", use_container_width=True)

                if register_clicked:
                    if reg_email and reg_password and role:
                        with st.spinner("Creating account..."):
                            success, message = register_user(reg_email, reg_password, role)
                        if success:
                            st.success("✓ " + message)
                        else:
                            st.error("✗ " + message)
                    else:
                        st.warning("Please fill in all fields")

        st.markdown('</div>', unsafe_allow_html=True)


# Dashboard Header
def show_header():
    st.markdown(f"""
    <div class="main-header">
        <h1>Enterprise Admin Dashboard</h1>
        <p class="subtitle">Welcome back, {st.session_state.user_email} • Role: {st.session_state.user_role or 'User'}</p>
    </div>
    """, unsafe_allow_html=True)


# Dashboard Metrics with Real-time Updates
def show_dashboard_metrics():
    # Get fresh data every time
    clients = get_clients()
    invoices = get_invoices()

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.markdown(f"""
        <div class="metric-card" id="metric-{st.session_state.data_refresh_trigger}">
            <div class="metric-label">Total Clients</div>
            <div class="metric-value">{len(clients)}</div>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown(f"""
        <div class="metric-card" id="metric-{st.session_state.data_refresh_trigger}">
            <div class="metric-label">Total Invoices</div>
            <div class="metric-value">{len(invoices)}</div>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        paid_invoices = len([inv for inv in invoices if inv.get('status') == 'paid'])
        st.markdown(f"""
        <div class="metric-card" id="metric-{st.session_state.data_refresh_trigger}">
            <div class="metric-label">Paid Invoices</div>
            <div class="metric-value">{paid_invoices}</div>
        </div>
        """, unsafe_allow_html=True)

    with col4:
        total_amount = sum([float(inv.get('amount', 0)) for inv in invoices if inv.get('status') == 'paid'])
        st.markdown(f"""
        <div class="metric-card" id="metric-{st.session_state.data_refresh_trigger}">
            <div class="metric-label">Revenue</div>
            <div class="metric-value">${total_amount:,.0f}</div>
        </div>
        """, unsafe_allow_html=True)

    # Payment Status Summary
    st.markdown("### Payment Status Summary")

    # Calculate status counts
    status_counts = {}
    for invoice in invoices:
        status = invoice.get('status', 'unknown')
        status_counts[status] = status_counts.get(status, 0) + 1

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        draft_count = status_counts.get('draft', 0)
        st.markdown(f"""
        <div class="metric-card" id="status-metric-{st.session_state.data_refresh_trigger}">
            <div class="metric-label">Draft Invoices</div>
            <div class="metric-value">{draft_count}</div>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        sent_count = status_counts.get('sent', 0)
        st.markdown(f"""
        <div class="metric-card" id="status-metric-{st.session_state.data_refresh_trigger}">
            <div class="metric-label">Sent Invoices</div>
            <div class="metric-value">{sent_count}</div>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        overdue_count = status_counts.get('overdue', 0)
        st.markdown(f"""
        <div class="metric-card" id="status-metric-{st.session_state.data_refresh_trigger}">
            <div class="metric-label">Overdue Invoices</div>
            <div class="metric-value">{overdue_count}</div>
        </div>
        """, unsafe_allow_html=True)

    with col4:
        pending_amount = sum(
            [float(inv.get('amount', 0)) for inv in invoices if inv.get('status') in ['sent', 'overdue']])
        st.markdown(f"""
        <div class="metric-card" id="status-metric-{st.session_state.data_refresh_trigger}">
            <div class="metric-label">Pending Amount</div>
            <div class="metric-value">${pending_amount:,.0f}</div>
        </div>
        """, unsafe_allow_html=True)


# Clients Management Page
def clients_page():
    st.markdown('<div class="page-transition">', unsafe_allow_html=True)
    st.markdown("### Client Management")

    col1, col2 = st.columns([3, 1])

    with col1:
        st.markdown("#### Client Directory")

    with col2:
        if st.button("Add New Client", key="add_client_btn"):
            st.session_state.show_add_client = True

    # Add client form
    if st.session_state.get('show_add_client', False):
        st.markdown("#### Add New Client")

        with st.form("add_client_form"):
            col1, col2 = st.columns(2)

            with col1:
                username = st.text_input("Full Name", placeholder="Enter client name")
                phone_no = st.number_input("Phone Number", min_value=1000000000, max_value=9999999999, value=1234567890)

            with col2:
                user_address = st.text_area("Address", placeholder="Enter client address")
                dob = st.date_input("Date of Birth")

            col1, col2, col3 = st.columns([2, 1, 1])
            with col2:
                if st.form_submit_button("Save Client", use_container_width=True):
                    if username and user_address and phone_no:
                        client_data = {
                            "username": username,
                            "user_address": user_address,
                            "dob": dob.strftime('%Y-%m-%d'),
                            "phone_no": phone_no
                        }

                        with st.spinner("Saving client..."):
                            success, result = create_client(client_data)

                        if success:
                            st.success("Client added successfully!")
                            st.session_state.show_add_client = False
                            st.rerun()
                        else:
                            st.error(f"Failed to add client: {result}")
                    else:
                        st.warning("Please fill in all required fields")

            with col3:
                if st.form_submit_button("Cancel"):
                    st.session_state.show_add_client = False
                    st.rerun()

    # Display clients
    clients = get_clients()
    if clients:
        st.markdown("#### Current Clients")

        # Display as a styled table
        for i, client in enumerate(clients):
            with st.container():
                st.markdown('<div class="invoice-row">', unsafe_allow_html=True)
                col1, col2, col3, col4, col5 = st.columns([2, 2, 2, 1, 1])

                with col1:
                    st.write(f"**{client.get('username', 'N/A')}**")

                with col2:
                    st.write(f"Phone: {client.get('phone_no', 'N/A')}")

                with col3:
                    st.write(f"Address: {client.get('user_address', 'N/A')}")

                with col4:
                    created_at = client.get('created_at', '')
                    if created_at:
                        date_obj = datetime.fromisoformat(created_at.replace('Z', '+00:00'))
                        st.write(f"Date: {date_obj.strftime('%Y-%m-%d')}")

                with col5:
                    st.markdown('<div class="danger-button">', unsafe_allow_html=True)
                    if st.button("Delete", key=f"delete_{client.get('id')}", help="Delete client"):
                        if delete_client(client.get('id')):
                            st.success("Client deleted!")
                            st.rerun()
                        else:
                            st.error("Failed to delete client")
                    st.markdown('</div>', unsafe_allow_html=True)

                st.markdown('</div>', unsafe_allow_html=True)
    else:
        st.info("No clients found. Add some clients to get started!")

    st.markdown('</div>', unsafe_allow_html=True)


# Invoices Management Page with Working Update Functionality
def invoices_page():
    st.markdown('<div class="page-transition">', unsafe_allow_html=True)
    st.markdown("### Invoice Management")

    col1, col2 = st.columns([3, 1])

    with col1:
        st.markdown("#### Invoice Directory")

    with col2:
        if st.button("Create Invoice", key="add_invoice_btn"):
            st.session_state.show_add_invoice = True

    # Add invoice form
    if st.session_state.get('show_add_invoice', False):
        st.markdown("#### Create New Invoice")

        clients = get_clients()
        if not clients:
            st.warning("Please add clients first before creating invoices")
            st.markdown('</div>', unsafe_allow_html=True)
            return

        with st.form("add_invoice_form"):
            col1, col2 = st.columns(2)

            with col1:
                client_options = {f"{c.get('username')} (ID: {c.get('id')})": c.get('id') for c in clients}
                selected_client = st.selectbox("Select Client", options=list(client_options.keys()))
                amount = st.number_input("Amount ($)", min_value=0.01, value=100.0, step=0.01)

            with col2:
                due_date = st.date_input("Due Date")
                status = st.selectbox("Status", ["draft", "sent", "paid", "overdue"])

            col1, col2, col3 = st.columns([2, 1, 1])
            with col2:
                if st.form_submit_button("Create Invoice", use_container_width=True):
                    client_id = client_options[selected_client]

                    invoice_data = {
                        "client": client_id,
                        "amount": amount,
                        "due_date": due_date.strftime('%Y-%m-%d'),
                        "status": status
                    }

                    with st.spinner("Creating invoice..."):
                        success, result = create_invoice(invoice_data)

                    if success:
                        st.success("Invoice created successfully!")
                        st.session_state.show_add_invoice = False
                        st.rerun()
                    else:
                        st.error(f"Failed to create invoice: {result}")

            with col3:
                if st.form_submit_button("Cancel"):
                    st.session_state.show_add_invoice = False
                    st.rerun()

    # Display invoices with working update functionality
    invoices = get_invoices()
    if invoices:
        st.markdown("#### Current Invoices")

        for i, invoice in enumerate(invoices):
            with st.container():
                st.markdown(
                    f'<div class="invoice-row" id="invoice-{invoice.get("id")}-{st.session_state.data_refresh_trigger}">',
                    unsafe_allow_html=True)
                col1, col2, col3, col4, col5, col6, col7 = st.columns([1.5, 1.5, 1, 1, 1, 1, 1])

                with col1:
                    st.write(f"**Invoice #{invoice.get('id')}**")

                with col2:
                    st.write(f"Client ID: {invoice.get('client')}")

                with col3:
                    st.write(f"${invoice.get('amount', 0)}")

                with col4:
                    due_date = invoice.get('due_date', '')
                    st.write(f"Due: {due_date}")

                with col5:
                    status = invoice.get('status', 'draft')
                    status_class = f"status-{status}"
                    st.markdown(f'<span class="status-badge {status_class}">{status.upper()}</span>',
                                unsafe_allow_html=True)

                with col6:
                    # Update status dropdown
                    current_status = invoice.get('status', 'draft')
                    status_options = ["draft", "sent", "paid", "overdue"]
                    current_index = status_options.index(current_status) if current_status in status_options else 0

                    new_status = st.selectbox(
                        "Update",
                        status_options,
                        index=current_index,
                        key=f"status_{invoice.get('id')}_{st.session_state.data_refresh_trigger}"
                    )

                    if new_status != current_status:
                        st.markdown('<div class="update-button">', unsafe_allow_html=True)
                        if st.button("Update",
                                     key=f"update_{invoice.get('id')}_{st.session_state.data_refresh_trigger}"):
                            with st.spinner("Updating status..."):
                                success, result = update_invoice_status(invoice.get('id'), new_status)
                            if success:
                                st.success("Status updated successfully!")
                                time.sleep(0.5)  # Brief pause to show success message
                                st.rerun()
                            else:
                                st.error(f"Failed to update: {result}")
                        st.markdown('</div>', unsafe_allow_html=True)

                with col7:
                    st.markdown('<div class="danger-button">', unsafe_allow_html=True)
                    if st.button("Delete",
                                 key=f"delete_inv_{invoice.get('id')}_{st.session_state.data_refresh_trigger}",
                                 help="Delete invoice"):
                        if delete_invoice(invoice.get('id')):
                            st.success("Invoice deleted!")
                            st.rerun()
                        else:
                            st.error("Failed to delete invoice")
                    st.markdown('</div>', unsafe_allow_html=True)

                st.markdown('</div>', unsafe_allow_html=True)
    else:
        st.info("No invoices found. Create some invoices to get started!")

    st.markdown('</div>', unsafe_allow_html=True)


# Analytics Page with Real-time Updates
def analytics_page():
    st.markdown('<div class="page-transition">', unsafe_allow_html=True)
    st.markdown("### Business Analytics")

    # Get fresh data
    invoices = get_invoices()
    clients = get_clients()

    if not invoices:
        st.info("No data available for analytics. Create some invoices first!")
        st.markdown('</div>', unsafe_allow_html=True)
        return

    col1, col2 = st.columns(2)

    with col1:
        st.markdown('<div class="chart-container">', unsafe_allow_html=True)
        st.markdown('<div class="chart-title">Invoice Status Distribution</div>', unsafe_allow_html=True)

        # Status distribution with fresh data
        status_counts = {}
        for invoice in invoices:
            status = invoice.get('status', 'unknown')
            status_counts[status] = status_counts.get(status, 0) + 1

        if status_counts:
            fig_pie = px.pie(
                values=list(status_counts.values()),
                names=list(status_counts.keys()),
                color_discrete_sequence=px.colors.qualitative.Set3
            )
            fig_pie.update_layout(
                showlegend=True,
                height=400,
                font=dict(family="Inter"),
                paper_bgcolor="rgba(0,0,0,0)",
                plot_bgcolor="rgba(0,0,0,0)"
            )
            # Use unique key to force refresh
            st.plotly_chart(fig_pie, use_container_width=True, key=f"pie_chart_{st.session_state.data_refresh_trigger}")

        st.markdown('</div>', unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="chart-container">', unsafe_allow_html=True)
        st.markdown('<div class="chart-title">Revenue by Month</div>', unsafe_allow_html=True)

        # Monthly revenue with fresh data
        monthly_revenue = {}
        for invoice in invoices:
            if invoice.get('status') == 'paid' and invoice.get('created_at'):
                try:
                    date_obj = datetime.fromisoformat(invoice['created_at'].replace('Z', '+00:00'))
                    month_key = date_obj.strftime('%Y-%m')
                    amount = float(invoice.get('amount', 0))
                    monthly_revenue[month_key] = monthly_revenue.get(month_key, 0) + amount
                except:
                    continue

        if monthly_revenue:
            months = list(monthly_revenue.keys())
            revenues = list(monthly_revenue.values())

            fig_bar = px.bar(
                x=months,
                y=revenues,
                labels={'x': 'Month', 'y': 'Revenue ($)'},
                color_discrete_sequence=['#1f4e79']
            )
            fig_bar.update_layout(
                height=400,
                font=dict(family="Inter"),
                paper_bgcolor="rgba(0,0,0,0)",
                plot_bgcolor="rgba(0,0,0,0)",
                xaxis=dict(showgrid=False),
                yaxis=dict(showgrid=True, gridcolor='lightgray')
            )
            # Use unique key to force refresh
            st.plotly_chart(fig_bar, use_container_width=True, key=f"bar_chart_{st.session_state.data_refresh_trigger}")
        else:
            st.info("No paid invoices yet to show revenue data.")

        st.markdown('</div>', unsafe_allow_html=True)

    # Status trend chart with fresh data
    st.markdown('<div class="chart-container">', unsafe_allow_html=True)
    st.markdown('<div class="chart-title">Invoice Status Timeline</div>', unsafe_allow_html=True)

    # Prepare timeline data
    timeline_data = []
    for invoice in invoices:
        if invoice.get('created_at'):
            try:
                date_obj = datetime.fromisoformat(invoice['created_at'].replace('Z', '+00:00'))
                timeline_data.append({
                    'Date': date_obj.strftime('%Y-%m-%d'),
                    'Status': invoice.get('status', 'unknown').title(),
                    'Amount': float(invoice.get('amount', 0)),
                    'Invoice': f"Invoice #{invoice.get('id')}"
                })
            except:
                continue

    if timeline_data:
        df_timeline = pd.DataFrame(timeline_data)
        fig_timeline = px.scatter(
            df_timeline,
            x='Date',
            y='Amount',
            color='Status',
            hover_data=['Invoice'],
            title="Invoice Timeline by Status"
        )
        fig_timeline.update_layout(
            height=400,
            font=dict(family="Inter"),
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)"
        )
        # Use unique key to force refresh
        st.plotly_chart(fig_timeline, use_container_width=True,
                        key=f"timeline_chart_{st.session_state.data_refresh_trigger}")

    st.markdown('</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)


# Main Application
def main():
    # Check authentication
    if not st.session_state.access_token:
        auth_page()
        return

    # Show header
    show_header()

    # Sidebar navigation with fixed alignment
    with st.sidebar:
        st.markdown("### Navigation")

        pages = {
            "Dashboard": "dashboard",
            "Clients": "clients",
            "Invoices": "invoices",
            "Analytics": "analytics"
        }

        selected_page = st.radio("Select Page", list(pages.keys()), key="page_selection")

        st.markdown("---")

        # Fixed button alignment
        col1, col2 = st.columns([1, 1])
        with col1:
            if st.button("Refresh", use_container_width=True):
                # Force refresh all data
                force_refresh_data()
                st.rerun()

        with col2:
            st.markdown('<div class="danger-button">', unsafe_allow_html=True)
            if st.button("Logout", use_container_width=True):
                # Clear session
                for key in ['access_token', 'refresh_token', 'user_email', 'user_role']:
                    if key in st.session_state:
                        del st.session_state[key]
                st.rerun()
            st.markdown('</div>', unsafe_allow_html=True)

    # Page routing
    current_page = pages[selected_page]

    if current_page == "dashboard":
        show_dashboard_metrics()
        st.markdown("### Recent Activity")

        col1, col2 = st.columns(2)

        with col1:
            st.markdown("#### Recent Clients")
            clients = get_clients()
            recent_clients = clients[-5:] if len(clients) > 5 else clients
            for client in recent_clients:
                st.write(f"• {client.get('username', 'N/A')} - {client.get('phone_no', 'N/A')}")

        with col2:
            st.markdown("#### Recent Invoices")
            invoices = get_invoices()
            recent_invoices = invoices[-5:] if len(invoices) > 5 else invoices
            for invoice in recent_invoices:
                status = invoice.get('status', 'unknown')
                status_class = f"status-{status}"
                st.markdown(
                    f"• Invoice #{invoice.get('id')} - ${invoice.get('amount', 0)} <span class='status-badge {status_class}'>{status.upper()}</span>",
                    unsafe_allow_html=True)

    elif current_page == "clients":
        clients_page()

    elif current_page == "invoices":
        invoices_page()

    elif current_page == "analytics":
        analytics_page()


if __name__ == "__main__":
    main()
