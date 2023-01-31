import gurobipy as gp
from gurobipy import GRB
#We will then create an optimization model, add some binary integer variables to the model, and add some linear constraints to the model.

# Create a model
model = gp.Model();

# Add binary variables v[0], v[1], v[2], v[3]
v = model.addVars(4, vtype=GRB.BINARY, name="v");

# Add some constraints
model.addConstr(v[0] + 2 * v[2] + 3 * v[3] <= 4, "constr0");
model.addConstr(gp.quicksum([v[i] for i in [0,1]]) == 1, "constr1");
#We can also set an optimization objective. In this case, let's add the assignment to maximize the sum v[1] + v[2] + v[3].

# Add maximization objective
model.setObjective(gp.quicksum([v[i] for i in [1,2,3]]), GRB.MAXIMIZE);
#Now, let's call the solver to find a model that satisfies the constraints and achieves the optimization objective.

model.optimize();
#If model.optimize() found an (optimal) model, we can access it as follows, for example:

if model.status == GRB.OPTIMAL:
    for v in model.getVars():
        print("{}: {}".format(v.varName, v.x));
else:
    print("No optimal model found!");