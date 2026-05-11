# test_vectorlib.py
"""
Tests for VectorLib module.
"""

import unittest
from vectorlib import VectorLib

class TestVectorLib(unittest.TestCase):
    """Test cases for VectorLib class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = VectorLib()
        self.assertIsInstance(instance, VectorLib)
        
    def test_run_method(self):
        """Test the run method."""
        instance = VectorLib()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
