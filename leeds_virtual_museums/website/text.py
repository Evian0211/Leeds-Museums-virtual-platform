# ------------- Evaluation ---------------

NO_EVALUATION_TEXT = "You have not done an evaluation."

EVALUATION_QUESTIONS = [
    ("Q1. Which subject do you think is the most interesting one?", ["History", "Art", "Politics", "Business"]),
    ("Q2. In the following occupations, which one are you interested the most?", ["Engineer", "Artist", "Lawyer", "Police"]),
    ("Q3. If you receive a parcel, what do you think it will be in the parcel?", ["A golden treasure", "A gun", "A painting", "A football"]),
    ("Q4. In the following places, which one do you think you would like to go?", ["Park", "Cinema", "Circus", "Zoo"]),
    ("Q5. Which part of a museum do you like the most?", ["Heritage", "Natural Science", "Art galleries", "Historical figures"])
]

EVALUATION_TYPES = ["Leeds over time", "Leeds at war", "Creativity at Leeds", "Industrial Leeds", "Leeds Society and Community", "Leeds: Empire and Colonialism"]

# ----------------------------------------
# ------------- Curriculum ---------------

COURSE_ONE_NAME = "Leeds Over Time"

COURSE_ONE_CONTENT = [
    ("Section 1 header", "https://www.mylearning.org/stories/leeds-to-the-world-the-story-of-two-leeds-engines/1515?"),
    ("Section 2 header", "https://www.mylearning.org/stories/leeds-to-the-world-the-story-of-two-leeds-engines/1515?")    
]

COURSE_ONE_QUESTIONS = [
    ("C1 Question 1 text", ["choice 1", "choice 2", "choice 3"]),
    ("C1 Question 2 text", ["a", "b", "c", "d"]),
    ("C1 Question 3 text", ["a", "b", "c", "d", "e"])
]



COURSE_TWO_NAME = "Leeds At War"

COURSE_TWO_CONTENT = [
    ("Section 1 header", "https://www.mylearning.org/stories/leeds-to-the-world-the-story-of-two-leeds-engines/1515?"),
    ("Section 2 header", "https://www.mylearning.org/stories/leeds-to-the-world-the-story-of-two-leeds-engines/1515?")    
]

COURSE_TWO_QUESTIONS = [
    ("C2 Question 1 text", ["choice 1", "choice 2", "choice 3"]),
    ("C2 Question 2 text", ["a", "b", "c", "d"]),
    ("C2 Question 3 text", ["a", "b", "c", "d", "e"])
]

CURRICULUM = [
    (0, COURSE_ONE_NAME, COURSE_ONE_CONTENT, COURSE_ONE_QUESTIONS),
    (1, COURSE_TWO_NAME, COURSE_TWO_CONTENT, COURSE_TWO_QUESTIONS)
]

RECOMMAND_COURSE = {
    EVALUATION_TYPES[0]: CURRICULUM[0],
    EVALUATION_TYPES[1]: CURRICULUM[1]
}

# -----------------------------------------
# ---------------- Items ------------------

COURSE_ONE_FULL_MARK = "The Artist"
COURSE_TWO_FULL_MARK = "The Historian"
COURSE_ONE_RECOMMANDED_PASS = "The Great Artist"
COURSE_TWO_RECOMMANDED_PASS = "The Great Historian"