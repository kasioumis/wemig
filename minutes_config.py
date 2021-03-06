#!/usr/bin/python
# -*- coding: utf-8 -*-

###################
# Template settings
###################

# Dictionary that holds all the template configuration
TEMPLATE_CONFIGURATION = {

    # The title of the application as shown by the browser
    "title" : "My title",

    # List of comma-separated categories to use with autocompletion
    "categories" : """ 
    "Algebra",
    "Analysis",
    "Category theory",
    "Cryptography",
    "Discrete mathematics",
    "Geometry",
    "Number theory",
    "Topology"
    """,

    # List of comma-separated subcategories to use with autocompletion
    "subcategories" : """ 
    "Abstract algebra",
    "Algebraic geometry",
    "Algebraic topology",
    "Commutative algebra",
    "Computer algebra",
    "Diagram algebras",
    "Elementary algebra",
    "Galois theory",
    "Homological algebra",
    "Linear algebra",
    "Mathematical identities",
    "Permutations",
    "Polynomials",
    "Symmetric functions",
    "Algebra stubs",
    "Analytic number theory",
    "Asymptotic analysis",
    "Calculus",
    "Calculus of variations",
    "Complex analysis",
    "Continuous mappings",
    "Differential operators",
    "Dynamical systems",
    "Ergodic theory",
    "Finite differences",
    "Fixed points",
    "Fourier analysis",
    "Fractals",
    "Functional analysis",
    "Generalized functions",
    "Harmonic analysis",
    "Inequalities",
    "Interpolation",
    "Inverse functions",
    "Mathematical analysts",
    "Means",
    "Norms",
    "Numerical analysis",
    "Optimization",
    "Perturbation theory",
    "Real analysis",
    "Sequences and series"
    """,

    # Define the category and subcategory font-weifht CSS attribute [normal|bold]
    "category_font_weight" : "normal",
    "subcategory_font_weight" : "normal",

}

##########################
# Web Application settings
##########################

# Should we restrict the access to specific IPs?
RESTRICT_BY_IP = False

# List of safe IPs to access the application
IPS = ("127.0.0.1",
       "192.168.1.123",)

# The host IP to run the application from
#HOST = "127.0.0.1"
HOST = "0.0.0.0"

# The port to run the application from
PORT = 5000

# Is this a debug application?
#DEBUG = True
DEBUG = False

