import os
import subprocess
import streamlit as st
import pandas as pd
from Utilities.DBManager import DBManager

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
    try:
        result = subprocess.run(
            ["behave", feature_path, "--name", scenario_name],
            capture_output=True,
            text=True
        )
        output = result.stdout
        if "1 scenario passed" in output or "0 failed" in output:
            return "Pass"
        return "Fail"
    except Exception as e:
        return "Fail"

st.title("🧪 Behave Test Runner Dashboard")

test_options = get_tests()
if not test_options:
    st.warning("No tests available.")
else:
    selected = st.multiselect(
        "Select scenarios to run",
        options=test_options,
        format_func=lambda x: x[1]
    )

    if st.button("Run Selected Scenarios"):
        with st.spinner("Running selected scenarios..."):
            for test_id, scenario_name in selected:
                feature_path = find_feature_file_by_scenario_name(scenario_name)
                if feature_path:
                    update_run_status(test_id, "Running", "...")
                    result = run_behave_test(feature_path, scenario_name)
                    update_run_status(test_id, "Run", result)
                else:
                    update_run_status(test_id, "Skipped", "Feature Not Found")
            st.success("Behave tests completed.")

    # Show updated table
    st.subheader("📋 Current Test Table")
    df = pd.read_sql("SELECT * FROM tests", conn)
    st.dataframe(df)
