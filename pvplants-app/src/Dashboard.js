import React from 'react';
import { PageContainer } from '@ant-design/pro-layout';

const Dashboard = () => {
  return (
    <PageContainer>
      <h1>Welcome to the PV Plants O&M Platform Dashboard</h1>
      <p>This is the dashboard page, where you can view key performance indicators and metrics for your PV plants.</p>
      <div style={{ display: 'flex', justifyContent: 'space-between' }}>
        <div style={{ width: '30%', backgroundColor: '#FFF', padding: 20, borderRadius: 4 }}>
          <h2>Plant Availability</h2>
          <p>90%</p>
        </div>
        <div style={{ width: '30%', backgroundColor: '#FFF', padding: 20, borderRadius: 4 }}>
          <h2>Plant Performance Ratio</h2>
          <p>80%</p>
        </div>
        <div style={{ width: '30%', backgroundColor: '#FFF', padding: 20, borderRadius: 4 }}>
          <h2>Total Energy Generated</h2>
          <p>10,000 kWh</p>
        </div>
      </div>
    </PageContainer>
  );
};

export default Dashboard;
