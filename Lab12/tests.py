# tests.py

"""
CS 034 - Data Structures and Advanced Python
Lab 12: Implementing and Applying the Set ADT
Group 14: Ju Ho Kim, Sangmin Kim
Date: May, 15th, 2025

GitHub repo:
"""

import unittest
from Set import Set
from EnrollmentManager import EnrollmentManager
import os
import tempfile

class TestSet(unittest.TestCase):
    """Test cases for the Set class implementation."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.empty_set = Set()
        
        self.set_a = Set()
        for item in ["apple", "banana", "cherry"]:
            self.set_a.add(item)
        
        self.set_b = Set()
        for item in ["banana", "cherry", "date"]:
            self.set_b.add(item)
    
    def test_init(self):
        """Test that a new set is empty."""
        self.assertEqual(len(self.empty_set), 0)
    
    def test_add(self):
        """Test adding elements to a set."""
        test_set = Set()
        test_set.add("element")
        self.assertTrue(test_set.contains("element"))
        self.assertEqual(len(test_set), 1)
        
        # Adding a duplicate element should not increase size
        test_set.add("element")
        self.assertEqual(len(test_set), 1)
        
        # Adding None should be ignored
        test_set.add(None)
        self.assertEqual(len(test_set), 1)
    
    def test_remove(self):
        """Test removing elements from a set."""
        test_set = Set()
        test_set.add("element")
        test_set.remove("element")
        self.assertFalse(test_set.contains("element"))
        self.assertEqual(len(test_set), 0)
        
        # Removing an element that doesn't exist should raise KeyError
        with self.assertRaises(KeyError):
            test_set.remove("nonexistent")
    
    def test_contains(self):
        """Test checking if an element exists in a set."""
        self.assertTrue(self.set_a.contains("apple"))
        self.assertFalse(self.set_a.contains("date"))
    
    def test_union(self):
        """Test the union operation."""
        result = self.set_a.union(self.set_b)
        
        # Union should contain all elements from both sets
        for item in ["apple", "banana", "cherry", "date"]:
            self.assertTrue(result.contains(item))
        
        # Size should be the sum of sizes minus duplicates
        self.assertEqual(len(result), 4)
    
    def test_intersection(self):
        """Test the intersection operation."""
        result = self.set_a.intersection(self.set_b)
        
        # Intersection should contain only common elements
        self.assertTrue(result.contains("banana"))
        self.assertTrue(result.contains("cherry"))
        self.assertFalse(result.contains("apple"))
        self.assertFalse(result.contains("date"))
        
        # Size should be the number of common elements
        self.assertEqual(len(result), 2)
    
    def test_difference(self):
        """Test the difference operation."""
        result = self.set_a.difference(self.set_b)
        
        # Difference should contain elements in A but not in B
        self.assertTrue(result.contains("apple"))
        self.assertFalse(result.contains("banana"))
        self.assertFalse(result.contains("cherry"))
        self.assertFalse(result.contains("date"))
        
        # Size should be the number of elements in A but not in B
        self.assertEqual(len(result), 1)
    
    def test_len(self):
        """Test getting the length of a set."""
        self.assertEqual(len(self.empty_set), 0)
        self.assertEqual(len(self.set_a), 3)
    
    def test_str(self):
        """Test the string representation of a set."""
        self.assertEqual(str(self.empty_set), "Set{}")
        
        # Order may vary, so we check parts of the string
        str_rep = str(self.set_a)
        self.assertTrue(str_rep.startswith("Set{"))
        self.assertTrue(str_rep.endswith("}"))
        for item in ["apple", "banana", "cherry"]:
            self.assertIn(item, str_rep)
    
    def test_iter(self):
        """Test iterating through a set."""
        items = []
        for item in self.set_a:
            items.append(item)
        
        # Check that all items were iterated through
        self.assertEqual(len(items), 3)
        for item in ["apple", "banana", "cherry"]:
            self.assertIn(item, items)


class TestEnrollmentManager(unittest.TestCase):
    """Test cases for the EnrollmentManager class."""
    
    def setUp(self):
        """Set up test fixtures."""
        # Create temporary CSV files for testing
        self.temp_dir = tempfile.mkdtemp()
        
        # Create course A CSV file
        self.course_a_path = os.path.join(self.temp_dir, "course_a.csv")
        with open(self.course_a_path, "w") as f:
            f.write("student_id\n")
            f.write("S001\n")
            f.write("S002\n")
            f.write("S003\n")
        
        # Create course B CSV file
        self.course_b_path = os.path.join(self.temp_dir, "course_b.csv")
        with open(self.course_b_path, "w") as f:
            f.write("student_id\n")
            f.write("S002\n")
            f.write("S004\n")
            f.write("S005\n")
        
        # Create an EnrollmentManager with the test files
        self.manager = EnrollmentManager(self.course_a_path, self.course_b_path)
    
    def tearDown(self):
        """Clean up test fixtures."""
        # Delete temporary files
        os.remove(self.course_a_path)
        os.remove(self.course_b_path)
        os.rmdir(self.temp_dir)
    
    def test_load_course_data(self):
        """Test loading course data from a CSV file."""
        # Check that the data was loaded correctly
        self.assertTrue(self.manager.course_a.contains("S001"))
        self.assertTrue(self.manager.course_a.contains("S002"))
        self.assertTrue(self.manager.course_a.contains("S003"))
        self.assertEqual(len(self.manager.course_a), 3)
        
        self.assertTrue(self.manager.course_b.contains("S002"))
        self.assertTrue(self.manager.course_b.contains("S004"))
        self.assertTrue(self.manager.course_b.contains("S005"))
        self.assertEqual(len(self.manager.course_b), 3)
    
    def test_students_in_both(self):
        """Test finding students in both courses."""
        result = self.manager.students_in_both()
        self.assertTrue(result.contains("S002"))
        self.assertEqual(len(result), 1)
    
    def test_students_only_in_a(self):
        """Test finding students only in course A."""
        result = self.manager.students_only_in_a()
        self.assertTrue(result.contains("S001"))
        self.assertTrue(result.contains("S003"))
        self.assertEqual(len(result), 2)
    
    def test_students_only_in_b(self):
        """Test finding students only in course B."""
        result = self.manager.students_only_in_b()
        self.assertTrue(result.contains("S004"))
        self.assertTrue(result.contains("S005"))
        self.assertEqual(len(result), 2)
    
    def test_all_students(self):
        """Test finding all students in either course."""
        result = self.manager.all_students()
        for student in ["S001", "S002", "S003", "S004", "S005"]:
            self.assertTrue(result.contains(student))
        self.assertEqual(len(result), 5)


if __name__ == "__main__":
    unittest.main()