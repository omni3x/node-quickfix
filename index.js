const binary = require('node-pre-gyp');
const libpath = require('path');

const bindingPath = binary.find(libpath.resolve(__dirname, './package.json'));
const NodeQuickfix = require(bindingPath);

exports.logonProvider = NodeQuickfix.FixLoginProvider;
exports.initiator = NodeQuickfix.FixInitiator;
exports.acceptor = NodeQuickfix.FixAcceptor;
