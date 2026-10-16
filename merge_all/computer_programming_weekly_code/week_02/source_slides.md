# Week 02 — Data science and Matplotlib charts

Source PDF pages 98–150. The PDF does not consistently label these sections with official week numbers; numbering here is inferred from slide-deck boundaries and topic progression.

Extracted text is kept as close to the source as possible. Ellipses (`...`) in the original slides indicate omitted/incremental code and are not necessarily runnable. See `runnable_examples/` for completed examples.

## PDF page 98

```text
010123138 
Computer Programming
```

## PDF page 99

```text
2
Check Attendance..
```

## PDF page 100

```text
3
Data Science
```

## PDF page 101

```text
4
Data Science
Process of acquiring knowledge through data
```

## PDF page 102

```text
5
Data Science
Process of acquiring knowledge through data
Interdisciplinary field that uses data to    
- understand patterns
- answer questions
- make predictions
- support decision-making
```

## PDF page 103

```text
6
Data Science
Process of acquiring knowledge through data
     Data --> Information --> Knowledge
```

## PDF page 104

```text
7
Data
Data (The Raw Facts)
Raw, unorganized, and unprocessed facts, numbers
Factory machine logs 
e.g. "Machine A: Break down date : 12/3/25"
```

## PDF page 105

```text
8
Information
Information (Processed Data)
Data that has been cleaned, processed, organized, and 
structured 
to give it meaning and make it easier to understand 
and use.
By summarize logs, get monthly report showing
 Machine A break down 3 times
 Machine B break down 1 times
 Machine C ...
```

## PDF page 106

```text
9
Knowledge
Knowledge (Actionable Understanding)
Information that has been understood and combined 
to provide insights, patterns, or rules that can 
guide human decisions and actions
Machine A break down 3 times, is there a problem with 
it? May check its past history to determine whether 
it should be replaced.
```

## PDF page 107

```text
10
Knowledge
Example: Hospital Patient Monitoring System 
Data (Raw Facts):
Patient's heart rate, oxygen, and temperature log
Information (Processed Data):
Patient's heart rate and temperature have been increasing for 4 hours
Knowledge (Understanding):
Doctors recognize that these changes may indicate a problem, such as 
infection or internal bleeding, so they can check the patient and take action 
early.
```

## PDF page 108

```text
11
Knowledge
Example: Customer Reviews
Data (Raw Facts):
Customer star ratings: 5, 4, 2, 1, 5, 3, 2, 1
Information (Processed Data):
Most low ratings mention slow delivery
Knowledge (Understanding):
Delivery speed is a key factor affecting customer satisfaction, so 
improving delivery time may improve customer experience
```

## PDF page 109

```text
12
Data Science Workflow
Identifying a problem 
Data Collection
Data Processing
Exploratory Data Analysis (EDA)
Data Modeling
Communication
```

## PDF page 110

```text
13
Data Science Workflow
Identifying a problem 
define the business problem, formulate hypotheses, 
and decide what metrics matter
AI can help identify anomalies or hidden 
opportunities in historical data that humans might 
miss
```

## PDF page 111

```text
14
Data Science Workflow
Identifying a problem 
Data Collection
Write program, querying databases, etc.
AI tools automate data extraction
For example, Computer Vision models can extract text 
from scanned documents or images
Natural Language Processing (NLP) can scrape, parse, 
and clean unstructured text from the web
```

## PDF page 112

```text
15
Data Science Workflow
Identifying a problem 
Data Collection
Data Processing
handling missing values, removing duplicates, correct 
values, detect outlier
AI may assist
```

## PDF page 113

```text
16
Data Science Workflow
Identifying a problem 
Data Collection
Data Processing
Exploratory Data Analysis (EDA)
Data Modeling
Communication
```

## PDF page 114

```text
17
Data Science Workflow
Exploratory Data Analysis (EDA)
Examine the data to discover patterns, relationships, 
trends, and unusual observations
Use statistics and visualizations such as charts, 
graphs, and correlation analysis
```

## PDF page 115

```text
18
Data Science Workflow
Data Modeling
Build statistical or machine-learning models to 
answer the problem or make predictions
Select an appropriate algorithm, train the model, and 
evaluate its performance.
```

## PDF page 116

```text
19
Data Science Workflow
Communication
Present the findings and results to stakeholders in a 
clear and understandable way
(use reports, dashboards, visualizations)
Explain the key insights and how they can support 
decision-making
```

## PDF page 117

```text
20
...
```

## PDF page 118

```text
21
Data Visualization
Raw numbers vs. visual patterns
```

## PDF page 119

```text
22
Data Visualization
Raw numbers 
x,y
10.0,8.04
8.0,6.95
13.0,7.58
9.0,8.81
11.0,8.33
14.0,9.96
6.0,7.24
4.0,4.26
12.0,10.84
7.0,4.82
5.0,5.68
```

## PDF page 120

```text
23
Data Visualization
Raw numbers vs. visual patterns
x,y
10.0,8.04
8.0,6.95
13.0,7.58
9.0,8.81
11.0,8.33
14.0,9.96
6.0,7.24
4.0,4.26
12.0,10.84
7.0,4.82
5.0,5.68
```

## PDF page 121

