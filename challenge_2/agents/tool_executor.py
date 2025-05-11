# Calls Synera tools or mocks them

import subprocess
import logging

class ToolExecutor:
    def __init__(self, tool_name, mock=False):
        self.tool_name = tool_name
        self.mock = mock
        self.logger = logging.getLogger(__name__)

    def execute(self, *args):
        if self.mock:
            self.logger.info(f"Mock execution of {self.tool_name} with args: {args}")
            return f"Mock result of {self.tool_name} with args: {args}"
        else:
            self.logger.info(f"Executing {self.tool_name} with args: {args}")
            result = subprocess.run([self.tool_name] + list(args), capture_output=True, text=True)
            if result.returncode != 0:
                self.logger.error(f"Error executing {self.tool_name}: {result.stderr}")
                raise RuntimeError(f"Error executing {self.tool_name}: {result.stderr}")
            return result.stdout