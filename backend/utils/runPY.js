const { spawn } = require("child_process");

module.exports = function runPY(scriptPath, args = []) {
  return new Promise((resolve, reject) => {
    const py = spawn("python", [scriptPath, ...args]);

    let output = "";
    let error = "";

    py.stdout.on("data", (data) => {
      output += data.toString();
    });

    py.stderr.on("data", (data) => {
      error += data.toString();
    });

    py.on("close", (code) => {
      if (code !== 0) {
        reject(new Error(`Python script exited with code ${code}: ${error}`));
      } else {
        resolve(output.trim());
      }
    });
  });
};
