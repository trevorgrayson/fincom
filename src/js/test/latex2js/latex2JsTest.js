const assert = require('assert');
const latex2js = require("latex2js/latex2js");


describe("latex2js", function() {

  it("renders newtons", function() {
    const force = "m * a^2";
    const result = latex2js.render(force);

    assert.ok(result == "m*pow(a,2)", result)
  });

  //it("renders quadratic", function() {
  //  const fn = "\\frac{-b\\pm\\sqrt{b^2-4a*c}}{2*a}";
  //  const result = latex2js.render(fn);

  //  assert.ok(result == "m*pow(a,2)", result)
  //});

  it("renders quadratic, plus only", function() {
    const fn = "\\frac{-b+\\sqrt{b^2-4a*c}}{2*a}";
    const result = latex2js.render(fn);

    assert.ok(result == "(-b+sqrt(pow(b,2)-4a*c))/(2*a)", result)
  });

  it("executes force", function() {
    const fn = "m * a^2";
    const script = latex2js.render(fn);
    const result = latex2js.eval(
      "a = 2; m = 3; " +
      latex2js.render(fn)
    );

    assert.ok(result == 12, result)
  });

  it("executes", function() {
    const fn = "\\frac{-b+\\sqrt{b^2-4*a*c}}{2*a}";
    const script = latex2js.render(fn);
    const result = latex2js.eval(
      "var pow = Math.pow; " + 
      "var sqrt = Math.sqrt; " + 
      "a = 2; b = 3; c = 5;" +
      script
    );

    assert.ok(isNaN(result), script + " = " + result)
  });

  it("subscripts", function() {
    const fn = "\\frac{t_0}{t_1}"
    const script = latex2js.render(fn);

    assert.ok(script == "(t_0)/(t_1)", script);
  });

  it("constants", function() {
    const fn = "\\omega*t"
    const script = latex2js.render(fn);
    // s/\\//g
    //const result = latex2js.eval(
    //  "var omega = 2; " + 
    //  "var t = 3; " + 
    //  script
    //);

    //assert.ok(result == 6, script + " = " + result);
  });
});

