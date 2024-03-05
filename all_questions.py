# Add import files
import pickle



# -----------------------------------------------------------
def question1():
    answers = {}

    # type: bool (True/False)
    answers["(a)"] = True

    # type: explanatory string (at least four words)
    answers["(a) explain"] = "Hierarchical clustering is more flexible in handling outliers compared to k-means."

    # type: bool (True/False)
    answers["(b)"] = False

    # type: explanatory string (at least four words)
    answers["(b) explain"] = "Hierarchical clustering can produce different clusterings based on linkage criteria, and k-means can produce different clusterings due to random initialization."
"

    # type: bool (True/False)
    answers["(c)"] = False

    # type: explanatory string (at least four words)
    answers["(c) explain"] = "While k-means is more efficient than hierarchical clustering, it is not the most efficient clustering algorithm possible."

    # type: bool (True/False)
    answers["(d)"] = True

    # type: explanatory string (at least four words)
    answers["(d) explain"] = "Splitting a cluster and reassigning points generally leads to a decrease in SSE."

    # type: bool (True/False)
    answers["(e)"] = True

    # type: explanatory string (at least four words)
    answers["(e) explain"] = "A decrease in SSE indicates that cohesion within clusters is increasing."

    # type: bool (True/False)
    answers["(f)"] = True

    # type: explanatory string (at least four words)
    answers["(f) explain"] = "An increase in SSB indicates that separation between clusters is increasing."

    # type: bool (True/False)
    answers["(g)"] = True

    # type: explanatory string (at least four words)
    answers["(g) explain"] = "Cohesion and separation can be independent measures in k-means clustering."

    # type: bool (True/False)
    answers["(h)"] = False

    # type: explanatory string (at least four words)
    answers["(h) explain"] = "SSE + BSS is not constant; as SSE decreases, BSS increases"

    # type: bool (True/False)
    answers["(i)"] = False

    # type: explanatory string (at least four words)
    answers["(i) explain"] = "An increase in cohesion does not necessarily lead to an increase in separation."

    return answers




# -----------------------------------------------------------
def question2():
    answers = {}

    # type: bool (True/False)
    answers["(a)"] = True

    # type: explanatory string (at least four words)
    answers["(a) explain"] = "Each shaded circle represents a distinct cluster with uniform density, so the final centroid will be at the center of each circle."

    # type: bool (True/False)
    answers["(b)"] = False

    # type: explanatory string (at least four words)
    answers["(b) explain"] = "The final clusters may not be limited to points from only one shaded region due to the influence of initial centroid positions"

    # type: bool (True/False)
    answers["(c)"] = False

    # type: explanatory string (at least four words)
    answers["(c) explain"] = "K-means aims to assign each point to a cluster, so an empty cluster is unlikely unless there are more centroids than distinct data points."

    return answers




# -----------------------------------------------------------
def question3():
    answers = {}

    # type: a string that evaluates to a float
    answers["(a) SSE"] = "(R^2)*4"  # SSE = (1^2 + 1^2) for the two points in the cluster.

    # type: a string that evaluates to a float
    answers["(b) SSE"] = "4*((a*a) + (b*b) + (c*c))"  # SSE = (1^2 + 1^2) for the two points in the cluster.

    # type: a string that evaluates to a float
    answers["(c) SSE"] = "4*((R^2) + ((R/2)^2))"  # SSE = (2^2 + 2^2) for the two points in the cluster.

    return answers




# -----------------------------------------------------------
def question4():
    answers = {}

    # type: int
    answers["(a) Circle (a)"] = 1  # All 4 points from Cluster 1 are within Circle (a).

    # type: int
    answers["(a) Circle (b)"] = 1  # 3 points from Cluster 1 are within Circle (b).

    # type: int
    answers["(a) Circle (c)"] = 1  # 2 points from Cluster 1 are within Circle (c).

    # type: explanatory string (at least four words)
    answers["(a) explain"] = "A and B, each with 100 points, have equal influence on a centroid, with one favoring A. However, Circle C, with 100,000 points, ensures a centroid is held due to its stronger attraction, despite initially lacking one. Equal point distribution in A and B ensures each attracts a centroid."

    # type: int
    answers["(b) Circle (a)"] = 1  # 2 points from Cluster 2 are within Circle (a).

    # type: int
    answers["(b) Circle (b)"] = 1 # 2 points from Cluster 2 are within Circle (b).

    # type: int
    answers["(b) Circle (c)"] = 1  # 1 point from Cluster 2 is within Circle (c).

    # type: explanatory string (at least four words)
    answers["(b) explain"] = "The centroid remains at A, lacking a stronger pull. C's stronger attraction draws one centroid from B, resulting in one centroid for each of the three circles."

    # type: int
    answers["(c) Circle (a)"] = 0  # No points from Cluster 3 are within Circle (a).

    # type: int
    answers["(c) Circle (b)"] = 0  # No points from Cluster 3 are within Circle (b).


    # type: int
    answers["(c) Circle (c)"] = 2 # No points from Cluster 3 are within Circle (c).

    # type: explanatory string (at least four words)
    answers["(c) explain"] = "Close A and B share points, assigned to A's centroid. C's points split between two centroids, each with 50,000 points. A and B, with equal points, share a moving centroid. C's centroids slightly separate but stay within C with half the points each."

    return answers




