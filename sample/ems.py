'''
This file contains the data model for EMS managed microgrid system.
'''

# ==========
# user model
# ==========

class SystemAdmin:
    def __init__(self, username, password, email):
        self.username = username  # username of the system admin
        self.password = password  # password of the system admin
        self.email = email  # email address of the system admin

class Organization:
    def __init__(self, name, address, contact_person, contact_email, contact_phone):
        self.name = name  # name of the organization
        self.address = address  # physical address of the organization
        self.contact_person = contact_person  # name of the contact person for the organization
        self.contact_email = contact_email  # email address of the contact person for the organization
        self.contact_phone = contact_phone  # phone number of the contact person for the organization
        self.users = []  # list of users associated with the organization
        self.microgrids = []  # list of microgrids owned by the organization
        self.subscriptions = []  # list of subscriptions for the organization

class User:
    def __init__(self, username, password, email, role, organization):
        self.username = username  # username of the user
        self.password = password  # password of the user
        self.email = email  # email address of the user
        self.role = role  # role of the user (e.g., admin, operator)
        self.organization = organization  # organization that the user belongs to

# ==========
# microgrid model
# ==========
class Microgrid:
    def __init__(self, name, location, capacity, organization, topology):
        self.name = name  # name of the microgrid
        self.location = location  # physical location of the microgrid
        self.capacity = capacity  # total capacity of the microgrid
        self.organization = organization  # organization that owns the microgrid
        self.devices = []  # list of devices associated with the microgrid
        self.topology = topology  # topology of the microgrid (e.g., grid-connected, islanded)

class Device:
    def __init__(self, name, device_type, manufacturer, model, location, capacity, status, microgrid):
        self.name = name  # name of the device
        self.device_type = device_type  # type of the device (e.g., ESS, EV Charger, Load)
        self.manufacturer = manufacturer  # manufacturer of the device
        self.model = model  # model of the device
        self.location = location  # physical location of the device
        self.capacity = capacity  # capacity of the device
        self.status = status  # current status of the device (e.g., online, offline)
        self.microgrid = microgrid  # microgrid that the device belongs to

class ESS(Device):
    def __init__(self, name, manufacturer, model, location, capacity, status, microgrid, charge_rate, discharge_rate, soc):
        super().__init__(name, "ESS", manufacturer, model, location, capacity, status, microgrid)
        self.charge_rate = charge_rate  # charge rate of the ESS
        self.discharge_rate = discharge_rate  # discharge rate of the ESS
        self.soc = soc  # state of charge of the ESS

class EVCharger(Device):
    """
    Class representing an electric vehicle charger device.

    Inherits from Device class.
    """

    def __init__(self, name, manufacturer, model, location, capacity, status, microgrid, charging_rate, num_ports):
        """
        Constructor for EVCharger class.

        Parameters:
        - name (str): Name of the EV charger.
        - manufacturer (str): Manufacturer of the EV charger.
        - model (str): Model of the EV charger.
        - location (str): Location of the EV charger.
        - capacity (float): Capacity of the EV charger in kW.
        - status (str): Status of the EV charger (e.g. online, offline).
        - microgrid (Microgrid): Microgrid that the EV charger belongs to.
        - charging_rate (float): Maximum charging rate of the EV charger in kW.
        - num_ports (int): Number of charging ports available in the EV charger.
        """

        super().__init__(name, "EV Charger", manufacturer, model, location, capacity, status, microgrid)
        self.charging_rate = charging_rate
        self.num_ports = num_ports

class Load(Device):
    """
    Class representing a load device.

    Inherits from Device class.
    """

    def __init__(self, name, manufacturer, model, location, capacity, status, microgrid, power):
        """
        Constructor for Load class.

        Parameters:
        - name (str): Name of the load.
        - manufacturer (str): Manufacturer of the load.
        - model (str): Model of the load.
        - location (str): Location of the load.
        - capacity (float): Capacity of the load in kW.
        - status (str): Status of the load (e.g. on, off).
        - microgrid (Microgrid): Microgrid that the load belongs to.
        - power (float): Power demand of the load in kW.
        """

        super().__init__(name, "Load", manufacturer, model, location, capacity, status, microgrid)
        self.power = power

