from enum import Enum

class HealthStatus(str, Enum):
    OK = "OK"
    ERROR = "FAILURE"