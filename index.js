import express from 'express';
import fs from 'fs';
import {PythonShell} from 'python-shell';

const app = express();
app.get("/:word", (req, res) => {
    const {word} = req.params;
    fs.createWriteStream("index.txt", "utf-8").write(word);
    PythonShell.run("index.py", null).then(() => {
        console.log("script finished")
    })
    fs.readFile("binary.txt", (err, data) => {
        if(err){
            res.writeHead(404, {'content-type': "text/plain"});
            return res.end("404, not found");
        }
        res.writeHead(200, {'content-type': "text/plain"});
        res.write(data);
        res.end()
    })
}).listen(8080, () => console.log("http://127.0.0.1:8080/hellothere"))