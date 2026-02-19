const express = require('express');
const app = express();
const path=require('path');
const routes=require('./routes/algo_routes')
 const bodyparser=require('body-parser');
 app.use(bodyparser.urlencoded({ extended: false }));
 app.use(bodyparser.json());
const PORT = process.env.PORT || 3000;


app.get("/", (req, res) => {
  res.send("Algorithm Analyzer Backend Running");
});

app.use('/sort',routes);
app.use('/static', express.static(path.join(__dirname, 'public')));

app.listen(PORT,()=>{
  console.log("Server running on port", PORT);
})