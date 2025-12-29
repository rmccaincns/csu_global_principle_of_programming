# Course Information Lookup Program
# This program stores course information in dictionaries and allows
# users to look up course details by entering a course number.

def main():
    # Dictionary containing course numbers and room numbers
    rooms = {
        'CSC101': '3004',
        'CSC102': '4501',
        'CSC103': '6755',
        'NET110': '1244',
        'COM241': '1411'
    }

    # Dictionary containing course numbers and instructor names
    instructors = {
        'CSC101': 'Haynes',
        'CSC102': 'Alvarado',
        'CSC103': 'Rich',
        'NET110': 'Burke',
        'COM241': 'Lee'
    }

    # Dictionary containing course numbers and meeting times
    meeting_times = {
        'CSC101': '8:00 a.m.',
        'CSC102': '9:00 a.m.',
        'CSC103': '10:00 a.m.',
        'NET110': '11:00 a.m.',
        'COM241': '1:00 p.m.'
    }

    # Prompt the user to enter a course number
    course_number = input('Enter a course number: ')

    # Look up the course and display information
    if course_number in rooms:
        print(f'Room Number: {rooms[course_number]}')
        print(f'Instructor: {instructors[course_number]}')
        print(f'Meeting Time: {meeting_times[course_number]}')
    else:
        print(f'{course_number} is not a valid course number.')


# Call the main function
if __name__ == '__main__':
    main()

