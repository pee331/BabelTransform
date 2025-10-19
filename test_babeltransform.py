# test_babeltransform.py
"""
Tests for BabelTransform module.
"""

import unittest
from babeltransform import BabelTransform

class TestBabelTransform(unittest.TestCase):
    """Test cases for BabelTransform class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = BabelTransform()
        self.assertIsInstance(instance, BabelTransform)
        
    def test_run_method(self):
        """Test the run method."""
        instance = BabelTransform()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
