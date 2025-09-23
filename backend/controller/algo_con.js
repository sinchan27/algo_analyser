const path = require('path');
const runPY = require('../utils/runPY');

exports.bubble_sorting = async (req, res) => {
  try {
    const { array, sizes } = req.body;
    const script = path.join(__dirname, '../algo/bubble_sorting.py');

    let args = [];

    if (array && Array.isArray(array)) {
      
      args = [JSON.stringify({ mode: "array", data: array })];
    } 
    else if (sizes && Array.isArray(sizes)) {
      
      args = [JSON.stringify({ mode: "sizes", data: sizes })];
    } 
    else {
      return res.status(400).json({ error: "Provide either 'array' or 'sizes' in body" });
    }

    const result = await runPY(script, args);
    const parsed = JSON.parse(result);
    if (sizes) {
            parsed.push({
                graph_url: "http://localhost:3000/static/graphs/bubble_sort_analysis.png"
            });
        }

    res.json(parsed);

  } catch (err) {
    console.error(err);
    res.status(500).json({ error: err.message });
  }
}


exports.merge_sorting = async (req, res) => {
  try {
    const { array, sizes } = req.body;
    const script = path.join(__dirname, '../algo/merge_sorting.py');

    let args = [];

    if (array && Array.isArray(array)) {
     
      args = [JSON.stringify({ mode: "array", data: array })];
    } 
    else if (sizes && Array.isArray(sizes)) {
      
      args = [JSON.stringify({ mode: "sizes", data: sizes })];
    } 
    else {
      return res.status(400).json({ error: "Provide either 'array' or 'sizes' in body" });
    }

    const result = await runPY(script, args);
    const parsed = JSON.parse(result);
    if (sizes) {
            parsed.push({
                graph_url: "http://localhost:3000/static/graphs/merge_sort_analysis.png"
            });
        }

    res.json(parsed);

  } catch (err) {
    console.error(err);
    res.status(500).json({ error: err.message });
  }
}

