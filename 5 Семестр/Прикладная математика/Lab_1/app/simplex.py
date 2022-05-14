from app.check import check
from app.basicCol import basicCol
from app.makeTau import makeTau
from app.forceImprove import forceImprove
from app.step import step
from app.pivotPos import pivotPos
from app.solve import solve
from app.input import input

def simplex(filename):
    inputData = input(filename)

    tau = check(basicCol(makeTau(inputData['fx'], inputData['matrix']['a'], inputData['matrix']['b'])))

    while forceImprove(tau, inputData['max']):
        tau = step(tau, pivotPos(tau, inputData['max']))

    return solve(tau)