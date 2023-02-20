import psycopg2
from psycopg2.extras import RealDictCursor
from datetime import datetime

import graphene
from graphene.types import Scalar
from graphene.types.json import JSONString

# Define custom JSON scalar type
class JSON(Scalar):
    @staticmethod
    def serialize(value):
        return value

    @staticmethod
    def parse_literal(node):
        return node.value

    @staticmethod
    def parse_value(value):
        return value


# Define database connection parameters
db_config = {
    "host": "your_host",
    "database": "your_database",
    "user": "your_user",
    "password": "your_password",
}


# Define helper function to execute database queries
def execute_query(query, params=None):
    with psycopg2.connect(**db_config) as conn:
        with conn.cursor(cursor_factory=RealDictCursor) as cur:
            cur.execute(query, params)
            result = cur.fetchall()
    return result


# Define the GraphQL types for the different database tables
class SystemAdminType(graphene.ObjectType):
    id = graphene.Int()
    username = graphene.String()
    password = graphene.String()
    email = graphene.String()


class OrganizationType(graphene.ObjectType):
    id = graphene.Int()
    name = graphene.String()
    address = graphene.String()
    contact_person = graphene.String()
    contact_email = graphene.String()
    contact_phone = graphene.String()
    admin_id = graphene.Int()

    def resolve_admin_id(parent, info):
        query = "SELECT * FROM SystemAdmin WHERE id=%s"
        result = execute_query(query, (parent["admin_id"],))
        return result[0] if result else None

class EMSUserType(graphene.ObjectType):
    id = graphene.Int()
    username = graphene.String()
    password = graphene.String()
    email = graphene.String()
    role = graphene.String()
    organization_id = graphene.Int()

    def resolve_organization_id(parent, info):
        query = "SELECT * FROM Organization WHERE id=%s"
        result = execute_query(query, (parent["organization_id"],))
        return result[0] if result else None

class MicrogridType(graphene.ObjectType):
    id = graphene.Int()
    name = graphene.String()
    location = graphene.String()
    max_load = graphene.Float()
    max_generation = graphene.Float()
    voltage = graphene.Float()
    frequency = graphene.Float()
    topology = JSON()

    owner_id = graphene.Int()
    utility_id = graphene.Int()
    renewable_ppa_id = graphene.Int()
    system_settings_id = graphene.Int()

    def resolve_owner_id(parent, info):
        query = "SELECT * FROM Organization WHERE id=%s"
        result = execute_query(query, (parent["owner_id"],))
        return result[0] if result else None

    def resolve_utility_id(parent, info):
        query = "SELECT * FROM Utility WHERE id=%s"
        result = execute_query(query, (parent["utility_id"],))
        return result[0] if result else None

    def resolve_renewable_ppa_id(parent, info):
        query = "SELECT * FROM RenewablePPAContract WHERE id=%s"
        result = execute_query(query, (parent["renewable_ppa_id"],))
        return result[0] if result else None

    def resolve_system_settings_id(parent, info):
        query = "SELECT * FROM SystemSettings WHERE id=%s"
        result = execute_query(query, (parent["system_settings_id"],))
        return result[0] if result else None


class DeviceType(graphene.ObjectType):
    id = graphene.Int()
    device_type = graphene.String()
    name = graphene.String()
    description = graphene.String()
    manufacturer = graphene.String()
    model_number = graphene.String()
    serial_number = graphene.String()
    microgrid_id = graphene.Int()

    ess = graphene.Field(lambda: ESSType)
    ev_charger = graphene.Field(lambda: EVChargerType)
    load = graphene.Field(lambda: LoadType)
    solar_energy = graphene.Field(lambda: SolarEnergyType)

    def resolve_ess(parent, info):
        query = "SELECT * FROM ESS WHERE device_id=%s"
        result = execute_query(query, (parent["id"],))
        return result[0] if result else None

    def resolve_ev_charger(parent, info):
        query = "SELECT * FROM EVCharger WHERE device_id=%s"
        result = execute_query(query, (parent["id"],))
        return result[0] if result else None

    def resolve_load(parent, info):
        query = "SELECT * FROM Load WHERE device_id=%s"
        result = execute_query(query, (parent["id"],))
        return result[0] if result else None

    def resolve_solar_energy(parent, info):
        query = "SELECT * FROM SolarEnergy WHERE device_id=%s"
        result = execute_query(query, (parent["id"],))
        return result[0] if result else None


