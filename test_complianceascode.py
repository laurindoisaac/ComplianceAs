# test_complianceascode.py
"""
Tests for ComplianceAsCode module.
"""

import unittest
from complianceascode import ComplianceAsCode

class TestComplianceAsCode(unittest.TestCase):
    """Test cases for ComplianceAsCode class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = ComplianceAsCode()
        self.assertIsInstance(instance, ComplianceAsCode)
        
    def test_run_method(self):
        """Test the run method."""
        instance = ComplianceAsCode()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
