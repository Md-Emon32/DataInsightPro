# PrismUI

A modern CSS component library for beautiful websites. PrismUI provides a collection of customizable UI components and layout patterns with a clean, minimal design.

## Features

- **Modern Design**: Clean, minimal design with attention to details, accessible components, and beautiful defaults
- **Lightweight**: No JavaScript dependencies, minimal CSS footprint, and modular architecture
- **Customizable**: Easy to customize with CSS variables, create your own themes, and extend with your styles
- **Responsive**: All components are fully responsive and work on all devices
- **Framework Agnostic**: Use with any frontend framework (React, Vue, Angular) or with vanilla HTML/CSS

## Installation

### Option 1: Direct Include

Include the PrismUI CSS files directly in your HTML:

```html
<!-- Core CSS -->
<link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/your-username/prism-ui/prism.css">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/your-username/prism-ui/components.css">

<!-- Optional additional CSS -->
<link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/your-username/prism-ui/layouts.css">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/your-username/prism-ui/utilities.css">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/your-username/prism-ui/advanced.css">
```

### Option 2: Download

1. Download the CSS files from the GitHub repository
2. Include them in your project:

```html
<link rel="stylesheet" href="path/to/prism.css">
<link rel="stylesheet" href="path/to/components.css">
<link rel="stylesheet" href="path/to/layouts.css">
<link rel="stylesheet" href="path/to/utilities.css">
<link rel="stylesheet" href="path/to/advanced.css">
```

### Option 3: npm (Coming Soon)

```bash
npm install prism-ui
```

Then import in your project:

```js
import 'prism-ui/prism.css';
import 'prism-ui/components.css';
import 'prism-ui/layouts.css';
import 'prism-ui/utilities.css';
import 'prism-ui/advanced.css';
```

## Usage

PrismUI follows a similar pattern to other CSS frameworks. Simply add the appropriate classes to your HTML elements:

### Basic Components

```html
<!-- Button Examples -->
<button class="btn btn-primary">Primary Button</button>
<button class="btn btn-secondary">Secondary Button</button>
<button class="btn btn-outline-primary">Outline Button</button>

<!-- Card Example -->
<div class="card">
  <div class="card-header">
    <h5 class="card-title">Card Title</h5>
  </div>
  <div class="card-body">
    <p class="card-text">This is a basic card example.</p>
    <button class="btn btn-primary">Learn More</button>
  </div>
</div>

<!-- Alert Example -->
<div class="alert alert-success">
  This is a success alert indicating a successful operation.
</div>
```

### Layout Components

```html
<!-- Two-column Layout -->
<div class="layout-two-column">
  <div>Column 1</div>
  <div>Column 2</div>
</div>

<!-- Dashboard Layout -->
<div class="layout-dashboard">
  <header class="layout-dashboard-header">Header</header>
  <aside class="layout-dashboard-sidebar">Sidebar</aside>
  <main class="layout-dashboard-main">Main Content</main>
  <footer class="layout-dashboard-footer">Footer</footer>
</div>

<!-- Card Grid Layout -->
<div class="layout-card-grid">
  <div class="card">Card 1</div>
  <div class="card">Card 2</div>
  <div class="card">Card 3</div>
  <div class="card">Card 4</div>
</div>
```

### Utility Classes

PrismUI comes with a range of utility classes for spacing, typography, colors, and more:

```html
<!-- Margin and Padding -->
<div class="mt-4 mb-2 p-3">
  Content with margin-top: 1rem, margin-bottom: 0.5rem, and padding: 0.75rem
</div>

<!-- Typography -->
<p class="text-lg font-bold">Large bold text</p>
<p class="text-sm text-muted">Small muted text</p>

<!-- Colors -->
<div class="bg-primary text-white">Primary background with white text</div>
<div class="bg-neutral-100 text-neutral-800">Light background with dark text</div>

<!-- Display and Flexbox -->
<div class="d-flex justify-content-between align-items-center">
  Flexbox container with space-between alignment
</div>
```

## Components

PrismUI includes the following core components:

- Buttons
- Cards
- Alerts
- Badges
- Forms
- Navigation
- Tables
- Modals
- Tabs
- Accordions
- Pagination
- Progress Bars

## Layout Components

Advanced layout patterns:

- Two-column Layout
- Three-column Layout
- Four-column Layout
- Holy Grail Layout
- Dashboard Layout
- Sidebar Layout
- Card Grid Layout
- Hero Layout
- Feature Layout
- Split Layout
- Z-Pattern Layout
- Fixed Header Layout
- Sticky Footer Layout
- Overlay Layout
- Gallery Layout
- Sidebar Navigation Layout

## Browser Support

PrismUI supports all modern browsers, including:

- Chrome (latest)
- Firefox (latest)
- Safari (latest)
- Edge (latest)

## License

MIT License