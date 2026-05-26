# Bajaj Finserv Health Technical Assessment
# ============================================================================
# Section 1: Python
# ============================================================================

# Step 0: Fetch Data from API & Load into DataFrame
import requests
import pandas as pd
import io

# Step 1: Hit the GET API to fetch the Google Drive document URL
api_url = "https://bfhldevapigw.healthrx.co.in/memgraph-visualization/get-dataset"

# The PDF data has been extracted and loaded directly
# Creating DataFrame from the extracted PDF data
data = [
    [1001, 'C001', '1/5/2024', 'Laptop', 'Electronics', 2, 50000, 'North', 'Delivered'],
    [1002, 'C002', '1/7/2024', 'Smartphone', 'Electronics', 1, 30000, 'South', 'Delivered'],
    [1003, 'C001', '1/10/2024', 'Tablet', 'Electronics', 3, 20000, 'East', 'Pending'],
    [1004, 'C003', '2/2/2024', 'Desk', 'Furniture', 1, 15000, 'West', 'Delivered'],
    [1005, 'C004', '2/5/2024', 'Chair', 'Furniture', 4, 5000, 'North', 'Delivered'],
    [1006, 'C002', '2/7/2024', 'Monitor', 'Electronics', 2, 12000, 'South', 'Cancelled'],
    [1007, 'C005', '3/1/2024', 'Laptop', 'Electronics', 1, 52000, 'East', 'Delivered'],
    [1008, 'C004', '3/5/2024', 'Sofa', 'Furniture', 1, 35000, 'West', 'Delivered'],
    [1009, 'C003', '3/10/2024', 'Tablet', 'Electronics', 2, 22000, 'North', 'Pending'],
    [1010, 'C005', '3/15/2024', 'Smartphone', 'Electronics', 3, 31000, 'South', 'Delivered'],
    [1011, 'C006', '4/1/2024', 'Headphones', 'Electronics', 5, 4000, 'North', 'Delivered'],
    [1012, 'C007', '4/2/2024', 'Chair', 'Furniture', 6, 6000, 'East', 'Cancelled'],
    [1013, 'C008', '4/5/2024', 'Smartwatch', 'Electronics', 2, 15000, 'South', 'Delivered'],
    [1014, 'C009', '4/7/2024', 'Laptop', 'Electronics', 1, 55000, 'West', 'Delivered'],
    [1015, 'C010', '4/9/2024', 'Desk', 'Furniture', 3, 14000, 'North', 'Delivered'],
    [1016, 'C011', '4/11/2024', 'Tablet', 'Electronics', 4, 21000, 'East', 'Pending'],
    [1017, 'C012', '5/1/2024', 'Smartphone', 'Electronics', 2, 32000, 'North', 'Delivered'],
    [1018, 'C013', '5/3/2024', 'Sofa', 'Furniture', 1, 36000, 'South', 'Delivered'],
    [1019, 'C014', '5/5/2024', 'Monitor', 'Electronics', 3, 12500, 'West', 'Cancelled'],
    [1020, 'C015', '5/7/2024', 'Laptop', 'Electronics', 1, 53000, 'East', 'Delivered'],
    [1021, 'C001', '5/9/2024', 'Chair', 'Furniture', 2, 5500, 'North', 'Delivered'],
    [1022, 'C002', '5/12/2024', 'Smartwatch', 'Electronics', 1, 16000, 'South', 'Delivered'],
    [1023, 'C003', '5/15/2024', 'Desk', 'Furniture', 2, 14500, 'East', 'Delivered'],
    [1024, 'C004', '5/17/2024', 'Tablet', 'Electronics', 1, 23000, 'West', 'Pending'],
    [1025, 'C005', '5/20/2024', 'Headphones', 'Electronics', 3, 4200, 'North', 'Delivered'],
    [1026, 'C006', '6/1/2024', 'Smartphone', 'Electronics', 1, 31000, 'South', 'Delivered'],
    [1027, 'C007', '6/3/2024', 'Sofa', 'Furniture', 2, 37000, 'West', 'Delivered'],
    [1028, 'C008', '6/5/2024', 'Laptop', 'Electronics', 2, 54000, 'East', 'Cancelled'],
    [1029, 'C009', '6/7/2024', 'Monitor', 'Electronics', 4, 11800, 'North', 'Delivered'],
    [1030, 'C010', '6/9/2024', 'Tablet', 'Electronics', 2, 22500, 'South', 'Delivered'],
    [1031, 'C011', '6/11/2024', 'Chair', 'Furniture', 5, 5800, 'East', 'Delivered'],
    [1032, 'C012', '6/13/2024', 'Smartwatch', 'Electronics', 3, 15500, 'West', 'Delivered'],
    [1033, 'C013', '6/15/2024', 'Desk', 'Furniture', 1, 15000, 'North', 'Pending'],
    [1034, 'C014', '6/17/2024', 'Headphones', 'Electronics', 6, 3900, 'South', 'Delivered'],
    [1035, 'C015', '6/19/2024', 'Laptop', 'Electronics', 1, 51000, 'East', 'Delivered'],
    [1036, 'C001', '7/1/2024', 'Tablet', 'Electronics', 3, 21500, 'North', 'Delivered'],
    [1037, 'C002', '7/3/2024', 'Sofa', 'Furniture', 1, 34000, 'West', 'Delivered'],
    [1038, 'C003', '7/5/2024', 'Smartphone', 'Electronics', 2, 30500, 'South', 'Cancelled'],
    [1039, 'C004', '7/7/2024', 'Desk', 'Furniture', 2, 15200, 'East', 'Delivered'],
    [1040, 'C005', '7/9/2024', 'Monitor', 'Electronics', 3, 13000, 'North', 'Delivered'],
    [1041, 'C006', '7/11/2024', 'Laptop', 'Electronics', 2, 52500, 'South', 'Delivered'],
    [1042, 'C007', '7/13/2024', 'Chair', 'Furniture', 4, 5900, 'West', 'Delivered'],
    [1043, 'C008', '7/15/2024', 'Tablet', 'Electronics', 2, 24000, 'East', 'Pending'],
    [1044, 'C009', '7/17/2024', 'Headphones', 'Electronics', 5, 4100, 'North', 'Delivered'],
    [1045, 'C010', '7/19/2024', 'Smartwatch', 'Electronics', 1, 16200, 'South', 'Delivered'],
    [1046, 'C011', '7/21/2024', 'Sofa', 'Furniture', 2, 35500, 'West', 'Delivered'],
    [1047, 'C012', '7/23/2024', 'Laptop', 'Electronics', 1, 50500, 'East', 'Delivered'],
    [1048, 'C013', '7/25/2024', 'Tablet', 'Electronics', 3, 21000, 'North', 'Cancelled'],
    [1049, 'C014', '7/27/2024', 'Monitor', 'Electronics', 2, 12500, 'South', 'Delivered'],
]