class SolarEnergySelfUse(Device):
    """
    Class representing a self-use solar energy device.

    Inherits from Device class.
    """

    def __init__(self, name, manufacturer, model, location, capacity, status, microgrid, generation_rate):
        """
        Constructor for SolarEnergySelfUse class.

        Parameters:
        - name (str): Name of the self-use solar energy device.
        - manufacturer (str): Manufacturer of the self-use solar energy device.
        - model (str): Model of the self-use solar energy device.
        - location (str): Location of the self-use solar energy device.
        - capacity (float): Capacity of the self-use solar energy device in kW.
        - status (str): Status of the self-use solar energy device (e.g. online, offline).
        - microgrid (Microgrid): Microgrid that the self-use solar energy device belongs to.
        - generation_rate (float): Maximum energy generation rate of the self-use solar energy device in kW.
        """

        super().__init__(name, "Solar Energy (Self-use)", manufacturer, model, location, capacity, status, microgrid)
        self.generation_rate = generation_rate


class SolarEnergyPPA(Device):
    """
    Class representing a solar energy device purchased through a PPA.

    Inherits from Device class.
    """

    def __init__(self, name, manufacturer, model, location, capacity, status, microgrid, generation_rate, ppa):
        """
        Constructor for SolarEnergyPPA class.

        Parameters:
        - name (str): Name of the solar energy device purchased through a PPA.
        - manufacturer (str): Manufacturer of the solar energy device purchased through a PPA.
        - model (str): Model of the solar energy device purchased through a PPA.
        - location (str): Location of the solar energy device purchased through a PPA.
        - capacity (float): Capacity of the solar energy device purchased through a PPA in kW.
        - status (str): Status of the solar energy device purchased through a PPA (e.g. online, offline).
        - microgrid (Microgrid): Microgrid that the solar energy device purchased through a PPA belongs to.
        - generation_rate (float): Maximum energy generation rate of the solar energy device purchased through a PPA in kW.
        - ppa (RenewablePPAContract): PPA information for the solar energy device.
        """

        super().__init__(name, "Solar Energy (PPA)", manufacturer, model, location, capacity, status, microgrid)
        self.generation_rate = generation_rate
        self.ppa = ppa


class WindEnergyPPA(Device):
    """
    Class representing a wind energy device purchased through a PPA.

    Inherits from Device class.
    """

    def __init__(self, name, manufacturer, model, location, capacity, status, microgrid, generation_rate, ppa):
        """
        Constructor for WindEnergyPPA class.

        Parameters:
        - name (str): Name of the wind energy device purchased through a PPA.
        - manufacturer (str): Manufacturer of the wind energy device purchased through a PPA.
        - model (str): Model of the wind energy device purchased through a PPA.
        - location (str): Location of the wind energy device purchased through a PPA.
        - capacity (float): Capacity of the wind energy device purchased through a PPA in kW.
        - status (str): Status of the wind energy device purchased through a PPA (e.g. online, offline).
        - microgrid (Microgrid): Microgrid that the wind energy device purchased through a PPA belongs
        - generation_rate (float): Maximum energy generation rate of the solar energy device purchased through a PPA in kW.
        - ppa (RenewablePPAContract): PPA information for the solar energy device.

        """
        self.generation_rate = generation_rate
        self.ppa = ppa

# ========
# Contract & Pricing 
# ========

class RenewablePPAContract:
    """
    Class representing a Power Purchase Agreement (PPA) for renewable energy.

    A PPA is a legal contract between an energy buyer and a renewable energy provider.

    Parameters:
    - supplier (str): Name of the renewable energy provider.
    - price (float): Price of the renewable energy in USD/kWh.
    - capacity (float): Capacity of the renewable energy plant in kW.
    - term (int): Length of the PPA contract in years.
    - start_date (str): Start date of the PPA contract in YYYY-MM-DD format.
    - end_date (str): End date of the PPA contract in YYYY-MM-DD format.
    - contract_capacity (float): Amount of energy to be purchased under the PPA in kW.
    - technology (str): Type of renewable energy technology (e.g. solar, wind).
    """

    def __init__(self, supplier, price, capacity, term, start_date, end_date, contract_capacity, technology):
        self.supplier = supplier
        self.price = price
        self.capacity = capacity
        self.term = term
        self.start_date = start_date
        self.end_date = end_date
        self.contract_capacity = contract_capacity
        self.technology = technology

