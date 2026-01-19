# COMP382 Assignment-1

A Python based app to test a string against a regex pattern

## Dependencies

- [uv](https://docs.astral.sh/uv/getting-started/installation/) (version 0.9.24)
Easiest way to install is:
    - Mac: `brew install uv`
    - Windows: `winget install --id=astral-sh.uv  -e`
    - Linux: `sudo apt install uv`
    - Manually from the docs.

## Installation

```bash
uv sync
```

## Usage

```bash
uv run main
```

## Testing

```bash
uv run test
```


## Citations & References

- **Linear Algebra & Regex Theory**: Sipser, M. (2013). *Introduction to the Theory of Computation* (3rd ed.). Cengage Learning. (Definition 1.52, pg 64).
- **GUI Framework**: [Qt for Python (PySide6) Documentation](https://doc.qt.io/qtforpython-6/).
- **Python Language**: [Python 3.12 Documentation](https://docs.python.org/3/).

## AI Usage Documentation

This project was developed with the assistance of an AI programming agent (Google DeepMind's Antigravity).

- **Role**: The AI agent acted as a "Pair Programmer," assisting with UI design, auto-complete, refactoring, debugging, and brainstorming on edge cases.
- **Process**:
    - **Planning**: The agent analyzed the assignment requirements and provided feedback and gaps in the current project implementation, highlighting gaps in the initial implementation.
    - **Implementation**: It generated the intial code for GUI components.
    - **Verification**: It analyzed stack traces and error messages to debug the code.

## Design Justifications

- **GUI Based application**: The traditional CLI interface are boring and require users to carefully read and follow instructions. A GUI based application has capability to expose more feature with less cognitive load. We went with a GUI based application to make it convenient for the users to try the application and provide enhanced features like virtual keyboard, block user from entering invalid characters, an existing list of examples and live real time update as the user types.

- **Virtual Keyboard**: Included to ensure users input valid symbols (Union `∪`, Concatenation `◦`, Epsilon `ε`, Empty Set `∅`) which are not present on standard keyboards. This prevents syntax errors from incorrect characters.

- **Modular GUI Architecture**: The UI was broken down into small, reusable components (`InputBar`, `StatusIndicator`, `VirtualKeyboard`). This "separation of concerns" makes the code cleaner, easier to test, and allows for isolated updates (e.g., changing the styling of the status indicator without affecting the logic).

- **Multi-language Support**: The application is structured to support multiple languages by simply adding a new JSON file to the `src/comp382_assignment_1/gui/strings` directory. This allows for easy addition of new languages and makes the application more accessible to a wider audience, and deployable in more environments.

- **Recursive Descent Parser**: Chosen for the regex engine because formal regular expressions (Definition 1.52) have a recursive structure. This approach maps directly to the mathematical definition, making the code easier to reason about and verify.

## GUI Component Guide (Copilot generated)

```
+-------------------------------------------------------------------------------------------------+
|                                     [MainWindow]                                                |
+-------------------------------------------------------------------------------------------------+
| [LeftSidebar]            | [MainPanel]                                                          |
|                          |                                                                      |
| Definition 1.52 Ref      |   [Header]                                                           |
| (HeadingLabel)           |   Regular Expression Practice Lab (HeadingLabel)                     |
|                          |   Alphabet Σ ≡ {a - b} (Text)                                        |
| 1. $a for some... (Text) |                                                                      |
| 2. ε (empty string)      |   ----------------------------------------------------------------   |
| 3. ∅ (empty language)    |                                                                      |
| 4. (R1 ∪ R2)             |   [SectionStep1]                                                     |
| 5. (R1 ◦ R2)             |   1. Define your Regular Expression (HeadingLabel)                   |
| 6. (R1*)                 |   Enter R: (Text)                                                    |
|                          |   +---------------------------------------+  +-------------------+   |
|                          |   | (ValidatedLineEdit)                   |  | (StatusIndicator) |   |
|                          |   +---------------------------------------+  +-------------------+   |
|                          |                   [InputBar]                                         |
|                          |                                                                      |
|                          |   [VirtualKeyboard]                                                  |
|                          |   [ U ] [ . ] [ * ] [ ε ] [ ∅ ] [ ( ] [ ) ] [ a ] [ b ] [ <X ]       |
|                          |        (KeyboardButton)                          (BackspaceButton)|
|                          |                                                                      |
|                          |   [Separator] (Horizontal Line)                                      |
|                          |                                                                      |
|                          |   [SectionStep2]                                                     |
|                          |   2. Test Strings (HeadingLabel)                                     |
|                          |   Type a string to check... (Text)                                   |
|                          |   +---------------------------------------+  +-------------------+   |
|                          |   | (ValidatedLineEdit)                   |  | (StatusIndicator) |   |
|                          |   +---------------------------------------+  +-------------------+   |
|                          |                   [InputBar]                                         |
|                          |                                                                      |
|                          |   [VirtualKeyboard]                                                  |
|                          |   [ a ] [ b ] [ <X ]                                                 |
|                          |                                                                      |
+-------------------------------------------------------------------------------------------------+
```