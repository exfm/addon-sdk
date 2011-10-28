Object.defineProperty(this, "global", { value: this });

exports.testGlobals = function(test) {
  // the only globals in module scope should be:
  //   module, exports, require, dump, console
  test.assertObject(module, "have 'module', good");
  test.assertObject(exports, "have 'exports', good");
  test.assertFunction(require, "have 'require', good");
  test.assertFunction(dump, "have 'dump', good");
  test.assertObject(console, "have 'console', good");

  // in particular, these old globals should no longer be present
  test.assertUndefined(global.packaging, "no 'packaging', good");
  test.expectFail(
    // this will be fixed by bug 620559
    function () test.assertUndefined(global.memory, "no 'memory', good")
  );

  test.assertMatches(module.uri, /test-globals\.js$/,
                     'should contain filename');
};
