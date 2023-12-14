# Hungarian Algorithm Implementation in Flask

#### Project: Freelance Project - Hungarian Algorithm Implementation in Flask

This freelance project is a Flask web application that implements the Hungarian Algorithm for solving assignment problems. It facilitates users in inputting cost matrices and obtaining the optimal resource assignment, offering a practical solution to complex assignment tasks.

#### Key Features:
1. **Matrix Size Selection**: Users can define the size of the cost matrix.
2. **Cost Input**: Enables the entry of individual cost values for each matrix element.
3. **Optimal Assignment Calculation**: Employs the Hungarian Algorithm to determine the most efficient assignment.

#### Usage:
- Launch the Flask application.
- Select the desired size for the cost matrix.
- Input cost values for the matrix.
- Review the calculated optimal assignment.

#### Technologies Used:
- Flask for backend development.
- HTML/CSS for frontend design.
- `scipy.optimize.linear_sum_assignment` for implementing the Hungarian Algorithm.

#### How to Run:
1. Install necessary dependencies: `pip install flask scipy`.
2. Execute the application: `python hungarian_example.py`.

#### Additional Notes:
- Further enhancements could include improved user input validation and error handling.
- The application was deployed on an AWS EC2 instance and using Ubuntu as a OS (Ubuntu 22.04.3 LTS (Codename: jammy))
- For my case I run it on an Apache server (version 2.4.52 on Ubuntu).

