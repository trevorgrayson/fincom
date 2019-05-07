const assert = require('assert');
const latex2js = require("latex2js/latex2js");


describe("wikipedia", function() {

  it("Orbital Inclination", function() {
    //const fn = "\\sqrt{h_z\\over(\\abs{h})}"
    const fn = '\cos(2)'
    assert.equal(latex2js.render(fn), "cos(2)");
  });

  it("arccos", function(){
    const fn = '\cos(\\frac{h_z}{h})'
    assert.equal(latex2js.render(fn), 'cos((h_z)/(h))')
  });

  // functions https://www.maths.tcd.ie/~dwilkins/LaTeXPrimer/StdFuncts.html

});

