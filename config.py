from enum import Enum

class TaskModel(str, Enum):
    gpt = 'gpt-4'
    deepseek = 'DeepSeek-V1'

