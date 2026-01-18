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