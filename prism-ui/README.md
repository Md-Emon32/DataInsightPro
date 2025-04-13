# PrismUI

A modern CSS component library featuring neumorphic design and minimalist UI elements for building beautiful websites. PrismUI provides a collection of customizable UI components, layout patterns, and interactive animations with a clean, sophisticated design aesthetic.

## Features

- **Modern Neumorphic Design**: Stunning soft UI design with subtle shadows, creating a three-dimensional experience while maintaining minimalism
- **Extensive Component Library**: Rich collection of components from basic buttons to advanced layout patterns
- **Interactive Animations**: Subtle animations and transitions that enhance user experience
- **Lightweight**: Optional JavaScript enhancements, minimal CSS footprint, and modular architecture
- **Customizable**: Easy to customize with CSS variables, create your own themes, and extend styles
- **Responsive**: All components fully responsive and optimized for all devices
- **Framework Agnostic**: Use with any frontend framework (React, Vue, Angular) or with vanilla HTML/CSS

## Quick Start

Add PrismUI to your project:

```html
<head>
  <!-- Core PrismUI CSS -->
  <link rel="stylesheet" href="prism.css">
  <link rel="stylesheet" href="components.css">
  
  <!-- Additional CSS modules as needed -->
  <link rel="stylesheet" href="advanced.css">
  <link rel="stylesheet" href="layouts.css">
  <link rel="stylesheet" href="utilities.css">
  <link rel="stylesheet" href="icons.css">
  
  <!-- Optional JavaScript for enhanced interactions -->
  <script src="script.js" defer></script>
</head>
```

Create your first neumorphic component:

```html
<div class="neu-card">
  <h3>Getting Started with PrismUI</h3>
  <p>Welcome to the modern neumorphic design system!</p>
  <button class="neu-btn neu-btn-primary">Get Started</button>
</div>
```

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

## Neumorphic Design Components

PrismUI features a comprehensive set of neumorphic design components with modern minimal UI styling:

### Neumorphic UI Elements
- Neumorphic Buttons (neu-btn, neu-btn-primary, neu-btn-secondary)
- Neumorphic Cards (neu-card, neu-card-pressed, neu-card-convex, neu-card-concave)
- Neumorphic Form Elements (neu-input, neu-checkbox, neu-radio, neu-toggle, neu-range)
- Neumorphic Badges (neu-badge, neu-badge-primary, neu-badge-secondary)
- Neumorphic Progress Bars (neu-progress, neu-progress-bar)
- Neumorphic Alerts (neu-alert, neu-alert-primary, neu-alert-warning)
- Neumorphic Icon Containers (neu-icon-container)

### Neumorphic Usage Examples

```html
<!-- Neumorphic Buttons -->
<button class="neu-btn">Default</button>
<button class="neu-btn neu-btn-primary">Primary</button>
<button class="neu-btn neu-btn-secondary">Secondary</button>

<!-- Neumorphic Cards -->
<div class="neu-card">
  <h4>Flat Card</h4>
  <p>A basic neumorphic card with flat shadow effect.</p>
</div>

<div class="neu-card-pressed">
  <h4>Pressed Card</h4>
  <p>A neumorphic card with inset shadow effect.</p>
</div>

<!-- Neumorphic Form Elements -->
<input type="text" class="neu-input" placeholder="Neumorphic Input">

<label class="neu-checkbox">
  Option One
  <input type="checkbox" checked>
  <span class="neu-checkbox-mark"></span>
</label>

<label class="neu-toggle">
  <input type="checkbox">
  <span class="neu-toggle-slider"></span>
</label>

<input type="range" class="neu-range" min="0" max="100" value="50">

<!-- Neumorphic Progress -->
<div class="neu-progress">
  <div class="neu-progress-bar" style="width: 75%"></div>
</div>

<!-- Neumorphic Badges -->
<span class="neu-badge">Default</span>
<span class="neu-badge neu-badge-primary">Primary</span>

<!-- Neumorphic Alerts -->
<div class="neu-alert neu-alert-primary">
  <h4 class="neu-alert-title">Primary Alert</h4>
  <p class="neu-alert-body">This is an important message.</p>
</div>

<!-- Neumorphic Icon Container -->
<div class="neu-icon-container">
  <span class="icon-fa-heart"></span>
</div>
```

## Icon Components

Modern icon components and styles:

### Font Awesome Icons
- Font Awesome integration with `icon-fa-*` prefix (icon-fa-home, icon-fa-user, etc.)
- 50+ common Font Awesome icons included
- Compatible with all icon styling and animations

### SVG Icons
- SVG Icons (home, user, settings, menu, search, alert, close)
- Icon Sizes (xs, sm, md, lg, xl, 2x, 3x, 4x)
- Icon Buttons
- Floating Action Buttons
- Notification Badges
- Icon Animations (spin, pulse, shake)

### Modern Icon Styles
- Glassmorphism Icons
- Neumorphic Icons
- 3D Icons
- Feature Icon Cards

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

## Animations and Interactions

PrismUI includes a variety of subtle animations and interactive effects to enhance the user experience:

### Component Animations
- Button Ripple Effects: Visual feedback on button clicks with customizable ripple animations
- Hover Lift Effects: Elements that subtly lift and enhance shadows on hover
- Progress Bar Animations: Animated progress bars with shimmer effects
- Alert Fade-in Animations: Smooth entrance animations for alerts
- Badge Scale Animations: Interactive scaling effects for badges
- Pulse Animations: Subtle pulse effects for checkboxes and radio buttons when selected
- Loading Spinners: Animated loading indicators

### Interactive Effects
- Form Control Transitions: Smooth transitions for form inputs, checkboxes, and toggles
- Card Hover Animations: Enhanced depth and shadow effects on card hover
- Icon Container Animations: Lift and scale effects for icon containers
- Page Transitions: Smooth fade-in effects for page elements

### JavaScript Interactions
- Ripple Effect Implementation: Script-powered ripple effects for buttons
- Progress Bar Animation Controls: Interactive progress bar demonstrations
- Toggle States: Persistent toggle state management
- Tooltip System: Dynamic tooltip creation and positioning
- Accordion Functionality: Collapsible content sections

## Browser Support

PrismUI supports all modern browsers, including:

- Chrome (latest)
- Firefox (latest)
- Safari (latest)
- Edge (latest)

## License

MIT License