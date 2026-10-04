import datetime

class EmergencyAlertDispatcher:
    def __init__(self, region_id: str = "Mumbai_Urban_District"):
        self.region_id = region_id

    def dispatch_sms_alert(self, risk_type: str, probability: float, lat: float, lon: float):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        return {
            "status": "DISPATCHED",
            "region": self.region_id,
            "hazard": risk_type,
            "probability": probability,
            "coordinates": {"lat": lat, "lon": lon},
            "timestamp": timestamp,
            "recipient": "District Collector, Disaster Management Authority & SDRF Command Center"
        }