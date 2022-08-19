const express = require('express')
const app = express()

app.get("/callback/api", (req,res) => {
    res.json({ code: req.query.code });
})

app.listen(3000, () => {
    console.log("listening on port 3000");
})