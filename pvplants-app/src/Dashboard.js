import React, { useState, useEffect } from 'react';

const Dashboard = () => {
  const [plant, setPlant] = useState('G0008');

  useEffect(() => {
    const iframe = document.getElementById('dashboard-iframe');

    if (iframe) {
      const dashboardUrl = 'http://localhost:3000/d/x4cmMgJ4z/plant-analysis-v-2';

      const iframeUrl = `${dashboardUrl}?orgId=1&kiosk=tv&theme=light&from=now-30m&to=now&panelId=1&var-plant=${plant}&embed`;

      iframe.src = iframeUrl;
    }
  }, [plant]);

  const handlePlantChange = (event) => {
    setPlant(event.target.value);
  };

  return (
    <div style={{ position: "relative", width: "100%", height: "100%" }}>
      <label htmlFor="plant">Plant:</label>
      <select id="plant" value={plant} onChange={handlePlantChange}>
        <option value="G0008">G0008</option>
        <option value="G0009">G0009</option>
        <option value="G0010">G0010</option>
      </select>
      <iframe id="dashboard-iframe" title="dashboard" width="100%" height="100%" frameBorder="0"></iframe>
    </div>
  );
};

export default Dashboard;