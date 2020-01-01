from enum import Enum


class QueueEnum(Enum):
    SEND_MESSAGE = {'route': 'send_message', 'queue': 'send_message_q', 'worker_count': 1}
    UNSEND_MESSAGE = {'route': 'unsend_message', 'queue': 'unsend_message_q', 'worker_count': 1}