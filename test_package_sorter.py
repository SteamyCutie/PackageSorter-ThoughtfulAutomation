import unittest
from package_sorter import sort


class TestPackageSorter(unittest.TestCase):
    
    def test_standard_package(self):
        """Test a standard package (not bulky, not heavy)"""
        result = sort(50, 50, 50, 10)
        self.assertEqual(result, "STANDARD")
    
    def test_standard_package_edge_case(self):
        """Test package just below bulky and heavy thresholds"""
        result = sort(149, 149, 45, 19.9)
        self.assertEqual(result, "STANDARD")
    
    def test_bulky_by_volume(self):
        """Test package that is bulky due to volume >= 1,000,000 cm³"""
        result = sort(100, 100, 100, 10)
        self.assertEqual(result, "SPECIAL")
    
    def test_bulky_by_volume_exact(self):
        """Test package with volume exactly 1,000,000 cm³"""
        result = sort(100, 100, 100, 15)
        self.assertEqual(result, "SPECIAL")
    
    def test_bulky_by_width(self):
        """Test package that is bulky due to width >= 150 cm"""
        result = sort(150, 50, 50, 10)
        self.assertEqual(result, "SPECIAL")
    
    def test_bulky_by_height(self):
        """Test package that is bulky due to height >= 150 cm"""
        result = sort(50, 150, 50, 10)
        self.assertEqual(result, "SPECIAL")
    
    def test_bulky_by_length(self):
        """Test package that is bulky due to length >= 150 cm"""
        result = sort(50, 50, 150, 10)
        self.assertEqual(result, "SPECIAL")
    
    def test_heavy_package(self):
        """Test package that is heavy (mass >= 20 kg)"""
        result = sort(50, 50, 50, 20)
        self.assertEqual(result, "SPECIAL")
    
    def test_heavy_package_over_threshold(self):
        """Test package that is significantly heavy"""
        result = sort(50, 50, 50, 25)
        self.assertEqual(result, "SPECIAL")
    
    def test_rejected_bulky_and_heavy(self):
        """Test package that is both bulky (by volume) and heavy"""
        result = sort(100, 100, 100, 20)
        self.assertEqual(result, "REJECTED")
    
    def test_rejected_bulky_by_dimension_and_heavy(self):
        """Test package that is both bulky (by dimension) and heavy"""
        result = sort(150, 50, 50, 20)
        self.assertEqual(result, "REJECTED")
    
    def test_rejected_very_bulky_and_very_heavy(self):
        """Test package that is significantly bulky and heavy"""
        result = sort(200, 200, 200, 50)
        self.assertEqual(result, "REJECTED")
    
    def test_small_dimensions(self):
        """Test package with small dimensions"""
        result = sort(10, 10, 10, 5)
        self.assertEqual(result, "STANDARD")
    
    def test_zero_mass(self):
        """Test package with zero mass"""
        result = sort(50, 50, 50, 0)
        self.assertEqual(result, "STANDARD")


if __name__ == '__main__':
    unittest.main()
