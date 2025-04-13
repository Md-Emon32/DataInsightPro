// Test script to check theme switching functionality
// Run this in the browser console when viewing the PrismUI page

function testThemeSwitching() {
  console.log('Testing theme switching functionality...');
  
  // Get all theme names from the themes object in script.js
  const themeNames = ['default', 'metro', 'material', 'clay', 'glass', 'skeuomorphic', 'minimal', 'dark'];
  
  // Get current theme
  const currentBodyClasses = document.body.className;
  console.log('Current body classes:', currentBodyClasses);
  
  // Test each theme
  themeNames.forEach(themeName => {
    console.log(`Testing theme: ${themeName}`);
    
    // Call setActiveTheme function (should be available globally)
    if (typeof setActiveTheme === 'function') {
      setActiveTheme(themeName);
      
      // Verify that the theme was applied
      const hasThemeClass = themeName === 'default' || document.body.classList.contains(`theme-${themeName}`);
      console.log(`Theme ${themeName} applied:`, hasThemeClass);
      
      // Check that theme-specific CSS properties have been applied
      const computedStyle = window.getComputedStyle(document.body);
      console.log(`Primary color for ${themeName}:`, computedStyle.getPropertyValue('--prism-primary'));
      console.log(`Radius for ${themeName}:`, computedStyle.getPropertyValue('--prism-radius-md'));
      
      // Small delay to visually see theme change
      console.log('----------------------------------');
    } else {
      console.error('setActiveTheme function not found. Theme switching is not working.');
    }
  });
  
  console.log('Theme switching test completed.');
}

// Run the test
testThemeSwitching();