class UtilityPriceContract:
    """
    Class representing a contract between a microgrid and a utility company.

    Attributes:
    - utility (Utility): The utility company providing the energy.
    - start_date (datetime): The start date of the contract.
    - end_date (datetime): The end date of the contract.
    - energy_rate (float): The rate charged by the utility company for energy (in $/kWh).
    - demand_charge (float): The rate charged by the utility company for peak demand (in $/kW).
    """

    def __init__(self, utility, start_date, end_date, energy_rate, demand_charge):
        """
        Constructor for UtilityPriceContract class.

        Parameters:
        - utility (Utility): The utility company providing the energy.
        - start_date (datetime): The start date of the contract.
        - end_date (datetime): The end date of the contract.
        - energy_rate (float): The rate charged by the utility company for energy (in $/kWh).
        - demand_charge (float): The rate charged by the utility company for peak demand (in $/kW).
        """

        self.utility = utility
        self.start_date = start_date
        self.end_date = end_date
        self.energy_rate = energy_rate
        self.demand_charge = demand_charge

# ========
# Microgrid Settings
# ========

class EnergyDispatchPreference:
    """
    Class representing the energy dispatch preference for a microgrid.

    """

    def __init__(self, microgrid, devices, optimization_strategy, min_power, max_power):
        """
        Constructor for EnergyDispatchPreference class.

        Parameters:
        - microgrid (Microgrid): Microgrid that the dispatch preference belongs to.
        - devices (List[Device]): List of devices in the microgrid.
        - optimization_strategy (str): Strategy used to optimize the energy dispatch.
        - min_power (float): Minimum power that the microgrid should consume in kW.
        - max_power (float): Maximum power that the microgrid can consume in kW.
        """
        self.microgrid = microgrid
        self.devices = devices
        self.optimization_strategy = optimization_strategy
        self.min_power = min_power
        self.max_power = max_power

# ========
# System Settings
# ========
class SystemSettings:
    """
    Class representing the system settings.

    """

    def __init__(self, time_zone, language, units_of_measurement):
        """
        Constructor for SystemSettings class.

        Parameters:
        - time_zone (str): Time zone for the system.
        - language (str): Language used in the system.
        - units_of_measurement (str): Units of measurement used in the system (e.g. kW, kWh).
        """

        self.time_zone = time_zone
        self.language = language
        self.units_of_measurement = units_of_measurement

class Subscription:
    """
    Class representing a subscription plan.
    The subscription plan is used to manage the features could used on the platform. 

    """

    def __init__(self, name, description, price, billing_cycle, renewal_date, features, organization):
        """
        Constructor for Subscription class.

        Parameters:
        - name (str): Name of the subscription plan.
        - description (str): Description of the subscription plan.
        - price (float): Price of the subscription plan.
        - billing_cycle (str): Billing cycle of the subscription plan (e.g. monthly, yearly).
        - renewal_date (datetime): Date of renewal for the subscription plan.
        - features (List[str]): List of features included in the subscription plan.
        - organization (str): Name of the organization that offers the subscription plan.
        """

        self.name = name
        self.description = description
        self.price = price
        self.billing_cycle = billing_cycle
        self.renewal_date = renewal_date
        self.features = features
        self.organization = organization

class LiveData:
    def __init__(self, timestamp, device, data):
        """
        Represents live data for a specific device at a given timestamp.

        Args:
            timestamp (datetime): The timestamp when the data was collected.
            device (Device): The device for which the data was collected.
            data (float): The data value collected for the device at the given timestamp.
        """
        self.timestamp = timestamp
        self.device = device
        self.data = data

