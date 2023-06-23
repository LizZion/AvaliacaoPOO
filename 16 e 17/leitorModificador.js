// Dependência
const fs = require("fs");

// Leitura de arquivos
fs.exists("Demo.txt", function (existe) {
  if (existe) {
    fs.readFile("Demo.txt", "utf8", function (err, data) {
      console.log(data);
    });
  } else {
    fs.writeFile("Demo.txt", "Teste", "utf8", function (err) {
      console.log("Arquivo criado!");
    });
    console.log("Arquivo não existe, criando arquivo...");
  }
});
