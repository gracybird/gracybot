
import logging

import config
import db

from typing import Optional, Tuple, Sequence

logger = logging.getLogger("gracybot")

class access():
    """
    Controls access to the bot per module name.
    """
    def __init__(self):
        self.config = config.Config()

    async def lookup_role_id(role_name: str) -> int:
        """
        Attempt to look up the role ID by name.

        :param role_name: The name of the role.
        :return: int, the id of the specified role.
        """
        result = "This will probably use discord.py"
        logger.debug()
        return result

    async def allow_role(role_id: int, module_name:str) -> bool:
        """
        Add a role to the allow list.
        
        :param role_id: The ID of the role to allow.
        :param module_nam: The name of the module to allow for the role.
        :return: boolean, True on success.
        """
        query = ""
        result = db.write(query, role_id, module_name)
        logger.debug(result)
        if result is not None:
            return True
        else:
            return False

    async def disallow_role(role_id: int, module_name:str) -> bool:
        """
        Remove a role to the allow list.
        
        :param role_id: The ID of the role to disallow.
        :param module_nam: The name of the module to disallow for the role.
        :return: boolean, True on success.
        """
        query = ""
        result = db.write(query, role_id, module_name)
        logger.debug(result)
        if result is not None:
            return True
        else:
            return False

    async def is_allowed(user_role_id: int) -> bool:
        """
        This function will check if a user is allowed.

        :param user_role_id: The ID of the user's role that should be checked.
        :return: True if the user is allowed, False if not.
        """
        query = "SELECT * FROM allowed_roles WHERE user_role=?"
        result = db.read(query, user_role_id)
        logger.debug(result)
        if result is not None:
            return True
        else:
            return False
