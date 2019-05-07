const latex_to_js = require("./latex_to_js");
const evaluate = require("./methods");


var latex2js = {
  render: latex_to_js,
  eval: evaluate
};

module.exports = latex2js;