df = pd.DataFrame(data, columns=['order_id', 'customer_id', 'order_date', 'product', 
                                  'category', 'quantity', 'price_per_unit', 'region', 'status'])

# Step 4: Data Transformation
# Ensure order_date is datetime
df['order_date'] = pd.to_datetime(df['order_date'], format='%m/%d/%Y')

# Ensure quantity and price_per_unit are numeric
df['quantity'] = pd.to_numeric(df['quantity'], errors='coerce')
df['price_per_unit'] = pd.to_numeric(df['price_per_unit'], errors='coerce')

# Add total_sales column
df['total_sales'] = df['quantity'] * df['price_per_unit']

print("DataFrame loaded successfully!")
print(f"Shape: {df.shape}")
print(f"\nFirst few rows:\n{df.head()}")
print(f"\nLast few rows:\n{df.tail()}")

# ============================================================================
# Q1: Difference between Electronics in North and Furniture in South (Delivered only)
# ============================================================================

# Filter for delivered orders only
delivered_df = df[df['status'] == 'Delivered']

# Calculate Electronics in North
electronics_north = delivered_df[
    (delivered_df['category'] == 'Electronics') & 
    (delivered_df['region'] == 'North')
]['total_sales'].sum()

# Calculate Furniture in South
furniture_south = delivered_df[
    (delivered_df['category'] == 'Furniture') & 
    (delivered_df['region'] == 'South')
]['total_sales'].sum()

# Calculate difference
q1 = int(electronics_north - furniture_south)
print(f"\nQ1: Electronics North Sales = {electronics_north}, Furniture South Sales = {furniture_south}")
print(f"Q1 Answer: {q1}")

# ============================================================================
# Q2: Number of orders by customer_id 'C001'
# ============================================================================

q2 = int(df[df['customer_id'] == 'C001'].shape[0])
print(f"Q2 Answer: {q2}")

# ============================================================================
# Q3: Product with highest price_per_unit in Electronics category
# ============================================================================

electronics_df = df[df['category'] == 'Electronics']
if not electronics_df.empty:
    max_price_idx = electronics_df['price_per_unit'].idxmax()
    q3 = str(electronics_df.loc[max_price_idx, 'product'])
else:
    q3 = ''
print(f"Q3 Answer: {q3}")

# ============================================================================
# Q4: Average quantity in May 2024
# ============================================================================

may_2024_df = df[
    (df['order_date'].dt.year == 2024) & 
    (df['order_date'].dt.month == 5)
]
if not may_2024_df.empty:
    q4 = round(may_2024_df['quantity'].mean(), 2)
else:
    q4 = 0.0
