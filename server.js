/**
 * PrismUI - Server
 * A node.js server to serve the PrismUI component library
 */

const http = require('http');
const fs = require('fs');
const path = require('path');

// Define the port to use
const PORT = process.env.PORT || 5000;

// Create the HTTP server
const server = http.createServer((req, res) => {
  // Get the file path from the URL
  let filePath = req.url;
  
  // If requesting the root, redirect to the PrismUI directory index.html
  if (filePath === '/') {
    filePath = '/prism-ui/index.html';
  } else {
    // Otherwise prefix with the prism-ui directory
    filePath = '/prism-ui' + filePath;
  }
  
  // Convert URL to local file path
  filePath = path.join(__dirname, filePath);
  
  // Get the file extension
  const extname = path.extname(filePath);
  
  // Set the default content type
  let contentType = 'text/html';
  
  // Check the file extension and set the content type
  switch (extname) {
    case '.js':
      contentType = 'text/javascript';
      break;
    case '.css':
      contentType = 'text/css';
      break;
    case '.json':
      contentType = 'application/json';
      break;
    case '.png':
      contentType = 'image/png';
      break;
    case '.jpg':
      contentType = 'image/jpg';
      break;
    case '.svg':
      contentType = 'image/svg+xml';
      break;
  }
  
  // Read the file
  fs.readFile(filePath, (err, content) => {
    if (err) {
      if (err.code === 'ENOENT') {
        // Page not found - serve the 404 page
        fs.readFile(path.join(__dirname, 'prism-ui/404.html'), (err, content) => {
          if (err) {
            // Even 404 page not found
            res.writeHead(404);
            res.end('404 Not Found');
          } else {
            res.writeHead(404, { 'Content-Type': 'text/html' });
            res.end(content, 'utf8');
          }
        });
      } else {
        // Server error
        res.writeHead(500);
        res.end(`Server Error: ${err.code}`);
      }
    } else {
      // Success
      res.writeHead(200, { 'Content-Type': contentType });
      res.end(content, 'utf8');
    }
  });
});

// Start the server
server.listen(PORT, () => {
  console.log(`PrismUI Server running at http://0.0.0.0:${PORT}/`);
  console.log('Press Ctrl+C to quit.');
});