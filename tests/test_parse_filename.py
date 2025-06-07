#!/usr/bin/env python3
"""
Test script to verify that the parse_filename function correctly handles all the required patterns.
"""

from name2date.core import parse_filename

def test_parse_filename():
    """Test the parse_filename function with various filename patterns."""
    test_cases = [
        # Original format
        "PXL_20240815_174155846.mp4",

        # Variations with suffixes
        "PXL_20240815_174155846.NIGHT.jpg",
        "PXL_20240815_190034025.MP(1).jpg",
        "PXL_20240815_190034025.MP.jpg",
        "PXL_20240815_190405948.MP.jpg",
        "PXL_20240815_190407130(1).jpg",
        "PXL_20240815_190407130.jpg",
        "PXL_20240815_190408002.MP.jpg",
        "PXL_20240815_190830722.jpg",
        "PXL_20240815_190849820.RESTORED.jpg",
        "PXL_20240815_190856072.RESTORED.jpg",
        "PXL_20240811_084139455_exported_0_1723365759303.jpg",

        # New format
        "lv_0_20240813134545.mp4",

        # Invalid formats (should return None)
        "invalid_filename.mp4",
        "PXL_invalid_date.mp4",
        "lv_0_invalid_date.mp4"
    ]

    print("Testing parse_filename function...")
    for filename in test_cases:
        dt = parse_filename(filename)
        if dt:
            print(f"✓ {filename} -> {dt.strftime('%Y-%m-%d %H:%M:%S.%f %Z')}")
        else:
            print(f"✗ {filename} -> None (not recognized)")

    print("\nTest completed.")

if __name__ == "__main__":
    test_parse_filename()