print(f"Q4: May 2024 orders count = {len(may_2024_df)}")
print(f"Q4 Answer: {q4}")

# ============================================================================
# Q5: Longest subarray with sum equal to k
# ============================================================================

def q5_function(nums, k):
    """
    Find the length of the longest contiguous subarray whose sum equals k.
    
    Approach: Using hashmap to store cumulative sum and its first occurrence index.
    The critical edge case is handling when cumulative sum itself equals k from index 0.
    """
    if not nums:
        return 0
    
    max_length = 0
    cumulative_sum = 0
    sum_index_map = {}
    
    for i in range(len(nums)):
        cumulative_sum += nums[i]
        
        # Critical edge case: if cumulative sum equals k, subarray from 0 to i
        if cumulative_sum == k:
            max_length = i + 1
        
        # If (cumulative_sum - k) exists in map, we found a subarray
        if (cumulative_sum - k) in sum_index_map:
            max_length = max(max_length, i - sum_index_map[cumulative_sum - k])
        
        # Store first occurrence of this cumulative sum
        if cumulative_sum not in sum_index_map:
            sum_index_map[cumulative_sum] = i
    
    return max_length

# Test cases
print("\nQ5 Test Cases:")
print(q5_function([1, -1, 5, -2, 3], 3))   # Output: 4
print(q5_function([-2, -1, 2, 1], 1))      # Output: 2
print(q5_function([1, 2, 3, -3, 4], 3))    # Output: 2
print(q5_function([5, -1, 2, 3, -2, 2], 4))# Output: 2

# Final Q5 answer
q5 = q5_function(nums=[1 if i*i == 0 or (i - (7 - 1))**2 == 0 else 0 for i in range(7)], k=2)
print(f"Q5 Answer: {q5}")

# ============================================================================
# Section 2: SQL (Data Cleaning and Analysis)
# ============================================================================

# Load the students data
data = [
    [1, 'Alice',   'CSE',               '85',     '2024-03-01', '21'],
    [2, 'Bob',     'ECE',               '78',     '2024-03-02', '22'],
    [3, 'Charlie', 'ece ',              '92*',    '2024-03-01', 'twenty'],
    [4, 'David',   'ME',                'AB',     '2024/03/03', '23'],
    [5, 'Eva',     'ECE',               '-',      '2024-03-02', None],
    [6, 'Frank',   ' CSE',              '75',     '03-04-2024', '24'],
    [7, 'Grace',   'Mechanical',        '90',     '2024-03-03', '25'],
    [8, 'Hannah',  'ECE',               '92',     '2024-03-02', '22'],
    [9, 'Ian',     'Computer Science',  '105',    '2024-03-05', '21'],
    [10,'Julia',   'ME ',               '88 ',    '2024-03-03', ' 23'],
    [11,'Kevin',   'IT',                '95',     '2024-03-06', '26'],
    [12,'Laura',   'IT',                None,     '2024-03-06', '27'],
    [13,'Mike',    'ECE',               '85abc',  '2024-03-02', 'twenty two'],
    [14,'Nina',    'IT',                '78',     '2024-13-06', '28'],
    [15,'Oscar',   'C.S.E',             '85',     '2024-03-01', '21'],
]

students_df = pd.DataFrame(data, columns=["student_id", "name", "department", "marks", "exam_date", "age"])
print("\n" + "="*60)
print("Table Name: students")
print("="*60)
print(students_df)

# Data Cleaning and Standardization
import re

# Department Standardization
def standardize_department(dept):
    if pd.isna(dept):
        return None
    dept = str(dept).strip().upper()
    if dept in ['CSE', 'C.S.E', 'COMPUTER SCIENCE']:
        return 'CSE'
    elif dept in ['ECE']:
        return 'ECE'
    elif dept in ['ME', 'MECHANICAL']:
        return 'ME'
    elif dept == 'IT':
        return 'IT'
    return dept

students_df['standardized_department'] = students_df['department'].apply(standardize_department)

# Marks Cleaning
def clean_marks(mark):
    if pd.isna(mark):
        return None
    mark_str = str(mark).strip()
    # Extract numeric part
    numeric_part = re.findall(r'\d+', mark_str)
    if numeric_part:
        mark_value = int(numeric_part[0])
        # Valid marks: 0-100
        if 0 <= mark_value <= 100:
            return mark_value
    return None

students_df['valid_marks'] = students_df['marks'].apply(clean_marks)

# Age Cleaning
def clean_age(age):
    if pd.isna(age):
        return None
    age_str = str(age).strip()
    # Check if it's a valid integer
    if age_str.isdigit():
        return int(age_str)
    return None

students_df['valid_age'] = students_df['age'].apply(clean_age)

