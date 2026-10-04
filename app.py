import streamlit as st
import requests

st.set_page_config(
    page_title="MoES AI Nowcasting Dashboard",
    page_icon="⚡",
    layout="wide"
)

st.title("🌧️ MoES AI-Driven Hyper-Local Weather Nowcasting System")
st.markdown("**Smart India Hackathon 2026 — SIH26077** | Real-time Severe Weather Risk Assessment & Automated Disaster Dispatch")

st.sidebar.header("🌍 Region & Coordinate Selector")
region_name = st.sidebar.selectbox(
    "Select Target Region",
    ["Mumbai_Urban_District", "Khammam_District", "Chennai_Coastal_Zone", "Delhi_NCR", "Custom_Coordinates"]
)

# Preset coordinates including Khammam
coords_map = {
    "Mumbai_Urban_District": {"lat": 19.0760, "lon": 72.8777},
    "Khammam_District": {"lat": 17.2473, "lon": 80.1514},
    "Chennai_Coastal_Zone": {"lat": 13.0827, "lon": 80.2707},
    "Delhi_NCR": {"lat": 28.6139, "lon": 77.2090},
}

if region_name == "Custom_Coordinates":
    lat = st.sidebar.number_input("Latitude", value=19.0760, format="%.4f")
    lon = st.sidebar.number_input("Longitude", value=72.8777, format="%.4f")
    region_id = st.sidebar.text_input("Region ID", value="Custom_Region")
else:
    lat = coords_map[region_name]["lat"]
    lon = coords_map[region_name]["lon"]
    region_id = region_name

st.sidebar.markdown(f"**Selected Coordinates:**<br>Lat: `{lat}` | Lon: `{lon}`", unsafe_allow_html=True)

if st.sidebar.button("🚀 Run Nowcasting Simulation", type="primary"):
    with st.spinner("Analyzing IMDAA, INSAT-3D/3DR & CartoDEM topography..."):
        try:
            payload = {
                "latitude": lat,
                "longitude": lon,
                "region_id": region_id
            }
            response = requests.post("http://127.0.0.1:8000/api/v1/predict-risk", json=payload)
            
            if response.status_code == 200:
                data = response.json()
                st.success(f"Nowcasting simulation completed for {region_id}!")
                
                # Display metrics
                col1, col2, col3 = st.columns(3)
                risks = data.get("risks", {})
                col1.metric("Thunderstorm Probability", f"{risks.get('thunderstorm_probability', 0)*100:.1f}%")
                col2.metric("Cloudburst Probability", f"{risks.get('cloudburst_probability', 0)*100:.1f}%")
                col3.metric("Flash Flood Probability", f"{risks.get('flash_flood_probability', 0)*100:.1f}%")
                
                st.info(f"**Alert Status:** `{data.get('alert_status')}`")
            else:
                st.error(f"API Error: {response.status_code} - {response.text}")
        except requests.exceptions.ConnectionError:
            st.error("Could not connect to FastAPI backend. Make sure your server is running on port 8000!")