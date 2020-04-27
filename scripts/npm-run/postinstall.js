const libpath = require('path');
const libfs = require('fs');

const libVersion = '17';
const platformArch = `${process.platform}-${process.arch}`;

console.log(`platformArch = ${platformArch}`);

const projectDirPath = libpath.resolve(__dirname, '../..');
const libDirPath = `${projectDirPath}/lib/${platformArch}`;

let libFileName;
let targetLibDirPath;

switch (platformArch) {
  case 'linux-x64':
    libFileName = `libquickfix.so.${libVersion}`;
    targetLibDirPath = '/lib64';
    break;
  case 'darwin-x64':
    libFileName = `libquickfix.${libVersion}.dylib`;
    targetLibDirPath = '/usr/local/lib';
    break;
  default:
    process.exit(0);
    break;
}

const libFilePath = `${libDirPath}/${libFileName}`;

console.log(`libFilePath = ${libFilePath}`);

if (!libfs.existsSync(libFilePath) || !libfs.statSync(libFilePath).isFile()) {
  console.error(`${libFilePath}: file does not exist`);
  process.exit(1);
}

console.log(`targetLibDirPath = ${targetLibDirPath}`);

if (
  !libfs.existsSync(targetLibDirPath) ||
  !libfs.statSync(targetLibDirPath).isDirectory()
) {
  console.error(`${targetLibDirPath}: directory does not exist`);
  process.exit(1);
}

const targetLibFilePath = `${targetLibDirPath}/${libFileName}`;

console.log(`Copying ${libFilePath} to ${targetLibFilePath}...`);

libfs.copyFileSync(libFilePath, targetLibFilePath);
