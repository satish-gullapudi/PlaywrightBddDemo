import os
import subprocess
import streamlit as st
import pandas as pd
from Utilities.DBManager import DBManager

# Initiating DB object for fetching tests and writing test results
db = DBManager()
conn, cursor = db.conn, db.cursor

def get_tests():
    cursor.execute("SELECT id, test_name FROM tests")
    rows = cursor.fetchall()
    return rows

def update_run_status(test_id, run_status, result_status):
    cursor.execute("""
        UPDATE tests 
        SET run_status = ?, result_status = ?
        WHERE id = ?
    """, (run_status, result_status, test_id))
    conn.commit()

def find_feature_file_by_scenario_name(scenario_name, root_dir="./Features"):
    """
    Search for a .feature file that contains the given scenario name.
    """
    for root, _, files in os.walk(root_dir):
        for file in files:
            if file.endswith(".feature"):
                path = os.path.join(root, file)
                with open(path, "r", encoding="utf-8") as f:
                    content = f.read()
                    if scenario_name in content:
                        return path
    return None

def run_behave_test(feature_path, scenario_name):
    # Get the absolute path to the virtual environment's python.exe
    # This variable was set in start_project.bat
    VENV_PYTHON_EXE = os.environ.get("VENV_PYTHON_EXE_PATH")

    # Strip surrounding quotes if the batch script added them
    if VENV_PYTHON_EXE:
        VENV_PYTHON_EXE = VENV_PYTHON_EXE.strip('"')

    if not VENV_PYTHON_EXE or not os.path.exists(VENV_PYTHON_EXE):
        print("ERROR: Could not find virtual environment Python executable.")
        return "Fail"

    try:
        command_list = [
            VENV_PYTHON_EXE,
            "-m", "behave",
            feature_path,
            "--name", scenario_name
        ]

        result = subprocess.run(
            command_list,
            capture_output=True,
            text=True,
        )

        output = result.stdout
        stderr_output = result.stderr

        # Debugging: Print full output for confirmation
        print(f"--- Behave Command Output for {scenario_name} ---")
        print(f"Executing: {' '.join(command_list)}")
        print(f"STDOUT:\n{output}")
        if stderr_output:
            print(f"STDERR:\n{stderr_output}")
        print("-----------------------------------------------------")

        # Pass/Fail Logic
        if "1 scenario passed" in output and "0 failed" in output:
            return "Pass"

        return "Fail"

    except Exception as e:
        print(f"Critical Exception running behave test: {e}")
        return "Fail"


# --- Streamlit UI and Logic ---

st.title("🧪 Behave Test Runner Dashboard")


# 4. Cancel and Close Function
def close_app():
    st.success("Closing Streamlit application...")
    # os._exit(0) forcefully terminates the Python process, shutting down Streamlit
    os._exit(0)


# Initialize session state for test selections if not present
if 'test_selections' not in st.session_state:
    st.session_state.test_selections = {}

test_options = get_tests()
if not test_options:
    st.warning("No tests available.")
else:
    st.subheader("Select scenarios to run")


    # 3. Select All / Unselect All Functions
    def select_all():
        # Loop through all test options and set the CHECKBOX key state to True
        for test_id, test_name in test_options:
            st.session_state[f"checkbox_{test_id}"] = True


    def unselect_all():
        # Loop through all test options and set the CHECKBOX key state to False
        for test_id, test_name in test_options:
            st.session_state[f"checkbox_{test_id}"] = False


    # Select All / Unselect All Buttons
    col_select_all, col_unselect_all = st.columns(2)
    with col_select_all:
        st.button("Select All", on_click=select_all)
    with col_unselect_all:
        st.button("Unselect All", on_click=unselect_all)

    st.markdown("---")

    selected_scenarios = []

    # 1 & 2. Checkboxes for Scenario-Specific Listing
    for test_id, scenario_name in test_options:
        # Initialize session state value for the selection status
        if test_id not in st.session_state.test_selections:
            st.session_state.test_selections[test_id] = False

        # Create checkbox, using the test_id as the key in session state
        is_selected = st.checkbox(
            f"**{scenario_name}**",  # Scenario-specific name
            value=st.session_state.test_selections[test_id],
            key=f"checkbox_{test_id}"  # Unique key for the Streamlit widget
        )

        # Update selection status in session state
        st.session_state.test_selections[test_id] = is_selected

        if is_selected:
            selected_scenarios.append((test_id, scenario_name))

    st.markdown("---")

    # Run and Cancel Buttons Side-by-Side
    col_run, col_cancel = st.columns([3, 1])

    with col_run:
        if st.button(f"Run {len(selected_scenarios)} Selected Scenarios", type="primary"):
            if not selected_scenarios:
                st.warning("Please select at least one scenario to run.")
            else:
                with st.spinner("Running selected scenarios..."):
                    for test_id, scenario_name in selected_scenarios:
                        feature_path = find_feature_file_by_scenario_name(scenario_name)
                        if feature_path:
                            update_run_status(test_id, "Running", "...")
                            result = run_behave_test(feature_path, scenario_name)
                            update_run_status(test_id, "Run", result)
                        else:
                            update_run_status(test_id, "Skipped", "Feature Not Found")
                    st.success("Behave tests completed.")

    with col_cancel:
        # 4. Cancel and Close Button
        if st.button("Cancel and Close"):
            close_app()

    # Show updated table
    st.subheader("📋 Current Test Table")
    df = pd.read_sql("SELECT * FROM tests", conn)
    st.dataframe(df)