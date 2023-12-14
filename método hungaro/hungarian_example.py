from flask import Flask, render_template, request
from scipy.optimize import linear_sum_assignment

app = Flask(__name__)

def hungarian_algorithm(cost_matrix):
    row_ind, col_ind = linear_sum_assignment(cost_matrix)
    return row_ind, col_ind

@app.route('/', methods=['GET', 'POST'])
def index():
    cost_matrix = None
    assignment_matrix = None
    
    if request.method == 'POST':
        form_type = request.form.get('form_type')
        
        if form_type == 'size_selection':
            # Define la matriz de costos basada en la selección del tamaño.
            n = int(request.form.get('nmatriz', 0))  # Proporciona un valor predeterminado de 0
            
            cost_matrix = [[0 for _ in range(n)] for _ in range(n)]
        
        elif form_type == 'cost_submission':
            # Aquí deberías obtener el tamaño de la matriz de una forma más confiable
            n = int(request.form.get('matrix_size', 0))  # De nuevo, un valor predeterminado de 0
            
            cost_matrix = [
                [int(request.form.get(f'cost_{i}_{j}', 0)) for j in range(n)]
                for i in range(n)
            ]
            
            row_ind, col_ind = hungarian_algorithm(cost_matrix)
            assignment_matrix = [['' for _ in range(n)] for _ in range(n)]
            
            for i, j in zip(row_ind, col_ind):
                assignment_matrix[i][j] = 'X'

    return render_template('index.html', cost_matrix=cost_matrix, assignment_matrix=assignment_matrix)

if __name__ == '__main__':
    app.run()