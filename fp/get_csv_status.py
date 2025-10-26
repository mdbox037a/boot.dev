from enum import Enum


class CSVExportStatus(Enum):
    PENDING = 1
    PROCESSING = 2
    SUCCESS = 3
    FAILURE = 4


def get_csv_status(status, data):
    match status:
        case CSVExportStatus.PENDING:
            # list_data = list(map(lambda x: map(str, data[x]), data))
            list_data = list(map(lambda lst: list(map(lambda d: str(d), lst)), data))
            return ("Pending...", list_data)
        case CSVExportStatus.PROCESSING:
            rows = list(map(",".join, data))
            table = "\n".join(rows)
            return ("Processing...", table)
        case CSVExportStatus.SUCCESS:
            return ("Success!", data)
        case CSVExportStatus.FAILURE:
            pending_data = get_csv_status(CSVExportStatus.PENDING, data)[1]
            processing_data = get_csv_status(CSVExportStatus.PROCESSING, pending_data)[
                1
            ]
            return ("Unknown error, retrying...", processing_data)
        case _:
            raise Exception("unknown export status")