class ESSType(graphene.ObjectType):
    id = graphene.Int()
    device_id = graphene.Int()
    capacity = graphene.Float()
    charge_efficiency = graphene.Float()
    discharge_efficiency = graphene.Float()
    max_charge_rate = graphene.Float()
    max_discharge_rate = graphene.Float()
    soc = graphene.Float()

    device = graphene.Field(lambda: DeviceType)

    def resolve_device(parent, info):
        query = "SELECT * FROM Device WHERE id=%s"
        result = execute_query(query, (parent["device_id"],))
        return result[0] if result else None
    
class EVChargerType(graphene.ObjectType):
    id = graphene.Int()
    device_id = graphene.Int()
    num_ports = graphene.Int()
    max_charging_power = graphene.Float()

    device = graphene.Field(lambda: DeviceType)

    def resolve_device(parent, info):
        query = "SELECT * FROM Device WHERE id=%s"
        result = execute_query(query, (parent["device_id"],))
        return result[0] if result else None


class LoadType(graphene.ObjectType):
    id = graphene.Int()
    device_id = graphene.Int()
    power = graphene.Float()
    priority = graphene.Int()

    device = graphene.Field(lambda: DeviceType)

    def resolve_device(parent, info):
        query = "SELECT * FROM Device WHERE id=%s"
        result = execute_query(query, (parent["device_id"],))
        return result[0] if result else None


class SolarEnergyType(graphene.ObjectType):
    id = graphene.Int()
    device_id = graphene.Int()
    max_power = graphene.Float()

    device = graphene.Field(lambda: DeviceType)

    def resolve_device(parent, info):
        query = "SELECT * FROM Device WHERE id=%s"
        result = execute_query(query, (parent["device_id"],))
        return result[0] if result else None


class RenewablePPAContractType(graphene.ObjectType):
    id = graphene.Int()
    start_date = graphene.String()
    end_date = graphene.String()
    price = graphene.Float()
    source_type = graphene.String()
    device = graphene.Field(lambda: DeviceType)


class RenewableSourceFromPPAType(graphene.ObjectType):
    id = graphene.Int()
    source_type = graphene.String()
    device = graphene.Field(lambda: DeviceType)
    renewable_ppa = graphene.Field(lambda: RenewablePPAContractType)


class LiveDataType(graphene.ObjectType):
    id = graphene.Int()
    timestamp = graphene.String()
    device_id = graphene.Int()
    data = JSON()

    device = graphene.Field(lambda: DeviceType)

    def resolve_device(parent, info):
        query = "SELECT * FROM Device WHERE id=%s"
        result = execute_query(query, (parent["device_id"],))
        return result[0] if result else None


class ESSLiveDataType(graphene.ObjectType):
    id = graphene.Int()
    timestamp = graphene.String()
    device_id = graphene.Int()
    soc = graphene.Float()

    device = graphene.Field(lambda: DeviceType)

    def resolve_device(parent, info):
        query = "SELECT * FROM Device WHERE id=%s"
        result = execute_query(query, (parent["device_id"],))
        return result[0] if result else None


class EVChargerLiveDataType(graphene.ObjectType):
    id = graphene.Int()
    timestamp = graphene.String()
    device_id = graphene.Int()
    port_id = graphene.Int()
    status = graphene.String()

    device = graphene.Field(lambda: DeviceType)

    def resolve_device(parent, info):
        query = "SELECT * FROM Device WHERE id=%s"
        result = execute_query(query, (parent["device_id"],))
        return result[0] if result else None


class LoadLiveDataType(graphene.ObjectType):
    id = graphene.Int()
    timestamp = graphene.String()
    device_id = graphene.Int()
    power = graphene.Float()

    device = graphene.Field(lambda: DeviceType)

    def resolve_device(parent, info):
        query = "SELECT * FROM Device WHERE id=%s"
        result = execute_query(query, (parent["device_id"],))
        return result[0] if result else None


class SolarEnergyLiveDataType(graphene.ObjectType):
    id = graphene.Int()
    timestamp = graphene.String()
    device_id = graphene.Int()
    power = graphene.Float()

    device = graphene.Field(lambda: DeviceType)

    def resolve_device(parent, info):
        query = "SELECT * FROM Device WHERE id=%s"
        result = execute_query(query, (parent["device_id"],))
        return result[0] if result else None
    

