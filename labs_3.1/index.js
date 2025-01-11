const express = require("express");
const { ulid } = require("ulid");

const app = express();
const port = 3000;

app.use(express.json());

app.get("/", (req, res) => {
    res.send("Hello, Express!");
});

app.get("/json", (req, res) => {
    res.json({ id: ulid(), message: "Voici une réponse JSON avec un ID ULID !" });
});

app.post("/echo", (req, res) => {
    const { name, age } = req.body;
    if (!name || !age) {
        return res.status(400).json({ error: "Merci d'envoyer un 'name' et un 'age'." });
    }
    res.json({ success: true, received: req.body });
});

app.listen(port, () => {
    console.log(`App running at http://localhost:${port}`);
});