```text
24
Similar Statistics
                                  Dataset I   Dataset II  Dataset III   Dataset IV
Mean_x                          9.000000    9.000000    9.000000    9.000000
Variance_x                     11.000000   11.000000   11.000000   11.000000
Mean_y                          7.500909    7.500909    7.500000    7.500909
Variance_y                      4.127269    4.127629    4.122620    4.123249
Correlation                     0.816421    0.816237    0.816287    0.816521
Linear Regression slope         0.500091    0.500000    0.499727    0.499909
Linear Regression intercept     3.000091    3.000909    3.002455    3.001727
Anscombe’s Quartet
```

## PDF page 122

```text
25
Different Patterns
```

## PDF page 123

```text
26
Outlier
```

## PDF page 124

```text
27
Outlier
Outlier - data value that is significantly different 
from the other values in a dataset
Should be processed carefully
not automatically remove an outlier, investigate why it is different
```

## PDF page 125

```text
28
...
```

## PDF page 126

```text
29
Matplotlib
A Python library for creating charts
```

## PDF page 127

```text
30
Matplotlib
A Python library for creating charts
   - line chart
   - bar chart
   - pie chart
```

## PDF page 128

```text
31
Line chart
import matplotlib.pyplot as plt
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]
plt.plot(x, y)
plt.title("Simple Line Plot")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.show()
```

## PDF page 129

```text
32
Line chart
import matplotlib.pyplot as plt
x = [1, 2, 3, 4, 5]     # x values
y = [2, 3, 5, 4, 10]    # y values
...
```

## PDF page 130

```text
33
Line chart
...
plt.plot(x, y, linestyle='--', marker='o')  
# plot using x and y
# set line style and marker
```

## PDF page 131

```text
34
Line chart
...
plt.plot(x, y, linestyle='--', marker='o')  
plt.title("Simple Line Plot")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.show()
# set title, labels
```

## PDF page 132

```text
35
Line chart
import matplotlib.pyplot as plt
x = [1, 2, 3, 4, 5]     
y = [2, 3, 5, 4, 10]
plt.plot(x, y, linestyle='--', marker='o') 
plt.title("Simple Line Plot")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.show()
```

## PDF page 133

```text
36
Bar chart
import matplotlib.pyplot as plt
products = ['Product A', 'Product B', 'Product C']
revenue = [45000, 78000, 32000]
...
```

## PDF page 134

```text
37
Bar chart
...
plt.bar( products, revenue, \
        color=['#1f77b4', '#ff7f0e', '#2ca02c'])
...
```

## PDF page 135

```text
38
Bar chart
...
plt.bar( products, revenue, \
        color=['#1f77b4', '#ff7f0e', '#2ca02c'])
plt.ylabel('Revenue ($)')
plt.title('Product Performance')
plt.show()
```

## PDF page 136

```text
39
Bar chart
```

## PDF page 137

```text
40
Pie chart
import matplotlib.pyplot as plt
hobbies = ['Gaming', 'Reading', 'Exercise', \         
           'Gardening']
hours = [10, 6, 5, 3]
...
```

## PDF page 138

```text
41
Pie chart
...
plt.pie( hours, labels=hobbies)
...
```

## PDF page 139

```text
42
Pie chart
...
plt.pie( hours, labels=hobbies)
plt.title('Weekly Time Spent on Hobbies')
plt.show()
```

## PDF page 140

```text
43
Pie chart
```

## PDF page 141

```text
44
Simple to use library
To create chart
...  plt.plot(x, y, linestyle='--', marker='o')  
...  plt.bar( products, revenue, ...
...  plt.pie( hours, labels=hobbies)
```

## PDF page 142

```text
45
...
```

## PDF page 143

```text
46
Guide Lines
Color & Contrast: Use readable color palettes; avoid 
clashing high-saturation colors
Chart Junk: Minimize unnecessary gridlines, 3D 
effects, or redundant labels
   Make it clear to see the result
```

## PDF page 144

```text
47
To try Python Libraries
NumPy - Numerical computations
Pandas - Data exploration, manipulation, and 
preparation
Scikit-learn - Machine learning model building, 
training, and evaluation to make predictions
https://en.wikipedia.org/wiki/Microsoft_Windows
```

## PDF page 145

```text
48
...
```

## PDF page 146

```text
49
A2 w14 update
1. Please add w14-update.pdf to your repository
In w14-update.pdf, explain what you have done in 
each commit made after w13-update.
For each commit, briefly describe:
- What you changed or implemented
- Any important fixes or improvements
- Any other relevant information about the commit
```

## PDF page 147

```text
50
A2 w14 update
2. Submit a text file containing the output 
of command:
git log --oneline
For example:
a1b2c3d Fix input validation
d4e5f6g Add XYZ functionality
...
```

## PDF page 148

```text
51
A2 w14 update
2. Submit a text file containing the output 
of command:
git log --oneline
Name the file using your student ID:
s<student-id>-w14-log.txt
For example:
s69-010126-5577-2-w14-log.txt
```

## PDF page 149

```text
52
A2 w14 update
Before submitting, make sure:
●
w14-update.pdf has been added to your repo.
●
w14-update.pdf explains every commit after w13
●
s<student-id>-w14-log.txt contains the output 
of git log --oneline.
●
You have used your own student ID in the 
filename.
●
Your repository is up to date.
```

## PDF page 150

```text
53
...
```

