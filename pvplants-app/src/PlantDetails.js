import React from 'react';
import { useParams } from 'react-router-dom';

const PlantDetails = () => {
  const { id } = useParams();
  return (
    <div>
      <h1>Plant Details</h1>
      <p>You are viewing details for plant {id}.</p>
    </div>
  );
};

export default PlantDetails;
