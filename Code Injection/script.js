const exec = require('child_process').exec;
const fs = require('fs');

exports.createFile = function(username, filename) {
  return new Promise((resolve, reject) => {
    exec(fs.closeSync(fs.openSync(`/tmp/jail/tmp/${username}/${filename}`, 'w')), (error, stdout, stderr) => {
        if (error !== null) reject(stderr);
        resolve();
    });
  });
}