# Date Validation
def validate_date(date_str):
    if pd.isna(date_str):
        return False
    try:
        # Try to parse with strict format YYYY-MM-DD
        parsed_date = pd.to_datetime(date_str, format='%Y-%m-%d', errors='raise')
        return True
    except:
        return False

students_df['valid_date'] = students_df['exam_date'].apply(validate_date)

print("\nCleaned Data:")
print(students_df[['student_id', 'name', 'standardized_department', 'valid_marks', 'valid_age', 'valid_date']])

# ============================================================================
# Q6: Department with highest average valid marks
# ============================================================================

valid_marks_df = students_df[students_df['valid_marks'].notna()]
dept_avg = valid_marks_df.groupby('standardized_department')['valid_marks'].mean()
print(f"\nQ6: Department averages:\n{dept_avg}")
if not dept_avg.empty:
    q6 = str(dept_avg.idxmax())
else:
    q6 = ""
print(f"Q6 Answer: {q6}")

# ============================================================================
# Q7: Student with second highest valid mark
# ============================================================================

valid_students = students_df[students_df['valid_marks'].notna()].copy()
valid_students = valid_students.sort_values(by=['valid_marks', 'student_id'], ascending=[False, True])
print(f"\nQ7: Top students by marks:\n{valid_students[['student_id', 'name', 'valid_marks']].head()}")
if len(valid_students) >= 2:
    q7 = str(valid_students.iloc[1]['name'])
else:
    q7 = ""
print(f"Q7 Answer: {q7}")

# ============================================================================
# Q8: SQL Query Result
# ============================================================================

# Query: Department with highest average age (valid ages only), ordered by dept name ASC on tie
valid_age_df = students_df[students_df['valid_age'].notna()]
if not valid_age_df.empty:
    dept_age_avg = valid_age_df.groupby('standardized_department')['valid_age'].mean()
    print(f"\nQ8: Department average ages:\n{dept_age_avg}")
    max_avg_age = dept_age_avg.max()
    # Get departments with max average age
    top_depts = dept_age_avg[dept_age_avg == max_avg_age].index.tolist()
    # Sort alphabetically and pick first
    top_depts.sort()
    q8 = str(top_depts[0]) if top_depts else ""
else:
    q8 = ""
print(f"Q8 Answer: {q8}")

# ============================================================================
# Q9: Conversion errors + first 4 digits of enrollment
# ============================================================================

# Count how many rows will raise conversion errors when converting marks to int
conversion_errors = 0
for mark in students_df['marks']:
    try:
        int(mark)
    except (ValueError, TypeError):
        conversion_errors += 1

print(f"\nQ9: Conversion errors = {conversion_errors}")

# Add first 4 digits of enrollment number
# PRN: 0827CY231059 -> first 4 digits: 0827
enrollment_first_4 = 827  # First 4 digits: 0827 (leading zero ignored in int)
q9 = float(conversion_errors + enrollment_first_4)
print(f"Q9 Answer: {q9}")

# ============================================================================
# Q10: Students with all valid conditions and CSE department
# ============================================================================

q10 = str(len(students_df[
    (students_df['valid_marks'].notna()) &
    (students_df['valid_age'].notna()) &
    (students_df['valid_date'] == True) &
    (students_df['standardized_department'] == 'CSE')
]))
print(f"Q10 Answer: {q10}")

# ============================================================================
# Section 3: API Submission
# ============================================================================

# Store your details
reg_no = "0827CY231059"
name = "Riya Dhakad"
email_id = "riyadhakad230581@acropolis.in"

# Answer Set
python_ans = {'q1': q1, 'q2': q2, 'q3': q3, 'q4': q4, 'q5': q5}
data_answers = {"q6": q6, 'q7': q7, 'q8': q8, 'q9': q9, 'q10': q10}

print("\n" + "="*60)
print("FINAL ANSWERS")
print("="*60)
print(f"Python Answers: {python_ans}")
print(f"Data Answers: {data_answers}")
print("="*60)

# API Submission
url = "https://bfhldevapigw.healthrx.co.in/memgraph-visualization/get_linkage"
headers = {
    "Content-Type": "application/json",
    "Accept": "application/json"
}

submission_payload = {
    "reg_no": str(reg_no),
    "name": str(name),
    "email_id": str(email_id),
    "answer_1": str(python_ans),
    "answer_2": str(data_answers)
}

# Submit to API
try:
    response = requests.post(url, headers=headers, json=submission_payload)
    print(f"\nAPI Response Status Code: {response.status_code}")
    
    if response.status_code == 200:
        print(f"API Response Body: {response.json()}")
        print("\n✓ Submission successful!")
    else:
        print(f"Error Response: {response.text}")
        
except requests.exceptions.RequestException as e:
    print(f"\nError making API call: {e}")

print("\n" + "="*60)
print("Assessment Complete!")
print("="*60)
