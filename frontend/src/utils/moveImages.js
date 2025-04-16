const fs = require('fs');
const path = require('path');

const sourceDir = path.join(__dirname, '../../public/images');
const targetDir = path.join(__dirname, '../../public/images/menu');

// Create menu directory if it doesn't exist
if (!fs.existsSync(targetDir)) {
  fs.mkdirSync(targetDir, { recursive: true });
}

// List of menu images to move
const menuImages = [
  'pasta.jpg',
  'pizza.jpg',
  'salad.jpg',
  'dessert.jpg'
];

// Move each image to the menu directory
menuImages.forEach(image => {
  const sourcePath = path.join(sourceDir, image);
  const targetPath = path.join(targetDir, image);
  
  if (fs.existsSync(sourcePath)) {
    fs.renameSync(sourcePath, targetPath);
    console.log(`Moved ${image} to menu directory`);
  } else {
    console.log(`${image} not found in source directory`);
  }
}); 