class ESSLiveData(LiveData):
    """
    Class to represent live data for an Energy Storage System (ESS) device.

    Attributes:
    - timestamp (datetime): the time at which the data was recorded
    - device (ESS): the ESS device that generated the data
    - data (dict): a dictionary of key-value pairs representing the live data
    - charge_rate (float): the rate at which the ESS is currently charging (in kW)
    - discharge_rate (float): the rate at which the ESS is currently discharging (in kW)
    - soc (float): the current state of charge of the ESS (as a percentage)
    - voltage (float): the voltage of the ESS (in V)
    - current (float): the current flowing through the ESS (in A)
    - temperature (float): the temperature of the ESS (in °C)
    - power (float): the current power output of the ESS (in kW)
    """
    def __init__(self, timestamp, device, data, charge_rate, discharge_rate, soc, voltage, current, temperature, power):
        super().__init__(timestamp, device, data)
        self.charge_rate = charge_rate
        self.discharge_rate = discharge_rate
        self.soc = soc
        self.voltage = voltage
        self.current = current
        self.temperature = temperature
        self.power = power

class EVChargerLiveData(LiveData):
    """
    Class to represent live data for an Electric Vehicle (EV) Charger device.

    Attributes:
    - timestamp (datetime): the time at which the data was recorded
    - device (EVCharger): the EV Charger device that generated the data
    - data (dict): a dictionary of key-value pairs representing the live data
    - charging_rate (float): the rate at which the EV Charger is currently charging (in kW)
    - num_ports (int): the number of ports on the EV Charger
    - energy_delivered (float): the amount of energy delivered by the EV Charger (in kWh)
    - energy_remaining (float): the amount of energy remaining in the EV Charger (in kWh)
    - session_time (float): the amount of time the current charging session has been active (in minutes)
    - session_cost (float): the cost of the current charging session (in the local currency)
    """
    def __init__(self, timestamp, device, data, charging_rate, num_ports, energy_delivered, energy_remaining, session_time, session_cost):
        super().__init__(timestamp, device, data)
        self.charging_rate = charging_rate
        self.num_ports = num_ports
        self.energy_delivered = energy_delivered
        self.energy_remaining = energy_remaining
        self.session_time = session_time
        self.session_cost = session_cost

class LoadLiveData(LiveData):
    """
    Class to represent live data for a Load device.

    Attributes:
    - timestamp (datetime): the time at which the data was recorded
    - device (Load): the Load device that generated the data
    - data (dict): a dictionary of key-value pairs representing the live data
    - power (float): the current power consumption of the Load (in kW)
    - energy_consumption (float): the total energy consumed by the Load up to this point (in kWh)
    - daily_energy_consumption (float): the total energy consumed by the Load today (in kWh)
    """
    def __init__(self, timestamp, device, data, power, energy_consumption, daily_energy_consumption):
        super().__init__(timestamp, device, data)
        self.power = power
        self.energy_consumption = energy_consumption
        self.daily_energy_consumption = daily_energy_consumption

class SolarEnergyLiveData(LiveData):
    """
    Class to represent live data for a Solar Energy device.

    Attributes:
    - timestamp (datetime): the time at which the data was recorded
    - device (SolarEnergy): the Solar Energy device that generated the data
    - data (dict): a dictionary of key-value pairs representing the live data
    - power (float): the current energy generation rate of the Solar Energy device (in kW)
    - energy_production_today (float): the amount of energy produced by the Solar Energy device today (in kWh)
    - energy_production_lifetime (float): the total amount of energy produced by the Solar Energy device over its lifetime (in kWh)
    - energy_consumption_today (float): the amount of energy consumed by the microgrid from the Solar Energy device today (in kWh)
    - energy_consumption_lifetime (float): the total amount of energy consumed by the microgrid from the Solar Energy device over its lifetime (in kWh)
    """
    def __init__(self, timestamp, device, data, power, energy_production_today, energy_production_this_week, energy_production_this_month, energy_production_this_year, energy_production_lifetime, energy_consumption_today, energy_consumption_this_week, energy_consumption_this_month, energy_consumption_this_year, energy_consumption_lifetime):
        super().__init__(timestamp, device, data)
        self.power = power
        self.energy_production_today = energy_production_today
        self.energy_production_lifetime = energy_production_lifetime
        self.energy_consumption_today = energy_consumption_today
        self.energy_consumption_lifetime = energy_consumption_lifetime