# -----------------------------------------------------------
def question5():
    answers = {}

    # type: set
    answers["(a)"] = set('Group A', 'Group C')

    # type: explanatory string (at least four words)
    answers["(a) explain"] = "Group A and Group C should be merged using the single link method because they have the closest neighboring points."

    # type: set
    answers["(b)"] = set('Group A', 'Group B')

    # type: explanatory string (at least four words)
    answers["(b) explain"] = "roup A and Group B should be merged using the complete link method because the greatest distance between points within these groups is less than that involving Group C"

    return answers




# -----------------------------------------------------------
def question6():
    answers = {}

    # type: set
    answers["(a) core"] = set()

    # type: set
    answers["(a) boundary"] = set()

    # type: set
    answers["(a) noise"] = set()

    # type: set
    answers["(b) cluster 1"] = set()

    # type: set
    answers["(b) cluster 2"] = set()

    # type: set
    answers["(b) cluster 3"] = set()

    # type: set
    answers["(b) cluster 4"] = set()

    # type: set
    answers["(c)-a core"] = set()

    # type: set
    answers["(c)-a boundary"] = set()

    # type: set
    answers["(c)-a noise"] = set()

    # type: set
    answers["(c)-b cluster 1"] = set()

    # type: set
    answers["(c)-b cluster 2"] = set()

    # type: set
    answers["(c)-b cluster 3"] = set()

    # type: set
    answers["(c)-b cluster 4"] = set()

    return answers




# -----------------------------------------------------------
def question7():
    answers = {}

    # type: string
    answers["(a)"] = "Cluster 4"

    # type: explanatory string (at least four words)
    answers["(a) explain"] = "Cluster 4 has the most even distribution across different land cover types (Forest, Farm, Shrubland, Urban, Water), with significant numbers in each category. This distribution suggests that Cluster 4 has the highest entropy because there is no single dominant land cover type and the categories are more mixed"

    # type: string
    answers["(b)"] = "Cluster 1"

    # type: explanatory string (at least four words)
    answers["(b) explain"] = "Cluster 1 has 30,000 Water and very few of the other types, making it highly dominated by the Water category. This indicates that Cluster 1 has the lowest entropy because it has the least disorder or randomness, with a clear dominance of one category over the others."

    return answers




# -----------------------------------------------------------
def question8():
    answers = {}

    # type: string
    answers["(a) Matrix 1"] = ""

    # type: explanatory string (at least four words)
    answers["(a) explain diag entries, Matrix 1"] = ""

    # type: explanatory string (at least four words)
    answers["(a) explain non-diag entries, Matrix 1"] = ""

    # type: string
    answers["(a) Matrix 2"] = ""

    # type: explanatory string (at least four words)
    answers["(a) explain diag entries, Matrix 2"] = ""

    # type: explanatory string (at least four words)
    answers["(a) explain non-diag entries, Matrix 2"] = ""

    # type: string
    answers["(a) Matrix 3"] = ""

    # type: explanatory string (at least four words)
    answers["(a) explain diag entries, Matrix 3"] = ""

    # type: explanatory string (at least four words)
    answers["(a) explain non-diag entries, Matrix 3"] = ""

    # type: string
    answers["(b) Row 1"] = ""

    # type: string
    answers["(b) Row 2"] = ""

    # type: string
    answers["(b) Row 3"] = ""

    # type: string
    answers["(b) Row 4"] = ""

    # type: explanatory string (at least four words)
    answers["(b) Row 1 explain"] = ""

    # type: explanatory string (at least four words)
    answers["(b) Row 2 explain"] = ""

    # type: explanatory string (at least four words)
    answers["(b) Row 3 explain"] = ""

    # type: explanatory string (at least four words)
    answers["(b) Row 4 explain"] = ""

    return answers




# -----------------------------------------------------------
def question9():
    answers = {}

    # type: list
    answers["(a)"] = []

    # type: list
    answers["(b)"] = []

    # type: list
    answers["(c)"] = []

    # type: list
    answers["(d)"] = []

    # type: list
    answers["(e)"] = []

    # type: explanatory string (at least four words)
    answers["(e) explain"] = ""

    return answers




# -----------------------------------------------------------
def question10():
    answers = {}

    # type: string
    answers["(a) Figure (a)"] = ""

    # type: string
    answers["(a) Figure (b)"] = ""

    # type: explanatory string (at least four words)
    answers["(a) explain"] = ""

    # type: string
    answers["(b) Figure (a)"] = ""

    # type: string
    answers["(b) Figure (b)"] = ""

    # type: explanatory string (at least four words)
    answers["(b) explain"] = ""

    # type: string
    answers["(c)"] = ""

    return answers

# --------------------------------------------------------
if __name__ == '__main__':
    answers_dict = {}
    answers_dict['question1'] = question1()
    answers_dict['question2'] = question2()
    answers_dict['question3'] = question3()
    answers_dict['question4'] = question4()
    answers_dict['question5'] = question5()
    answers_dict['question6'] = question6()
    answers_dict['question7'] = question7()
    answers_dict['question8'] = question8()
    answers_dict['question9'] = question9()
    answers_dict['question10'] = question10()
    print('end code')

    with open('answers.pkl', 'wb') as f:
        pickle.dump(answers_dict, f)
