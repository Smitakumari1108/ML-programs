import pandas as pd

# Define the data
data = {
    'StuEnroll': ['U0001', 'U0002', 'U0003', 'U0004', 'U0005', 'U0006', 'U0007', 'U0008', 'U0009', 'U0010'],
    'UniversityCode': ['B101', 'B102', 'B103', 'B104', 'B105', 'B106', 'B107', 'B108', 'B109', 'B110'],
    'UniversityName': ['Bangalore University'] * 10,
    'CollegeID': ['C0001101', 'C0002102', 'C0003103', 'C0004104', 'C0005105', 'C0006106', 'C0007107', 'C0008108', 'C0009109', 'C0010110'],
    'CollegeName': ['Oxford', 'Christ', 'AMC', 'Dayanandha', 'SFS', 'T.John', 'Christ', 'Oxford', 'Dayanandha', 'SFS'],
    'CourseID': [1101, 2102, 3103, 4104, 5105, 1101, 2102, 3103, 4104, 5105],
    'CourseName': ['BCA', 'B.SC', 'MCA', 'BCA', 'B.SC', 'BCA', 'B.SC', 'MCA', 'BCA', 'B.SC'],
    'AdminYear': [2021, 2022, 2020, 2021, 2020, 2021, 2022, 2020, 2021, 2020],
    'Substream': ['CS', 'CS', 'CA', 'CA', 'CS', 'CS', 'CS', 'CA', 'CA', 'CS'],
    'PUPresent': [90, 85, 90, 95, 90, 90, 85, 90, 95, 90],
    'Obtained': [80, 70, 85, 92, 85, 80, 70, 85, 92, 85]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Save the dataframe to a CSV file
csv_file_path = 'student_data.csv'
df.to_csv(csv_file_path, index=False)

print(f"CSV file has been saved to {csv_file_path}")
