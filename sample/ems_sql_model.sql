CREATE TABLE SystemAdmin (
    id SERIAL PRIMARY KEY,
    username TEXT NOT NULL,
    password TEXT NOT NULL,
    email TEXT NOT NULL
);

CREATE TABLE Organization (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    address TEXT NOT NULL,
    contact_person TEXT NOT NULL,
    contact_email TEXT NOT NULL,
    contact_phone TEXT NOT NULL,
    admin_id INTEGER NOT NULL
);

CREATE TABLE EMSUser (
    id SERIAL PRIMARY KEY,
    username TEXT NOT NULL,
    password TEXT NOT NULL,
    email TEXT NOT NULL,
    role TEXT NOT NULL,
    organization_id INTEGER NOT NULL REFERENCES Organization (id)
);

-- Create Microgrid table
CREATE TABLE Microgrid (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255),
  location VARCHAR(255),
  max_load FLOAT,
  max_generation FLOAT,
  voltage FLOAT,
  frequency FLOAT,
  topology JSONB,
  owner_id INTEGER REFERENCES Organization(id),
  utility_id INTEGER REFERENCES Utility(id),
  renewable_ppa_id INTEGER REFERENCES RenewablePPAContract(id),
  system_settings_id INTEGER REFERENCES SystemSettings(id)
);
-- Create Device table
CREATE TABLE Device (
  id SERIAL PRIMARY KEY,
  device_type  VARCHAR(255),
  name VARCHAR(255),
  description VARCHAR(255),
  manufacturer VARCHAR(255),
  model_number VARCHAR(255),
  serial_number VARCHAR(255),
  microgrid_id INTEGER REFERENCES Microgrid(id)
);

-- Create ESS table
CREATE TABLE ESS (
  id SERIAL PRIMARY KEY,
  device_id INTEGER REFERENCES Device(id),
  capacity FLOAT,
  charge_efficiency FLOAT,
  discharge_efficiency FLOAT,
  max_charge_rate FLOAT,
  max_discharge_rate FLOAT,
  soc FLOAT
);

-- Create EVCharger table
CREATE TABLE EVCharger (
  id SERIAL PRIMARY KEY,
  device_id INTEGER REFERENCES Device(id),
  num_ports INTEGER,
  max_charging_power FLOAT
);

-- Create Load table
CREATE TABLE Load (
  id SERIAL PRIMARY KEY,
  device_id INTEGER REFERENCES Device(id),
  power FLOAT
);

-- Create SolarEnergy table
CREATE TABLE SolarEnergy (
  id SERIAL PRIMARY KEY,
  device_id INTEGER REFERENCES Device(id),
  capacity FLOAT,
  efficiency FLOAT,
  tilt_angle FLOAT,
  azimuth_angle FLOAT
);

-- Create RenewableSourceFromPPA table
CREATE TABLE RenewableSourceFromPPA (
  id SERIAL PRIMARY KEY,
  source_type VARCHAR(100), -- solar, wind, etc.
  device_id INTEGER REFERENCES Device(id),
  renewable_ppa_id INTEGER REFERENCES RenewablePPAContract(id)
);

-- Create LiveData table
CREATE TABLE LiveData (
    id SERIAL PRIMARY KEY,
    timestamp TIMESTAMP,
    device_id INTEGER REFERENCES Device(id),
    data JSONB
);

CREATE TABLE ESSLiveData (
    id SERIAL PRIMARY KEY,
    timestamp TIMESTAMP NOT NULL,
    device_id INTEGER NOT NULL,
    charge_rate FLOAT NOT NULL,
    discharge_rate FLOAT NOT NULL,
    soc FLOAT NOT NULL,
    data JSONB NOT NULL
);

CREATE TABLE EVChargerLiveData (
    id SERIAL PRIMARY KEY,
    timestamp TIMESTAMP NOT NULL,
    device_id INTEGER NOT NULL,
    charging_rate FLOAT NOT NULL,
    num_ports INTEGER NOT NULL,
    data JSONB NOT NULL
);

CREATE TABLE LoadLiveData (
    id SERIAL PRIMARY KEY,
    timestamp TIMESTAMP NOT NULL,
    device_id INTEGER NOT NULL,
    power FLOAT NOT NULL,
    data JSONB NOT NULL
);

CREATE TABLE SolarEnergyLiveData (
    id SERIAL PRIMARY KEY,
    timestamp TIMESTAMP NOT NULL,
    device_id INTEGER NOT NULL,
    power FLOAT NOT NULL,
    energy_production_today FLOAT NOT NULL,
    energy_production_lifetime FLOAT NOT NULL,
    energy_consumption_today FLOAT NOT NULL,
    energy_consumption_lifetime FLOAT NOT NULL,
    data JSONB NOT NULL
);

CREATE TABLE SolarPlantLiveData (
    id SERIAL PRIMARY KEY,
    timestamp TIMESTAMP NOT NULL,
    plant_id INTEGER NOT NULL,
    power FLOAT NOT NULL,
    data JSONB NOT NULL
);

CREATE TABLE WindEnergyLiveData (
    id SERIAL PRIMARY KEY,
    timestamp TIMESTAMP NOT NULL,
    device_id INTEGER NOT NULL,
    power FLOAT NOT NULL,
    data JSONB NOT NULL
);

CREATE TABLE WindPlantLiveData (
    id SERIAL PRIMARY KEY,
    timestamp TIMESTAMP NOT NULL,
    plant_id INTEGER NOT NULL,
    power FLOAT NOT NULL,
    data JSONB NOT NULL
);

CREATE TABLE Utility (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    location VARCHAR(255) NOT NULL,
    energy_sources JSONB NOT NULL,
    peak_demand FLOAT NOT NULL,
    peak_demand_time TIME NOT NULL,
    energy_rates JSONB NOT NULL
);


CREATE TABLE UtilityPriceContract (
    id SERIAL PRIMARY KEY,
    price FLOAT NOT NULL,
    capacity FLOAT NOT NULL,
    term INTEGER NOT NULL,
    start_date DATE NOT NULL,
    end_date DATE NOT NULL,
    contract_capacity FLOAT NOT NULL,
    microgrid_id INTEGER REFERENCES Microgrid(id),
    utility_id INTEGER REFERENCES Utility(id)
);
CREATE TABLE RenewablePPAContract (
    id SERIAL PRIMARY KEY,
    supplier VARCHAR(255) NOT NULL,
    price FLOAT NOT NULL,
    capacity FLOAT NOT NULL,
    term INTEGER NOT NULL,
    start_date DATE NOT NULL,
    end_date DATE NOT NULL,
    contract_capacity FLOAT NOT NULL,
    technology VARCHAR
