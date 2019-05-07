const assert = require('assert');
const latex2js = require("latex2js/latex2js");


describe("Bank", function() {

  it("Compound Interest", function() {
    const amount = "P*(1+r*(\\frac{1}{k}))*(1+r*(\\frac{1}{k}))";
    const eqn    = latex2js.render(amount);
    const result = latex2js.eval(eqn, "P=100; k=2; r=5");
    //TODO, shouldn't have to render to eqn

    assert.equal("P*(1+r*((1)/(k)))*(1+r*((1)/(k)))", eqn);
    assert.equal(1225, result);

  });

});

