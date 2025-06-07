#!/usr/bin/env python3
"""
Test script for name2date functionality.
This script creates sample filenames and demonstrates how the main script would process them.
"""

import os
import tempfile
import datetime
import pytz
from name2date.core import parse_filename, update_file_modification_time

def test_parse_filename():
    """Test the parse_filename function with various filenames."""
    test_cases = [
        # Valid cases
        ("PXL_20240813_051351918.mp4", datetime.datetime(2024, 8, 13, 5, 13, 51, 918000, tzinfo=pytz.UTC)),
        ("PXL_20230101_000000000.mp4", datetime.datetime(2023, 1, 1, 0, 0, 0, 0, tzinfo=pytz.UTC)),
        ("PXL_20241231_235959999.mp4", datetime.datetime(2024, 12, 31, 23, 59, 59, 999000, tzinfo=pytz.UTC)),

        # Invalid cases
        ("IMG_20240813_051351.jpg", None),
        ("video.mp4", None),
        ("PXL_2024081_051351918.mp4", None),  # Incorrect format
    ]

    print("Testing parse_filename function:")
    for filename, expected in test_cases:
        result = parse_filename(filename)
        if result == expected:
            print(f"✓ {filename}: {result}")
        else:
            print(f"✗ {filename}: Expected {expected}, got {result}")

def test_update_file_modification_time():
    """Test the update_file_modification_time function with a temporary file."""
    # Create a temporary file
    with tempfile.NamedTemporaryFile(delete=False) as temp:
        temp_path = temp.name

    try:
        # Sample datetime (August 13, 2024, 05:13:51 UTC)
        dt = datetime.datetime(2024, 8, 13, 5, 13, 51, 0, tzinfo=pytz.UTC)

        print("\nTesting update_file_modification_time function:")
        # Update the file's modification time
        success = update_file_modification_time(temp_path, dt)

        if success:
            # Get the file's new modification time
            mtime = os.path.getmtime(temp_path)
            mtime_dt = datetime.datetime.fromtimestamp(mtime, pytz.UTC)

            # Compare timestamps (allowing for small differences due to precision)
            time_diff = abs((mtime_dt - dt).total_seconds())
            if time_diff < 1:  # Less than 1 second difference
                print(f"✓ UTC: {mtime_dt}")
            else:
                print(f"✗ UTC: Expected {dt}, got {mtime_dt}")
        else:
            print(f"✗ UTC: Failed to update file modification time")

    finally:
        # Clean up the temporary file
        if os.path.exists(temp_path):
            os.unlink(temp_path)

def main():
    """Run all tests."""
    test_parse_filename()
    test_update_file_modification_time()

    print("\nUsage example:")
    print("name2date /path/to/videos -v")

if __name__ == "__main__":
    main()
