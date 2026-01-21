# COMP382 Assignment-1

A Python based app to test a string against a regex pattern

View [Youtube VLOG](https://youtu.be/GEckhW0PgqY)

## Dependencies

- [uv](https://docs.astral.sh/uv/getting-started/installation/) (version 0.9.24)
Easiest way to install is:
    - Mac: `brew install uv`
    - Windows: `winget install --id=astral-sh.uv  -e`
    - Linux: `sudo apt install uv`
    - Manually from the docs.

- [direnv](https://direnv.net/docs/installation.html)
    - Mac: `brew install direnv`
    - Windows: `winget install direnv`
    - Linux: `sudo apt install direnv`
    - Manually from the docs.

## Installation

If you see error about allowing `.envrc` file, like this:

```bash
>> direnv: error /Users/rishabmanocha/Downloads/mynewdir/.envrc is blocked. Run `direnv allow` to approve its content
```

Run `direnv allow`. This is only needed once.

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

- **Course Materials**: Campbell, R. (2024). Week 1: Sec 1.1 Finite Automata Introduction to the Theory of Computation [Lecture slides]. COMP 382: Languages, Computation, and Machines. University of the Fraser Valley.
- **Linear Algebra & Regex Theory**: Sipser, M. (2013). *Introduction to the Theory of Computation* (3rd ed.). Cengage Learning. (Definition 1.52, pg 64).
- **GUI Framework**: [Qt for Python (PySide6) Documentation](https://doc.qt.io/qtforpython-6/).
- **Python Language**: [Python 3.12 Documentation](https://docs.python.org/3/).

## AI Usage Documentation

This project was developed with the assistance of AI programming tools including Google DeepMind's Antigravity and DeepSeek.

- **Roles**: 
    - **Pair Programmer (Google DeepMind's Antigravity)**: Assisted with UI design, auto-complete, refactoring, debugging, and brainstorming on edge cases.
    - **Conceptual Clarification Assistant (DeepSeek):**: Helped understand first week concepts including "Definition 1.52 on pg 64" at a deeper level to improve articulation of ideas and theoretical foundations.
- **Process**:
    - **Planning**: The agent analyzed the assignment requirements and provided feedback and gaps in the current project implementation, highlighting gaps in the initial implementation.
    - **Conceptual Understanding**: Used DeepSeek to gain deeper insight into Definition 1.52 (page 64) from the textbook, which enhanced my ability to articulate mathematical concepts and ensure proper implementation of related algorithms.
    - **Implementation**:
          - It generated the intial code for GUI components.
          - Created the comprehensive def run_all_tests() function for test_matcher.py to establish a user-friendly testing interface with clear feedback mechanisms.
          - Developed the initial main() function (removed now) for matcher.py that provided a command-line interface before transitioning to GUI.
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
