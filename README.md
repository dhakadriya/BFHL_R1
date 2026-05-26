# Bajaj Finserv Health Technical Assessment

## Overview
Python and MySQL technical assessment solution for evaluating core programming and database skills.

**Duration:** 1 hour  
**Candidate:** Riya Dhakad  
**Registration:** 0827CY231059  
**Email:** riyadhakad230581@acropolis.in

---

## Prerequisites

```bash
pip install requests pandas
```

---

## Project Structure

```
.
├── main.py          # Complete assessment solution
└── README.md        # This file
```

---

## Assessment Sections

### **Section 1: Python (Q1-Q5)**

- **Q1:** Calculate sales difference between Electronics (North) and Furniture (South) for delivered orders
- **Q2:** Count total orders by customer C001
- **Q3:** Find product with highest price in Electronics category
- **Q4:** Calculate average quantity ordered in May 2024
- **Q5:** DSA - Longest contiguous subarray with sum equal to k

### **Section 2: SQL/Data Analysis (Q6-Q10)**

Data cleaning and standardization tasks:
- Department standardization (CSE, ECE, ME, IT)
- Marks validation (0-100 range, numeric only)
- Age validation (integer values only)
- Date validation (YYYY-MM-DD format)

**Questions:**
- **Q6:** Department with highest average valid marks
- **Q7:** Student with second highest valid marks
- **Q8:** Department with highest average age
- **Q9:** Count conversion errors + enrollment digits
- **Q10:** Students meeting all validation criteria in CSE

### **Section 3: API Submission**

Automated submission of answers to assessment API endpoint.

---

## How to Run

```bash
python main.py
```

The script will:
1. Load and process sales data (49 orders)
2. Solve all Python questions (Q1-Q5)
3. Clean and analyze student data (Q6-Q10)
4. Display all answers with detailed output
5. Automatically submit results to API

---

## Key Features

✅ Direct data loading from PDF extraction  
✅ Comprehensive data validation and cleaning  
✅ Efficient algorithms with edge case handling  
✅ Detailed output for verification  
✅ Automatic API submission  
✅ Clean, readable code with comments  

---

## Output

The script displays:
- DataFrame shape and preview
- Step-by-step calculations for each question
- Final answers summary
- API submission status

---

## Notes

- All answers are stored in designated variables (q1-q10)
- Data types are strictly maintained as per requirements
- Q5 implements optimal O(n) solution using hashmap
- Q9 includes first 4 digits of enrollment number (0827 = 827)

---

## API Endpoint

**Submission URL:** `https://bfhldevapigw.healthrx.co.in/memgraph-visualization/get_linkage`

**Method:** POST  
**Content-Type:** application/json

---

## License

This is an assessment submission for Bajaj Finserv Health.

---

**Assessment Completed:** ✓
