# Python Portfolio — Projects, Algorithms & Concepts

A comprehensive collection of **40+ Python projects and exercises** spanning game development, GUI applications, API integrations, data analysis, and automation.

---

## Table of Contents

- [Overview](#overview)
- [Tech Stack](#tech-stack)
- [Repository Structure](#repository-structure)
- [Projects](#projects)
  - [Game Development](#game-development)
  - [GUI Desktop Applications](#gui-desktop-applications)
  - [API & Automation](#api--automation)
  - [Data Analysis](#data-analysis)
  - [File Processing & Utilities](#file-processing--utilities)
  - [One-File Programs](#one-file-programs)
- [Python Notes & Concepts](#python-notes--concepts)
- [Getting Started](#getting-started)

---

## Overview

| Category | Count |
|----------|-------|
| Complete Projects | 19 |
| One-File Programs | 23 |
| Concept Reference Files | 15+ |

This repository demonstrates proficiency across multiple domains of Python development — from desktop applications with persistent storage to external API consumption and data analysis.

---

## Tech Stack

| Area | Technologies |
|------|-------------|
| **Language** | Python 3 |
| **GUI** | Tkinter, Turtle Graphics |
| **Data** | Pandas, CSV, JSON |
| **Networking** | Requests, smtplib (SMTP) |
| **Utilities** | datetime, os, random, pyperclip, colorgram |
| **Paradigms** | OOP, Event-Driven Programming, Functional Programming |

---

## Repository Structure

```
├── Python Examples/        # 19 multi-file projects + 23 one-file programs
│   ├── 025_Snake_Game_Full/
│   ├── 026_Pong_Game_Full/
│   ├── 027_Turtle_Cross/
│   ├── 033_Pomodoro/
│   ├── 034_Password_Manager/
│   ├── 035_Flash_Card_Project/
│   ├── 036_Birthday_Wisher/
│   ├── 037_ISS_Location_API_Requests/
│   ├── 039_Quizzler_App/
│   └── ...
└── Python Notes/           # Concept references (OOP, Pandas, Tkinter, etc.)
    ├── 009_Pandas_Library/
    ├── 010_OOP/
    └── 013_Tkinter_GUI_Library/
```

---

## Projects

### Game Development

Three complete games built with **object-oriented architecture**, each separated into modular components.

#### Snake Game
> `Python Examples/025_Snake_Game_Full/`

Full implementation of the classic Snake game with modular OOP design.

- **Architecture:** 4 modules — `snake.py`, `food.py`, `scoreboard.py`, `snake_main.py`
- **Features:** Keyboard controls (W/A/S/D), collision detection (walls, food, self-collision), dynamic speed scaling, persistent score tracking
- **Concepts:** Game loop, state management, event-driven input, OOP composition

#### Pong Game
> `Python Examples/026_Pong_Game_Full/`

Two-player Pong recreation with physics-based ball mechanics.

- **Architecture:** 4 modules — `paddle.py`, `ball.py`, `scoreboard.py`, `pong_main.py`
- **Features:** Dual-player controls (Arrow keys & W/S), ball trajectory and bounce physics, per-player scoring, progressive difficulty
- **Concepts:** Physics simulation, real-time multiplayer input, coordinate geometry

#### Turtle Crossing
> `Python Examples/027_Turtle_Cross/`

Frogger-style arcade game with procedural enemy generation.

- **Architecture:** 4 modules — `player.py`, `car_manager.py`, `scoreboard.py`, `turtle_cross_main.py`
- **Features:** Randomized car spawning, multi-lane collision detection, level progression with increasing difficulty
- **Concepts:** Procedural generation, difficulty scaling, game state machines

---

### GUI Desktop Applications

Production-quality desktop applications built with **Tkinter**.

#### Pomodoro Timer
> `Python Examples/033_Pomodoro/`

A fully-featured productivity timer implementing the Pomodoro Technique.

- 25-min work / 5-min break / 20-min long break cycles
- Visual countdown with canvas-based UI
- Session progress tracking with checkmarks
- Start/Reset controls

#### Password Manager
> `Python Examples/034_Password_Manager/`

Secure password management tool with persistent JSON storage.

- Random password generation with configurable complexity
- JSON-based encrypted storage with search/lookup
- One-click clipboard copy (pyperclip integration)
- Dialog-based user feedback and confirmation

#### Flash Card App
> `Python Examples/035_Flash_Card_Project/`

Adaptive language learning application (German → English).

- Auto-flip cards with timed reveal (3s delay)
- Adaptive learning — removes mastered words from rotation
- Progress persistence via CSV export
- Visual card interface with image assets

#### Quizzler
> `Python Examples/039_Quizzler_App/`

API-powered trivia quiz with real-time question fetching.

- **Architecture:** 5 modules — `ui.py`, `question_model.py`, `quiz_brain.py`, `data.py`, `main.py`
- Fetches questions from Open Trivia Database API
- True/False GUI with score tracking
- Clean separation of data, logic, and presentation layers

---

### API & Automation

#### ISS Tracker
> `Python Examples/037_ISS_Location_API_Requests/`

Real-time International Space Station position tracker.

- Consumes ISS location API for live coordinates
- Integrates sunrise/sunset API for geolocation-based calculations
- JSON response parsing and data extraction

#### Birthday Wisher — Email Automation
> `Python Examples/036_Birthday_Wisher/`

Automated birthday email system with template personalization.

- CSV-based birthday database with date matching
- Randomized letter template selection
- SMTP email delivery (configurable provider)
- Scheduled execution via datetime comparison

#### Kanye Quote Generator
> `Python Examples/038_Kanye_Quote_API_Request/`

REST API consumer that fetches and displays random quotes with Tkinter UI.

---

### Data Analysis

#### NYC Squirrel Census Analysis
> `Python Examples/029_Great_Squirrel_Census_Data_Example/`

Data pipeline analyzing the 2018 Central Park Squirrel Census dataset.

- Pandas DataFrame operations: filtering, grouping, aggregation
- CSV I/O with data transformation
- Statistical summary generation

#### US States Geography Quiz
> `Python Examples/030_US_States_Game/`

Interactive map-based quiz combining data analysis with visualization.

- Pandas-driven state lookup with coordinate mapping
- Turtle-based map rendering with dynamic label placement
- Exports unguessed states to CSV for further study

#### NATO Phonetic Alphabet Converter
> `Python Examples/031_NATO_Alphabet_Project/`

Dictionary-based converter with CSV data source and exception handling.

---

### File Processing & Utilities

#### Mail Merge
> `Python Examples/028_Mail_Merge_Project/`

Batch letter personalization engine.

- Template-based text replacement
- Bulk file generation from name list
- Clean directory-based output organization

#### Miles to Kilometers Converter
> `Python Examples/032_Miles_to_Kilometers_Tkinter/`

Lightweight unit conversion tool with Tkinter interface.

---

### One-File Programs

> `Python Examples/017_One_File_Examples/`

23 focused programs covering foundational Python patterns:

| Program | Key Concept |
|---------|-------------|
| Blackjack | Full card game with dealer AI logic |
| Coffee Machine | State machine simulation with resource management |
| Hangman | Game state tracking, ASCII art |
| Rock Paper Scissors | Conditional logic, random selection |
| Random Password Generator | String composition, security patterns |
| Caesar Cipher | Encryption/decryption algorithm |
| Number Guessing Game | Binary feedback loops |
| Turtle Race | Animation, event listeners |
| Turtle Random Walk | Generative graphics |
| Turtle Dot Painting | Procedural art with colorgram |
| Auction Program | Dictionary-based data management |
| Higher-Lower Game | Comparative logic with real data |

---

## Python Notes & Concepts

Structured reference files covering Python fundamentals to advanced topics.

### Core Language

| File | Topic |
|------|-------|
| `001` | Built-in Functions (`len`, `range`, `type`) |
| `002` | Strings — slicing, formatting, methods |
| `003` | Integers & Floats — arithmetic, type casting |
| `004` | Lists — indexing, slicing, methods, nesting |
| `005` | Tuples — immutable sequences |
| `006` | Sets — uniqueness, set operations |
| `007` | Dictionaries — key-value pairs, nested dicts |
| `008` | Classes — definitions, instances |
| `00x` | Random Module — `choice`, `shuffle`, `randint` |
| `011` | List & Dict Comprehensions |
| `012` | `*args` and `**kwargs` |
| `014` | Exception Handling (`try`/`except`/`finally`) |
| `015` | HTTP Requests (PUT/GET) and API Usage |

### Advanced Topics

| Directory | Contents |
|-----------|----------|
| `010_OOP/` | 4-part OOP series: Classes → Instance Variables → Static Methods → Inheritance |
| `009_Pandas_Library/` | DataFrame operations, CSV I/O, data filtering and transformation |
| `013_Tkinter_GUI_Library/` | 3-part GUI series: Widgets → Layouts → Event Handling |

---

## Getting Started

### Prerequisites

```bash
python >= 3.8
```

### Installation

```bash
git clone https://github.com/<your-username>/<repo-name>.git
cd <repo-name>
pip install pandas requests pyperclip colorgram.py
```

### Running a Project

```bash
# Run any project
python "Python Examples/025_Snake_Game_Full/snake_main.py"
```

---

<p align="center">
  <strong>Built with Python</strong> — Covering OOP, GUI development, API integration, data analysis, and automation.
</p>
