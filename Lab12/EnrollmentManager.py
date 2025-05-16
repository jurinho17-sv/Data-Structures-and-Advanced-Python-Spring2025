# EnrollmentManager.py

"""
CS 034 - Data Structures and Advanced Python
Lab 12: Implementing and Applying the Set ADT
Group 14: Ju Ho Kim, Sangmin Kim
Date: May, 15th, 2025

GitHub repo:
"""

import csv
import sys
from Set import Set

class EnrollmentManager:
    """
    A class to manage student enrollments across courses using Set operations.
    
    This class loads student data from CSV files and provides methods to analyze
    enrollment patterns.
    """
    
    def __init__(self, file_a=None, file_b=None):
        """
        Initialize the EnrollmentManager with data from two course files.
        
        Args:
            file_a (str): Path to the CSV file for course A
            file_b (str): Path to the CSV file for course B
        """
        # Initialize empty sets for each course
        self.course_a = Set()
        self.course_b = Set()
        
        # Load data if filenames are provided
        if file_a:
            self.load_course_data(file_a, self.course_a)
        if file_b:
            self.load_course_data(file_b, self.course_b)
    
    def load_course_data(self, filename, target_set):
        """
        Load student IDs from a CSV file into a set.
        
        Args:
            filename (str): Path to the CSV file
            target_set (Set): The set to load the data into
            
        Returns:
            bool: True if loading was successful, False otherwise
        """
        try:
            with open(filename, 'r') as file:
                # Create a CSV reader
                reader = csv.reader(file)
                
                # Skip the header row (assuming there is one)
                next(reader, None)
                
                # Add each student ID to the set
                for row in reader:
                    if row:  # Skip empty rows
                        student_id = row[0].strip()
                        if student_id:  # Skip empty IDs
                            target_set.add(student_id)
            
            return True
        
        except FileNotFoundError:
            print(f"Error: File '{filename}' not found.")
            return False
        except Exception as e:
            print(f"Error loading data from '{filename}': {e}")
            return False
    
    def students_in_both(self):
        """
        Find students enrolled in both courses.
        
        Returns:
            Set: A set of student IDs enrolled in both courses
        """
        return self.course_a.intersection(self.course_b)
    
    def students_only_in_a(self):
        """
        Find students enrolled in course A only.
        
        Returns:
            Set: A set of student IDs enrolled only in course A
        """
        return self.course_a.difference(self.course_b)
    
    def students_only_in_b(self):
        """
        Find students enrolled in course B only.
        
        Returns:
            Set: A set of student IDs enrolled only in course B
        """
        return self.course_b.difference(self.course_a)
    
    def all_students(self):
        """
        Find all students enrolled in either course.
        
        Returns:
            Set: A set of all student IDs
        """
        return self.course_a.union(self.course_b)
    
    def display_statistics(self):
        """
        Display enrollment statistics to the console.
        """
        # Get the analysis results
        in_both = self.students_in_both()
        only_a = self.students_only_in_a()
        only_b = self.students_only_in_b()
        all_students = self.all_students()
        
        # Display formatted results
        print("\n=== Enrollment Analysis ===")
        print(f"Total students in Course A: {len(self.course_a)}")
        print(f"Total students in Course B: {len(self.course_b)}")
        print(f"Total unique students: {len(all_students)}")
        print("\n--- Detailed Breakdown ---")
        print(f"Students in both courses: {len(in_both)}")
        if len(in_both) > 0:
            print(f"  {in_both}")
        
        print(f"Students only in Course A: {len(only_a)}")
        if len(only_a) > 0:
            print(f"  {only_a}")
        
        print(f"Students only in Course B: {len(only_b)}")
        if len(only_b) > 0:
            print(f"  {only_b}")


def main():
    """
    Main function to run the enrollment manager from the command line.
    """
    # Check command line arguments
    if len(sys.argv) != 3:
        print("Usage: python EnrollmentManager.py courseA.csv courseB.csv")
        return
    
    # Get file paths from command line arguments
    file_a = sys.argv[1]
    file_b = sys.argv[2]
    
    # Create an enrollment manager and load the data
    manager = EnrollmentManager(file_a, file_b)
    
    # Display the statistics
    manager.display_statistics()


if __name__ == "__main__":
    main()