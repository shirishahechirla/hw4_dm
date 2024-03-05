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
    answers["(b)"] = True

    # type: explanatory string (at least four words)
    answers["(b) explain"] = "K-means is random in initial centroids, yielding varied results. In contrast, Agglomerative hierarchical clustering is deterministic, ensuring consistent outcomes."

    # type: bool (True/False)
    answers["(c)"] = False

    # type: explanatory string (at least four words)
    answers["(c) explain"] = "While k-means is more efficient than hierarchical clustering, it is not the most efficient clustering algorithm possible."

    # type: bool (True/False)
    answers["(d)"] = False

    # type: explanatory string (at least four words)
    answers["(d) explain"] = "Splitting reduces the sum of squared errors by introducing two centroids for the same set, resulting in a decrease in the distance to the nearest centroids."

    # type: bool (True/False)
    answers["(e)"] = True

    # type: explanatory string (at least four words)
    answers["(e) explain"] = "A decrease in SSE indicates that cohesion within clusters is increasing."

    # type: bool (True/False)
    answers["(f)"] = True

    # type: explanatory string (at least four words)
    answers["(f) explain"] = "An increase in SSB indicates that separation between clusters is increasing."

    # type: bool (True/False)
    answers["(g)"] = False

    # type: explanatory string (at least four words)
    answers["(g) explain"] = "In k-means, cohesion and separation are independent; enhancing cohesion doesn't necessarily enhance separation."

    # type: bool (True/False)
    answers["(h)"] = True

    # type: explanatory string (at least four words)
    answers["(h) explain"] = "The sum of squared distances (TSS) in k-means is the sum of SSE (within-cluster sum of squares) and SSB (between-cluster sum of squares). Additionally, TSS remains constant throughout the k-means clustering process."

    # type: bool (True/False)
    answers["(i)"] = True

    # type: explanatory string (at least four words)
    answers["(i) explain"] = "SSB measures cluster separation, while SSE is an inverse measure of cluster cohesion. Therefore, as cohesion increases, SSE decreases, and separation (SSB) increases."


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
    answers["(c)"] = True

    # type: explanatory string (at least four words)
    answers["(c) explain"] = "The centroid at 12.5 is distant from all points, leading to the emptiness of all other clusters."

    return answers




# -----------------------------------------------------------
def question3():
    answers = {}

    # type: a string that evaluates to a float
    answers["(a) SSE"] = "(R^2)*4"  

    # type: a string that evaluates to a float
    answers["(b) SSE"] = "4*((a*a) + (b*b) + (R*R))"  

    # type: a string that evaluates to a float
    answers["(c) SSE"] = "10*(R*R)"

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
    answers["(a)"] = set('Group A', 'Group B')

    # type: explanatory string (at least four words)
    answers["(a) explain"] = "Merging Group A and B is possible due to the minimal single-link distance between the rightmost point of A and the leftmost point of B."

    # type: set
    answers["(b)"] = set('Group A', 'Group C')

    # type: explanatory string (at least four words)
    answers["(b) explain"] = "Group A and C can be combined as the smallest complete-link distance is between the rightmost point of A and the farthest point of C."

    return answers




# -----------------------------------------------------------
def question6():
    answers = {}

    # type: set
    answers["(a) core"] = {'B', 'C', 'E', 'F', 'I', 'J', 'L', 'M'}

    # type: set
    answers["(a) boundary"] = {'D', 'G'}

    # type: set
    answers["(a) noise"] = {'A', 'H'}

    # type: set
    answers["(b) cluster 1"] = {'B','C','D','E','F','G'}

    # type: set
    answers["(b) cluster 2"] = {'I','J','L','M'}

    # type: set
    answers["(b) cluster 3"] = set()

    # type: set
    answers["(b) cluster 4"] = set()

    # type: set
    answers["(c)-a core"] = {'I', 'G', 'J', 'E', 'M', 'B', 'L', 'F', 'D', 'C'}

    # type: set
    answers["(c)-a boundary"] = {'A', 'H'}

    # type: set
    answers["(c)-a noise"] = set()

    # type: set
    answers["(c)-b cluster 1"] = {'G', 'I', 'H', 'J', 'E', 'M', 'B', 'D', 'F', 'L', 'C'}

    # type: set
    answers["(c)-b cluster 2"] = {'A'}

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
    answers["(a)"] = ['Hierarchical', 'Overlapping', 'Partial']

    # type: list
    answers["(b)"] = ['Partitional', 'Exclusive', 'Complete']

    # type: list
    answers["(c)"] = ['Partitional', 'fuzzy', 'complete']

    # type: list
    answers["(d)"] = ['Hierarchical', 'overlapping', 'partial']

    # type: list
    answers["(e)"] = ['Partitional', 'Exclusive', 'Complete']

    # type: explanatory string (at least four words)
    answers["(e) explain"] = "Grades are exclusive categories, no overlap. Each student gets one grade per class, ensuring completeness for all students."

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