class SolarPlantLiveData(LiveData):
    """
    Class to represent live data for a solar energy system from a solar plant via PPA.

    Attributes:
    - timestamp (datetime): the time at which the data was recorded
    - device (SolarEnergy): the Solar Energy device that generated the data
    - data (dict): a dictionary of key-value pairs representing the live data
    - power (float): the current energy generation rate of the Solar Energy device (in kW)
    - energy_production_today (float): the amount of energy produced by the Solar Energy device today (in kWh)
    - energy_production_this_week (float): the amount of energy produced by the Solar Energy device this week (in kWh)
    - energy_production_this_month (float): the amount of energy produced by the Solar Energy device this month (in kWh)
    - energy_production_this_year (float): the amount of energy produced by the Solar Energy device this year (in kWh)
    - energy_production_lifetime (float): the total amount of energy produced by the Solar Energy device over its lifetime (in kWh)
    - price (float): the current price of the PPA for the solar energy system in USD/kWh
    """
    def __init__(self, timestamp, device, data, power, energy_production_today, energy_production_this_week, energy_production_this_month, energy_production_this_year, energy_production_lifetime, price):
        super().__init__(timestamp, device, data)
        self.power = power
        self.energy_production_today = energy_production_today
        self.energy_production_this_week = energy_production_this_week
        self.energy_production_this_month = energy_production_this_month
        self.energy_production_this_year = energy_production_this_year
        self.energy_production_lifetime = energy_production_lifetime
        self.price = price

class WindPlantLiveData(LiveData):
    """
    Class to represent live data for a Wind Energy plant.

    Attributes:
    - timestamp (datetime): the time at which the data was recorded
    - device (WindEnergy): the Wind Energy device that generated the data
    - data (dict): a dictionary of key-value pairs representing the live data
    - generation_rate (float): the current energy generation rate of the Wind Energy device (in kW)
    - energy_production_today (float): the amount of energy produced by the Wind Energy device today (in kWh)
    - energy_production_this_week (float): the amount of energy produced by the Wind Energy device this week (in kWh)
    - energy_production_this_month (float): the amount of energy produced by the Wind Energy device this month (in kWh)
    - energy_production_this_year (float): the amount of energy produced by the Wind Energy device this year (in kWh)
    - energy_production_lifetime (float): the total amount of energy produced by the Wind Energy device over its lifetime (in kWh)
    - energy_consumption_today (float): the amount of energy consumed by the microgrid from the Wind Energy device today (in kWh)
    - energy_consumption_this_week (float): the amount of energy consumed by the microgrid from the Wind Energy device this week (in kWh)
    - energy_consumption_this_month (float): the amount of energy consumed by the microgrid from the Wind Energy device this month (in kWh)
    - energy_consumption_this_year (float): the amount of energy consumed by the microgrid from the Wind Energy device this year (in kWh)
    - energy_consumption_lifetime (float): the total amount of energy consumed by the microgrid from the Wind Energy device over its lifetime (in kWh)
    - wind_speed (float): the current wind speed (in meters per second) at the Wind Energy plant
    - wind_direction (float): the current wind direction (in degrees) at the Wind Energy plant
    """
    def __init__(self, timestamp, device, data, generation_rate, energy_production_today, energy_production_this_week, energy_production_this_month, energy_production_this_year, energy_production_lifetime, energy_consumption_today, energy_consumption_this_week, energy_consumption_this_month, energy_consumption_this_year, energy_consumption_lifetime, wind_speed, wind_direction):
        super().__init__(timestamp, device, data)
        self.generation_rate = generation_rate
        self.energy_production_today = energy_production_today
        self.energy_production_this_week = energy_production_this_week
        self.energy_production_this_month = energy_production_this_month
        self.energy_production_this_year = energy_production_this_year
        self.energy_production_lifetime = energy_production_lifetime
        self.energy_consumption_today = energy_consumption_today
        self.energy_consumption_this_week = energy_consumption_this_week
        self.energy_consumption_this_month = energy_consumption_this_month
        self.energy_consumption_this_year = energy_consumption_this_year
        self.energy_consumption_lifetime = energy_consumption_lifetime
        self.wind_speed = wind_speed
        self.wind_direction = wind_direction
