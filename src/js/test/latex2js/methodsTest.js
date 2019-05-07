const assert = require('assert');
const latex2js = require("latex2js/latex2js");


describe("methods", function() {

  it("evals force", function() {
    const force = "m*a";
    const result = latex2js.eval(force, "m=2;a=3");

    assert.ok(result == 6);
  });

});

