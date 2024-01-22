```python
import os
from agent import Agent

# Check if the feature toggle is enabled
TOGGLE_FEATURE_ENV = "SMOL_DEVELOPER_FEATURE_TOGGLE"
feature_toggle = os.getenv(TOGGLE_FEATURE_ENV, "false").lower() in ("true", "1", "t")

class DebuggerNoModal:
    def __init__(self):
        if feature_toggle:
            self.agent = Agent()

    def debug_code(self, code, language):
        if not feature_toggle:
            print("Feature is not enabled.")
            return

        # Assuming that the Agent class has a method debug_code
        # which takes the code and language as parameters
        return self.agent.debug_code(code, language)

if __name__ == "__main__":
    debugger = DebuggerNoModal()
    # Example usage, should be replaced with actual code and language
    code_to_debug = "print('Hello, World!')"
    language = "python"
    result = debugger.debug_code(code_to_debug, language)
    print(result)
```