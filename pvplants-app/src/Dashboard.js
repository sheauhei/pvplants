import React, { useEffect } from 'react';

function Dashboard() {
  const apikey = 'eyJrIjoicDdNcXN6SlFqa2VYSzFDV3lxbzVKMlc4ZGl1NWJHMkciLCJuIjoiR3JhZmFuYSBFbWJlZCIsImlkIjoxfQ==';
  const dashboardUrl = 'http://localhost:3000/d/x4cmMgJ4z/plant-analysis-v-2';

  useEffect(() => {
    const iframe = document.createElement('iframe');
    iframe.src = dashboardUrl;
    document.body.appendChild(iframe);
  }, []);

  return (
    <div>
      <h1>Dashboard</h1>
    </div>
  );
}

export default Dashboard;
