# Playwright Python BDD Automation Framework

This project is a robust, data-driven automation framework built using **Playwright** for web interaction and the **Behave** framework for **Behavior-Driven Development (BDD)**. It is designed for efficient, maintainable, and scalable test automation with integrated reporting, logging, and a user-friendly Streamlit interface for test management and execution.

---

## ✨ Features

* **BDD Approach:** Leverages the **Behave** framework for writing clear, executable specifications.
* **Centralized Locators:** All UI element locators (e.g., XPath, CSS Selectors) are externalized in a `config.ini` file for easy management and modification, accessed via `Readconfig.py`.
* **Page Object Model (POM):** Common methods for each application page are encapsulated in individual page object files within the `Feature` folder, promoting code reuse and maintainability.
* **Integrated Reporting:** Includes comprehensive **Allure Reporting** for detailed, interactive test results.
* **Streamlit UI for Test Management:** Features a built-in web interface for viewing test history, selecting desired tests, executing them, and viewing updated results in a live grid.
* **Detailed Logging:** Scenario-specific logging is enabled for every test run, with log files named after the scenario, managed by `LogUtil.py`.
* **Video Recording:** Automatically captures a `.webm` video for every scenario run, stored in the `VideoReports` folder.
* **Trace Viewer Integration:** Stores a `trace.zip` file for deep debugging using Playwright's Trace Viewer.
* **Utility & Data Management:** Includes dedicated utility files and a database manager for common tasks and persistent test data storage.
* **Self-Sufficient Setup:** A single batch file (`start_project.bat`) handles virtual environment creation and dependency installation.

---

## 🚀 Getting Started

The project is designed to be self-sufficient. You only need a recent Python installation on your system.

### Prerequisites

1.  **Python:** Ensure you have the latest version of Python installed.

### Execution

1.  **Run the Starter Script:** Execute the main batch file from the project root:
    ```bash
    .\start_project.bat
    ```
2.  **Initial Setup (Automatic):** The `start_project.bat` script will automatically perform the following steps if needed:
    * Checks for and creates a **virtual environment**.
    * Installs all required dependencies listed in `requirements.txt`.
    * Initializes the database using `DBManger.py` if it doesn't exist.
3.  **Launch Streamlit UI:** The script will then launch the Streamlit web application in your default browser.
4.  **Select & Run Tests:**
    * The UI displays all available tests and their historical results (fetched from the database).
    * Use the multi-choice option to select the tests you wish to run.
    * Click the **Execute** button to start the test run.
    * The results grid will update live upon completion.

---

## 📂 Project Structure

| Folder/File                              | Purpose                                                                                                                                                       |
|:-----------------------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **`Secure Configuration`** | All sensitive data (credentials, URLs, tokens) are managed externally via a **`secrets.env`** file and are **never** hard-coded or exposed in the repository. |
| **`Features`**                           | Contains all core BDD components: **Feature files**, **Step Definitions** (step files), and **Page Object Model** files.                                      |
| **`TestData`**                           | Stores necessary dummy files (e.g., PDF, TXT, Word) required as input data for tests.                                                                         |
| **`VideoReports`**                       | Stores the `.webm` video recording of each executed scenario.                                                                                                 |
| **`Logs`**                               | Stores generated scenario-specific log files.                                                                                                                 |
| **`Utilities`**                          | Houses essential helper modules:                                                                                                                              |
| &nbsp;&nbsp;&nbsp;&nbsp; `Controller.py` | Common methods: date/time generation, email/password generation, random text.                                                                                 |
| &nbsp;&nbsp;&nbsp;&nbsp; `DBManger.py`   | Handles database creation and management for storing tests and results.                                                                                       |
| &nbsp;&nbsp;&nbsp;&nbsp; `LogUtil.py`    | Custom logging utility for scenario-specific log file generation.                                                                                             |
| &nbsp;&nbsp;&nbsp;&nbsp; `Readconfig.py` | File to fetch locator paths from `config.ini`.                                                                                                                |
| `config.ini`                             | Located under Configurations directory Central repository for all UI element locators.                                                                        |
| `requirements.txt`                       | Lists all necessary Python dependencies (libraries).                                                                                                          |
| `start_project.bat`                      | The main execution script for setup and running the Streamlit application.                                                                                    |
| `trace.zip`                              | Artifact generated during a test run containing the Playwright trace information.                                                                             |

---

## 🔒 Secure Configuration

All security-related points, user credentials, application routes, and environment URLs are read from a **`secrets.env`** file. This file **must** be created in the project root directory and is excluded from version control for security.

### `secrets.env` File Structure

Create a file named **`secrets.env`** in the root of the project and populate it with the required configuration:

BASE_URL=https://myproj.com/

BROWSER=my_desired_browser #chrome/firefox as of now

USERNAME=test_username

USER_EMAIL=test_useremail@test.com

PASSWORD=test_password

USER_DETAIL_API=https://myproj.com/api/test_api?email=

EXISTING_USER=test_existing_user

EXISTING_EMAIL=test_existing_user@yopmail.com
`

## 🛠 Debugging and Reporting

### 1. Detailed Allure Reporting

To view a detailed and interactive report of the most recent test run:

```bash
allure serve allure-results