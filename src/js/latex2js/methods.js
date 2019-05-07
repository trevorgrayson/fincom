var pow = Math.pow;
var sqrt = Math.sqrt;
var cos = Math.cos;
var arccos = Math.acos;
var abs = Math.abs;

module.exports = function(eqn, variables) {
  try {
    return eval(variables + ";" + eqn);
  }
  catch(err) {
    throw "Exception running equation! " + err

  }
}

