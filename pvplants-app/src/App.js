import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Dashboard from './Dashboard';
import PlantDetails from './PlantDetails';
import MaintenanceLogs from './MaintenanceLogs';

function App() {
  return (
    <Router>
      <div>
        <Routes>
          <Route exact path="/" element={<Dashboard />} />
          <Route exact path="/plants/:id" element={<PlantDetails />} />
          <Route exact path="/maintenance" element={<MaintenanceLogs />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;