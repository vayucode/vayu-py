# vayu_sdk/apis/api_measurements.py
from openapi.api.measurements_api import MeasurementsApi
from vayu_sdk.clients.vayu_client import VayuClient
from openapi.models.create_measurement_request import CreateMeasurementRequest
from openapi.models.create_measurement_response import CreateMeasurementResponse
from openapi.models.delete_measurement_response import DeleteMeasurementResponse
from openapi.models.get_measurement_response import GetMeasurementResponse
from openapi.models.list_measurements_response import ListMeasurementsResponse


class MeasurementsAPI:
    __client: MeasurementsApi = None

    def __init__(self, vayu_client: VayuClient):
        self.__client = MeasurementsApi(vayu_client.client)

    def create(self, request: CreateMeasurementRequest):
        return self.__client.create_measurement(create_measurement_request=request)

    def delete(self, id: str):
        return self.__client.delete_measurement(measurement_id=id)

    def get(self, id: str):
        return self.__client.get_measurement(measurement_id=id)

    def list(self, limit: int = None, cursor: str = None):
        return self.__client.list_measurements(limit=limit, cursor=cursor)
