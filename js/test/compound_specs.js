var assert = require('assert');
var compound = require('../compound');

describe('compound', function() {

  describe('#compoundInterest', function() {

    it('compounds zero times', function() {
      var result = compound.compoundInterest(100, 0.06, 0);
      assert.equal(result, 100);
    });

    it('compounds once', function() {
      var result = compound.compoundInterest(100, 0.06, 1);
      assert.equal(result, 106);
    });

    it('compounds ten times', function() {
      var result = compound.compoundInterest(100, 0.06, 10);
      assert.equal(result, 179);
    });

    it('works with reasonably sized years', function() {
      var lotOfMoney = 450000
      var result = compound.compoundInterest(lotOfMoney, 0.06, 10);
      assert.equal(result, 805881);
    });

    it('should work on a reasonably sized number', function() {
      var lotOfMoney = 1000000000000
      var result = compound.compoundInterest(lotOfMoney, 0.06, 10);
      assert.equal(result, 1790847696543);
    });
  });

});