# Define the GraphQL resolvers for the different queries
class Query(graphene.ObjectType):
    # Define resolver for systemAdmin query
    systemAdmin = graphene.Field(SystemAdminType, id=graphene.Int(required=True))

    def resolve_systemAdmin(parent, info, id):
        query = "SELECT * FROM SystemAdmin WHERE id=%s"
        result = execute_query(query, (id,))
        return result[0] if result else None

    # Define resolver for systemAdmins query
    systemAdmins = graphene.List(SystemAdminType)

    def resolve_systemAdmins(parent, info):
        query = "SELECT * FROM SystemAdmin"
        result = execute_query(query)
        return result

    # Define resolver for organization query
    organization = graphene.Field(OrganizationType, id=graphene.Int(required=True))

    def resolve_organization(parent, info, id):
        query = "SELECT * FROM Organization WHERE id=%s"
        result = execute_query(query, (id,))
        return result[0] if result else None

    # Define resolver for organizations query
    organizations = graphene.List(OrganizationType)

    def resolve_organizations(parent, info):
        query = "SELECT * FROM Organization"
        result = execute_query(query)
        return result

    # Define resolver for emsUser query
    emsUser = graphene.Field(EMSUserType, id=graphene.Int(required=True))

    def resolve_emsUser(parent, info, id):
        query = "SELECT * FROM EMSUser WHERE id=%s"
        result = execute_query(query, (id,))
        return result[0] if result else None

    # Define resolver for emsUsers query
    emsUsers = graphene.List(EMSUserType, organization_id=graphene.Int(required=True))

    def resolve_emsUsers(parent, info, organization_id):
        query = "SELECT * FROM EMSUser WHERE organization_id=%s"
        result = execute_query(query, (organization_id,))
        return result

    # Define resolver for microgrid query
    microgrid = graphene.Field(MicrogridType, id=graphene.Int(required=True))

    def resolve_microgrid(parent, info, id):
        query = "SELECT * FROM Microgrid WHERE id=%s"
        result = execute_query(query, (id,))
        return result[0] if result else None

    # Define resolver for microgrids query
    microgrids = graphene.List(MicrogridType)

    def resolve_microgrids(parent, info):
        query = "SELECT * FROM Microgrid"
        result = execute_query(query)
        return result

    # Define resolver for device query
    device = graphene.Field(DeviceType, id=graphene.Int(required=True))

    def resolve_device(parent, info, id):
        query = "SELECT * FROM Device WHERE id=%s"
        result = execute_query(query, (id,))
        return result[0] if result else None

    # Define resolver for devices query
    devices = graphene.List(DeviceType, microgrid_id=graphene.Int(required=True))

    def resolve_devices(parent, info, microgrid_id):
        query = "SELECT * FROM Device WHERE microgrid_id=%s"
        result = execute_query(query, (microgrid_id,))
        return result

    # Define resolver for ess query
    ess = graphene.Field(ESSType, id=graphene.Int(required=True))

    def resolve_ess(parent, info, id):
        query = "SELECT * FROM ESS WHERE id=%s"
        result = execute_query(query, (id,))
        return result[0] if result else None

    # Define resolver for evCharger query
    evCharger = graphene.Field(EVChargerType, id=graphene.Int(required=True))

    def resolve_evCharger(parent, info, id):
        query = "SELECT * FROM EVCharger WHERE id=%s"
        result = execute_query(query, (id,))
        return result[0] if result else None

    # Define resolver for evChargers query
    evChargers = graphene.List(EVChargerType, microgrid_id=graphene.Int(required=True))

    def resolve_evChargers(parent, info, microgrid_id):
        query = "SELECT * FROM EVCharger WHERE microgrid_id=%s"
        result = execute_query(query, (microgrid_id,))
        return result

    # Define resolver for load query
    load = graphene.Field(LoadType, id=graphene.Int(required=True))

    def resolve_load(parent, info, id):
        query = "SELECT * FROM Load WHERE id=%s"
        result = execute_query(query, (id,))
        return result[0] if result else None

    # Define resolver for loads query
    loads = graphene.List(LoadType, microgrid_id=graphene.Int(required=True))

    def resolve_loads(parent, info, microgrid_id):
        query = "SELECT * FROM Load WHERE microgrid_id=%s"
        result = execute_query(query, (microgrid_id,))
        return result

    # Define resolver for solarEnergy query
    solarEnergy = graphene.Field(SolarEnergyType, id=graphene.Int(required=True))

    def resolve_solarEnergy(parent, info, id):
        query = "SELECT * FROM SolarEnergy WHERE id=%s"
        result = execute_query(query, (id,))
        return result[0] if result else None

    # Define resolver for solarEnergyList query
    solarEnergyList = graphene.List(SolarEnergyType, microgrid_id=graphene.Int(required=True))

    def resolve_solarEnergyList(parent, info, microgrid_id):
        query = "SELECT * FROM SolarEnergy WHERE microgrid_id=%s"
        result = execute_query(query, (microgrid_id,))
        return result

    # Define resolver for liveData query
    liveData = graphene.Field(LiveDataType, id=graphene.Int(required=True))

    def resolve_liveData(parent, info, id):
        query = "SELECT * FROM LiveData WHERE id=%s"
        result = execute_query(query, (id,))
        return result[0] if result else None

    # Define resolver for liveDataList query
    liveDataList = graphene.List(LiveDataType, device_id=graphene.Int(required=True))

    def resolve_liveDataList(parent, info, device_id):
        query = "SELECT * FROM LiveData WHERE device_id=%s"
        result = execute_query(query, (device_id,))
        return result

    # Define resolver for essLiveData query
    essLiveData = graphene.Field(ESSLiveDataType, id=graphene.Int(required=True))

    def resolve_essLiveData(parent, info, id):
        query = "SELECT * FROM ESSLiveData WHERE id=%s"
        result = execute_query(query, (id,))
        return result[0] if result else None

    def resolve_essLiveDataList(parent, info, device_id):
        query = "SELECT * FROM ESSLiveData WHERE device_id=%s"
        result = execute_query(query, (device_id,))
        return result
    
    # Define resolver for evChargerLiveData query
    evChargerLiveData = graphene.Field(EVChargerLiveDataType, id=graphene.Int(required=True))

    def resolve_evChargerLiveData(parent, info, id):
        query = "SELECT * FROM EVChargerLiveData WHERE id=%s"
        result = execute_query(query, (id,))
        return result[0] if result else None

    # Define resolver for evChargerLiveDataList query
    evChargerLiveDataList = graphene.List(EVChargerLiveDataType, device_id=graphene.Int(required=True))

    def resolve_evChargerLiveDataList(parent, info, device_id):
        query = "SELECT * FROM EVChargerLiveData WHERE device_id=%s"
        result = execute_query(query, (device_id,))
        return result

    # Define resolver for loadLiveData query
    loadLiveData = graphene.Field(LoadLiveDataType, id=graphene.Int(required=True))

    def resolve_loadLiveData(parent, info, id):
        query = "SELECT * FROM LoadLiveData WHERE id=%s"
        result = execute_query(query, (id,))
        return result[0] if result else None

    # Define resolver for loadLiveDataList query
    loadLiveDataList = graphene.List(LoadLiveDataType, device_id=graphene.Int(required=True))

    def resolve_loadLiveDataList(parent, info, device_id):
        query = "SELECT * FROM LoadLiveData WHERE device_id=%s"
        result = execute_query(query, (device_id,))
        return result

    # Define resolver for solarEnergyLiveData query
    solarEnergyLiveData = graphene.Field(SolarEnergyLiveDataType, id=graphene.Int(required=True))

    def resolve_solarEnergyLiveData(parent, info, id):
        query = "SELECT * FROM SolarEnergyLiveData WHERE id=%s"
        result = execute_query(query, (id,))
        return result[0] if result else None

    # Define resolver for solarEnergyLiveDataList query
    solarEnergyLiveDataList = graphene.List(SolarEnergyLiveDataType, microgrid_id=graphene.Int(required=True))

    def resolve_solarEnergyLiveDataList(parent, info, microgrid_id):
        query = "SELECT * FROM SolarEnergyLiveData WHERE microgrid_id=%s"
        result = execute_query(query, (microgrid_id,))
        return result

    # Define resolver for solarPlantLiveData query
    solarPlantLiveData = graphene.Field(SolarPlantLiveDataType, id=graphene.Int(required=True))

    def resolve_solarPlantLiveData(parent, info, id):
        query = "SELECT * FROM SolarPlantLiveData WHERE id=%s"
        result = execute_query(query, (id,))
        return result[0] if result else None

    # Define resolver for solarPlantLiveDataList query
    solarPlantLiveDataList = graphene.List(SolarPlantLiveDataType, plant_id=graphene.Int(required=True))

    def resolve_solarPlantLiveDataList(parent, info, plant_id):
        query = "SELECT * FROM SolarPlantLiveData WHERE plant_id=%s"
        result = execute_query(query, (plant_id,))
        return result

    # Define resolver for windEnergyLiveData query
    windEnergyLiveData = graphene.Field(WindEnergyLiveDataType, id=graphene.Int(required=True))

    def resolve_windEnergyLiveData(parent, info, id):
        query = "SELECT * FROM WindEnergyLiveData WHERE id=%s"
        result = execute_query(query, (id,))
        return result[0] if result else None

    # Define resolver for windEnergyLiveDataList query
    windEnergyLiveDataList = graphene.List(WindEnergyLiveDataType, microgrid_id=graphene.Int(required=True))



