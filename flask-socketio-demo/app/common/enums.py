from enum import Enum

__all__ = ['RedisKeyEnum', 'EventType', 'ConversationStatusEnum', 'HttpMethodEnum', 'QueueEnum',
           'AgentStatusEnum', 'UserRolesEnum', 'ChannelName']


class RedisKeyEnum(Enum):
    account_settings = "account_{account_id}"
    conversation_assignment = "conversation_assignment_{bot_id}"
    agent_status = "agent_{user_id}"
    bot_level_lock = "lock_bot_{bot_id}"


class AgentStatusEnum(Enum):
    AVAILABLE = 1
    AWAY = 2


class ConversationStatusEnum(Enum):
    OPEN = 1
    CLOSE = 2


class EventType(Enum):
    ASSIGNEE = 3
    STATUS = 4


class UserRolesEnum(Enum):
    OWNER = 1
    ADMIN = 2
    AGENT = 3


class HttpMethodEnum(Enum):
    POST = 'POST'
    PUT = 'PUT'
    GET = 'GET'
    DELETE = 'DELETE'


class ChannelName(Enum):
    WHATSAPP = "whatsapp"


class ValidateExtentions(Enum):
    ALLOWED_EXTENSIONS = ('png', 'jpg', 'jpeg', 'aac', 'm4a', 'amr', 'mp3', 'ogg', 'opus', 'pdf', 'doc', 'docx', 'ppt',
                          'pptx', 'xls', 'xlsx')


class AllowedContent(Enum):
    ALLOWED_CONTENT = ["text", "location", "media"]


class QueueEnum(Enum):
    SEND_MESSAGE = {'route': 'whatsapp-incoming-message-handler',
                    'queue': 'whatsapp-incoming-message-handler-queue-dx',
                    'worker_count': 1,
                    'exchange_type': 'direct',
                    'exchange_name': 'wotnot.direct'}
