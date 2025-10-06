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
        """Test sqrt() approximation using Taylor series expansion"""
        for val in [0.5, 1.0, 2.0]:
            with self.subTest(x=val):
                approx = sqrt(val)
                true_val = math.sqrt(val)
                error = abs(approx - true_val)
                print(f"sqrt({val}) = {approx:.10f}, math.sqrt = {true_val:.10f}, error = {error:.2e}")
                self.assertLess(error, 1e-3, f"sqrt() failed for x={val}, error={error}")

    def test_arcsin(self):
        """Test arcsin() approximation using Taylor series expansion"""
        for val in [0.0, 0.25, 0.29]:
            with self.subTest(x=val):
                approx = arcsin(val)
                true_val = math.asin(val)
                error = abs(approx - true_val)
                print(f"arcsin({val}) = {approx:.10f}, math.asin = {true_val:.10f}, error = {error:.2e}")
                self.assertLess(error, 1e-4, f"arcsin() failed for x={val}, error={error}")

    def test_launch_angle_range(self):
        """Test launch_angle_range() returns correct structure"""
        result = launch_angle_range(2.0, 0.25, 0.02)
        self.assertIsInstance(result, tuple, "launch_angle_range() should return a tuple")
        self.assertEqual(len(result), 2, "launch_angle_range() should return two values (min, max)")
        print(f"launch_angle_range(2.0, 0.25, 0.02) = {result}")


if __name__ == "__main__":
    print("=== GOPH 419 - Automated Test Suite (unittest) ===\n")
    unittest.main(verbosity=2)