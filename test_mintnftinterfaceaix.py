# test_mintnftinterfaceaix.py
"""
Tests for MintNftInterfaceAIX module.
"""

import unittest
from mintnftinterfaceaix import MintNftInterfaceAIX

class TestMintNftInterfaceAIX(unittest.TestCase):
    """Test cases for MintNftInterfaceAIX class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = MintNftInterfaceAIX()
        self.assertIsInstance(instance, MintNftInterfaceAIX)
        
    def test_run_method(self):
        """Test the run method."""
        instance = MintNftInterfaceAIX()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
