# PrismUI

PrismUI is a modern, lightweight CSS component library designed to help developers create beautiful and responsive web interfaces quickly. With a focus on simplicity, customization, and performance, PrismUI provides everything you need to build modern websites without the bloat.

## Features

- **Modern Design**: Clean, minimal design with attention to details and beautiful defaults
- **Lightweight**: No JavaScript dependencies, minimal CSS footprint
- **Customizable**: Easy to customize with CSS variables
- **Responsive**: Mobile-first design that works on all screen sizes
- **Modular**: Use only what you need
- **Accessible**: Built with accessibility in mind
- **Dark Mode**: Built-in dark mode support
- **Cross-Browser**: Compatible with all modern browsers

## Installation

### CDN

Add PrismUI to your project using the CDN:

```html
<!-- Base styles -->
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/prism-ui/dist/prism.min.css">

<!-- Optional: Component styles -->
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/prism-ui/dist/components.min.css">

<!-- Optional: Advanced component styles -->
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/prism-ui/dist/advanced.min.css">

<!-- Optional: Utility styles -->
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/prism-ui/dist/utilities.min.css">
```

### NPM

Install PrismUI using NPM:

```bash
npm install prism-ui
```

Then import the CSS files in your project:

```js
// Import all styles
import 'prism-ui/dist/prism.min.css';
import 'prism-ui/dist/components.min.css';
import 'prism-ui/dist/advanced.min.css';
import 'prism-ui/dist/utilities.min.css';

// Or import only what you need
import 'prism-ui/dist/prism.min.css';
import 'prism-ui/dist/components.min.css';
```

### Download

Download the CSS files and include them in your project:

```html
<link rel="stylesheet" href="path/to/prism.css">
<link rel="stylesheet" href="path/to/components.css">
<link rel="stylesheet" href="path/to/advanced.css">
<link rel="stylesheet" href="path/to/utilities.css">
```

## Basic Usage

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>My PrismUI Project</title>
    <link rel="stylesheet" href="path/to/prism.css">
    <link rel="stylesheet" href="path/to/components.css">
    
    <!-- Optional: Include Google Fonts -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Plus+Jakarta+Sans:wght@400;500;600;700&display=swap" rel="stylesheet">
</head>
<body>
    <!-- Navbar -->
    <nav class="navbar navbar-light">
        <div class="container">
            <a class="navbar-brand" href="#">PrismUI</a>
            <div class="navbar-nav">
                <a class="nav-link" href="#">Home</a>
                <a class="nav-link" href="#">Features</a>
                <a class="nav-link" href="#">Pricing</a>
            </div>
        </div>
    </nav>
    
    <!-- Content -->
    <div class="container my-5">
        <h1>Welcome to PrismUI</h1>
        <p>Start building beautiful websites with PrismUI.</p>
        
        <button class="btn btn-primary">Get Started</button>
        <button class="btn btn-outline-primary">Learn More</button>
        
        <div class="grid grid-cols-1 md:grid-cols-3 gap-4 mt-5">
            <div class="card">
                <div class="card-body">
                    <h5 class="card-title">Feature 1</h5>
                    <p class="card-text">This is a feature card.</p>
                </div>
            </div>
            
            <div class="card">
                <div class="card-body">
                    <h5 class="card-title">Feature 2</h5>
                    <p class="card-text">This is a feature card.</p>
                </div>
            </div>
            
            <div class="card">
                <div class="card-body">
                    <h5 class="card-title">Feature 3</h5>
                    <p class="card-text">This is a feature card.</p>
                </div>
            </div>
        </div>
    </div>
</body>
</html>
```

## Customizing PrismUI

PrismUI uses CSS variables for easy customization. You can override these variables in your own CSS:

```css
:root {
    /* Change primary color */
    --prism-primary: #ff5722;
    --prism-primary-light: #ff7e47;
    --prism-primary-dark: #e64a19;
    
    /* Change font family */
    --prism-font-sans: 'Roboto', sans-serif;
    --prism-font-heading: 'Montserrat', sans-serif;
    
    /* Change border radius */
    --prism-radius-md: 0.5rem;
    --prism-radius-lg: 0.75rem;
}
```

## Components

PrismUI includes a wide range of components:

- **Layout**: Container, Grid, Flexbox
- **Components**: Buttons, Cards, Badges, Alerts, Forms, Navs, Navbar
- **Advanced**: Tables, Modal, Progress, Spinners, List Group, Breadcrumb
- **Special**: Gradient Cards, Glass Cards, Feature Cards, Pricing Tables, Avatars, Timeline, Tags/Chips
- **Utilities**: Spacing, Colors, Typography, Flexbox, Grid, Borders, Shadows

## Browser Support

PrismUI supports all modern browsers:

- Chrome (latest)
- Firefox (latest)
- Safari (latest)
- Edge (latest)
- Opera (latest)

## License

PrismUI is released under the MIT License.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Documentation

For full documentation, visit [https://prismui.dev/docs](https://prismui.dev/docs).