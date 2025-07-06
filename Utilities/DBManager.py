import sqlite3
import os
from pathlib import Path
from datetime import datetime
from typing import Optional


class DBManager:
    def __init__(self, db_name: str = "./automation_results.db"):
        self.db_path = os.path.join(str(Path.cwd()), db_name)
        self.conn = sqlite3.connect(self.db_path, check_same_thread=False)
        self.cursor = self.conn.cursor()
        self._initialize_tables()

    def _initialize_tables(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS test_results (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                test_name TEXT,
                module TEXT,
                status TEXT,
                start_time TEXT,
                end_time TEXT,
                elapsed_time TEXT,
                error_message TEXT,
                screenshot_path TEXT,
                browser TEXT,
                environment TEXT
            )
        ''')
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS tests (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                test_name TEXT UNIQUE,
                run_status TEXT DEFAULT 'Not Run',
                result_status TEXT DEFAULT 'None'
            )
        ''')
        self.conn.commit()

    def log_test_result(
        self,
        test_name: str,
        module: str,
        status: str,
        start_time,
        end_time,
        error_message: str = "",
        screenshot_path: str = "",
        browser: str = "chrome",
        environment: str = "QA"
    ):
        try:
            elapsed = str(end_time - start_time)

            self.cursor.execute('''
                INSERT INTO test_results (
                    test_name, module, status, start_time, end_time, elapsed_time,
                    error_message, screenshot_path, browser, environment
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (
                test_name, module, status,
                start_time.strftime('%Y-%m-%d %H:%M:%S'),
                end_time.strftime('%Y-%m-%d %H:%M:%S'),
                elapsed, error_message, screenshot_path, browser, environment
            ))

            self.update_test_status(test_name, run_status="Run", result_status=status)

            self.conn.commit()
        except Exception as e:
            print(f"[DB Error] Failed to log result for {test_name}: {e}")

    def update_test_status(self, test_name: str, run_status: str, result_status: str):
        try:
            self.cursor.execute('''
                INSERT INTO tests (test_name, run_status, result_status)
                VALUES (?, ?, ?)
                ON CONFLICT(test_name) DO UPDATE SET
                    run_status=excluded.run_status,
                    result_status=excluded.result_status
            ''', (test_name, run_status, result_status))
            self.conn.commit()
        except Exception as e:
            print(f"[DB Error] Failed to update test status for {test_name}: {e}")

    def close(self):
        self.conn.close()
