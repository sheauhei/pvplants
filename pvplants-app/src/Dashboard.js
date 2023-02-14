import React, { useEffect } from 'react';

function Dashboard() {
  const apikey = 'eyJrIjoicDdNcXN6SlFqa2VYSzFDV3lxbzVKMlc4ZGl1NWJHMkciLCJuIjoiR3JhZmFuYSBFbWJlZCIsImlkIjoxfQ==';
  const dashboardUrl = 'http://localhost:3000/d/x4cmMgJ4z/plant-analysis-v-2';
  const iframeUrl = `${dashboardUrl}?orgId=1&kiosk=tv&theme=light&from=now-30m&to=now&panelId=1&embed`;

  useEffect(() => {
    // const iframeUrl = `${dashboardUrl}?orgId=1&theme=light&from=now-30m&to=now&panelId=1&embed`;
    // const iframeId = 'grafana-iframe';

    // Check if the iframe already exists
    // const existingIframe = document.getElementById(iframeId);
    // if (existingIframe) {
    //   return;
    // }
    
    // const cssRules = 'position: "relative", width: 100%; height: 100%;';
    // const iframe = document.createElement('iframe');
    // iframe.style = cssRules;
    // iframe.src = iframeUrl;
    // iframe.id = iframeId;
    // document.getElementById("grafana-container").appendChild(iframe);
  }, []);

  return (
    <div style={{ position: "relative", width: "100%", height: "100%" }}>
      <iframe
        title="Grafana Dashboard"
        src={iframeUrl}
        style={{ position: "absolute", top: 0, left: 0, width: "100%", height: "100%" }}
      />
    </div>
  );
}

export default Dashboard;
