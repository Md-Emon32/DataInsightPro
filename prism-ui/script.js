/**
 * PrismUI - Client-side JavaScript
 * Provides interactive functionality for PrismUI components.
 * 
 * Features:
 * - Button ripple effects
 * - Progress bar animations
 * - Tooltip system
 * - Dark mode toggle
 * - Accordion functionality
 * - Form input animations
 * - Card hover effects
 * - Neumorphic interactive elements
 */

document.addEventListener('DOMContentLoaded', function() {
  // Progress bar demo
  const progressDemo = document.getElementById('progress-demo');
  if (progressDemo) {
    progressDemo.addEventListener('click', function() {
      const progressBar = progressDemo.closest('div').querySelector('.neu-progress-bar');
      // Reset to 0%
      progressBar.style.width = '0%';
      
      // Animate to 100%
      setTimeout(() => {
        progressBar.style.width = '100%';
      }, 50);
    });
  }
  
  // Ripple effect for buttons
  document.querySelectorAll('.neu-btn').forEach(button => {
    button.addEventListener('click', function(e) {
      const rect = button.getBoundingClientRect();
      const x = e.clientX - rect.left;
      const y = e.clientY - rect.top;
      
      const ripple = document.createElement('span');
      ripple.classList.add('ripple-effect');
      ripple.style.left = `${x}px`;
      ripple.style.top = `${y}px`;
      
      button.appendChild(ripple);
      
      setTimeout(() => {
        ripple.remove();
      }, 600);
    });
  });
  
  // Toggle dark mode
  const darkModeToggle = document.getElementById('dark-mode-toggle');
  if (darkModeToggle) {
    darkModeToggle.addEventListener('change', function() {
      document.body.classList.toggle('dark-mode', this.checked);
      localStorage.setItem('darkMode', this.checked ? 'enabled' : 'disabled');
    });
    
    // Check for saved dark mode preference
    if (localStorage.getItem('darkMode') === 'enabled') {
      darkModeToggle.checked = true;
      document.body.classList.add('dark-mode');
    }
  }
  
  // Initialize tooltips
  document.querySelectorAll('[data-tooltip]').forEach(element => {
    element.addEventListener('mouseenter', function() {
      const tooltipText = this.getAttribute('data-tooltip');
      
      const tooltip = document.createElement('div');
      tooltip.classList.add('tooltip');
      tooltip.textContent = tooltipText;
      
      document.body.appendChild(tooltip);
      
      const rect = this.getBoundingClientRect();
      tooltip.style.left = `${rect.left + (rect.width / 2) - (tooltip.offsetWidth / 2)}px`;
      tooltip.style.top = `${rect.top - tooltip.offsetHeight - 10}px`;
      
      this.addEventListener('mouseleave', function() {
        tooltip.remove();
      }, { once: true });
    });
  });
  
  // Accordion functionality
  document.querySelectorAll('.accordion-header').forEach(header => {
    header.addEventListener('click', function() {
      const content = this.nextElementSibling;
      const isOpen = this.classList.contains('active');
      
      // Close all accordions
      document.querySelectorAll('.accordion-header').forEach(h => {
        h.classList.remove('active');
        h.nextElementSibling.style.maxHeight = null;
      });
      
      // Open this one if it was closed
      if (!isOpen) {
        this.classList.add('active');
        content.style.maxHeight = content.scrollHeight + 'px';
      }
    });
  });
  
  // Neumorphic range sliders
  document.querySelectorAll('.neu-range').forEach(range => {
    // Update on load
    updateRangeValue(range);
    
    // Update on change
    range.addEventListener('input', function() {
      updateRangeValue(this);
    });
  });
  
  // Function to update range value display
  function updateRangeValue(range) {
    const valueDisplay = range.nextElementSibling;
    if (valueDisplay && valueDisplay.classList.contains('range-value')) {
      valueDisplay.textContent = range.value;
      // Calculate percentage
      const percent = ((range.value - range.min) / (range.max - range.min)) * 100;
      // Update position of value display
      valueDisplay.style.left = `calc(${percent}% - 15px)`;
    }
  }
  
  // Neumorphic checkboxes and radio buttons - pulse effect on click
  document.querySelectorAll('.neu-checkbox-mark, .neu-radio-mark').forEach(mark => {
    mark.addEventListener('click', function() {
      this.classList.add('pulse');
      
      // Remove pulse class after animation completes
      setTimeout(() => {
        this.classList.remove('pulse');
      }, 500);
    });
  });
  
  // Enhanced card hover effect
  document.querySelectorAll('.neu-card').forEach(card => {
    card.addEventListener('mouseenter', function() {
      this.style.transform = 'translateY(-10px)';
      this.style.boxShadow = 'var(--prism-neu-hover)';
    });
    
    card.addEventListener('mouseleave', function() {
      this.style.transform = 'translateY(0)';
      this.style.boxShadow = 'var(--prism-neu-flat)';
    });
  });
  
  // Neumorphic toggle animations
  document.querySelectorAll('.neu-toggle input[type="checkbox"]').forEach(toggle => {
    toggle.addEventListener('change', function() {
      const slider = this.nextElementSibling;
      
      if (this.checked) {
        slider.classList.add('active');
      } else {
        slider.classList.remove('active');
      }
    });
  });
  
  // Add CSS animations for ripple effect and other animations
  const style = document.createElement('style');
  style.textContent = `
    .ripple-effect {
      position: absolute;
      border-radius: 50%;
      background-color: rgba(255, 255, 255, 0.4);
      transform: scale(0);
      animation: ripple-animation 0.6s linear;
      pointer-events: none;
    }
    
    @keyframes ripple-animation {
      to {
        transform: scale(4);
        opacity: 0;
      }
    }
    
    .tooltip {
      position: fixed;
      background-color: var(--prism-neutral-800);
      color: white;
      padding: 0.5rem 0.75rem;
      border-radius: 4px;
      font-size: 0.875rem;
      z-index: 1000;
      box-shadow: 0 4px 8px rgba(0, 0, 0, 0.15);
      opacity: 0;
      animation: tooltip-fade-in 0.2s ease forwards;
    }
    
    @keyframes tooltip-fade-in {
      to {
        opacity: 1;
      }
    }
    
    .pulse {
      animation: pulse-animation 0.5s ease;
    }
    
    @keyframes pulse-animation {
      0% {
        transform: scale(1);
      }
      50% {
        transform: scale(1.05);
      }
      100% {
        transform: scale(1);
      }
    }
    
    .neu-toggle .neu-toggle-slider.active {
      background-color: var(--prism-primary);
    }
    
    .neu-toggle .neu-toggle-slider.active:before {
      transform: translateX(20px);
    }
    
    .range-value {
      position: absolute;
      top: -25px;
      transform: translateX(-50%);
      background-color: var(--prism-primary);
      color: white;
      padding: 2px 6px;
      border-radius: 3px;
      font-size: 12px;
      transition: left 0.2s ease;
    }
  `;
  document.head.appendChild(style);
});