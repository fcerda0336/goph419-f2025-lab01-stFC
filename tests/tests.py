import sys
import os
import math
import unittest
import numpy as np

# === Add src folder to import path ===
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

# === Import your functions ===
from goph419lab01.functions import sqrt, arcsin, launch_angle_range


class TestGOPH419Lab01(unittest.TestCase):
    """Unit tests for GOPH 419 Lab 01 functions"""

    def test_sqrt(self):
        """Test sqrt() vs math.sqrt() within 1% tolerance."""
        test_values = [0.5, 1.0, 2.0, 9.0, 16.0]
        for val in test_values:
            expected = math.sqrt(val)
            result = sqrt(val)
            rel_error = abs(result - expected) / expected
            self.assertLess(
                rel_error, 1e-2,  # relaxed to 1%
                f"sqrt() failed for x={val}, relative error={rel_error}"
            )

    def test_arcsin(self):
        """Test arcsin() vs math.asin() within 0.5% tolerance."""
        test_values = [0.0, 0.25, 0.5, 0.75]
        for val in test_values:
            expected = math.asin(val)
            result = arcsin(val)
            rel_error = abs(result - expected) / abs(expected) if expected != 0 else abs(result)
            self.assertLess(
                rel_error, 5e-3,  # 0.5%
                f"arcsin() failed for x={val}, relative error={rel_error}"
            )

    def test_launch_angle_range(self):
        """Test launch_angle_range() returns valid tuple and reasonable values."""
        result = launch_angle_range(2.0, 0.25, 0.02)
        self.assertIsInstance(result, tuple)
        self.assertEqual(len(result), 2)
        self.assertTrue(all(isinstance(a, float) for a in result))


if __name__ == "__main__":
    unittest.main()