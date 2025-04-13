// Theme Testing Script
const themes = ['default', 'metro', 'material', 'clay', 'glass', 'skeuomorphic', 'minimal', 'dark'];

function testAllThemes() {
  console.log('Starting theme test...');
  
  themes.forEach((theme, index) => {
    setTimeout(() => {
      console.log(`Testing theme: ${theme}`);
      
      // Apply theme
      document.body.className = theme === 'default' ? '' : `theme-${theme}`;
      
      // Log computed style values to verify CSS variables
      const style = getComputedStyle(document.body);
      const primaryColor = style.getPropertyValue('--prism-primary').trim();
      const surfaceBg = style.getPropertyValue('--prism-surface-bg').trim();
      const radius = style.getPropertyValue('--prism-radius-md').trim();
      
      console.log(`${theme} theme values:`, {
        primaryColor,
        surfaceBg,
        radius
      });
      
      if (index === themes.length - 1) {
        console.log('Theme testing completed!');
      }
    }, index * 1000); // Apply each theme with a 1-second delay
  });
}

// Run the test
testAllThemes();
