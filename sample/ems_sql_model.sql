-- Microgrid table
CREATE TABLE microgrids (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    location TEXT NOT NULL,
    capacity REAL NOT NULL,
    status TEXT NOT NULL
);

-- Device table
CREATE TABLE devices (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    type TEXT NOT NULL,
    manufacturer TEXT NOT NULL,
    model TEXT NOT NULL,
    location TEXT NOT NULL,
    capacity REAL NOT NULL,
    status TEXT NOT NULL,
    microgrid_id INTEGER NOT NULL REFERENCES microgrids(id)
);

-- SolarEnergy table (inherits from Device)
CREATE TABLE solar_energy (
    id INTEGER PRIMARY KEY REFERENCES devices(id),
    generation_rate REAL NOT NULL
);

-- WindEnergy table (inherits from Device)
CREATE TABLE wind_energy (
    id INTEGER PRIMARY KEY REFERENCES devices(id),
    generation_rate REAL NOT NULL
);

-- ESS table (inherits from Device)
CREATE TABLE ess (
    id INTEGER PRIMARY KEY REFERENCES devices(id),
    capacity REAL NOT NULL,
    charge_rate REAL NOT NULL,
    discharge_rate REAL NOT NULL,
    soc REAL NOT NULL
);

-- EVCharger table (inherits from Device)
CREATE TABLE ev_chargers (
    id INTEGER PRIMARY KEY REFERENCES devices(id),
    charging_rate REAL NOT NULL,
    num_ports INTEGER NOT NULL
);

-- Load table (inherits from Device)
CREATE TABLE loads (
    id INTEGER PRIMARY KEY REFERENCES devices(id),
    power REAL NOT NULL,
    energy_consumption_today REAL NOT NULL,
    energy_consumption_lifetime REAL NOT NULL
);

-- LiveData table
CREATE TABLE live_data (
    id SERIAL PRIMARY KEY,
    timestamp TIMESTAMP NOT NULL,
    device_id INTEGER NOT NULL REFERENCES devices(id),
    data JSONB NOT NULL,
    charge_rate REAL,
    discharge_rate REAL,
    soc REAL,
    charging_rate REAL,
    num_ports INTEGER,
    power REAL,
    energy_production_today REAL,
    energy_production_this_week REAL,
    energy_production_this_month REAL,
    energy_production_this_year REAL,
    energy_production_lifetime REAL,
    energy_consumption_today REAL,
    energy_consumption_this_week REAL,
    energy_consumption_this_month REAL,
    energy_consumption_this_year REAL,
    energy_consumption_lifetime REAL,
    generation_rate REAL
);

-- PPA table
CREATE TABLE ppas (
    id SERIAL PRIMARY KEY,
    supplier TEXT NOT NULL,
    price REAL NOT NULL,
    capacity REAL NOT NULL,
    term INTEGER NOT NULL,
    start_date DATE NOT NULL,
    end_date DATE NOT NULL,
    contract_capacity REAL NOT NULL,
    technology TEXT NOT NULL
);

-- RenewablePPAContract table (inherits from PPA)
CREATE TABLE renewable_ppa_contracts (
    id INTEGER PRIMARY KEY REFERENCES ppas(id),
    from_solar_plant BOOLEAN NOT NULL,
    from_wind_plant BOOLEAN NOT NULL,
    solar_plant_name TEXT,
    wind_plant_name TEXT
);

-- Utility table
CREATE TABLE utilities (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    location TEXT NOT NULL,
    energy_sources JSONB NOT NULL,
    peak_demand REAL NOT NULL,
    peak_demand_time TIME NOT NULL,
    energy_rates JSONB NOT NULL
);

-- UtilityPriceContract table (inherits from Contract)
CREATE TABLE utility_price_contracts (
    id INTEGER PRIMARY KEY REFERENCES contracts(id),
    utility_id INTEGER NOT NULL REFERENCES utilities(id),
    energy_price REAL NOT NULL,
    start_time TIME NOT NULL,
    end_time TIME NOT NULL,
    weekday_rates JSONB NOT NULL,
    weekend_rates JSONB NOT NULL
);
