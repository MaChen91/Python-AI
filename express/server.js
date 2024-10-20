// server.js
const express = require("express")
const app = express();
const axios = require('axios');  // 引入 axios
const cors = require('cors');
const port = 3000;

// Serve static files from the dist directory
app.use(express.static('dist'));
app.use(cors());

// 前端可以请求 /api/express-python，这将转发到 Python 后端
app.get('/api/express-python', async (req, res) => {
  try {
    // 向 Python 服务器发送请求，Python 服务器运行在 http://localhost:5000
    const response = await axios.get('http://localhost:5000/python-api');
    
    // 获取 Python 后端的返回数据并返回给前端
    res.json(response.data);
  } catch (error) {
    // 如果请求失败，返回错误信息
    res.status(500).json({ message: 'Error fetching data from Python API', error: error.toString() });
  }
});

// 定义一个简单的 API 路由
app.get('/api/message', (req, res) => {
  res.json({ message: 'Hello from Express!' });
});


app.get('/api', (req, res) => {
  res.send({ message: 'Hello from Express!' });
});

app.listen(port, () => {
  console.log(`Server is running on http://localhost:${port}`);
});
