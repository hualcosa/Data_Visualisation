# this implementation correspond to a solution of an exercise
# in which the objective was to recreate a graph. We were given
# an image of the graph and should implement the matching code using
# matplotlib

from matplotlib import pyplot as plt

# bars with errors

past_years_averages = [82, 84, 83, 86, 74, 84, 90]
years = [2000, 2001, 2002, 2003, 2004, 2005, 2006]
error = [1.5, 2.1, 1.2, 3.2, 2.3, 1.7, 2.4]

ax = plt.subplot()
plt.figure(figsize=(10, 8))
plt.bar(range(len(past_years_averages)), past_years_averages,  yerr=error, capsize=5)
plt.axis([-0.5, 6.5, 70, 95])
ax.set_xticks(range(len(years)))
ax.set_xticklabels((years))
plt.title('Final Exam Averages')
plt.xlabel('Year')
plt.ylabel('Test average')
plt.savefig('my_bar_chart.png')
plt.show() 



# side by side bars

unit_topics = ['Limits', 'Derivatives', 'Integrals', 'Diff Eq', 'Applications']
middle_school_a = [80, 85, 84, 83, 86]
middle_school_b = [73, 78, 77, 82, 86]

def create_x(t, w, n, d):
    return [t*x + w*n for x in range(d)]

school_b_x = [1.6, 3.6, 5.6, 7.6, 9.6]

t = 2 # There are two sets of data: A and B
w = 0.8 # We generally want bars to be 0.8
n = 1 # A is first set of data
d = 5 # There are 5 topics we're plotting
school_a_x = create_x(t,w,n,d)
# for the second data set, we need to change n
n = 2
school_b_x = create_x(t,w,n,d)
middle_x = [(a + b)/2 for a, b in zip(school_a_x,school_b_x)]

plt.figure(figsize=(10,8))
ax = plt.subplot()
plt.bar(school_a_x, middle_school_a)
plt.bar(school_b_x, middle_school_b)
ax.set_xticks(middle_x)
ax.set_xticklabels(unit_topics)
plt.legend(["Middle School A", "Middle School B"])
plt.title('Test Averages on Different Units')
plt.xlabel('Unit')
plt.ylabel('Test Average')
plt.savefig('my_side_by_side.png')
plt.show()

# Stacked bars
import numpy as np

unit_topics = ['Limits', 'Derivatives', 'Integrals', 'Diff Eq', 'Applications']
As = [6, 3, 4, 3, 5]
Bs = [8, 12, 8, 9, 10]
Cs = [13, 12, 15, 13, 14]
Ds = [2, 3, 3, 2, 1]
Fs = [1, 0, 0, 3, 0]

x = range(5)

c_bottom = np.add(As, Bs)

d_bottom = np.add(c_bottom, Cs)
f_bottom = np.add(d_bottom, Ds)

plt.figure(figsize=(10,8))
ax = plt.subplot()
plt.bar(x, As)
plt.bar(x, Bs, bottom=As)
plt.bar(x, Cs, bottom=c_bottom)
plt.bar(x, Ds, bottom=d_bottom)
plt.bar(x, Fs, bottom=f_bottom)
ax.set_xticks(range(len(unit_topics)))
ax.set_xticklabels(unit_topics)
plt.title('Grade distribution')
plt.ylabel('Number of Students')
plt.xlabel('Unit')
plt.legend(['A', 'B', 'C', 'D', 'F'])
plt.savefig('my_stacked_bar.png')
plt.show()

# Histograms

exam_scores1 = [62.58, 67.63, 81.37, 52.53, 62.98, 72.15, 59.05, 73.85, 97.24, 76.81, 89.34, 74.44, 68.52, 85.13, 90.75, 70.29, 75.62, 85.38, 77.82, 98.31, 79.08, 61.72, 71.33, 80.77, 80.31, 78.16, 61.15, 64.99, 72.67, 78.94]
exam_scores2 = [72.38, 71.28, 79.24, 83.86, 84.42, 79.38, 75.51, 76.63, 81.48,78.81,79.23,74.38,79.27,81.07,75.42,90.35,82.93,86.74,81.33,95.1,86.57,83.66,85.58,81.87,92.14,72.15,91.64,74.21,89.04,76.54,81.9,96.5,80.05,74.77,72.26,73.23,92.6,66.22,70.09,77.2]

plt.figure(figsize=(10, 8))
plt.hist(exam_scores1, bins=12, normed=True, histtype='step', linewidth=2)
plt.hist(exam_scores2, bins=12, normed=True, histtype='step', linewidth=2)
plt.legend(["1st Yr Teaching", "2nd Yr Teaching"])
plt.title('Final Exam Score Distribution')
plt.xlabel('Percentage')
plt.ylabel('Frequency')
plt.savefig('my_histogram.png')
plt.show()

# pie chart

unit_topics = ['Limits', 'Derivatives', 'Integrals', 'Diff Eq', 'Applications']
num_hardest_reported = [1, 3, 10, 15, 1]

plt.figure(figsize=(10,8))
plt.pie(num_hardest_reported, labels=unit_topics, autopct='%d%%')
plt.axis('equal')
plt.title('Hardest Topics')
plt.savefig('my_pie_chart.png')
plt.show())


# Line graph with error margins 

hours_reported =[3, 2.5, 2.75, 2.5, 2.75, 3.0, 3.5, 3.25, 3.25,  3.5, 3.5, 3.75, 3.75,4, 4.0, 3.75,  4.0, 4.25, 4.25, 4.5, 4.5, 5.0, 5.25, 5, 5.25, 5.5, 5.5, 5.75, 5.25, 4.75]
exam_scores = [52.53, 59.05, 61.15, 61.72, 62.58, 62.98, 64.99, 67.63, 68.52, 70.29, 71.33, 72.15, 72.67, 73.85, 74.44, 75.62, 76.81, 77.82, 78.16, 78.94, 79.08, 80.31, 80.77, 81.37, 85.13, 85.38, 89.34, 90.75, 97.24, 98.31]


hours_lower_bound = [el*0.8 for el in hours_reported]
hours_upper_bound = [el*1.2 for el in hours_reported]

plt.figure(figsize=(10,8))
plt.plot(exam_scores, hours_reported, linewidth=2)
plt.fill_between(exam_scores, hours_lower_bound, hours_upper_bound, alpha=0.2)
plt.title('Time spent studying vs final exam scores')
plt.xlabel('Score')
plt.ylabel('Hours studying (self-reported)')
plt.savefig('my_line_graph.png')
plt.show()