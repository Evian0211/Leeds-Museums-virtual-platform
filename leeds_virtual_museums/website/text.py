# ------------- Evaluation ---------------

NO_EVALUATION_TEXT = "You have not done an evaluation."

EVALUATION_QUESTIONS = [
    ("Question 1 text", ["choice 1", "choice 2", "choice 3"]),
    ("Question 2 text", ["a", "b", "c", "d"]),
    ("Question 3 text", ["a", "b", "c", "d", "e"])
]

EVALUATION_TYPES = ["Type A", "Type B"]

# ----------------------------------------
# ------------- Curriculum ---------------

COURSE_ONE_NAME = "Leeds Art"

COURSE_ONE_CONTENT = [
    ("Section 1 header", [
        "This is the content of section 1 course 1 paragraph 1.", 
        "This is the content of section 1 course 1 paragraph 2."
        ]),
    ("Section 2 header", [
        "This is the content of section 2 course 1 paragraph 1.",
        "This is the content of section 2 course 1 paragraph 2.",
        ])    
]

COURSE_ONE_QUESTIONS = [
    ("Question 1 text", ["choice 1", "choice 2", "choice 3"]),
    ("Question 2 text", ["a", "b", "c", "d"]),
    ("Question 3 text", ["a", "b", "c", "d", "e"])
]



COURSE_TWO_NAME = "Leeds History"

COURSE_TWO_CONTENT = [
    ("Section 1 header", [
        "This is the content of section 1 course 2 paragraph 1.", 
        "This is the content of section 1 course 2 paragraph 2."
        ]),
    ("Section 2 header", [
        "This is the content of section 2 course 2 paragraph 1.",
        "This is the content of section 2 course 2 paragraph 2.",
        ])    
]

COURSE_TWO_QUESTIONS = [
    ("Question 1 text", ["choice 1", "choice 2", "choice 3"]),
    ("Question 2 text", ["a", "b", "c", "d"]),
    ("Question 3 text", ["a", "b", "c", "d", "e"])
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