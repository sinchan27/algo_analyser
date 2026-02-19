const express = require("express");
const { bubble_sorting, merge_sorting } = require("../controller/algo_con.js");
const router = express.Router();

router.get("/test", (req, res) => {
  res.json({ message: "API working" });
});

router.post("/bubble_sort", bubble_sorting);
router.post("/merge_sort",merge_sorting);

module.exports = router;
