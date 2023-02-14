import React, { useState, useEffect } from 'react';
import { Select } from 'antd';
const { Option } = Select;

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

  // const handlePlantChange = (event) => {
  //   setPlant(event.target.value);
  // };

  const handlePlantChange = value => {
    setPlant(value);
  };

  return (
    <div style={{ position: "relative", width: "100%", height: "100%" }}>
      <div style={{ padding: '10px', borderBottom: '1px solid #eee' }}>
        <Select value={plant} style={{ width: 120 }} onChange={handlePlantChange}>
          <Option value="G0008">G0008</Option>
          <Option value="G0009">G0009</Option>
          <Option value="G0010">G0010</Option>
        </Select>
      </div>
      <iframe id="dashboard-iframe" title="dashboard" width="100%" height="100%" frameBorder="0"></iframe>
    </div>
  );
};

export default Dashboard;